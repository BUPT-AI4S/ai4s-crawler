"""Verify only already-discovered, DOI-matched public PDF locations."""
import sys,json,pathlib,re,unicodedata,urllib.request,urllib.parse,urllib.error
import concurrent.futures as cf,threading,time,collections
def find_repo_root():
 for parent in pathlib.Path(__file__).resolve().parents:
  if (parent/'reviews/source-assignments-2026.json').is_file() and (parent/'metadata/2026/snapshot.json').is_file():return parent
 raise RuntimeError('Repository root not found from script location')
ROOT=find_repo_root()
sys.path.insert(0,str(ROOT))
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
import dinglijun_2026_finalize as f
OUT=f.OUT
def doi(v):return re.sub(r'^(?:https?://(?:dx\.)?doi.org/|doi:)','',str(v or '').strip(),flags=re.I).lower()
def title(v):return ''.join(c for c in unicodedata.normalize('NFKC',str(v or '')).casefold() if c.isalnum())
def same_title(a,b):return title(a)==title(b)

def candidates():
 work,ledger=f.inputs();inc=[w for w in work if ledger[w['key']]['decision']=='include'];records={}
 catalogue={doi(r.get('doi') or r['id']):r for r in f.read(OUT/'ijcai-catalogue.json')['records']}
 rejected=[]
 def add(target,url,source,version,priority,evidence,identity):
  if not url or not str(url).startswith(('https://','http://')):return
  # Existing URLs are kept exactly as discovered, including redirect queries.
  row=records.setdefault(target,{'doi':target,'title':identity['record_title'],'locations':[]})
  loc={'url':url,'source':source,'version':version,'priority':priority,'evidence_urls':list(dict.fromkeys(x for x in evidence if x)),'identity':identity}
  old=next((x for x in row['locations'] if x['url']==url),None)
  if old:
   old['evidence_urls']=list(dict.fromkeys(old['evidence_urls']+loc['evidence_urls']))
   if priority<old['priority']:
    old.update({k:v for k,v in loc.items() if k!='evidence_urls'})
  else:row['locations'].append(loc)
 for w in inc:
  r=w['record'];target=doi(r.get('doi') or r['id']);md=w.get('publisher_verified_metadata') or {};effective_title=md.get('title') or r['title']
  identity={'record_doi':target,'record_title':effective_title}
  rawid=doi(r['id'])
  if rawid.startswith('10.') and rawid!=target:
   rejected.append({'key':w['key'],'reason':'input id and doi differ'});continue
  official=catalogue.get(target)
  if r['venue']=='ijcai' and official:
   if same_title(official['title'],effective_title):
    add(target,official.get('pdf_url'),'IJCAI official 2026 proceedings catalogue','publishedVersion',0,[official.get('url'),'https://www.ijcai.org/proceedings/2026/'],dict(identity,source_title=official['title'],doi_match=True,title_match=True))
   else:rejected.append({'key':w['key'],'source':'IJCAI catalogue','reason':'title mismatch','other_title':official['title']})
  if r.get('pdf_url'):
   add(target,r['pdf_url'],'existing publisher-linked paper metadata','publisher version (as recorded)',1,[md.get('url'),r.get('publisher_url'),r.get('url')],dict(identity,doi_match=True,title_match=True,identity_basis='DOI-linked input paper record; raw PDF URL not synthesized'))
  oa=w.get('openalex_metadata') or {}
  if not oa:continue
  oa_doi=doi(oa.get('doi'));oa_title=oa.get('title') or oa.get('display_name')
  if oa_doi!=target or not same_title(oa_title,effective_title):
   rejected.append({'key':w['key'],'source':'OpenAlex','reason':'work DOI or title mismatch','other_doi':oa_doi,'other_title':oa_title});continue
  locations=[oa.get('primary_location')]+list(oa.get('locations') or [])
  for loc in locations:
   if not isinstance(loc,dict) or not loc.get('pdf_url'):continue
   if loc.get('is_oa') is not True:
    rejected.append({'key':w['key'],'source':'OpenAlex location','url':loc.get('pdf_url'),'reason':'location not explicitly open access'});continue
   version=loc.get('version') or 'unknown public copy version'
   priority=2 if version=='publishedVersion' else 3 if version=='acceptedVersion' else 4
   add(target,loc['pdf_url'],'DOI/title-matched OpenAlex open-access location',version,priority,[oa.get('id'),loc.get('landing_page_url')],dict(identity,source_title=oa_title,doi_match=True,title_match=True,location_is_oa=True))
 for r in records.values():r['locations'].sort(key=lambda x:x['priority'])
 data={'checked_at':'2026-11-17','included_records':len(inc),'candidate_dois':len(records),'candidate_urls':sum(len(x['locations']) for x in records.values()),'records':records,'rejected_identity_or_access':rejected}
 f.save(OUT/'public-pdf-candidates.json',data)
 print('CANDIDATES',data['included_records'],data['candidate_dois'],data['candidate_urls'],'IDENTITY_REJECTIONS',len(rejected),flush=True)
 return data

def probe(loc):
 url=loc['url'];result={k:loc[k] for k in ['url','source','version','evidence_urls','identity']}
 result['checked_at']='2026-11-17';result['verified_public_pdf']=False
 try:
  req=urllib.request.Request(url,method='HEAD',headers={'User-Agent':'AI4S-Metadata-Review/1.0'})
  try:
   with urllib.request.urlopen(req,timeout=10) as res:
    ctype=res.headers.get('Content-Type','').lower();code=res.status;result.update(http_status=code,content_type=ctype,final_url=res.geturl(),method='HEAD')
   if code==200 and 'application/pdf' in ctype:
    result.update(status='verified_pdf',verified_public_pdf=True);return result
   if 'html' in ctype:
    result['status']='html_landing_page';return result
   if code!=200:
    result['status']='http_'+str(code);return result
  except urllib.error.HTTPError as e:
   result.update(http_status=e.code,content_type=(e.headers.get('Content-Type','') if e.headers else '').lower(),method='HEAD')
   if e.code not in (405,501):
    result.update(status='http_'+str(e.code),error=str(e));return result
  # HEAD unsupported or MIME ambiguous: read at most eight bytes, no full PDF.
  req=urllib.request.Request(url,method='GET',headers={'User-Agent':'AI4S-Metadata-Review/1.0','Range':'bytes=0-7'})
  with urllib.request.urlopen(req,timeout=10) as res:
   prefix=res.read(8);ctype=res.headers.get('Content-Type','').lower();code=res.status
   result.update(http_status=code,content_type=ctype,final_url=res.geturl(),method='GET first 8 bytes',prefix_ascii=prefix.decode('ascii','replace'))
   if code in (200,206) and prefix.startswith(b'%PDF'):
    result.update(status='verified_pdf',verified_public_pdf=True)
   else:result['status']='not_a_verified_pdf'
 except Exception as e:
  result.update(status='request_failed',error=str(e))
 return result

def run():
 data=candidates();success_path=OUT/'enrichment-public-pdfs.json';attempts_path=OUT/'public-pdf-verification-attempts.json'
 successful={};attempted={};lock=threading.Lock()
 def one(item):
  target,row=item;checks=[];selected=None
  for loc in row['locations']:
   check=probe(loc);checks.append(check)
   if check['verified_public_pdf']:
    selected=check;break
  with lock:
   attempted[target]={'title':row['title'],'attempts':checks,'status':'verified' if selected else 'unverified'}
   if selected:
    # Preserve the exact verified URL; redirects are recorded in verification.
    successful[target]={'verified_metadata':{'pdf_url':selected['url'],'evidence_urls':list(dict.fromkeys(selected['evidence_urls']+[selected['url']]))},'pdf_verification':selected}
   f.save(success_path,successful);f.save(attempts_path,attempted)
  print('PDF',target,'VERIFIED' if selected else 'UNVERIFIED',selected['version'] if selected else [x['status'] for x in checks],flush=True)
 with cf.ThreadPoolExecutor(max_workers=3) as ex:list(ex.map(one,data['records'].items()))
 counts=collections.Counter(c['status'] for v in attempted.values() for c in v['attempts'])
 summary={'checked_at':'2026-11-17','included_records':data['included_records'],'candidate_dois':data['candidate_dois'],'candidate_urls':data['candidate_urls'],'attempted_dois':len(attempted),'verified_public_pdf_dois':len(successful),'attempt_statuses':dict(counts),'unverified_dois':len(attempted)-len(successful),'scope':'Only pre-existing concrete PDF locations; no URLs guessed or synthesized; HEAD or first 8 GET bytes only.'}
 f.save(OUT/'public-pdf-verification-summary.json',summary);print('SUMMARY',json.dumps(summary),flush=True)

if __name__=='__main__':
 if len(sys.argv)>1 and sys.argv[1]=='candidates':candidates()
 else:run()
