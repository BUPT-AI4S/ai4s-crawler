"""Apply only the authorized Chen Chen abstract/rescreen records to current checkout."""
import copy,hashlib,json,subprocess
from collections import Counter
from pathlib import Path
P=Path(__file__).resolve().parent
ROOT=P.parents[3]
OWNER='陈晨';DATE='2026-11-17';BATCH='2024-chenchen-abstract-backfill-rescreen-20261117'
REL=P.relative_to(ROOT).as_posix()
def read(path):return json.loads((ROOT/path).read_text())
def dump(path,obj,style='pretty'):
 text=json.dumps(obj,ensure_ascii=False,indent=2) if style=='pretty' else (json.dumps(obj,ensure_ascii=False,separators=(',',':')) if style=='compact' else '[\n'+',\n'.join(json.dumps(r,ensure_ascii=False,separators=(',',':')) for r in obj)+'\n]')
 (ROOT/path).write_text(text+'\n')
def k(r):return (r['venue'],r['year'],r['id'])
def digest(r):return hashlib.sha256(json.dumps(r,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode()).hexdigest()
back=read(REL+'/original-abstract-backfill-870.json');back={tuple(x['key']):x for x in back}
recommend=read(REL+'/rescreen-recommendations-722.json');suggest={tuple(x['key']):x for x in recommend}
assert len(suggest)==722 and Counter(r['recommendation'] for r in recommend)=={'include':452,'exclude':270}
assert all(back[key].get('abstract_original') for key in suggest)
main_path='reviews/2024/chenchen052512.json';main=read(main_path);before_main=copy.deepcopy(main);idx={k(r):r for r in main};assert len(idx)==len(main)
base_commit=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT).decode().strip()
audit=[]
for key,s in suggest.items():
 r=idx[key];rev=r['ai4s_review'];assert rev['owner']==OWNER and rev['decision']=='exclude',(key,'unexpected changed review')
 b=back[key];assert s['doi']==b['doi'] and s['title']==b['title']
 audit.append({'key':list(key),'previous_review':copy.deepcopy(rev),'new_decision':s['recommendation'],'new_rationale':s['rationale_cn']})
 for name in ['abstract_requirement','owner_decision_confirmation','abstract_absence_evidence']:
  rev.pop(name,None)
 rev.update(batch_id=BATCH,reviewed_at=DATE,decision=s['recommendation'],rationale=s['rationale_cn'],review_method='individual_semantic_rescreen_of_verified_original_abstract',evidence_location='出版方完整原作者摘要（已补回；见verified_metadata.abstract）',vocabulary_base_commit=base_commit,user_policy='负责人授权回填原摘要并应用逐篇复筛；摘要不能确认条件时按证据不足排除。',rescreen_audit_file=REL+'/rescreen-recommendations-722.json',previous_review_audit_file=REL+'/previous-target-reviews.json')
 rev['tags']=[{'axis':t['axis'],'label':t['label'],'label_en':t['label_en'],'evidence_location':'已补官网原摘要','rationale':t.get('evidence_cn') or s['rationale_cn']} for t in s['tags']] if s['recommendation']=='include' else []
 vm=rev.setdefault('verified_metadata',{})
 for name in ['abstract_absence_evidence','abstract_requirement','original_abstract_missing_reason']:
  vm.pop(name,None)
 vm.update(doi=b['doi'],title=b['title'],abstract=b['abstract_original'],abstract_status='verified_publisher_original_abstract',original_abstract_status='verified_publisher_original_abstract',abstract_source_url=b['source_url'],abstract_checked_at=DATE)
 article=(b.get('target_identity') or {}).get('official_url_from_target_list') or b.get('official_url') or b.get('publisher_url')
 if article:vm['url']=article
 vm['evidence_urls']=list(dict.fromkeys([*(vm.get('evidence_urls') or []),b['source_url'],*([article] if article else [])]))
 # Keep original crawler fields and snapshot ownership unchanged.
 assert {a:z for a,z in r.items() if a!='ai4s_review'}=={a:z for a,z in next(x for x in before_main if k(x)==key).items() if a!='ai4s_review'}
for a,z in zip(before_main,main):
 if k(a) not in suggest:assert a==z
assert len(main)==len(before_main)
dump(main_path,main,'compact')
assert (ROOT/main_path).stat().st_size<100*1024*1024,'GitHub 100MiB blob limit exceeded'
dump(REL+'/previous-target-reviews.json',audit)
# Fill all 722 corresponding per-journal catalogue records, preserving originals in audit.
raw_before=[];raw_counts={};raw_by_key={}
for venue in sorted({key[0] for key in suggest}):
 path=f'metadata/{venue}/2024/papers.json';rows=read(path);original=copy.deepcopy(rows);changed=0
 for r in rows:
  key=k(r)
  if key in suggest:
   b=back[key];raw_before.append({'key':list(key),'previous_abstract':r.get('abstract'),'previous_abstract_requirement':r.get('abstract_requirement')})
   r['abstract']=b['abstract_original'];r.pop('abstract_requirement',None)
   r['abstract_provenance']={'type':'original_author_abstract','source_url':b['source_url'],'checked_by':OWNER,'checked_at':DATE,'evidence_file':REL+'/original-abstract-backfill-870.json'}
   raw_by_key[key]=copy.deepcopy(r);changed+=1
 for a,z in zip(original,rows):
  if k(a) not in suggest:assert a==z
 assert changed==sum(key[0]==venue for key in suggest)
 dump(path,rows,'lines');raw_counts[venue]=changed
assert len(raw_by_key)==722
dump(REL+'/previous-catalogue-abstracts.json',raw_before)
# Promote only newly accepted, verified full-corpus additions to candidate indexes.
annual_path='metadata/2024/ai4s.json';annual=read(annual_path);annual_original=copy.deepcopy(annual);candidate_updates={}
def sync_candidates(rows,allowed):
 old={k(r):r for r in rows};added=filled=0
 for key in allowed:
  if key in old:
   row=old[key];row['abstract']=back[key]['abstract_original'];row.pop('abstract_requirement',None);filled+=1
  elif suggest[key]['recommendation']=='include':
   row=copy.deepcopy(raw_by_key[key]);row.pop('ai4s_review',None)
   row['candidate_addition']={'reason':'verified_full_corpus_missed_candidate_after_original_abstract_backfill','checked_by':OWNER,'checked_at':DATE,'review_file':main_path,'rescreen_audit_file':REL+'/rescreen-recommendations-722.json'}
   rows.append(row);old[key]=row;added+=1
 return added,filled
added,filled=sync_candidates(annual,set(suggest));assert added==452 and filled==0
dump(annual_path,annual,'lines');candidate_updates['annual']={'added':added,'filled':filled}
for a,z in zip(annual_original,annual):assert a==z # Existing other records unchanged.
for venue in sorted(raw_counts):
 path=f'metadata/{venue}/2024/ai4s.json';rows=read(path);allowed={key for key in suggest if key[0]==venue};added,filled=sync_candidates(rows,allowed)
 if added or filled:dump(path,rows,'lines')
 candidate_updates[venue]={'added':added,'filled':filled,'total':len(rows)}
# Update only the eight affected source feedback rows; preserve total reconciliation proof.
feedback_path='reviews/2024/feedback/chenchen052512.json';feedback=read(feedback_path);before_feedback=copy.deepcopy(feedback)
for row in feedback:
 venue=row.get('source_code')
 if venue not in raw_counts:continue
 own=[r for r in main if r['venue']==venue];counts=Counter(r['ai4s_review']['decision'] for r in own)
 annual_rows=[r for r in annual if r['venue']==venue and r['year']==2024];missing=sum(not isinstance(r.get('abstract'),str) or not r['abstract'].strip() for r in annual_rows)
 row['coverage_note']=f'2026-11-17完整原摘要补查复筛已同步。本源审核交付{len(own)}条：纳入{counts["include"]}、排除{counts["exclude"]}、待定{counts["pending"]}、未审{counts["unreviewed"]}。新增纳入已同步年度及分刊候选并带原摘要；本轮补回{raw_counts[venue]}份完整作者摘要。总量口径及核验凭证保持，见既有official_total/reference_check。'
 row['candidate_count']=len(annual_rows);row['own_review_count']=len(own);row['own_review_counts']={z:counts[z] for z in ['include','exclude','pending','unreviewed']};row['work_status']='complete'
 row['candidate_abstract_coverage']={'candidate_file':annual_path,'candidate_total':len(annual_rows),'missing_original_input_abstracts':missing,'checked_at':DATE,'note':'只统计本来源当前AI4S候选；已纳入的本轮补录均有原摘要，原未入候选的排除记录不扩增候选集合。'}
 row['abstract_backfill_rescreen']={'checked_at':DATE,'complete_original_abstracts':raw_counts[venue],'recommendation_counts':dict(Counter(s['recommendation'] for key,s in suggest.items() if key[0]==venue)),'audit_file':REL+'/rescreen-recommendations-722.json'}
 for field in ['evidence_files','evidence_urls']:
  row.setdefault(field,[])
 row['evidence_files']=list(dict.fromkeys(row['evidence_files']+[REL+'/rescreen-recommendations-722.json',REL+'/original-abstract-backfill-870.json']))
 # Existing unresolved real issues are retained; do not hide them to get a green result.
 if isinstance(row.get('review_scope'),dict):
  proof=row['review_scope'];proof['candidate_count']=len(annual_rows);proof['candidate_ids_sha256']=hashlib.sha256(json.dumps(sorted(r['id'] for r in annual_rows),ensure_ascii=False,separators=(',',':')).encode()).hexdigest()
for a,z in zip(before_feedback,feedback):
 if a.get('source_code') not in raw_counts:assert a==z
dump(feedback_path,feedback)
summary={'source_base_commit':base_commit,'review_records_updated':722,'decision_transitions':dict(Counter(a['previous_review']['decision']+' -> '+a['new_decision'] for a in audit)),'original_review_fields_preserved':True,'unrelated_review_records_unchanged':len(main)-722,'per_journal_raw_abstracts_filled':raw_counts,'candidate_updates':candidate_updates,'final_personal_decisions':dict(Counter(r['ai4s_review']['decision'] for r in main)),'review_file_bytes':(ROOT/main_path).stat().st_size,'annual_lfs_archive_unchanged':True,'note':'Annual papers.json is an untouched historical LFS archive; current per-journal catalogues and candidate indexes contain the verified repaired abstracts.'}
dump(REL+'/sync-validation.json',summary)
print(json.dumps(summary,ensure_ascii=False,indent=2))
