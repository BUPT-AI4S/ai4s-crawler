"""Merge evidence-backed reviews; enforce owner scope and preserve raw records."""
import copy
import collections
import hashlib
import json
import pathlib
import re
import shutil
import subprocess
import sys
from dinglijun_2026_audit import ROOT, OUT, OWN, save, read, publisher_home
from dinglijun_2026_review import DOMAIN

CODES={s['code'] for s in OWN}
GROUP_FILES=[OUT/f'semantic-group{i}.json' for i in range(2,7)]+[OUT/'semantic-ijcai.json',OUT/'semantic-parser-audit.json']

def load_enrichment():
    extra={};verified_pdfs={}
    for p in sorted(OUT.glob('enrichment-*.json')):
        if p.name=='enrichment-changes.json':continue
        data=read(p)
        if not isinstance(data,(dict,list)):continue
        items=data.items() if isinstance(data,dict) else [(v.get('doi') or v.get('key',''),v) for v in data if isinstance(v,dict)]
        for k,v in items:
            if not isinstance(v,dict):continue
            doi=str(v.get('doi') or k.split('|')[-1]).lower()
            flat=dict(v)
            if isinstance(v.get('verified_metadata'),dict):flat.update(v['verified_metadata'])
            if p.name.startswith('enrichment-public-pdfs') and flat.get('pdf_url') and flat.get('pdf_verification'):
                verified_pdfs[doi]={'pdf_url':flat['pdf_url'],'pdf_verification':flat['pdf_verification']}
            dest=extra.setdefault(doi,{})
            for field,value in flat.items():
                if value in (None,[],{}):continue
                if field=='evidence_urls':value=list(dict.fromkeys(dest.get(field,[])+value))
                dest[field]=value
    # A DOI/title-matched OA location is a lead, not proof that a live PDF
    # is accessible. Only actual PDF responses enter verified_metadata.
    for doi,dest in extra.items():
        dest.pop('pdf_url',None);dest.pop('pdf_verification',None)
        if doi in verified_pdfs:dest.update(verified_pdfs[doi])
    return extra

def year_audit():
    p=OUT/'bibliography-discrepancy-reconciliation.json'
    return read(p) if p.exists() else {}

def inputs():
    work=read(OUT/'worklist.json');by={x['key']:x for x in work}
    cached={}
    ledger={}
    for p in GROUP_FILES:
        if p.exists():ledger.update(read(p))
    override=OUT/'semantic-root-adjudications.json'
    if override.exists():
        for key,patch in read(override).items():ledger[key].update(patch)
    # Missing records can be recovered only from the scoped full bibliography.
    for key in ledger:
        if key in by:continue
        code,pid=key.split('|',1)
        assert code in CODES,(code,pid)
        if code not in cached:cached[code]={str(x['id']):x for x in read(ROOT/f'metadata/{code}/2026/papers.json')}
        assert pid in cached[code],('review record missing from scoped bibliography',key)
        item={'key':key,'source_code':code,'record':cached[code][pid],'original_candidate':False,'additional_full_corpus_check':True}
        by[key]=item;work.append(item)
    # The full group ledger is authoritative over the parent's early pilot.
    missing=[w['key'] for w in work if w['key'] not in ledger]
    if missing:raise ValueError(f'{len(missing)} records have not received a semantic assessment: {missing[:8]}')
    extra=load_enrichment();dates=year_audit()
    official_ijcai={str(r['doi']).lower():r for r in read(OUT/'ijcai-catalogue.json')['records']}
    for w in work:
        r=w['record'];doi=str(r.get('doi') or r['id']).lower();e=extra.get(doi,{})
        md=w.setdefault('publisher_verified_metadata',{})
        md.pop('pdf_url',None);md.pop('pdf_verification',None)
        if e:
            md=w.setdefault('publisher_verified_metadata',{})
            for field in ['title','authors','abstract','keywords','article_type','url','pdf_url','code_url','project_url','dataset_url']:
                if e.get(field):md[field]=e[field]
            for field in ['declared_links','dataset_scope','warnings','version_note','cleaning_note','abstract_absence_confirmed','pdf_verification']:
                if e.get(field):md[field]=copy.deepcopy(e[field])
            urls=e.get('evidence_urls',[])
            w['enrichment_evidence']=list(dict.fromkeys(w.get('enrichment_evidence',[])+urls))
        if w['source_code']=='ijcai' and doi in official_ijcai:
            off=official_ijcai[doi];md=w.setdefault('publisher_verified_metadata',{})
            for field in ['title','authors','url','track','article_type']:
                if off.get(field):md[field]=copy.deepcopy(off[field])
            w['enrichment_evidence']=list(dict.fromkeys(w.get('enrichment_evidence',[])+[off['url'],'https://www.ijcai.org/proceedings/2026/']))
        if doi in dates:
            info=dates[doi];md=w.setdefault('publisher_verified_metadata',{})
            md['publication_year_scope']=info['resolution']
            md['publication_dates']=info.get('publication_dates',{})
            md['publication_year_note']=info['note']
            w['enrichment_evidence']=list(dict.fromkeys(w.get('enrichment_evidence',[])+info.get('evidence_urls',[])))
            if info['resolution']=='unknown' and ledger[w['key']]['decision']=='include':
                entry=copy.deepcopy(ledger[w['key']]);entry.update(decision='pending',labels=[],
                    rationale='科学AI贡献已有证据；官方引用编入2027卷期，但尚未核实2026在线首发日期，暂停本轮2026纳入。'+info['note'])
                ledger[w['key']]=entry
            if str(info.get('article_type','')).lower() in ('editorial','erratum','corrigendum','correction','retraction'):
                md['article_type']=info['article_type']
                entry=copy.deepcopy(ledger[w['key']]);entry.update(decision='exclude',domain=None,labels=[],
                    rationale='正式文献类型核实为'+info['article_type']+'，按类型排除。'+info.get('type_evidence',''))
                ledger[w['key']]=entry
    return work,ledger

def good_abstract(value):
    text=str(value or '').strip()
    return len(text)>=60 and not re.match(r'^(?:Highlights|Graphical abstract)\b',text,re.I)

def hash_records(rows):
    return hashlib.sha256(json.dumps(rows,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()

def build():
    work,ledger=inputs();baseline=read(OUT/'baseline.json');snapshot_at=baseline['snapshot_at']
    vocab=read(ROOT/'skills/ai4s-paper-review/references/tag-vocabulary.json')['tags']
    tags={t['label']:t for t in vocab}
    aliases={a:t['label'] for t in vocab for a in [t['label_en'],*t.get('aliases',[])]}
    baseline_changes={s['source_code']:s for s in read(OUT/'bibliography-changes.json')}
    original={s['code']:s for s in baseline['sources']}
    reviews=[];by_source=collections.defaultdict(list);candidates=collections.defaultdict(list)
    corrections=[]
    # Look up original metadata files once; always retain every full-corpus record.
    papers={code:read(ROOT/f'metadata/{code}/2026/papers.json') for code in CODES}
    pby={code:{str(x['id']):x for x in rows} for code,rows in papers.items()}
    all_extra=load_enrichment();dates=year_audit();work_keys={w['key'] for w in work}
    for code,rows in papers.items():
        for row in rows:
            doi=str(row.get('doi') or row['id']).lower();key=f"{code}|{row['id']}"
            if doi in dates:
                row['publication_year_scope']=dates[doi]['resolution']
                row['publication_year_evidence']=copy.deepcopy(dates[doi])
                at=dates[doi].get('article_type','')
                if str(at).lower() in ('editorial','erratum','corrigendum','correction','retraction'):
                    if row.get('article_type')!=at:row.setdefault('raw_metadata_before_dinglijun_review',{}).setdefault('article_type',row.get('article_type'))
                    row['article_type']=at
            # Also retain official metadata acquired while reconciling records
            # that never needed AI4S candidate review.
            if key in work_keys or doi not in all_extra:continue
            e=all_extra[doi]
            for field in ['abstract','keywords','article_type']:
                value=e.get(field)
                if field=='article_type' and str(row.get(field,'')).lower() in ('editorial','erratum','corrigendum','correction','retraction') and str(value).lower() in ('article','journal-article','journal article'):continue
                if value and value!=row.get(field):
                    if row.get(field):row.setdefault('raw_metadata_before_dinglijun_review',{}).setdefault(field,copy.deepcopy(row[field]))
                    row[field]=copy.deepcopy(value)
                    row['metadata_evidence_urls']=list(dict.fromkeys(row.get('metadata_evidence_urls',[])+e.get('evidence_urls',[])))
                    corrections.append({'key':key,'field':field,'evidence_urls':e.get('evidence_urls',[])})
    for w in work:
        decision=ledger[w['key']];r=copy.deepcopy(w['record']);code=w['source_code']
        assert r['venue']==code and r['year']==2026
        d=decision['decision'];assert d in ('include','exclude','pending','unreviewed')
        md=copy.deepcopy(w.get('publisher_verified_metadata') or {})
        if md.get('abstract_absence_confirmed'):md['abstract']=None
        abstract=md.get('abstract') or r.get('abstract')
        if d=='include' and (md.get('abstract_absence_confirmed') or not good_abstract(abstract)):
            raise ValueError('Included paper lacks a complete original abstract: '+w['key'])
        urls=list(w.get('enrichment_evidence') or [])
        if w.get('openalex_metadata',{}).get('id'):urls.append(w['openalex_metadata']['id'])
        doi=str(r.get('doi') or '')
        # DOI-matched publisher registrations establish identity, not live PDF access.
        if doi:
            md.setdefault('doi',doi)
            if code=='ijcai':urls.append('https://www.ijcai.org/proceedings/2026/'+doi.rsplit('/',1)[-1])
            else:urls.append('https://api.crossref.org/works/'+doi)
        if d=='include':
            md.setdefault('url',r.get('publisher_url') or r.get('url'))
            if r.get('abstract') and not md.get('abstract') and w.get('enrichment_evidence'):md['abstract']=r['abstract']
        md['evidence_urls']=list(dict.fromkeys(x for x in urls if x))
        labels=list(decision.get('labels') or [])
        if d=='include':
            domain=DOMAIN.get(decision.get('domain'))
            assert domain,('missing scientific domain',w['key'])
            labels=[domain]+labels
        else:labels=[]
        resolved=[]
        for label in labels:
            canonical=label if label in tags else aliases.get(label)
            if canonical is None:raise ValueError('Noncanonical review label '+repr(label)+' '+w['key'])
            if canonical not in resolved:resolved.append(canonical)
        review_tags=[{'axis':tags[label]['axis'],'label':label,'label_en':tags[label]['label_en'],
                      'evidence_location':decision.get('evidence_location') or '输入摘要',
                      'rationale':decision['rationale']} for label in resolved]
        rationale=decision['rationale']
        if not w.get('original_candidate') and d=='include':
            added=set(baseline_changes.get(code,{}).get('added_dois',[]))
            if str(r.get('doi') or r['id']).lower() in added:
                prefix='官网漏采补录。' if code=='ijcai' else '全量漏采补录（DOI登记及正式摘要核实）。'
            else:prefix='初筛漏筛补录。'
            rationale=prefix+rationale
        review={'schema_version':2,'batch_id':'dinglijun-2026-20261117','owner':'丁利军','snapshot_at':snapshot_at,
                'decision':d,'rationale':rationale,'verified_metadata':md,'tags':review_tags}
        if decision.get('evidence_quote'):review['evidence_quote']=decision['evidence_quote']
        r['ai4s_review']=review
        # All original candidates remain in the personal review, including
        # exclusions. Unverified new leads remain solely in the audit ledger.
        if w.get('original_candidate') or d=='include':reviews.append(r);by_source[code].append(r)
        corpus=pby[code][str(r['id'])]
        if md.get('abstract_absence_confirmed'):
            if corpus.get('abstract'):
                corpus.setdefault('raw_metadata_before_dinglijun_review',{}).setdefault('abstract',corpus['abstract'])
                corrections.append({'key':w['key'],'field':'abstract','evidence_urls':md['evidence_urls']})
            corpus['abstract']=None
            corpus['abstract_absence_confirmed']=True
        for field in ['abstract','keywords','article_type','code_url','project_url','dataset_url','pdf_url']:
            if field=='abstract' and md.get('abstract_absence_confirmed'):continue
            value=md.get(field)
            if not value and field in ('abstract','keywords') and not corpus.get(field):value=r.get(field)
            if value and value!=corpus.get(field):
                if corpus.get(field):
                    corpus.setdefault('raw_metadata_before_dinglijun_review',{}).setdefault(field,copy.deepcopy(corpus[field]))
                corpus[field]=copy.deepcopy(value)
                corpus.setdefault('metadata_evidence_urls',[])
                corpus['metadata_evidence_urls']=list(dict.fromkeys(corpus['metadata_evidence_urls']+md['evidence_urls']))
                corrections.append({'key':w['key'],'field':field,'evidence_urls':md['evidence_urls']})
        if good_abstract(corpus.get('abstract')) and corpus.get('screening_status')=='needs_abstract':
            corpus['screening_status']='needs_article_type' if corpus.get('article_type') in (None,'unknown') else 'ready'
        link_status=[{'url':item.get('url'),'resource_types':item.get('resource_types',[]),
                      'declaration_status':item.get('declaration_status'),
                      'access_status':item.get('access_check',{}).get('status'),
                      'http_status':item.get('access_check',{}).get('http_status'),
                      'public_download_verified':item.get('public_download_verified',False)}
                     for item in md.get('declared_links',[]) if isinstance(item,dict)]
        if link_status:corpus['resource_link_status']=copy.deepcopy(link_status)
        # The candidate set contains confirmed AI4S records plus unresolved
        # original candidates; confirmed out-of-scope records are retained above.
        if d=='include' or (w.get('original_candidate') and d in ('pending','unreviewed')):
            candidate=copy.deepcopy(w['record'])
            for field in ['abstract','keywords','article_type','code_url','project_url','dataset_url','pdf_url']:
                if md.get(field):
                    candidate[field]=copy.deepcopy(md[field])
            # Corrections are fully archived in papers.json, the review's raw
            # input fields, and audit evidence; avoid duplicating old abstracts
            # again in the yearly candidate download.
            candidate.pop('raw_metadata_before_dinglijun_review',None)
            if link_status:candidate['resource_link_status']=copy.deepcopy(link_status)
            if good_abstract(candidate.get('abstract')) and candidate.get('screening_status')=='needs_abstract':
                candidate['screening_status']='needs_article_type' if candidate.get('article_type') in (None,'unknown') else 'ready'
            # Final decisions and evidence-backed bilingual tags live in the
            # prescribed personal review file; candidate JSON stays metadata.
            candidates[code].append(candidate)
    assert len({(r['venue'],r['year'],r['id']) for r in reviews})==len(reviews)
    save(OUT/'worklist.json',work)
    old_corrections=read(OUT/'metadata-corrections.json') if (OUT/'metadata-corrections.json').exists() else []
    combined={}
    for item in old_corrections+corrections:
        key=(item['key'],item['field'])
        previous=combined.get(key,{})
        combined[key]=dict(item,evidence_urls=list(dict.fromkeys(previous.get('evidence_urls',[])+item.get('evidence_urls',[]))))
    save(OUT/'metadata-corrections.json',list(combined.values()))
    save(ROOT/'reviews/2026/dinglijun.json',reviews)
    snapshot=read(ROOT/'metadata/2026/snapshot.json')
    untouched_snapshot={s['source']:copy.deepcopy(s) for s in snapshot['sources'] if s['source'] not in CODES}
    summary=[];feedback=[]
    for s in OWN:
        code=s['code'];pr=papers[code];ca=candidates[code];rs=by_source[code]
        assert len({str(r['id']) for r in pr})==len(pr),('duplicate source id',code)
        save(ROOT/f'metadata/{code}/2026/papers.json',pr)
        save(ROOT/f'metadata/{code}/2026/ai4s.json',ca)
        counts=collections.Counter(r['ai4s_review']['decision'] for r in rs)
        pending=[r for r in rs if r['ai4s_review']['decision']=='pending']
        missing=sum(not good_abstract(r.get('abstract')) for r in ca)
        inc=[r for r in rs if r['ai4s_review']['decision']=='include']
        official_path=OUT/'official'/f'{code}.json';official=read(official_path) if official_path.exists() else {}
        official_total=None;reference_total=None;unresolved=0;coverage=[];evidence=[]
        if code=='ijcai':
            ref=read(OUT/'ijcai-catalogue.json');reference_total=ref['all_catalogue_count'];ref_source='IJCAI official proceedings'
            scope='2026正式论文集973条目录，分轨研究范围875条；原始8条Springer workshop书目另存并排除审核'
            query=ref['official_url'];coverage.append('已按稳定DOI对照官网目录；补采1条正式记录（官方编号0620）。8条旧Workshop记录保留在全量档案，不作为当届正式研究正文纳入。')
            # The official catalogue total is for a different scope from the
            # archived full corpus, so it is not placed in official_total.
        else:
            ref=read(OUT/'crossref'/f'{code}.json');reference_total=ref.get('retrieved');ref_source='Crossref publisher-registered bibliography'
            query=ref['query_url'];scope=ref['scope']
            regids={x['DOI'].lower() for x in ref.get('items',[])}
            localids={str(x.get('doi') or x['id']).lower() for x in pr}
            outside=localids-regids
            resolved_dates={doi for doi in outside if dates.get(doi,{}).get('resolution') in ('in_scope_2026','out_of_scope')}
            in_scope_dates={doi for doi in outside if dates.get(doi,{}).get('resolution')=='in_scope_2026'}
            unresolved=len(outside-resolved_dates)+len(regids-localids)
            reference_total+=len(in_scope_dates)
            if resolved_dates:
                ref_source+=' + publisher citation and first-publication date reconciliation'
                scope+='; additionally includes DOI-matched 2026 first-online records subsequently assigned to 2027 print volumes'
            if not ref.get('complete'):unresolved+=1
            coverage.append(f'完成登记DOI逐项比对及日期对账；参考范围{reference_total}条。历史快照中{len(outside)}条不在当前pub-date查询，已核实{len(in_scope_dates)}条在2026首发后编入2027卷；另{len(outside-resolved_dates)}条首发年份未核实，保留原始书目，暂缓2026纳入。')
            np=OUT/'nature-catalogues'/f'{code}.json'
            if np.exists():
                nat=read(np);official_total=nat.get('displayed_total');evidence.append(nat['url'])
                coverage.append(f'官网2026年度筛选显示{official_total}条；目录分页受cookie/无内容响应影响，未把仅第一页视为逐项官网全量。')
                if official_total is not None and official_total!=len(pr):unresolved+=abs(official_total-len(pr))
            elif official.get('access')!='accessible':
                coverage.append('官网直接请求受限（403/429或cookie检查）；公开摘要导出、浏览器及替代来源尝试详见本轮访问日志。')
            else:coverage.append('官网主页可访问，但未据主页推断年度总数。')
        evidence.extend([publisher_home(original[code]),query]);issues=[];actions=[]
        if unresolved:
            issues.append(f'全量口径仍有{unresolved}项参考/官网差异待核；详见本轮coverage.json。')
            actions.append('按DOI复核保留的历史条目与官方卷期日期；本轮不删除无法确认的书目。')
        if pending:
            issues.append(f'原候选{len(pending)}篇仍待定；其中现有候选有效原摘要缺漏{missing}篇，另有类型、AI角色或首发年份证据问题。')
            actions.append('仅对保留的待定原候选补正式原摘要、方法/文献类型或首发年份证据；无法取得时继续保留待定。')
        if not official_total and code!='ijcai' and not unresolved:
            coverage.append('以完整登记列表同口径逐项对账完成作为参考核验，不将参考数冒充官网数。')
        held=sum(not w.get('original_candidate') and w['source_code']==code and ledger[w['key']]['decision']=='pending' for w in work)
        f={'year':2026,'source_code':code,'snapshot_at':snapshot_at,'official_total':official_total,
           'official_scope':'官网2026年度全部文章类型筛选；与原始采集论文和在线优先口径区别另见说明' if official_total is not None else '尚未核实同口径官网总数',
           'coverage_note':' '.join(coverage),'evidence_urls':list(dict.fromkeys(x for x in evidence if x)),
           'issues':issues,'next_actions':actions,
           'reference_check':{'status':'complete' if unresolved==0 else 'partial','source':ref_source,'total':reference_total,'scope':scope,'query_url':query,'checked_at':'2026-11-17','unresolved':unresolved},
           'candidate_total':len(ca),'candidate_missing_abstract':missing,'reviewed':len(rs),'included':len(inc),'excluded':counts['exclude'],'pending':counts['pending'],
           'unconfirmed_new_leads_held_out':held,'full_corpus_title_abstract_search':True,'audit_path':'reviews/2026/dinglijun/audit-20261117/report.md'}
        feedback.append(f)
        st=next(x for x in snapshot['sources'] if x['source']==code)
        st.update(papers=len(pr),with_abstract=sum(good_abstract(x.get('abstract')) for x in pr),ai4s=len(ca),duplicate_ids=0,owner_audit_checked_at='2026-11-17')
        summary.append({'source_code':code,'title':s['title'],'papers_before':original[code]['papers'],'papers_after':len(pr),
                        'metadata_added':baseline_changes.get(code,{}).get('added_count',0),'original_candidates':original[code]['candidates'],
                        'candidate_total':len(ca),'included':len(inc),'excluded':counts['exclude'],'pending':counts['pending'],
                        'new_includes':sum(not w.get('original_candidate') and w['source_code']==code and ledger[w['key']]['decision']=='include' for w in work),
                        'missing_valid_abstract':missing,'unconfirmed_new_leads_held_out':held,'reference_unresolved':unresolved})
    assert untouched_snapshot=={s['source']:s for s in snapshot['sources'] if s['source'] not in CODES}
    save(ROOT/'metadata/2026/snapshot.json',snapshot)
    save(ROOT/'reviews/2026/feedback/dinglijun.json',feedback)
    save(OUT/'coverage.json',feedback);save(OUT/'summary.json',summary)
    totals={k:sum(x[k] for x in summary) for k in ['papers_before','papers_after','metadata_added','original_candidates','candidate_total','included','excluded','pending','new_includes','missing_valid_abstract','unconfirmed_new_leads_held_out']}
    totals.update(sources=len(summary),semantic_assessments=len(ledger),main_commit=baseline['commit'])
    save(OUT/'totals.json',totals)
    annual_sync(candidates)
    report(summary,totals)
    print(json.dumps(totals,ensure_ascii=False),flush=True)

def annual_sync(candidates):
    path=ROOT/'metadata/2026/ai4s.json';raw=path.read_text();dec=json.JSONDecoder();pos=raw.index('[')+1;chunks=[];others=[];old=0
    while True:
        while pos<len(raw) and raw[pos] in ' \r\n\t,':pos+=1
        if raw[pos]==']':break
        start=pos;r,end=dec.raw_decode(raw,pos);pos=end
        if r.get('venue') in CODES:old+=1;continue
        chunks.append(raw[start:end]);others.append(r)
    other_hash=hash_records(others)
    own=[r for s in OWN for r in candidates[s['code']]]
    # Compact only this owner's replacements. Other records keep their original
    # serialized objects, preventing unrelated data changes and file-size growth.
    replacement=[json.dumps(r,ensure_ascii=False,separators=(',',':')) for r in own]
    output='[\n  '+',\n  '.join(chunks+replacement)+'\n]\n'
    assert len(output.encode())<100*1024*1024,'Annual candidate JSON exceeds GitHub regular-file limit'
    tmp=path.with_suffix('.json.tmp');tmp.write_text(output);tmp.replace(path)
    save(OUT/'annual-sync-validation.json',{'other_owner_records':len(others),'other_owner_records_sha256':other_hash,'replaced_own_records':old,'current_own_records':len(own),'bytes':path.stat().st_size,'other_owner_objects_unchanged':True})

def report(summary,totals):
    lines=['# 丁利军 2026 年采集与精筛交付','',f"输入主分支：`{totals['main_commit']}`；核查日期：2026-11-17。范围为2026分工表中丁利军的49个来源（48刊+IJCAI）。",'',
      f"全量元数据 {totals['papers_before']:,} → {totals['papers_after']:,} 条，补采 {totals['metadata_added']:,} 条。逐篇语义核查 {totals['semantic_assessments']:,} 条（原候选、漏筛线索及额外全量题名查漏）。",'',
      f"正式个人交付：纳入 {totals['included']:,}、排除 {totals['excluded']:,}、保留待定 {totals['pending']:,}。确认漏筛后新增纳入 {totals['new_includes']:,} 条。未确认的新线索 {totals['unconfirmed_new_leads_held_out']:,} 条仅存审计，不加入AI4S候选。",'',
      '## 处理口径','',
      '- 仅自然科学、生医、具体科学工程及信息系统研究；人文社科、教育、经管商业不补入候选。',
      '- 逐篇判断AI实际作用；生物neural、群体感应AI-2、自动生成图注提示、仅展望和通用器件MNIST演示不能作为AI4S依据。',
      '- 所有纳入条目具备原摘要及共享中英文词表标签。原候选排除记录仍保存在个人审核清单，缺证的原候选继续待定。',
      '- 精筛标签以个人审核文件的`ai4s_review.tags`为准；原`ai4s_tags`等初筛字段保留，候选文件不是最终纳入集。',
      '- 完整登记列表是Crossref参考口径，不冒称出版社官网全量；正式出版、在线优先、卷期及文献类型差异保留证据。',
      '- 全量papers保留全部原记录；补回或纠正元数据有来源，纠正前有值的字段另存raw_metadata_before_dinglijun_review。',
      '- 2026尚未结束，本轮覆盖截至核查时可取得的已登记/已发布记录。', '',
      '- 2027卷年不直接判为跨年排除：89条历史记录另核首发日期，36条证实2026首发，53条日期未核实；其中科学AI条目也须暂停2026纳入。',
      '- 代码、项目和数据链接区分作者声明、未来发布与实际访问状态；HEAD成功不代表已下载验证数据内容。', '',
      '## 来源结果','',
      '|来源编号|刊会|全量记录|补采|纳入|原候选排除|原候选待定|确认漏筛纳入|',
      '|---|---|---:|---:|---:|---:|---:|---:|']
    for s in summary:
        cells=[f"[{s['source_code']}](../../../../metadata/{s['source_code']}/2026/)"]+[str(s[k]).replace('|','/') for k in ['title','papers_after','metadata_added','included','excluded','pending','new_includes']]
        lines.append('|'+'|'.join(cells)+'|')
    lines+=['','## 尚未解决的事项','',
      f"候选中仍有 {totals['missing_valid_abstract']} 条缺少可用原摘要；此外少量条目仍有文献类型、AI角色或题名摘要一致性疑问。逐篇理由见个人JSON，来源级问题及后续行动见feedback。",'',
      '官网或替代源的403/429、cookie检查、无摘要以及浏览器导出情况均有记录。无法确认的官方总量不填零，未将待定清空或标成完成。', '',
      '## 文件','',
      '- `reviews/2026/dinglijun.json`：全部原候选及确认补录的逐篇审核、双语标签、核实元数据。',
      '- `reviews/2026/feedback/dinglijun.json`：49个来源的机器可读阶段反馈。',
      '- `metadata/<本人来源>/2026/papers.json` 与 `ai4s.json`：仅本人元数据修订及候选同步。',
      '- `metadata/2026/ai4s.json` 与 `snapshot.json`：仅本人来源的年度同步；其他来源论文对象和快照来源项保持一致。',
      '- 年度全量`metadata/2026/papers.json`保留仓库既有LFS指针；本轮全量补采以49个来源目录内的`papers.json`为准。',
      '- 本目录保留来源清单、语义审核轨迹、补证、逐项对账和验证结果。原始抓取响应以压缩证据归档保存。','']
    pdf_path=OUT/'public-pdf-verification-summary.json'
    if pdf_path.exists():
        pdf=read(pdf_path)
        if 'final_included_verified_pdf_count' in pdf:
            lines+=['## 公开资源核验','',
                f"对 {pdf['candidate_dois']:,} 个DOI完成公开PDF候选核验（共发现 {pdf['candidate_urls']:,} 个具体地址，找到有效PDF后停止该篇其余探测）；最终纳入论文中 {pdf['final_included_verified_pdf_count']:,} 篇找到实际PDF响应。正式版、接收稿和投稿稿按来源版本分别记录。",'',
                '返回HTML、403或请求错误的地址保留为未验证；未发现具体地址的论文未被声明为无公开版本。代码和数据链接另区分作者声明、将来发布与访问状态。','']
    (OUT/'report.md').write_text('\n'.join(lines))

if __name__=='__main__':
    if sys.argv[1]=='check':
        w,l=inputs();print('WORKLIST',len(w),'LEDGER',len(l),'decisions',dict(collections.Counter(x['decision'] for x in l.values())))
    elif sys.argv[1]=='build':build()
