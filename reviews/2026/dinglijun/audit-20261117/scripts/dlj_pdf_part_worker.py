import pathlib
import sys,json,threading,time,collections
import concurrent.futures as cf
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent));import dlj_public_pdf_verify as v
PART=int(sys.argv[1]);queue=v.f.read(v.OUT/f'public-pdf-remaining-part{PART}.json')
SUCCESS=v.OUT/f'enrichment-public-pdfs-part{PART}.json'
ATTEMPTS=v.OUT/f'attempts-part{PART}.json'
SUMMARY=v.OUT/f'public-pdf-summary-part{PART}.json'
successful=v.f.read(SUCCESS) if SUCCESS.exists() else {}
attempted=v.f.read(ATTEMPTS) if ATTEMPTS.exists() else {}
lock=threading.Lock()
def one(item):
 doi,row=item
 if doi in attempted:return
 checks=[];selected=None
 for loc in row['locations']:
  time.sleep(.1);check=v.probe(loc)
  if 'Tunnel connection failed: 403 Forbidden' in check.get('error',''):check['status']='proxy_tunnel_denied'
  checks.append(check)
  if check['verified_public_pdf']:selected=check;break
 with lock:
  attempted[doi]={'title':row['title'],'attempts':checks,'status':'verified' if selected else 'unverified'}
  if selected:successful[doi]={'verified_metadata':{'pdf_url':selected['url'],'evidence_urls':list(dict.fromkeys(selected['evidence_urls']+[selected['url']]))},'pdf_verification':selected}
  v.f.save(SUCCESS,successful);v.f.save(ATTEMPTS,attempted)
 print('PART',PART,doi,'VERIFIED' if selected else [x['status'] for x in checks],flush=True)
print('PART_QUEUE',PART,len(queue),sum(len(r['locations']) for r in queue.values()),flush=True)
with cf.ThreadPoolExecutor(max_workers=3) as ex:list(ex.map(one,queue.items()))
summary={'part':PART,'status':'complete','candidate_dois':len(queue),'candidate_urls':sum(len(r['locations']) for r in queue.values()),'attempted_dois':len(attempted),'verified_public_pdf_dois':len(successful),'attempt_statuses':dict(collections.Counter(x['status'] for r in attempted.values() for x in r['attempts']))}
v.f.save(SUMMARY,summary);print('SUMMARY',json.dumps(summary),flush=True)
