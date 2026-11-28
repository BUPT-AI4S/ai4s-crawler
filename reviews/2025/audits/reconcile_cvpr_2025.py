#!/usr/bin/env python3
"""Compare the 2025 CVF official proceedings with the fixed crawler snapshot."""

import concurrent.futures
import json
import urllib.request
from datetime import date
from pathlib import Path

from bs4 import BeautifulSoup

DIRECTORY = 'https://openaccess.thecvf.com/CVPR2025?day=all'
BASE = 'https://openaccess.thecvf.com'
PAPERS = Path('metadata/cvpr/2025/papers.json')
AUDIT = Path('reviews/2025/audits/wangwanting-cvpr-2025-official-diff.json')
UA = 'Mozilla/5.0 (compatible; BUPT-AI4S literature audit)'


def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': UA}), timeout=30) as response:
        return response.read().decode('utf-8', 'replace')


def parse_paper(pair):
    paper_id, url = pair
    try:
        soup = BeautifulSoup(get(url), 'html.parser')
        def meta(name):
            item = soup.find('meta', attrs={'name': name})
            return item.get('content', '').strip() if item else None
        abstract = soup.find(id='abstract')
        return {'id': paper_id, 'url': url, 'title': meta('citation_title'),
                'authors': [x.get('content', '').strip() for x in soup.find_all('meta', attrs={'name': 'citation_author'})],
                'abstract': abstract.get_text(' ', strip=True) if abstract else None,
                'pdf_url': meta('citation_pdf_url'), 'firstpage': meta('citation_firstpage'),
                'lastpage': meta('citation_lastpage')}
    except Exception as exc:
        return {'id': paper_id, 'url': url, 'error': str(exc)[:200]}


def main():
    soup = BeautifulSoup(get(DIRECTORY), 'html.parser')
    official = {}
    for link in soup.select('a[href*="/content/CVPR2025/html/"]'):
        href = link.get('href', '')
        if not href.endswith('_CVPR_2025_paper.html'):
            continue
        paper_id = href.rsplit('/', 1)[-1][:-5]
        official[paper_id] = BASE + href
    local = {p['id']: p for p in json.loads(PAPERS.read_text())}
    missing = sorted(set(official) - set(local))
    extra = sorted(set(local) - set(official))
    with concurrent.futures.ThreadPoolExecutor(max_workers=12) as pool:
        recovered = list(pool.map(parse_paper, [(key, official[key]) for key in missing]))
    report = {'checked_at': str(date.today()), 'directory': DIRECTORY, 'scope': 'CVPR 2025 official main conference paper HTML pages',
              'official_count': len(official), 'local_count': len(local), 'missing_count': len(missing),
              'extra_count': len(extra), 'extra_ids': extra, 'unresolved': [r for r in recovered if r.get('error') or not r.get('abstract')],
              'official_missing_in_snapshot': recovered}
    AUDIT.parent.mkdir(parents=True, exist_ok=True)
    AUDIT.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: report[k] for k in ['official_count', 'local_count', 'missing_count', 'extra_count']}
                     | {'unresolved_count': len(report['unresolved'])}))


if __name__ == '__main__':
    main()
