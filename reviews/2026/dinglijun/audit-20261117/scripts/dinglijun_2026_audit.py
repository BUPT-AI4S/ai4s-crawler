"""Scoped, resumable evidence collection for Ding Lijun's 2026 sources."""
import concurrent.futures as cf
import hashlib
import html
import json
import pathlib
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

ROOT = next(p for p in pathlib.Path(__file__).resolve().parents
            if (p/'teacher_sources.json').exists() and (p/'reviews/source-assignments-2026.json').exists())
sys.path.insert(0,str(ROOT))
OUT = ROOT / 'reviews/2026/dinglijun/audit-20261117'
OUT.mkdir(parents=True, exist_ok=True)
ASSIGN = json.loads((ROOT / 'reviews/source-assignments-2026.json').read_text())
OWN = [s for s in ASSIGN['sources'] if s['owner'] == '丁利军']
assert len(OWN) == 49
HEAD = subprocess.check_output(['git', '-C', str(ROOT), 'rev-parse', 'HEAD'], text=True).strip()

def save(path, data):
    path = pathlib.Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + '.tmp')
    temp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
    temp.replace(path)

def read(path):
    return json.loads(pathlib.Path(path).read_text())

def fetch(url, timeout=35):
    req = urllib.request.Request(url, headers={'User-Agent': 'AI4S-Bibliography-Audit/1.0 (public academic metadata)', 'Accept': 'application/json,text/html,application/xml;q=0.8'})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        raw = r.read(18_000_000)
        return raw, r.geturl(), dict(r.headers), r.status

def registry():
    teacher = {s['code']: s for s in read(ROOT/'teacher_sources.json')['sources']}
    journals = {s['slug']: s for name in ['additional_journals.json', 'nature_journals.json'] for s in read(ROOT/name)['journals']}
    result = []
    for s in OWN:
        code = s['code']
        a, b = [read(ROOT/f'metadata/{code}/2026/{n}.json') for n in ['papers', 'ai4s']]
        t, j = teacher.get(code, {}), journals.get(code, {})
        row = dict(s, papers_path=f'metadata/{code}/2026/papers.json', ai4s_path=f'metadata/{code}/2026/ai4s.json',
                   papers=len(a), candidates=len(b), missing_abstract=sum(not str(r.get('abstract') or '').strip() for r in b),
                   missing_keywords=sum(not r.get('keywords') for r in b),
                   official_url=j.get('homepage') or t.get('official_url') or ('https://www.ijcai.org/proceedings/2026/' if code=='ijcai' else None),
                   issns=j.get('issns') or sorted({r.get('issn') for r in a if r.get('issn')}),
                   baseline_hashes={n:hashlib.sha256((ROOT/f'metadata/{code}/2026/{n}.json').read_bytes()).hexdigest() for n in ['papers','ai4s']})
        result.append(row)
    return result

def publisher_home(s):
    url=s.get('official_url') or ''
    special={
      'ijcai':'https://www.ijcai.org/proceedings/2026/',
      'j-d058311f73':'https://link.springer.com/journal/42773',
      'j-291c5f64e2':'https://nanoconvergencejournal.springeropen.com/',
      'j-652a538c84':'https://molecularbiomedicine.biomedcentral.com/',
      'j-530a5c55b0':'https://link.springer.com/journal/12393',
      'j-2c17c1a9f2':'https://www.whxb.pku.edu.cn/EN/1000-6818/home.shtml'}
    if s['code'] in special:return special[s['code']]
    if 'api.crossref.org/' not in url:return url
    slug=re.sub(r'[^a-z0-9]+','-',s['title'].lower().replace('&','and')).strip('-')
    if s['code']=='j-5e43722961':slug='jacc-cardiooncology'
    return 'https://www.sciencedirect.com/journal/'+slug

def baseline():
    reg = registry()
    save(OUT/'baseline.json', {'commit':HEAD, 'assignment_source':{k:v for k,v in ASSIGN.items() if k!='sources'}, 'snapshot_at':read(ROOT/'metadata/2026/snapshot.json')['captured_at'], 'sources':reg})
    print('BASELINE',len(reg),sum(x['papers'] for x in reg),sum(x['candidates'] for x in reg),flush=True)

def official_one(s):
    dest=OUT/'official'/f"{s['code']}.json"
    if dest.exists(): return read(dest)
    url=publisher_home(s)
    if 'nature.com/' in str(url): url=url.rstrip('/')+'/articles?year=2026'
    if s['code']=='ijcai': url='https://www.ijcai.org/proceedings/2026/'
    result={'source_code':s['code'],'title':s['title'],'year':2026,'url':url,'checked_at':'2026-11-17','official_total':None}
    try:
        raw,final,headers,status=fetch(url,25)
        text=raw.decode('utf8','replace')
        (OUT/'official'/f"{s['code']}.html").write_text(text)
        result.update(status=status,final_url=final,bytes=len(raw),page_title=re.findall(r'<title[^>]*>(.*?)</title>',text,re.S)[:1],links=sorted(set(html.unescape(x) for x in re.findall(r'href=[\"\']([^\"\']+)[\"\']',text))))
        result['access']='challenge' if any(x in text.lower() for x in ['just a moment...', 'verify you are human', 'access denied', 'enable javascript and cookies']) else 'accessible'
    except Exception as e: result.update(access='failed',error=str(e))
    save(dest,result)
    print('OFFICIAL',s['code'],result['access'],result.get('status'),result.get('error',''),flush=True)
    return result

def official():
    sources=read(OUT/'baseline.json')['sources']
    with cf.ThreadPoolExecutor(max_workers=4) as ex: result=list(ex.map(official_one,sources))
    save(OUT/'official-access.json',result)

def references():
    # Serial public Crossref cursor queries; compact fields retain identities,
    # dates, author ordering and original abstracts without copying citations.
    fields='DOI,title,author,abstract,published,published-online,published-print,issued,type,URL,resource,link,ISSN,container-title,volume,issue,page,subject,relation'
    for s in read(OUT/'baseline.json')['sources']:
        if s['code']=='ijcai': continue
        dest=OUT/'crossref'/f"{s['code']}.json"
        if dest.exists() and read(dest).get('complete') and read(dest).get('retrieved',0)>0: continue
        # Some journals register only their electronic or print identifier.
        issn=s['issns'][1] if s['code'] in ('j-d058311f73','j-97a3b8d4d3') and len(s['issns'])>1 else s['issns'][0]
        if dest.exists():save(OUT/'crossref-attempts'/f"{s['code']}-first-issn.json",read(dest))
        base=f'https://api.crossref.org/journals/{issn}/works'
        params={'filter':'from-pub-date:2026-01-01,until-pub-date:2026-12-31,type:journal-article','rows':'1000','cursor':'*','select':fields}
        result={'source_code':s['code'],'source':'Crossref','year':2026,'query_url':base+'?'+urllib.parse.urlencode(params),'checked_at':'2026-11-17','scope':'Crossref pub-date 2026-01-01..2026-12-31; type journal-article; publisher-registered metadata; reference only, not an official catalogue total','complete':False,'items':[]}
        seen=set(); cursors=set()
        try:
            while True:
                url=base+'?'+urllib.parse.urlencode(params)
                for attempt in range(3):
                    try:
                        raw,_,_,_=fetch(url,55); msg=json.loads(raw)['message']; break
                    except Exception:
                        if attempt==2: raise
                        time.sleep(2)
                result['total_results']=msg['total-results']
                batch=msg.get('items',[])
                for item in batch:
                    doi=item.get('DOI','').lower()
                    if doi and doi not in seen: result['items'].append(item);seen.add(doi)
                save(dest,result)
                cursor=msg.get('next-cursor')
                if not batch or len(seen)>=result['total_results']:
                    result['complete']=True; break
                if not cursor or cursor in cursors: raise RuntimeError('cursor stopped before total-results')
                cursors.add(cursor);params['cursor']=cursor
                print('PAGE',s['code'],len(seen),result['total_results'],flush=True)
                time.sleep(.15)
        except Exception as e: result['error']=str(e)
        result['retrieved']=len(result['items'])
        original=read(ROOT/s['papers_path']); old={str(x.get('doi') or x.get('id') or '').lower():x for x in original}
        new={x['DOI'].lower():x for x in result['items']}
        result['missing_local']=sorted(new.keys()-old.keys())
        result['local_not_in_reference']=sorted(old.keys()-new.keys()) if result['complete'] else None
        save(dest,result)
        print('REFERENCE',s['code'],'local',len(original),'reference',len(new),'complete',result['complete'],'missing',len(result['missing_local']),result.get('error',''),flush=True)

if __name__=='__main__':
    {'baseline':baseline,'official':official,'references':references}[sys.argv[1]]()
