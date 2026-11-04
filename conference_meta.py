"""DBLP 分页枚举论文，OpenAlex 批量补摘要，缺失项再查 Crossref 与出版社。"""
import os
import re
import json
import time
from urllib.parse import quote, urlparse

import requests

from bs4 import BeautifulSoup
from loguru import logger

from ccf_venues import CONFERENCES, annotate_ccf_record
from fetch_util import HEADERS, get_json, is_transient, map_details, request_get
from abstract_sources import fill_abstracts
from kdd_meta import _doi_key, openalex_abstracts
from paper_record import make_record, norm_space

ENDPOINT = 'https://sparql.dblp.org/sparql'
PAGE_SIZE = 100

# DBLP SPARQL 的 503/502/超时是常态；单页失败先退避重试，不要让整个来源判死。
PAGE_RETRIES = max(1, int(os.environ.get('DBLP_PAGE_RETRIES', '5')))
PAGE_BACKOFF = max(1.0, float(os.environ.get('DBLP_PAGE_BACKOFF', '10')))


def _page_payload(venue: str, year: int, size: int, offset: int) -> dict:
    last: Exception | None = None
    for attempt in range(PAGE_RETRIES):
        try:
            return get_json(ENDPOINT, params={'query': build_query(venue, year, size, offset)},
                            headers={'Accept': 'application/sparql-results+json'}, timeout=60,
                            sleep_s=0.5, retries=1)
        except (requests.RequestException, RuntimeError) as exc:
            if not is_transient(exc):
                raise
            last = exc
            if attempt + 1 >= PAGE_RETRIES:
                break
            delay = min(120.0, PAGE_BACKOFF * (2 ** attempt))
            logger.warning(f'{venue} {year}: DBLP 枚举第 {attempt + 1} 次失败'
                           f'（{type(exc).__name__}），{delay:.0f} 秒后重试')
            time.sleep(delay)
    raise last


def build_query(venue: str, year: int, size: int, offset: int) -> str:
    if venue not in CONFERENCES or not 1900 <= year <= 2200 or size <= 0 or offset < 0:
        raise ValueError('会议、年份或分页参数无效')
    config = CONFERENCES[venue]
    streams = [config['dblp_stream']] + config.get('additional_streams', [])
    if not all(re.fullmatch(r'https://dblp\.org/streams/(?:conf|journals)/[A-Za-z0-9_-]+', s) for s in streams):
        raise ValueError('会议注册表中 DBLP stream 格式无效')
    values = ' '.join(f'<{s}>' for s in streams)
    toc_prefix = config.get('dblp_toc_prefix')
    if toc_prefix:
        if not re.fullmatch(r'https://dblp\.org/db/conf/[A-Za-z0-9_-]+/[A-Za-z0-9_-]+', toc_prefix):
            raise ValueError('会议注册表中 DBLP TOC 前缀格式无效')
        pattern = json.dumps('^' + re.escape(toc_prefix + str(year)) + r'($|[-/.])')
        year_clause = f'dblp:listedOnTocPage ?toc ; a ?type . FILTER(REGEX(STR(?toc), {pattern}))'
    else:
        year_clause = f'dblp:yearOfPublication "{year}"^^xsd:gYear ; a ?type .'
    return f'''PREFIX dblp: <https://dblp.org/rdf/schema#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
SELECT DISTINCT ?pub ?title WHERE {{
 VALUES ?stream {{ {values} }}
 ?pub dblp:publishedInStream ?stream ; dblp:title ?title ;
      {year_clause}
 FILTER(?type IN (dblp:Inproceedings, dblp:Article, dblp:Incollection))
}} ORDER BY ?pub LIMIT {size} OFFSET {offset}'''


def build_details_query(pubs: list[str]) -> str:
    if not pubs or not all(re.fullmatch(r'https://dblp\.org/rec/[^\s<>"{}|\\^`]+', pub) for pub in pubs):
        raise ValueError('无效的 DBLP 论文 URI')
    values = ' '.join(f'<{pub}>' for pub in pubs)
    return f'''PREFIX dblp: <https://dblp.org/rdf/schema#>
SELECT ?pub ?title ?doi ?pages ?booktitle ?toc ?year ?document ?ordinal ?authorName ?person WHERE {{
 VALUES ?pub {{ {values} }}
 ?pub dblp:title ?title .
 OPTIONAL {{ ?pub dblp:doi ?doi }}
 OPTIONAL {{ ?pub dblp:pagination ?pages }}
 OPTIONAL {{ ?pub dblp:publishedIn ?booktitle }}
 OPTIONAL {{ ?pub dblp:listedOnTocPage ?toc }}
 OPTIONAL {{ ?pub dblp:yearOfPublication ?year }}
 OPTIONAL {{ ?pub dblp:primaryDocumentPage ?document }}
 OPTIONAL {{ ?pub dblp:hasSignature ?sig .
   ?sig a dblp:AuthorSignature ; dblp:signatureOrdinal ?ordinal ;
        dblp:signatureDblpName ?authorName ; dblp:signatureCreator ?person .
 }}
}}'''


def _details(primary: list[dict]) -> list[dict]:
    # 先限定论文列表，再取作者等属性，避免让服务端对全图作者关联做聚合排序。
    by_pub = {row['pub']['value']: dict(row) for row in primary}
    try:
        payload = get_json(ENDPOINT, params={'query': build_details_query(list(by_pub))},
                           headers={'Accept': 'application/sparql-results+json'}, timeout=60,
                           sleep_s=0.5, retries=2)
    except (requests.RequestException, RuntimeError) as exc:
        if len(primary) <= 1 or not is_transient(exc):
            raise
        middle = len(primary) // 2
        logger.warning(f'DBLP 详情查询暂时失败，拆分 {len(primary)} 条为两个较小批次')
        return _details(primary[:middle]) + _details(primary[middle:])
    signatures = {}
    for detail in payload['results']['bindings']:
        pub = detail['pub']['value']
        if pub not in by_pub:
            raise ValueError('DBLP 详情返回了未请求的论文')
        by_pub[pub].update({k: v for k, v in detail.items() if k not in ('ordinal', 'authorName', 'person')})
        if all(k in detail for k in ('ordinal', 'authorName', 'person')):
            sig = ':::'.join(detail[k]['value'] for k in ('ordinal', 'authorName', 'person'))
            signatures.setdefault(pub, set()).add(sig)
    for pub, values in signatures.items():
        by_pub[pub]['authors'] = {'value': '|||'.join(values)}
    return list(by_pub.values())


def record_from_binding(binding: dict, venue: str, year: int) -> dict:
    def value(key):
        return binding.get(key, {}).get('value')

    doi = (value('doi') or '').split('doi.org/')[-1].strip().lower() or None
    people = []
    for item in (value('authors') or '').split('|||'):
        parts = item.split(':::', 2)
        if len(parts) == 3 and parts[0].isdigit():
            people.append((int(parts[0]), parts[1], parts[2]))
    people.sort()
    pub = value('pub')
    if not pub or not value('title'):
        raise ValueError('DBLP 返回记录缺少论文标识或标题')
    row = make_record(
        id=doi or pub, doi=doi, venue=venue, venue_type='conference', year=year,
        conference_title=CONFERENCES[venue]['name'], title=value('title'),
        authors=[p[1] for p in people], author_ids=[p[2] for p in people],
        pages=value('pages'), published=value('year') or str(year),
        url=value('document') or (f'https://doi.org/{doi}' if doi else pub), source='sparql.dblp.org',
        article_type='Conference Paper', track='unverified', screening_status='needs_abstract',
        dblp_key=pub, dblp_toc=value('toc'), booktitle=value('booktitle'),
    )
    return annotate_ccf_record(row, venue)


def crossref_abstract(doi: str) -> str | None:
    message = get_json('https://api.crossref.org/works/' + quote(doi, safe='/'), timeout=30, retries=1)['message']
    abstract = message.get('abstract')
    if not isinstance(abstract, str) or not abstract.strip():
        return None
    return norm_space(BeautifulSoup(abstract, 'lxml').get_text(' ', strip=True))


def parse_publisher_abstract(html: str) -> str | None:
    soup = BeautifulSoup(html, 'lxml')
    meta = soup.find('meta', attrs={'name': 'citation_abstract'})
    if meta and meta.get('content'):
        return norm_space(meta['content'])
    node = soup.select_one('.abstract, #abstract, .abstractSection, #Abs1-content, '
                           '.article__abstract, .acl-abstract, .field-name-field-paper-description, '
                           'section[data-title="Abstract"] .c-article-section__content')
    if node:
        return norm_space(re.sub(r'^Abstract\s*', '', node.get_text(' ', strip=True), flags=re.I))
    return None


def publisher_abstract(url: str | None) -> str | None:
    if not url:
        return None
    parts = urlparse(url)
    if parts.scheme != 'https' or parts.path.lower().endswith('.pdf'):
        return None
    domains = ('doi.org', 'mlr.press', 'jmlr.org', 'ijcai.org', 'acm.org', 'springer.com',
               'nature.com', 'ieee.org', 'usenix.org', 'aaai.org', 'iospress.com', 'dagstuhl.de',
               'vldb.org', 'aclanthology.org', 'siam.org', 'openreview.net', 'neurips.cc',
               'nips.cc', 'iacr.org', 'scipost.org', 'sciencedirect.com', 'wiley.com', 'oup.com',
               'ndss-symposium.org')
    host = (parts.hostname or '').lower()
    if not any(host == d or host.endswith('.' + d) for d in domains):
        return None
    # DOI可能重定向到PDF。使用流式请求，确认是HTML后才读取正文，不下载PDF。
    for attempt in range(2):
        try:
            with request_get(url, headers=HEADERS, timeout=20, stream=True) as response:
                response.raise_for_status()
                if 'text/html' not in response.headers.get('Content-Type', '').lower():
                    return None
                content = bytearray()
                for chunk in response.iter_content(65536):
                    content.extend(chunk)
                    if len(content) > 2_000_000:
                        return None
                return parse_publisher_abstract(content.decode(response.encoding or 'utf-8', errors='replace'))
        except (requests.ConnectionError, requests.exceptions.ChunkedEncodingError):
            if attempt:
                raise
            time.sleep(1)


def crawl_conference(venue: str, year: int, limit: int | None, existing: dict, on_new) -> list[dict]:
    if venue not in CONFERENCES or (limit is not None and limit <= 0):
        raise ValueError('会议或 limit 无效')
    config = CONFERENCES[venue]
    logger.info(f"CCF-{config['rank']} {config['acronym']} {year}: DBLP SPARQL")
    if config.get('coverage_note'):
        logger.warning(config['coverage_note'])
    records, seen, saved_ids = [], set(), set()
    offset = 0
    while True:
        size = min(PAGE_SIZE, limit - len(records)) if limit else PAGE_SIZE
        payload = _page_payload(venue, year, size, offset)
        bindings = payload['results']['bindings']
        if not bindings:
            break
        if all(binding['pub']['value'] in seen for binding in bindings):
            raise RuntimeError('DBLP 返回重复分页，停止以免静默截断')
        new_count = 0
        page_rows = []
        for binding in _details(bindings):
            row = record_from_binding(binding, venue, year)
            if row['dblp_key'] in seen:
                continue
            seen.add(row['dblp_key'])
            new_count += 1
            if row['id'] in saved_ids:
                continue
            saved_ids.add(row['id'])
            cached = existing.get(row['id'])
            if cached:
                row = annotate_ccf_record({**row, **cached}, venue)
            page_rows.append(row)
        missing = [row['doi'] for row in page_rows if row.get('doi') and not row.get('abstract')
                   and row.get('ccf_paper_status') != 'excluded']
        # One request can enrich many DOI records, including old checkpoints with no abstract.
        batch_abstracts = fill_abstracts(missing, openalex_abstracts)
        def enrich(row):
            match = batch_abstracts.get(_doi_key(row.get('doi')))
            if not row.get('abstract') and match:
                row['abstract'], host = match
                row['source'] = f'sparql.dblp.org+{host}'
            # 已知非长文只保留书目，不额外请求摘要。
            if not row.get('abstract') and row.get('doi') and row.get('ccf_paper_status') != 'excluded':
                try:
                    row['abstract'] = crossref_abstract(row['doi'])
                    if row['abstract']:
                        row['source'] = 'sparql.dblp.org+crossref.org'
                except Exception as exc:
                    logger.warning(f"摘要补全失败 {row['id']}: {exc}")
            if not row.get('abstract') and row.get('ccf_paper_status') != 'excluded':
                try:
                    row['abstract'] = publisher_abstract(row.get('url'))
                    if row['abstract']:
                        row['source'] = 'sparql.dblp.org+publisher'
                except Exception as exc:
                    host = urlparse(row.get('url') or '').hostname or 'unknown'
                    logger.warning(f"公开HTML摘要不可用 {row['id']} [upstream={host}]: {exc}")
            row['screening_status'] = 'ready' if row.get('abstract') else 'needs_abstract'
            return row

        for row in map_details(enrich, page_rows):
            records.append(row)
            on_new(row)
            if limit and len(records) >= limit:
                return records
        if not new_count:
            raise RuntimeError('DBLP 返回重复分页，停止以免静默截断')
        logger.info(f"{venue} {year}: 已读取 {len(records)} 条")
        offset += len(bindings)
        if len(bindings) < size:
            break
    if not records:
        logger.warning(f'{venue} {year} 未找到记录；可能该年未举办、尚未索引或由期刊承载，不能据此断言没有论文')
    return records
