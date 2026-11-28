"""Independent data and ownership invariants for the delivered 2026 review."""
import collections
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'audit-20261117'/'scripts'))
from dinglijun_2026_audit import ROOT, OWN, read, save
OUT=Path(__file__).resolve().parent

CODES={x['code'] for x in OWN}
def original(ref,path):
    return json.loads(subprocess.check_output(['git','-C',str(ROOT),'show',f'{ref}:{path}']))
def abstract_ok(value):
    return len(str(value or '').strip())>=60 and not re.match(r'^(Highlights|Graphical abstract)\b',str(value or '').strip(),re.I)
def nonowner_hash(raw):
    decoder=json.JSONDecoder();pos=raw.index('[')+1;digest=hashlib.sha256();count=0
    while True:
        while raw[pos] in ' \r\n\t,':pos+=1
        if raw[pos]==']':break
        row,pos=decoder.raw_decode(raw,pos)
        if row.get('venue') in CODES:continue
        digest.update(json.dumps(row,ensure_ascii=False,sort_keys=True,separators=(',',':')).encode());digest.update(b'\n');count+=1
    return count,digest.hexdigest()

def main():
    base=read(OUT.parent/'audit-20261117'/'baseline.json');ref=base['commit'];other_ref=sys.argv[1] if len(sys.argv)>1 else read(OUT/'continuation-baseline.json')['integration_base_commit']
    reviews=read(ROOT/'reviews/2026/dinglijun.json');by={};decisions=collections.Counter();vocab=read(ROOT/'skills/ai4s-paper-review/references/tag-vocabulary.json')['tags'];vocab={x['label']:x for x in vocab}
    all_dates=read(OUT/'effective-publication-dates.json')
    for r in reviews:
        k=(r['venue'],r['year'],r['id']);assert k not in by,('duplicate review',k);by[k]=r
        assert r['venue'] in CODES and r['year']==2026,('owner/year scope',k)
        a=r['ai4s_review'];d=a['decision'];assert a['owner']=='丁利军' and a['schema_version']==2
        assert a['snapshot_at']==base['snapshot_at'];assert d in ('include','exclude','pending'),('unreviewed record',k)
        decisions[d]+=1;tags=a['tags']
        if d=='include':
            assert abstract_ok(a.get('verified_metadata',{}).get('abstract') or r.get('abstract')),('no original abstract',k)
            assert tags and a['verified_metadata'].get('evidence_urls'),('missing evidence',k)
            assert all_dates.get(str(r.get('doi') or r['id']).lower(),{}).get('resolution')!='unknown',('unresolved publication year included',k)
            assert any(t['axis']=='domain' for t in tags)
        else:assert tags==[],('tags on noninclude',k)
        md=a.get('verified_metadata',{})
        if md.get('pdf_url'):
            pdf=md.get('pdf_verification',{})
            assert pdf.get('verified_public_pdf') is True and pdf.get('url')==md['pdf_url'],('unverified PDF promoted',k)
        for t in tags:
            assert t['label'] in vocab,('unknown label',k,t)
            v=vocab[t['label']]
            assert (t['axis'],t['label_en'])==(v['axis'],v['label_en']),('noncanonical bilingual tag',k,t)
            assert t.get('evidence_location') and t.get('rationale'),('tag lacks evidence',k)
            assert not(t['axis']=='domain' and t['label_en']=='AI for social sciences'),('excluded social domain',k)
    before=after=original_candidates=0;candidate_keys=set();removed_original_papers=[]
    mutable={'abstract','keywords','article_type','screening_status','source','code_url','project_url','dataset_url','pdf_url','metadata_evidence_urls','resource_link_status','publication_year_scope','publication_year_evidence','archive_scope'}
    for s in OWN:
        code=s['code'];path=f'metadata/{code}/2026/papers.json';old=original(ref,path);new=read(ROOT/path);nb={r['id']:r for r in new}
        assert len(nb)==len(new),('duplicate corpus ID',code)
        before+=len(old);after+=len(new)
        for row in old:
            assert row['id'] in nb,('deleted original full-corpus record',code,row['id'])
            current=nb[row['id']]
            for field,value in row.items():
                if field not in mutable:assert current.get(field)==value,('unexpected original metadata change',code,row['id'],field)
        old_candidates=original(ref,f'metadata/{code}/2026/ai4s.json');original_candidates+=len(old_candidates)
        for row in old_candidates:
            k=(code,2026,row['id'])
            assert k in by,('original candidate missing its review',code,row['id'])
            for field,value in row.items():
                assert by[k].get(field)==value,('original candidate field overwritten',k,field)
        ca=read(ROOT/f'metadata/{code}/2026/ai4s.json')
        for row in ca:
            k=(row['venue'],row['year'],row['id']);assert k not in candidate_keys;candidate_keys.add(k)
            assert k in by and by[k]['ai4s_review']['decision'] in ('include',),('unverified new or rejected candidate',k)
        expected={k for k,r in by.items() if k[0]==code and r['ai4s_review']['decision']=='include'}
        assert expected=={(r['venue'],r['year'],r['id']) for r in ca},('source candidates not synchronized',code)
    assert before==32266 and after==33202 and original_candidates==1688
    prior=original('56e227f14ab2152ce71622dc489659bd66a45451','reviews/2026/dinglijun.json')
    for row in prior:
        current=by[(row['venue'],row['year'],row['id'])]
        assert {k:v for k,v in current.items() if k!='ai4s_review'}=={k:v for k,v in row.items() if k!='ai4s_review'}
    pending=[r for r in reviews if r['ai4s_review']['decision']=='pending']
    assert len(pending)==2 and all(r['ai4s_review']['review_scope']['status']=='reference_only' for r in pending)
    assert len(candidate_keys)==2894 and decisions=={'include':2894,'exclude':273,'pending':2}
    assert (ROOT/'metadata/2026/ai4s.json').stat().st_size<100*1024*1024
    feedback=read(ROOT/'reviews/2026/feedback/dinglijun.json')
    assert len(feedback)==49 and {x['source_code'] for x in feedback}==CODES
    assert all(x['snapshot_at']==base['snapshot_at'] and x['year']==2026 for x in feedback)
    for f in feedback:
        code=f['source_code'];raw=ROOT/f'metadata/{code}/2026/papers.json'
        assert hashlib.sha256(raw.read_bytes()).hexdigest()==f['catalogue_audit']['raw_sha256']
        report=read(ROOT/f['catalogue_audit']['details_file'])
        assert report==f['catalogue_audit']['report']
        rows=read(raw)
        assert {str(r['id']) for r in rows}==set(report['matched_reference_ids'])
    npj=read(OUT/'npj-browser-catalogue-ids.json')
    assert set(npj['distinct_ids'])=={str(r.get('doi') or r['id']).lower() for r in read(ROOT/'metadata/npjamd/2026/papers.json')}
    # Validate other owners against the requested base, including any main
    # updates incorporated when the task's private branch is rebased.
    old_annual=subprocess.check_output(['git','-C',str(ROOT),'show',f'{other_ref}:metadata/2026/ai4s.json']).decode()
    current_annual=(ROOT/'metadata/2026/ai4s.json').read_text()
    old_hash=nonowner_hash(old_annual);new_hash=nonowner_hash(current_annual)
    assert old_hash==new_hash,('other owners changed',old_hash,new_hash)
    annual=json.loads(current_annual);actual={(r['venue'],r['year'],r['id']) for r in annual if r.get('venue') in CODES}
    assert actual==candidate_keys,('annual candidate IDs not synchronized',len(actual),len(candidate_keys))
    old_snapshot=original(other_ref,'metadata/2026/snapshot.json');current_snapshot=read(ROOT/'metadata/2026/snapshot.json')
    assert old_snapshot['captured_at']==current_snapshot['captured_at']==base['snapshot_at']
    assert [x for x in old_snapshot['sources'] if x['source'] not in CODES]==[x for x in current_snapshot['sources'] if x['source'] not in CODES], 'other source snapshot entries changed'
    changed=subprocess.check_output(['git','-C',str(ROOT),'diff','--name-only',other_ref],text=True).splitlines()
    for p in changed:
        allowed=(p in ('metadata/2026/ai4s.json','metadata/2026/snapshot.json','reviews/2026/dinglijun.json','reviews/2026/feedback/dinglijun.json')
          or p.startswith('reviews/2026/dinglijun/') or any(p.startswith(f'metadata/{code}/2026/') for code in CODES))
        assert allowed,('out-of-scope file changed',p)
    result={'status':'passed','sources':49,'papers_before':before,'papers_after':after,'metadata_added':after-before,
       'original_candidates_covered':original_candidates,'review_records':len(reviews),'decisions':dict(decisions),
       'candidate_records':len(candidate_keys),'all_includes_have_original_abstract':True,'all_bilingual_labels_canonical':True,
       'all_original_papers_preserved':True,'no_unreviewed_deliveries':True,'unknown_year_records_not_included':True,
       'all_original_candidate_fields_preserved':True,'all_verified_pdf_urls_have_live_pdf_evidence':True,
       'other_owner_records_unchanged':True,'other_owner_record_count':old_hash[0],'other_owner_hash':old_hash[1],
       'other_source_snapshot_entries_unchanged':True,'other_owner_base':other_ref,'changed_tracked_files':len(changed)}
    save(OUT/'validation.json',result);print(json.dumps(result,ensure_ascii=False))

if __name__=='__main__':main()
