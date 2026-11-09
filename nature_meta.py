"""按 ISSN 和发表年份抓 Nature 元数据，官网补摘要及文章类型。"""
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from loguru import logger

from fetch_util import get_json, get_text, map_details
from nature_journals import JOURNALS, resolve_issn
from paper_record import make_record, norm_space

CROSSREF = 'https://api.crossref.org/journals/{issn}/works'
CROSSREF_NATURE_FIELDS = (
    'DOI,container-title,title,author,abstract,subject,published-online,published,'
    'issued,published-print,page,resource,URL'
)


def _plain(value: str | None) -> str | None:
    return norm_space(BeautifulSoup(value, 'lxml').get_text(' ', strip=True)) if value else None


def _date(item: dict) -> str | None:
    for key in ('published-online', 'published', 'issued', 'published-print'):
        parts = item.get(key, {}).get('date-parts', [])
        if parts and parts[0]:
            return '-'.join(f'{part:04d}' if i == 0 else f'{part:02d}' for i, part in enumerate(parts[0]))
    return None


def record_from_crossref(item: dict, venue: str, year: int, issn: str) -> dict:
    doi = str(item.get('DOI') or '').strip().lower()
    return make_record(
        id=doi, doi=doi, venue=venue, venue_type='journal', year=year,
        journal_title=(item.get('container-title') or [JOURNALS.get(venue, {}).get('title', venue)])[0], issn=issn,
        title=_plain(' '.join(item.get('title') or [])),
        authors=[norm_space(' '.join(filter(None, (a.get('given'), a.get('family'))))) or a.get('name', '')
                 for a in item.get('author', [])],
        author_ids=[a['ORCID'] for a in item.get('author', []) if a.get('ORCID')],
        abstract=_plain(item.get('abstract')), keywords=item.get('subject') or [],
        published=_date(item), pages=item.get('page'),
        url=f'https://doi.org/{doi}', source='crossref.org', article_type='unknown',
    )


def parse_article_page(html: str) -> dict:
    soup = BeautifulSoup(html, 'lxml')

    def meta(name):
        el = soup.find('meta', attrs={'name': name})
        return norm_space(el.get('content')) if el else None

    abstract = meta('citation_abstract') or meta('dc.description')
    section = soup.select_one('section[data-title="Abstract"] .c-article-section__content, #Abs1-content')
    if section:
        abstract = section.get_text(' ', strip=True)
    article_type = meta('citation_article_type')
    if not article_type:
        el = soup.select_one('[data-test="article-category"], .c-article-identifiers__item')
        article_type = el.get_text(' ', strip=True) if el else None
    article_type = article_type or meta('prism.section') or meta('dc.type')
    return {
        'abstract': norm_space(abstract), 'article_type': article_type,
        'pdf_url': meta('citation_pdf_url'),
        'keywords': [m['content'].strip() for m in soup.find_all('meta', attrs={'name': 'dc.subject'}) if m.get('content')],
    }


def crawl_nature(venue: str, year: int, limit: int | None, existing: dict, on_new, *,
                 flush=None, defer_abstracts=False) -> list[dict]:
    if JOURNALS[venue].get('provider') == 'crossref':
        from journal_meta import crawl_journal
        return crawl_journal(venue, year, limit, existing, on_new, JOURNALS[venue], flush=flush,
                             defer_abstracts=defer_abstracts)
    if limit is not None and limit <= 0:
        raise ValueError('limit 必须为正整数')
    issn = JOURNALS[venue].get('issn_by_year', {}).get(str(year)) or resolve_issn(venue)
    logger.info(f"Nature: {JOURNALS[venue]['title']} {year}, ISSN={issn}")
    params = {'filter': f'from-pub-date:{year}-01-01,until-pub-date:{year}-12-31,type:journal-article',
              'rows': min(limit, 100) if limit else 100, 'cursor': '*',
              'select': CROSSREF_NATURE_FIELDS}
    rows, seen, cursors = [], set(), set()
    endpoint = CROSSREF.format(issn=issn)

    def enrich(job):
        row, item = job
        pid = row['id']
        if item is not None:
            # Only the publisher's public HTML is used for article details.
            url = item.get('resource', {}).get('primary', {}).get('URL') or item.get('URL') or row['url']
            host = (urlparse(url).hostname or '').lower()
            if host in ('doi.org', 'dx.doi.org'):
                url = f'https://www.nature.com/articles/{pid.split("/", 1)[-1]}'
            elif host not in ('nature.com', 'www.nature.com'):
                url = f'https://www.nature.com/articles/{pid.split("/", 1)[-1]}'
            try:
                detail = parse_article_page(get_text(url, timeout=45))
                for key in ('abstract', 'article_type', 'pdf_url'):
                    if detail.get(key):
                        row[key] = detail[key]
                row['keywords'] = list(dict.fromkeys(row.get('keywords', []) + detail['keywords']))
                row['url'] = url
                row['source'] = 'crossref.org+nature.com'
            except Exception as exc:
                logger.warning(f'Nature 页面补全失败 {pid}: {exc}')
        row['screening_status'] = ('needs_abstract' if not row.get('abstract') else
                                   'needs_article_type' if row.get('article_type') in (None, 'unknown') else 'ready')
        return row

    while True:
        cursor = params['cursor']
        if cursor in cursors:
            raise RuntimeError('Crossref 游标重复，停止以避免静默截断数据')
        cursors.add(cursor)
        try:
            message = get_json(endpoint, params=dict(params), timeout=90, retries=6)['message']
        except requests.HTTPError as exc:
            if exc.response is None or exc.response.status_code != 404 or endpoint != CROSSREF.format(issn=issn):
                raise
            # Some new journals have no /journals index; query works by the same ISSN.
            endpoint = 'https://api.crossref.org/works'
            params['filter'] = f"issn:{issn},{params['filter']}"
            logger.info(f'{venue}: Crossref 期刊索引未收录，改用 ISSN 作品检索')
            message = get_json(endpoint, params=dict(params), timeout=90, retries=6)['message']
        items = message.get('items', [])
        if not items:
            if not rows:
                logger.info(f'{venue} {year}: Crossref 按 ISSN 检索无该年论文')
            break
        jobs = []
        for item in items:
            if limit and len(rows) + len(jobs) >= limit:
                break
            row = record_from_crossref(item, venue, year, issn)
            pid = row['id']
            if not pid or not row['title'] or pid in seen:
                continue
            # Crossref 的筛选可能命中印刷日期；本项目优先采用在线发表年份。
            if row['published'] and int(row['published'][:4]) != year:
                continue
            seen.add(pid)
            cached = existing.get(pid)
            if cached and cached.get('abstract') and cached.get('article_type') not in (None, 'unknown'):
                row = dict(cached)
                item = None
            else:
                if cached:
                    row.update({k: v for k, v in cached.items() if v is not None})
            jobs.append((row, item))
        for row in map_details(enrich, jobs):
            rows.append(row)
            on_new(row)
            if limit and len(rows) >= limit:
                return rows
        next_cursor = message.get('next-cursor')
        if not next_cursor:
            break
        params['cursor'] = next_cursor
    return rows
