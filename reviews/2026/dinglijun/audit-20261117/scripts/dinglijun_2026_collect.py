"""Apply DOI-matched source metadata and retrieve reliable abstract fallbacks."""
import sys
sys.path.insert(0,'/tmp/dlj-2026-deps')
import concurrent.futures as cf
import hashlib
import json
import pathlib
import re
import time
import urllib.parse
from bs4 import BeautifulSoup
from dinglijun_2026_audit import ROOT, OUT, OWN, save, read, fetch
from dinglijun_2026_enrich import key, signal, publisher_one
from nature_meta import record_from_crossref

def merge_bibliographies():
    changes=[];work=read(OUT/'worklist.json');workkeys={w['key'] for w in work}
    old_changes={x['source_code']:x for x in read(OUT/'bibliography-changes.json')} if (OUT/'bibliography-changes.json').exists() else {}
    for s in OWN:
        code=s['code'];path=ROOT/f'metadata/{code}/2026/papers.json';rows=read(path);by={key(r):r for r in rows}
        cp=OUT/'crossref'/f'{code}.json';added=[];filled=[]
        if cp.exists():
            data=read(cp)
            for item in data.get('items',[]):
                doi=item['DOI'].lower()
                # A registration query is a reference bibliography, not an
                # assertion that the publisher's whole annual catalogue is complete.
                r=record_from_crossref(item,code,2026,(item.get('ISSN') or [''])[0])
                r['publisher_url']=((item.get('resource') or {}).get('primary') or {}).get('URL')
                r['publication_dates']={k:item[k]['date-parts'] for k in ['published','published-online','published-print','issued'] if k in item and 'date-parts' in item[k]}
                # Crossref subjects are index terms, not author keywords.
                r['index_subjects']=r.get('keywords',[]);r['keywords']=[]
                if doi not in by:
                    rows.append(r);by[doi]=r;added.append(doi)
                elif not by[doi].get('abstract') and r.get('abstract'):
                    by[doi]['abstract']=r['abstract'];by[doi]['source']=str(by[doi].get('source') or '')+'+crossref.org';filled.append(doi)
        if code=='ijcai':
            data=read(OUT/'ijcai-catalogue.json')
            for r in data['records']:
                if key(r) not in by:rows.append(r);by[key(r)]=r;added.append(key(r))
        save(path,rows)
        for r in rows:
            k=f"{code}|{r['id']}"
            if k not in workkeys and signal(r):work.append({'key':k,'source_code':code,'original_candidate':False,'record':r,'supplemental_bibliography':True});workkeys.add(k)
        old=old_changes.get(code,{})
        added=list(dict.fromkeys(old.get('added_dois',[])+added));filled=list(dict.fromkeys(old.get('crossref_abstracts_filled',[])+filled))
        changes.append({'source_code':code,'added_count':len(added),'added_dois':added,'crossref_abstracts_filled':filled})
    # Existing keys and indices stay stable for reviewers already working.
    for w in work:
        p=ROOT/f"metadata/{w['source_code']}/2026/papers.json"
        # Candidate records retain all original candidate-specific metadata.
        if w['original_candidate'] and not w['record'].get('abstract'):
            rr=next((x for x in read(p) if key(x)==key(w['record'])),None)
            if rr and rr.get('abstract'):w['record']['abstract']=rr['abstract']
    save(OUT/'worklist.json',work);save(OUT/'bibliography-changes.json',changes)
    print('BIBLIOGRAPHY ADDED',sum(x['added_count'] for x in changes),'worklist',len(work),flush=True)

def oa_batch(pair):
    index,dois=pair;dest=OUT/'openalex'/f'batch-{index:03}.json'
    if dest.exists() and read(dest).get('success'):return read(dest)
    params={'filter':'doi:'+'|'.join(dois),'per-page':str(len(dois)),
            'select':'id,doi,title,abstract_inverted_index,primary_location,locations,type,publication_date,keywords'}
    url='https://api.openalex.org/works?'+urllib.parse.urlencode(params)
    result={'source':'OpenAlex','query_url':url,'requested_dois':dois,'checked_at':'2026-11-17','success':False,'records':[]}
    try:
        raw,_,_,_=fetch(url,55);data=json.loads(raw)
        for x in data.get('results',[]):
            doi=str(x.get('doi') or '').lower().split('doi.org/')[-1]
            if doi not in dois:continue
            inv=x.pop('abstract_inverted_index',None) or {}
            pos=sorted((p,word) for word,positions in inv.items() for p in positions)
            x['abstract']=' '.join(word for _,word in pos) or None;x['doi']=doi
            result['records'].append(x)
        result['success']=True
    except Exception as e:result['error']=str(e)
    save(dest,result)
    print('OPENALEX',index,len(dois),len(result['records']),sum(bool(x.get('abstract')) for x in result['records']),result.get('error',''),flush=True)
    return result

def openalex():
    work=read(OUT/'worklist.json');dois=list(dict.fromkeys(key(x['record']) for x in sorted(work,key=lambda w:(not w['original_candidate'],bool(w['record'].get('abstract')))) if key(x['record']).startswith('10.')))
    # Keep the public OpenAlex endpoint at two concurrent queries.
    batches=[(i,dois[k:k+70]) for i,k in enumerate(range(0,len(dois),70))]
    with cf.ThreadPoolExecutor(max_workers=2) as ex:
        for _ in ex.map(oa_batch,batches):pass

def epmc():
    work=read(OUT/'worklist.json');dois=list(dict.fromkeys(key(w['record']) for w in work if not w['record'].get('abstract') and key(w['record']).startswith('10.')))
    for i,start in enumerate(range(0,len(dois),25)):
        ds=dois[start:start+25];dest=OUT/'europepmc'/f'batch-{i:03}.json'
        if dest.exists():continue
        query='('+' OR '.join('DOI:"'+doi+'"' for doi in ds)+')'
        url='https://www.ebi.ac.uk/europepmc/webservices/rest/search?'+urllib.parse.urlencode({'query':query,'format':'json','resultType':'core','pageSize':100})
        result={'source':'Europe PMC','query_url':url,'requested_dois':ds,'checked_at':'2026-11-17','success':False,'records':[]}
        try:
            raw,_,_,_=fetch(url,35);data=json.loads(raw)
            for r in data.get('resultList',{}).get('result',[]):
                if str(r.get('doi') or '').lower() not in ds:continue
                result['records'].append(r)
            result['success']=True
        except Exception as e:result['error']=str(e)
        save(dest,result);print('EUROPEPMC',i,len(ds),len(result['records']),result.get('error',''),flush=True)

def apply_enrichment():
    supplements={}
    for p in (OUT/'openalex').glob('*.json'):
        data=read(p)
        for x in data.get('records',[]):
            supplements.setdefault(x['doi'],{}).update(openalex=x)
    for p in (OUT/'europepmc').glob('*.json'):
        data=read(p)
        for x in data.get('records',[]):supplements.setdefault(x['doi'].lower(),{}).update(europepmc=x)
    pub={}
    for p in (OUT/'publisher-records').glob('*.json'):
        x=read(p)
        if x.get('success'):pub[x['key']]=x
    changed=[];work=read(OUT/'worklist.json')
    for w in work:
        r=w['record'];s=supplements.get(key(r),{});p=pub.get(w['key'],{});md=p.get('metadata',{})
        before=(bool(r.get('abstract')),bool(r.get('keywords')))
        evidence=w.setdefault('enrichment_evidence',[])
        if md.get('abstract'):
            # Retain the original input elsewhere; explicitly mark any verified correction.
            w['publisher_verified_metadata']=md
            if not r.get('abstract'):r['abstract']=md['abstract']
            evidence.append(p.get('url'))
        if not r.get('abstract'):
            e=s.get('europepmc',{});a=e.get('abstractText')
            if a:
                r['abstract']=BeautifulSoup(a,'lxml').get_text(' ',strip=True);evidence.append('https://europepmc.org/article/'+str(e.get('source','MED'))+'/'+str(e.get('id')))
            elif s.get('openalex',{}).get('abstract'):
                a=s['openalex'];r['abstract']=a['abstract'];evidence.append(a['id'])
        if not r.get('keywords') and md.get('keywords'):r['keywords']=md['keywords']
        e=s.get('europepmc',{})
        if not r.get('keywords') and e.get('keywordList',{}).get('keyword'):
            r['keywords']=e['keywordList']['keyword'];evidence.append('https://europepmc.org/article/'+str(e.get('source','MED'))+'/'+str(e.get('id')))
        if s.get('openalex'):
            w['openalex_metadata']=s['openalex']
        w['enrichment_evidence']=list(dict.fromkeys(x for x in evidence if x))
        if before!=(bool(r.get('abstract')),bool(r.get('keywords'))):changed.append({'key':w['key'],'abstract_filled':not before[0] and bool(r.get('abstract')),'keywords_filled':not before[1] and bool(r.get('keywords')),'evidence_urls':w['enrichment_evidence']})
    save(OUT/'worklist.json',work);save(OUT/'enrichment-changes.json',changed)
    print('ENRICHED',len(changed),'abstracts',sum(x['abstract_filled'] for x in changed),'keywords',sum(x['keywords_filled'] for x in changed),flush=True)

if __name__=='__main__':
    {'merge':merge_bibliographies,'openalex':openalex,'epmc':epmc,'apply':apply_enrichment}[sys.argv[1]]()
