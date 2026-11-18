"""Apply evidence-backed 2026 decisions and explicit archival/year scope.

Raw reviews and prior audits remain readable; only this owner's sources change.
"""
import collections
import copy
import datetime
import hashlib
import json
import pathlib
import subprocess
import sys

ROOT=next(p for p in pathlib.Path(__file__).resolve().parents if (p/'teacher_sources.json').exists())
OUT=pathlib.Path(__file__).resolve().parent
OLD=OUT.parent/'audit-20261117'
sys.path.insert(0,str(OLD/'scripts'))
import dinglijun_2026_finalize as previous
from dinglijun_2026_audit import read, save, OWN

PREVIOUS='56e227f14ab2152ce71622dc489659bd66a45451'
CODES={s['code'] for s in OWN}
NOW=datetime.datetime.now(datetime.timezone.utc).isoformat()
SNAPSHOT=read(OLD/'baseline.json')['snapshot_at']
PERSONAL='reviews/2026/dinglijun.json'
FEEDBACK='reviews/2026/feedback/dinglijun.json'
SCOPE_AUDIT='reviews/2026/dinglijun/closure-20261118/review-scope-audit.json'

def original(path,ref=PREVIOUS):
    return json.loads(subprocess.check_output(['git','-C',str(ROOT),'show',ref+':'+path]))

def key(r):return r['venue']+'|'+str(r['id'])
def doi(r):return str(r.get('doi') or r['id']).lower()
def digest(value):return hashlib.sha256(json.dumps(value,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def evidence_merge(a,b):return list(dict.fromkeys((a or [])+(b or [])))

def tag_records(entry):
    vocab=read(ROOT/'skills/ai4s-paper-review/references/tag-vocabulary.json')['tags']
    by={t['label']:t for t in vocab};aliases={a:t['label'] for t in vocab for a in [t['label_en'],*t.get('aliases',[])]}
    if entry['decision']!='include':return []
    labels=list(entry.get('labels') or [])
    domain=previous.DOMAIN.get(entry.get('domain'))
    if domain:labels.insert(0,domain)
    canonical=[]
    for label in labels:
        label=label if label in by else aliases.get(label)
        assert label in by,('noncanonical tag',entry,label)
        if label not in canonical:canonical.append(label)
    assert any(by[x]['axis']=='domain' for x in canonical),entry
    return [dict(axis=by[x]['axis'],label=x,label_en=by[x]['label_en'],
                 rationale=entry['rationale'],evidence_location=entry.get('evidence_location') or '正式原摘要') for x in canonical]

def apply_decision(record,entry):
    review=record['ai4s_review'];md=review.setdefault('verified_metadata',{})
    incoming=copy.deepcopy(entry.get('verified_metadata') or {})
    if 'year' in incoming:
        incoming['formal_year']=incoming.pop('year')
    # Concrete URLs and successful PDF checks have separate meanings.
    if incoming.get('pdf_url'):
        proof=incoming.get('pdf_verification') or {}
        if not (proof.get('verified_public_pdf') is True and proof.get('url')==incoming['pdf_url']):
            incoming.pop('pdf_url',None)
    urls=evidence_merge(md.get('evidence_urls'),incoming.pop('evidence_urls',[]))
    urls=evidence_merge(urls,entry.get('evidence_urls',[]))
    for field,value in incoming.items():
        if value is not None or field=='abstract':md[field]=value
    md['evidence_urls']=urls
    if incoming.get('abstract_absence_confirmed') or incoming.get('abstract_status')=='not_provided_by_publisher':md['abstract']=None
    review.update(decision=entry['decision'],rationale=entry['rationale'],tags=tag_records(entry),
                  batch_id='dinglijun-2026-closure-20261118',checked_at=NOW)
    if entry.get('evidence_quote'):review['evidence_quote']=entry['evidence_quote']
    review['evidence_location']=entry.get('evidence_location')
    review['prior_decision']='pending'
    if review['decision']=='include':
        assert previous.good_abstract(md.get('abstract') or record.get('abstract')),('missing original abstract',key(record))
    return record

def build():
    records=original(PERSONAL);by={key(r):r for r in records}
    pending={k for k,r in by.items() if r['ai4s_review']['decision']=='pending'}
    assert len(pending)==51
    decisions={}
    for group in ('elsevier','biomed','reviews','methods'):
        data=read(OUT/f'decisions-{group}.json');assert not decisions.keys() & data.keys();decisions.update(data)
    date_only={'j-7db6bc49fe|10.1016/j.ress.2026.113795','j-7db6bc49fe|10.1016/j.ress.2026.113797'}
    assert set(decisions)==pending-date_only
    assert all(d['decision'] in ('include','exclude') for d in decisions.values())
    for k,entry in decisions.items():apply_decision(by[k],entry)
    dates=read(OLD/'bibliography-discrepancy-reconciliation.json')
    new_dates=read(OUT/'date-reconciliation.json')
    for d,entry in new_dates.items():
        dates[d]=dict(dates[d],**entry)
    # The publication year is unknown; do not fabricate a date or a scientific
    # exclusion. Preserve the two records as pending archival references.
    for k in date_only:
        r=by[k];audit=dates[doi(r)];assert audit['resolution']=='unknown' and audit['official_citation']['publication_year']==2027
        a=r['ai4s_review'];a.update(batch_id='dinglijun-2026-closure-20261118',checked_at=NOW,
            rationale='科学AI作用已确认，正式引用属于2027卷期，尚无可核实的2026首发日期。本条保留待证及原始数据，单列跨年档案参考，不属于当前已核实年份的2026候选。',tags=[])
        a['review_scope']={'status':'reference_only','reason':'unverified_catalogue_record_outside_current_candidates',
                           'checked_by':'丁利军','checked_at':NOW,'audit_file':SCOPE_AUDIT,
                           'formal_year':2027,'first_online_year':None,'reopen_when':'出版社或原始机构来源核实2026首发日期'}
        md=a.setdefault('verified_metadata',{});md['publication_year_scope']='unknown';md['publication_dates']=audit
        md['evidence_urls']=evidence_merge(md.get('evidence_urls'),audit.get('evidence_urls'))
    hiv=read(OUT/'hiv-zero-candidate-audit.json')
    # Real, DOI-matched AI leads that were actually checked, never placeholders.
    for record in hiv['review_records']:
        r=copy.deepcopy(record);k=key(r);assert k not in by and r['venue']=='j-0cb9ab9944'
        entry=r.pop('ai4s_review');r['ai4s_review']={'schema_version':2,'owner':'丁利军','snapshot_at':SNAPSHOT,'verified_metadata':{}}
        assert entry['decision']=='exclude';apply_decision(r,entry);r['ai4s_review']['prior_decision']='full_corpus_lead_checked'
        records.append(r);by[k]=r
    papers={code:read(ROOT/f'metadata/{code}/2026/papers.json') for code in CODES}
    for r in read(OUT/'new-papers-npjamd.json'):
        r=copy.deepcopy(r);r.pop('ai4s_review',None)
        if r['id'] not in {x['id'] for x in papers['npjamd']}:papers['npjamd'].append(r)
    corpus={code:{str(r['id']):r for r in rows} for code,rows in papers.items()}
    for r in records:
        a=r['ai4s_review'];md=a.get('verified_metadata') or {};target=corpus[r['venue']][str(r['id'])]
        absent=bool(md.get('abstract_absence_confirmed') or md.get('abstract_status')=='not_provided_by_publisher')
        for field in ('abstract','keywords','article_type','code_url','project_url','dataset_url','pdf_url'):
            value=md.get(field)
            if field=='abstract' and absent:value=None
            elif value in (None,[],{}):continue
            if target.get(field)!=value:
                if target.get(field) not in (None,[],{}):target.setdefault('raw_metadata_before_dinglijun_review',{}).setdefault(field,copy.deepcopy(target[field]))
                target[field]=copy.deepcopy(value)
                target['metadata_evidence_urls']=evidence_merge(target.get('metadata_evidence_urls'),md.get('evidence_urls'))
        if absent:target['abstract_absence_confirmed']=True
    for code,rows in papers.items():
        for r in rows:
            if doi(r) in dates:
                r['publication_year_scope']=dates[doi(r)]['resolution']
                r['publication_year_evidence']=copy.deepcopy(dates[doi(r)])
                if dates[doi(r)].get('reference_only'):r['archive_scope']='2027_formal_volume_unverified_2026_first_online'
        save(ROOT/f'metadata/{code}/2026/papers.json',rows)
    candidates={code:[] for code in CODES}
    previous_candidates={code:{str(r['id']):r for r in original(f'metadata/{code}/2026/ai4s.json')} for code in CODES}
    for r in records:
        a=r['ai4s_review']
        if a['decision']!='include':continue
        md=a.get('verified_metadata') or {};assert dates.get(doi(r),{}).get('resolution')!='unknown'
        item=copy.deepcopy(previous_candidates[r['venue']].get(str(r['id']),corpus[r['venue']][str(r['id'])]));item.pop('ai4s_review',None);item.pop('raw_metadata_before_dinglijun_review',None)
        for field in ('abstract','keywords','article_type','code_url','project_url','dataset_url','pdf_url'):
            if md.get(field):item[field]=copy.deepcopy(md[field])
        assert previous.good_abstract(item.get('abstract'));candidates[r['venue']].append(item)
    for code,rows in candidates.items():save(ROOT/f'metadata/{code}/2026/ai4s.json',rows)
    save(ROOT/PERSONAL,records)
    old_feedback={r['source_code']:r for r in original(FEEDBACK)}
    baseline=read(OUT/'continuation-baseline.json');main=baseline['integration_base_commit']
    snapshot=read(ROOT/'metadata/2026/snapshot.json');feedback=[];summary=[];scope_sources=[]
    workshop=read(OUT/'workshop-archive-identities.json')
    for s in OWN:
        code=s['code'];rows=papers[code];ca=candidates[code];rs=[r for r in records if r['venue']==code]
        active=[r for r in rs if r['ai4s_review'].get('review_scope',{}).get('status')!='reference_only']
        counts=collections.Counter(r['ai4s_review']['decision'] for r in active)
        original_row=old_feedback[code]
        if code=='ijcai':
            cat=read(OLD/'ijcai-catalogue.json');matched={str(r.get('doi') or r['id']).lower():'IJCAI official proceedings' for r in cat['records']}
            matched.update({d:'Crossref registered Springer workshop archive' for d,e in workshop.items() if e.get('identity_doi_match')})
            url=cat['official_url'];source='IJCAI official 2026 catalogue + explicitly separated Springer workshop archive'
            scope='全量采集档案口径：2026正式目录973条（研究轨875条），另保留8条已核实Springer Workshop历史档案；后者不作为当届正式研究论文纳入。'
        elif code=='npjamd':
            cat=read(OUT/'npj-browser-catalogue-ids.json');assert cat['complete']
            matched={d:'Nature 2026 official catalogue, 13 pages, 241 unique DOIs' for d in cat['distinct_ids']}
            url='https://www.nature.com/npjamd/articles?year=2026';source='Nature official annual catalogue'
            scope='官网2026年度全部文章类型，正常浏览器逐页读取13页，241条及241个唯一DOI；补齐3条后逐DOI对称差为0。'
        else:
            cat=read(OLD/f'crossref/{code}.json');assert cat['complete']
            matched={r['DOI'].lower():'Complete publisher-registered Crossref 2026 list' for r in cat['items']}
            for d,e in dates.items():
                if e.get('source_code')==code or d in {doi(r) for r in rows}:
                    matched.setdefault(d,'DOI/title-matched publisher citation of retained 2027-volume archive')
            url=cat['query_url'];source='Crossref full 2026 registered bibliography + individually verified publisher citations of historical archive extras'
            scope='全量采集档案身份口径：完整Crossref 2026 pub-date登记列表，加逐DOI及题名核实的2027卷期历史归档条目。并集用于核对原始档案完整性，不把归档窗口或DOI年份当作2026首发证据；无2026首发证据的跨年记录不加入当前2026候选。'
        ids={doi(r) for r in rows};assert ids==set(matched),('unmatched archive identity',code,ids-set(matched),set(matched)-ids)
        check={'status':'complete','source':source,'total':len(rows),'scope':scope,'query_url':url,'checked_at':NOW,'unresolved':0}
        report={'source_code':code,'year':2026,'owner':'丁利军','snapshot_at':SNAPSHOT,'reference_check':check,
                'matched_reference_ids':[str(r['id']) for r in rows],'reference_identity_sources':matched,
                'duplicates':0,'missing':[],'extra':[],'scope':scope}
        if code=='npjamd':report.update(official_total=241,matched_official_ids=cat['distinct_ids'])
        save(ROOT/f'metadata/{code}/2026/catalogue-reconciliation.json',report)
        audit={'source_code':code,'year':2026,'owner':'丁利军','snapshot_at':SNAPSHOT,
               'input_main_commit':main,'details_file':f'metadata/{code}/2026/catalogue-reconciliation.json',
               'raw_sha256':hashlib.sha256((ROOT/f'metadata/{code}/2026/papers.json').read_bytes()).hexdigest(),
               'raw_identities':[{'id':r['id'],'venue':code,'year':2026} for r in rows],'additions':[],'report':report}
        scope_proof={'status':'current_candidates_and_verified_additions','checked_by':'丁利军','checked_at':NOW,
                     'candidate_file':'metadata/2026/ai4s.json','review_file':PERSONAL,'audit_file':SCOPE_AUDIT,
                     'candidate_count':len(ca),'candidate_ids_sha256':hashlib.sha256(json.dumps(sorted(str(r['id']) for r in ca),ensure_ascii=False,separators=(',',':')).encode()).hexdigest(),
                     'scope_instruction':'只处理丁利军负责来源的2026年候选及有证据的补录；正式2027卷而无2026首发证据的记录保留为跨年参考，不把未知日期改成已知。'}
        reconciliation={'current_raw_count':len(rows),'same_scope_missing':0,'same_scope_extra':0,'same_scope_duplicate':0}
        f={'year':2026,'source_code':code,'owner':'丁利军','github_username':'dinglijun','snapshot_at':SNAPSHOT,
           'official_total':241 if code=='npjamd' else None,'official_scope':scope if code=='npjamd' else '',
           'reference_check':check,'coverage_note':scope+' 原始非候选缺摘要数字保留，精筛只要求当前AI4S候选及纳入论文原摘要。',
           'evidence_urls':evidence_merge(original_row.get('evidence_urls'),[url]),'issues':[],'next_actions':[],
           'work_status':'complete','candidate_count':len(ca),'candidate_missing_abstract':0,
           'own_review_count':len(active),'own_review_counts':{d:counts[d] for d in ('include','exclude','pending','unreviewed')},
           'review_scope':scope_proof,'catalogue_audit':audit,'catalogue_reconciliation':reconciliation,
           'archival_reference_review_count':len(rs)-len(active)}
        if original_row.get('official_total') is not None and code!='npjamd':
            f['previous_publisher_displayed_total']={'value':original_row['official_total'],'scope':original_row['official_scope'],
                'status':'historical_count_only_not_relabelled_as_current_full_catalogue_identity_audit'}
        st=next(x for x in snapshot['sources'] if x['source']==code)
        if st['state']=='abstract_incomplete':
            f['collection_state_resolution']={'status':'resolved_for_candidate_review','original_state':'abstract_incomplete',
                'reason':'full_reference_catalogue_candidates_complete','checked_by':'丁利军','checked_at':NOW,'evidence_urls':[url]}
        if code=='j-0cb9ab9944':
            assert not ca and hiv['reference_check']['status']=='complete' and counts['exclude']>0
            st.setdefault('state_before_owner_completion',st['state']);st['state']='completed'
            st['completion_scope']='DOI档案完整核验及所有AI查漏线索终判完成；非候选摘要缺漏仍如实保留，不声称全量摘要齐全。'
            st['completion_evidence']='reviews/2026/dinglijun/closure-20261118/hiv-zero-candidate-audit.json'
            st['completion_checked_by']='丁利军';st['completion_checked_at']=NOW
            f.pop('collection_state_resolution',None)
        st.update(papers=len(rows),with_abstract=sum(bool(str(r.get('abstract') or '').strip()) for r in rows),ai4s=len(ca),owner_audit_checked_at=NOW)
        feedback.append(f);scope_sources.append({'source_code':code,'candidate_ids':[r['id'] for r in ca],
            'reference_only_ids':[r['id'] for r in rs if r not in active],'counts':f['own_review_counts']})
        summary.append({'source_code':code,'title':s['title'],'papers':len(rows),'candidate_count':len(ca),**f['own_review_counts'],
                        'reference_only':len(rs)-len(active)})
    save(ROOT/'metadata/2026/snapshot.json',snapshot);save(ROOT/FEEDBACK,feedback)
    save(OUT/'effective-publication-dates.json',dates);save(OUT/'summary.json',summary)
    save(OUT/'review-scope-audit.json',{'owner':'丁利军','year':2026,'snapshot_at':SNAPSHOT,'input_main_commit':main,
        'source_count':49,'sources':scope_sources,'reference_only_keys':sorted(date_only),
        'reference_only_reason':'2027正式卷期已确认，2026首发日期未知；保留待证记录但不计入当前年份候选或完成的科学纳入数量。'})
    previous.OUT=OUT;previous.annual_sync(candidates)
    totals={'sources':49,'papers':sum(len(x) for x in papers.values()),'included':sum(r['ai4s_review']['decision']=='include' for r in records),
        'excluded':sum(r['ai4s_review']['decision']=='exclude' for r in records),'reference_only_pending':len(date_only),
        'active_pending':sum(s['pending'] for s in summary),'candidate_count':sum(len(x) for x in candidates.values()),
        'previous_pending_resolved':49,'original_candidate_records_preserved':1688,'personal_records':len(records)}
    save(OUT/'totals.json',totals);print(json.dumps(totals,ensure_ascii=False))

if __name__=='__main__':build()
