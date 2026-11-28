#!/usr/bin/env python3
"""Check author citations on official CVF pages for DOI-less CVPR records."""

import concurrent.futures
import html
import json
import re
import urllib.request
from collections import Counter
from datetime import date
from pathlib import Path

PATH = Path('reviews/2026/Blueblue1101.json')
AUDIT = Path('reviews/2026/audits/wangwanting-2026-publisher-fields.json')
UA = 'Mozilla/5.0 (compatible; BUPT-AI4S bibliographic verification)'


def check(pair):
    i, p = pair
    url = p['url']
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=25) as f:
            body = f.read(300_000).decode('utf-8', 'replace')
        authors = [html.unescape(a) for a in re.findall(r'<meta\s+name=["\']citation_author["\']\s+content=["\']([^"\']+)', body, re.I)]
        first = authors[0].split(',')[0].lower() if authors else ''
        original = p['authors'][0].lower() if p.get('authors') else ''
        if not authors or first not in original:
            return i, 'author_mismatch', {'publisher_authors': authors[:3], 'original_first': p.get('authors', [''])[0]}
        return i, 'cvf_authors', {'authors': authors}
    except Exception as e:
        return i, 'error', {'error': str(e)[:180]}


def main():
    rows = json.loads(PATH.read_text())
    jobs = [(i, p) for i, p in enumerate(rows) if p.get('ai4s_review', {}).get('decision') == 'include'
            and p['venue'] == 'cvpr' and not p['ai4s_review']['verified_metadata'].get('authors')]
    counts = Counter()
    failures = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:
        for i, state, result in pool.map(check, jobs):
            counts[state] += 1
            if state != 'cvf_authors':
                failures.append({'venue': rows[i]['venue'], 'id': rows[i]['id'], 'state': state, **result})
                continue
            v = rows[i]['ai4s_review']['verified_metadata']
            v.update(result)
            v['checked_at'] = str(date.today())
    PATH.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n')
    all_cvpr = [p for p in rows if p['venue'] == 'cvpr' and p.get('ai4s_review', {}).get('decision') == 'include']
    still_missing = [{'id': p['id'], 'state': 'author_missing'} for p in all_cvpr
                     if not p['ai4s_review']['verified_metadata'].get('authors')]
    AUDIT.write_text(json.dumps({'checked_at': str(date.today()),
                                 'basis': 'Official CVF citation_author metadata',
                                 'included_cvpr': len(all_cvpr),
                                 'verified_author_count': len(all_cvpr) - len(still_missing),
                                 'this_run': counts,
                                 'unresolved': failures + still_missing}, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'jobs': len(jobs), 'cvpr_authors_verified': len(all_cvpr) - len(still_missing),
                      'unresolved': len(failures + still_missing)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
