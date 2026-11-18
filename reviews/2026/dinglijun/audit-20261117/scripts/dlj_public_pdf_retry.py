import pathlib
import sys,json,threading,collections,time
import concurrent.futures as cf
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent));import dlj_public_pdf_verify as v
data=v.f.read(v.OUT/'public-pdf-candidates.json')
successful=v.f.read(v.OUT/'enrichment-public-pdfs.json')
attempted=v.f.read(v.OUT/'public-pdf-verification-attempts.json')
todo={doi:r for doi,r in data['records'].items() if doi not in successful and any(c['status']=='proxy_tunnel_denied' for c in attempted[doi]['attempts'])}
lock=threading.Lock()
def one(item):
 doi,row=item;checks=[];selected=None
 old_by={c['url']:c for c in attempted[doi]['attempts']}
 for loc in row['locations']:
  previous=old_by.get(loc['url']) or {}
  if previous.get('status') not in ('proxy_tunnel_denied',None):continue
  time.sleep(.15)
  check=v.probe(loc)
  if 'Tunnel connection failed: 403 Forbidden' in check.get('error',''):check['status']='proxy_tunnel_denied'
  checks.append(check)
  if check['verified_public_pdf']:selected=check;break
 with lock:
  row_out=attempted[doi];row_out.setdefault('earlier_attempts',[]).extend(row_out['attempts'])
  row_out['attempts']=checks;row_out['status']='verified' if selected else 'unverified';row_out['normal_retry_after_proxy_denial']=True
  if selected:
   successful[doi]={'verified_metadata':{'pdf_url':selected['url'],'evidence_urls':list(dict.fromkeys(selected['evidence_urls']+[selected['url']]))},'pdf_verification':selected}
  v.f.save(v.OUT/'enrichment-public-pdfs.json',successful);v.f.save(v.OUT/'public-pdf-verification-attempts.json',attempted)
 print('PDF RETRY',doi,'VERIFIED' if selected else [c['status'] for c in checks],flush=True)
print('RETRY_QUEUE',len(todo),flush=True)
with cf.ThreadPoolExecutor(max_workers=3) as ex:list(ex.map(one,todo.items()))
counts=collections.Counter(c['status'] for r in attempted.values() for c in r['attempts'])
summary={'checked_at':'2026-11-17','included_records':data['included_records'],'candidate_dois':data['candidate_dois'],'candidate_urls':data['candidate_urls'],'attempted_dois':len(attempted),'verified_public_pdf_dois':len(successful),'latest_attempt_statuses':dict(counts),'unverified_dois':len(attempted)-len(successful),'normal_retry_dois':len(todo),'scope':'Existing PDF links only; exact DOI/title matching; 3 concurrent HEAD requests, GET first 8 bytes only when HEAD is unsupported or MIME ambiguous. One ordinary retry of proxy-denied locations; earlier failures retained.'}
v.f.save(v.OUT/'public-pdf-verification-summary.json',summary);print('SUMMARY',json.dumps(summary),flush=True)
