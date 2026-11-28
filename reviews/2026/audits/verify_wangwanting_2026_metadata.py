#!/usr/bin/env python3
"""Verify Wang Wanting's 2026 included-paper metadata against public records.

Only exact DOI/title matches are written. Unmatched records remain untouched and
are reported for manual checking. Run from the repository root.
"""

import argparse
import concurrent.futures
import difflib
import html
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

REVIEW = Path('reviews/2026/Blueblue1101.json')
FEEDBACK = Path('reviews/2026/feedback/Blueblue1101.json')
AUDIT = Path('reviews/2026/audits/wangwanting-2026-metadata-verification.json')
UA = 'BUPT-AI4S metadata verification (academic bibliography; contact via GitHub BUPT-AI4S)'


def norm(s):
    s = html.unescape(re.sub('<[^>]*>', ' ', str(s or ''))).casefold()
    return re.sub(r'[^a-z0-9]+', '', s)


def doi_of(p):
    for v in [p.get('doi'), p.get('id'), p.get('url')]:
        m = re.search(r'10\.\d{4,9}/[^\s?#]+', str(v or ''), re.I)
        if m:
            return urllib.parse.unquote(m.group(0)).rstrip('.,;)').lower()
    return None


def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': UA, 'Accept': 'application/json,text/html;q=0.9,*/*;q=0.5'})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=25) as r:
                return r.read(3_000_000).decode('utf-8', 'replace'), r.url
        except urllib.error.HTTPError as e:
            if e.code not in (429, 500, 502, 503, 504):
                raise
        except (TimeoutError, urllib.error.URLError):
            pass
        time.sleep(1.5 * (attempt + 1))
    raise RuntimeError('network retries exhausted')


def verify(p):
    doi = doi_of(p)
    if doi:
        api = 'https://api.crossref.org/works/' + urllib.parse.quote(doi, safe='/')
        try:
            body, _ = fetch(api)
            m = json.loads(body)['message']
            title = html.unescape((m.get('title') or [''])[0])
            score = difflib.SequenceMatcher(None, norm(title), norm(p['title'])).ratio()
            if m.get('DOI', '').lower() != doi or score < .90:
                return {'state': 'mismatch', 'doi': doi, 'score': round(score, 3), 'crossref_title': title}
            authors = [' '.join(filter(None, [a.get('given'), a.get('family')])) for a in m.get('author', [])]
            v = {'title': title, 'doi': doi, 'checked_at': str(date.today()), 'evidence_urls': [api]}
            if authors:
                v['authors'] = authors
            landing = m.get('resource', {}).get('primary', {}).get('URL') or m.get('URL')
            if landing and not landing.startswith('https://doi.org/'):
                v['url'] = landing
            elif p.get('url') and not re.search(r'(doi\.org|crossref\.org)', p['url']):
                v['url'] = p['url']
            return {'state': 'verified_crossref', 'doi': doi, 'metadata': v, 'score': round(score, 3)}
        except Exception as e:
            return {'state': 'error', 'doi': doi, 'error': str(e)[:180]}
    url = p.get('url', '')
    if 'openaccess.thecvf.com/content/CVPR2026/html/' not in url:
        return {'state': 'no_doi_or_supported_publisher_url'}
    try:
        body, final = fetch(url)
        metas = dict((k.lower(), html.unescape(v)) for k, v in re.findall(r'<meta\s+[^>]*?name=["\']([^"\']+)["\'][^>]*?content=["\']([^"\']+)["\']', body, re.I))
        title = metas.get('citation_title')
        if not title:
            return {'state': 'missing_publisher_metadata'}
        score = difflib.SequenceMatcher(None, norm(title), norm(p['title'])).ratio()
        if score < .90:
            return {'state': 'mismatch', 'score': round(score, 3), 'publisher_title': title}
        v = {'title': title, 'url': final, 'checked_at': str(date.today()), 'evidence_urls': [final]}
        pdf = metas.get('citation_pdf_url')
        if pdf:
            v['pdf_url'] = urllib.parse.urljoin(final, pdf)
        if metas.get('citation_doi'):
            v['doi'] = metas['citation_doi']
        return {'state': 'verified_publisher', 'metadata': v, 'score': round(score, 3)}
    except Exception as e:
        return {'state': 'error', 'error': str(e)[:180]}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--venues', nargs='*', help='Only process these source codes; default: all')
    ap.add_argument('--workers', type=int, default=10)
    ap.add_argument('--retry-unresolved', action='store_true')
    args = ap.parse_args()
    records = json.loads(REVIEW.read_text())
    previous = json.loads(AUDIT.read_text()) if args.retry_unresolved and AUDIT.exists() else None
    retry_keys = {(x['venue'], x['id']) for x in previous['unresolved']} if previous else None
    included = [(i, p) for i, p in enumerate(records) if p.get('ai4s_review', {}).get('decision') == 'include'
                and (not args.venues or p['venue'] in args.venues)
                and (retry_keys is None or (p['venue'], p['id']) in retry_keys)]
    outcomes = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(verify, p): i for i, p in included}
        for future in concurrent.futures.as_completed(futures):
            i = futures[future]
            outcomes[i] = future.result()
    report = defaultdict(lambda: Counter())
    if previous:
        for venue, counts in previous['counts'].items():
            report[venue].update(counts)
    failures = []
    for i, p in included:
        res = outcomes[i]
        if previous:
            report[p['venue']]['error'] -= 1
        report[p['venue']][res['state']] += 1
        if not res['state'].startswith('verified_'):
            failures.append({'venue': p['venue'], 'id': p['id'], 'title': p['title'], **res})
            continue
        old = p['ai4s_review'].get('verified_metadata') or {}
        new = res['metadata']
        ev = list(dict.fromkeys((old.get('evidence_urls') or []) + new.pop('evidence_urls')))
        old.update(new)
        old['evidence_urls'] = ev
        p['ai4s_review']['verified_metadata'] = old
    REVIEW.write_text(json.dumps(records, ensure_ascii=False, indent=2) + '\n')
    if previous:
        old_failures = [x for x in previous['unresolved'] if (x['venue'], x['id']) not in retry_keys]
        failures = old_failures + failures
    AUDIT.write_text(json.dumps({'checked_at': str(date.today()), 'basis': 'Crossref publisher-deposited DOI/title/author; CVF official paper page for DOI-less CVPR records', 'base_snapshot': '2026-11-08', 'counts': report, 'unresolved': failures}, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'target': len(included), 'counts': report, 'unresolved': len(failures)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
