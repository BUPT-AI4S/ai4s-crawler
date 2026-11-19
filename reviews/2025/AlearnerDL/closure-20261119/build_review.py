import json,pathlib,hashlib,collections
out=pathlib.Path(__file__).resolve().parent;root=out.parents[3]
codes={s['code'] for s in json.load(open(root/'reviews/source-assignments-2025.json'))['sources'] if s['owner']=='龙兆科'};p=[x for x in json.load(open(root/'metadata/2025/ai4s.json')) if x['venue'] in codes];v=json.load(open(root/'skills/ai4s-paper-review/references/tag-vocabulary.json'))['tags'];v={t['label']:t for t in v}
d=json.load(open(out/'model-decisions.json'))
recovered={x['index']:x for x in json.load(open(out/'aamas-abstract-source.json'))}
recovered[25]=json.load(open(out/'ase-25-abstract-source.json'))
if (out/'extra-abstracts.json').exists():recovered.update({x['index']:x for x in json.load(open(out/'extra-abstracts.json'))})
proofs={x['index']:x for x in json.load(open(out/'nonresearch-type-proofs.json'))} if (out/'nonresearch-type-proofs.json').exists() else {}
for i,x in enumerate(p):
 dec=d.get(str(i),{'decision':'unreviewed','rationale':None});evidence=('官方PDF第1页摘要及文献类型' if i<7 else '作者所在大学论文记录原摘要') if i in recovered else '输入摘要';urls=[recovered[i]['url']] if i in recovered else [x['url']]
 if i in recovered:evidence=recovered[i].get('evidence_location',evidence)
 r={'schema_version':2,'batch_id':'longzhaoke-2025-20261119','owner':'龙兆科','snapshot_at':'2026-11-09T10:51:18+08:00',**{k:dec[k] for k in ['decision','rationale']},'verified_metadata':{},'tags':[]}
 if str(i) in d:
  r['verified_metadata']={'url':x['url'],'evidence_urls':urls}
  if i in proofs:
   r['verified_metadata']['evidence_urls']=proofs[i]['evidence_urls']
   r['verified_metadata']['document_type']=proofs[i]['document_type']
  if i in recovered:
   r['verified_metadata']['abstract']=recovered[i]['abstract'].split('CCS CONCEPTS')[0].strip()
   if i<7:r['verified_metadata']['pdf_url']=recovered[i]['url']
  if dec['decision']=='include':
   label=dec['domain'];tag=v[label];r['tags']=[{'axis':tag['axis'],'label':label,'label_en':tag['label_en'],'evidence_location':evidence,'rationale':dec['rationale']}]
 x['ai4s_review']=r
(root/'reviews/2025/AlearnerDL.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n')
print(collections.Counter(x['ai4s_review']['decision'] for x in p))
