import json,hashlib,collections,pathlib
out=pathlib.Path(__file__).resolve().parent;root=out.parents[3]
load=lambda p:json.load(open(root/p))
codes={s['code'] for s in load('reviews/source-assignments-2025.json')['sources'] if s['owner']=='龙兆科'}
original=[p for p in load('metadata/2025/ai4s.json') if p['venue'] in codes]
review=load('reviews/2025/AlearnerDL.json');supplement=load('reviews/2025/AlearnerDL/closure-20261119/supplemental-candidates.json');assert len(review)==len(original)==1552+len(supplement)
assert [(x['venue'],x['year'],x['id']) for x in original[-len(supplement):]]==[(x['venue'],x['year'],x['id']) for x in supplement]
v={(x['axis'],x['label'],x['label_en']) for x in load('skills/ai4s-paper-review/references/tag-vocabulary.json')['tags']}
keys=[]
for raw,p in zip(original,review):
 assert {k:val for k,val in p.items() if k!='ai4s_review'}==raw
 r=p['ai4s_review'];assert r['owner']=='龙兆科' and r['snapshot_at']=='2026-11-09T10:51:18+08:00'
 assert r['decision'] in ['include','exclude','pending','unreviewed']
 if r['decision']=='include':
  assert (r['verified_metadata'].get('abstract') or p.get('abstract') or '').strip()
  assert r['tags'] and r['verified_metadata']['evidence_urls']
  for t in r['tags']:assert (t['axis'],t['label'],t['label_en']) in v and t['rationale']
 else:assert r['tags']==[]
 keys.append((p['venue'],p['year'],p['id']))
assert len(keys)==len(set(keys))
for f in load('reviews/2025/feedback/AlearnerDL.json'):
 assert f['source_code'] in codes and f['year']==2025 and f['snapshot_at']=='2026-11-09T10:51:18+08:00'
 assert f['official_total']>0 and f['evidence_urls']
counts=dict(collections.Counter(p['ai4s_review']['decision'] for p in review))
report={'status':'passed','records':len(review),'all_original_fields_preserved':True,'unique_keys':True,'all_included_have_original_abstract_and_canonical_tags':True,'decisions':counts,'annual_task_complete':False}
(out/'validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n');print(json.dumps(report,ensure_ascii=False))
