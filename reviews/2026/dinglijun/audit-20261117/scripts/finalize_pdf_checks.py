"""Combine disjoint bounded public-PDF checks without dropping earlier failures."""
import collections
import copy
import json
from dinglijun_2026_finalize import OUT, inputs, read, save

def main():
    candidates=read(OUT/'public-pdf-candidates.json')
    attempts=copy.deepcopy(read(OUT/'public-pdf-verification-attempts.json'))
    successes=copy.deepcopy(read(OUT/'enrichment-public-pdfs.json'))
    covered=set()
    for part in range(1,5):
        summary=read(OUT/f'public-pdf-summary-part{part}.json')
        queue=read(OUT/f'public-pdf-remaining-part{part}.json')
        rows=read(OUT/f'attempts-part{part}.json')
        found=read(OUT/f'enrichment-public-pdfs-part{part}.json')
        assert summary['status']=='complete' and set(queue)==set(rows)
        assert not covered.intersection(rows)
        covered.update(rows)
        for doi,row in rows.items():
            previous=attempts[doi]
            latest=copy.deepcopy(row)
            latest['earlier_attempts']=previous.get('earlier_attempts',[])+previous.get('attempts',[])
            latest['normal_retry_after_proxy_denial']=True
            attempts[doi]=latest
        assert not set(successes).intersection(found)
        successes.update(found)
    remaining=read(OUT/'public-pdf-remaining.json')
    assert covered==set(remaining)
    assert set(attempts)==set(candidates['records'])
    for doi,entry in successes.items():
        check=entry['pdf_verification']
        assert check['verified_public_pdf'] is True
        assert entry['verified_metadata']['pdf_url']==check['url']
        assert check['url'] in {x['url'] for x in candidates['records'][doi]['locations']}
        assert attempts[doi]['status']=='verified'
    work,ledger=inputs()
    included=[w for w in work if ledger[w['key']]['decision']=='include']
    final_dois={str(w['record'].get('doi') or w['record']['id']).lower() for w in included}
    final_found=[successes[doi] for doi in final_dois if doi in successes]
    counts=collections.Counter(c['status'] for row in attempts.values() for c in row['attempts'])
    for doi,row in attempts.items():row['final_included']=doi in final_dois
    result={'checked_at':'2026-11-17','status':'complete','included_records':len(included),
        'initial_candidate_generation_includes':candidates['included_records'],
        'candidate_dois':candidates['candidate_dois'],'candidate_urls':candidates['candidate_urls'],
        'attempted_dois':len(attempts),'latest_url_checks':sum(counts.values()),
        'verified_public_pdf_dois':len(successes),'unverified_dois':len(attempts)-len(successes),
        'final_included_verified_pdf_count':len(final_found),
        'final_included_verified_pdf_versions':dict(collections.Counter(x['pdf_verification']['version'] for x in final_found)),
        'latest_attempt_statuses':dict(counts),'partition_retries_complete':len(covered),
        'no_duplicate_partition_dois':True,'all_successes_match_discovered_locations':True,
        'scope':'Only previously discovered DOI/title-matched PDF locations. HEAD, or at most 8 bytes when MIME ambiguous/HEAD unsupported. One ordinary retry after proxy denial; prior failures retained. Stop after first verified PDF per DOI. HTML and access errors are not proof that no public version exists.'}
    save(OUT/'public-pdf-verification-final.json',attempts)
    save(OUT/'public-pdf-verification-summary.json',result)
    print(json.dumps(result,ensure_ascii=False))

if __name__=='__main__':main()
