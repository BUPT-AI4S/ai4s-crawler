"""Read-only validation of this fixed candidate supplement against its input main."""
import collections, hashlib, json, pathlib, subprocess, sys, csv, datetime
R=pathlib.Path(__file__).resolve().parents[4]
A=pathlib.Path(__file__).resolve().parent
BASE='e589b0d2feabffde19ef6eed1ca1331caebaedfa'
def load(p):return json.loads((R/p).read_text())
def old(p):return json.loads(subprocess.check_output(['git','show',BASE+':'+p],cwd=R,text=True))
def key(x):return x['venue'],x['year'],x['id']
queue=load('reviews/2026/AlearnerDL/closure-20261119/remaining-tasks.json')
keys={(x['venue'],2026,x['id']) for x in queue};venues={x['venue'] for x in queue}
rp='reviews/2026/AlearnerDL.json';before=old(rp);after=load(rp)
assert len(before)==len(after) and len(set(map(key,after)))==len(after)
changed=[]
for b,a in zip(before,after):
 assert key(b)==key(a)
 if a==b:continue
 assert key(a) in keys
 assert {k:v for k,v in a.items() if k!='ai4s_review'}=={k:v for k,v in b.items() if k!='ai4s_review'}
 assert a['ai4s_review']['previous_review']==b['ai4s_review']
 changed.append(a)
assert len(changed)==254 and {key(x) for x in changed}==keys
bykey={key(x):x for x in after}
evidence={x['index']:x for x in load(str((A/'extracted-abstracts.json').relative_to(R)))}
decisions={int(x['index']):x for x in csv.DictReader((A/'model-decisions.tsv').open(),delimiter='\t')}
vocab={(x['axis'],x['label'],x['label_en']) for x in load('skills/ai4s-paper-review/references/tag-vocabulary.json')['tags']}
assert len(evidence)==252 and set(decisions)==set(range(254))
proofs={}
for i,q in enumerate(queue):
 p=bykey[(q['venue'],2026,q['id'])];r=p['ai4s_review'];vm=r['verified_metadata']
 assert r['owner']=='龙兆科' and r['snapshot_at']=='2026-11-08T21:38:12.854071+08:00'
 assert r['decision']==decisions[i]['decision'] and r['rationale']==decisions[i]['reason']
 assert r['decision'] in ['include','exclude'] and bool(r['tags'])==(r['decision']=='include')
 for t in r['tags']:assert (t['axis'],t['label'],t['label_en']) in vocab and t['rationale'] and t['evidence_location']
 if i in evidence:
  e=evidence[i];assert vm['abstract']==e['abstract'] and len(e['abstract'])>=300
  assert hashlib.sha256(e['abstract'].encode()).hexdigest()==e['abstract_sha256']==vm['abstract_sha256']
  assert q['publisher_url'].rsplit('/',1)[-1] in e['evidence_url'] and q['title']==e['title'] and q['id']==e['id']
  assert e['evidence_url'] in vm['evidence_urls']
 else:
  assert i in [230,231] and r['decision']=='exclude' and vm['article_type']=='Corrigendum'
  proof=r['abstract_requirement'];proofs[q['id']]=proof
  assert proof['status']=='not_required' and proof['reason']=='verified_nonresearch_document_type_exclusion'
  assert proof['paper_id']==q['id'] and proof['year']==2026 and proof['source_code']==q['venue']
  assert proof['checked_by']=='龙兆科' and datetime.datetime.fromisoformat(proof['checked_at']).utcoffset() is not None
  assert proof['primary_source_url'] in proof['evidence_urls'] and all(u in vm['evidence_urls'] for u in proof['evidence_urls'])
  cr=json.loads((A/f'crossref-{i}.json').read_text())['message']
  assert cr['DOI'].lower()==q['id'].lower() and any(u['type']=='erratum' and u['source']=='publisher' for u in cr['update-to'])
for path in ['metadata/2026/ai4s.json','metadata/j-a6cfe198b1/2026/ai4s.json']:
 b=old(path);a=load(path);assert len(a)==len(b);edits=[]
 for x,y in zip(b,a):
  assert key(x)==key(y)
  if x==y:continue
  assert y['id'] in proofs and y['venue']=='j-a6cfe198b1' and y['year']==2026
  assert {k:v for k,v in x.items() if k!='abstract_requirement'}=={k:v for k,v in y.items() if k!='abstract_requirement'}
  assert y['abstract_requirement']==proofs[y['id']];edits.append(y['id'])
 assert set(edits)==set(proofs) and len(edits)==2
assert (R/'metadata/2026/ai4s.json').stat().st_size<100*1024*1024
fp='reviews/2026/feedback/AlearnerDL.json';b=old(fp);a=load(fp);assert len(a)==len(b)
for x,y in zip(b,a):
 assert x['source_code']==y['source_code']
 if x['source_code'] not in venues:assert x==y
 else:
  assert x['catalogue_audit']==y['catalogue_audit'] and x['reference_check']==y['reference_check']
  assert not y['issues'] and not y['next_actions'] and y['candidate_abstract_missing']==0
for venue in venues:
 for name in ['papers.json','catalogue-reconciliation.json','catalogue-additions.json']:
  path=f'metadata/{venue}/2026/{name}'
  assert (R/path).read_bytes()==subprocess.check_output(['git','show',BASE+':'+path],cwd=R)
path='metadata/2026/snapshot.json'
assert (R/path).read_bytes()==subprocess.check_output(['git','show',BASE+':'+path],cwd=R)
mon=json.loads(pathlib.Path(sys.argv[1]).read_text());year=next(y for y in mon['years'] if y['year']==2026)
sources=[s for s in year['sources'] if s['code'] in venues]
assert len(sources)==3
for s in sources:
 assert not s['issues'] and s['abstract_supplement_required']==0 and s['final_missing_abstract']==0 and s['unsynced_included']==0
 assert not s['decisions'].get('pending',0) and not s['decisions'].get('unreviewed',0)
owner=next(o for o in year['owners'] if o['owner']=='龙兆科');assert owner['open_issues']==0 and owner['pending']==0
result={'input_main_commit':BASE,'validated_review_changes':254,'original_abstracts_recovered':252,'verified_corrigenda':2,'new_candidate_count':0,'new_decisions':dict(collections.Counter(x['ai4s_review']['decision'] for x in changed)),'original_fields_and_raw_data_preserved':True,'other_reviews_and_feedback_preserved':True,'vocabulary_valid':True,'all_included_have_original_abstracts':True,'monitor_source':sys.argv[1],'three_journals_green':True,'owner_2026_open_issues':0,'owner_2026_pending':0,'sources':[{k:s[k] for k in ['code','title','candidates','decisions','abstract_recovered','abstract_nonresearch_excluded','abstract_supplement_required','issues']} for s in sources]}
(A/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
