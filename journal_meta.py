"""Public journal metadata by verified ISSN; Crossref plus OpenAlex/publisher abstracts."""
import os
from concurrent.futures import ThreadPoolExecutor, TimeoutError
from threading import BoundedSemaphore, Lock
from time import monotonic
from urllib.parse import urlparse

import requests

from loguru import logger

from fetch_util import get_json, request_get, map_details
from abstract_sources import fill_abstracts
from kdd_meta import _doi_key, openalex_abstracts
from nature_meta import CROSSREF_NATURE_FIELDS, record_from_crossref, parse_article_page
from conference_meta import parse_publisher_abstract
from paper_record import dump_records, load_records

_PUBLISHER_RETRY_AT = {}
_PUBLISHER_LOCK = Lock()
_PREVIEW_POOL = ThreadPoolExecutor(max_workers=2, thread_name_prefix='journal-preview')
_PREVIEW_SLOTS = BoundedSemaphore(2)


def _queue_openalex_preview(dois):
    key = os.environ.get('OPENALEX_PREVIEW_API_KEY')
    if not key or not dois or not _PREVIEW_SLOTS.acquire(blocking=False):
        return None
    try:
        future = _PREVIEW_POOL.submit(openalex_abstracts, dois, api_key=key)
    except BaseException:
        _PREVIEW_SLOTS.release()
        raise
    future.add_done_callback(lambda _: _PREVIEW_SLOTS.release())
    return future


def publisher_details(url):
    parsed = urlparse(url)
    if parsed.scheme != 'https':
        return {}
    host = parsed.hostname
    with _PUBLISHER_LOCK:
        if _PUBLISHER_RETRY_AT.get(host, 0) > monotonic():
            return {}
    try:
        return _read_publisher_details(url)
    except requests.ConnectionError:
        # Cool down a failing publisher, but do not suppress the shared DOI resolver.
        if host not in ('doi.org', 'dx.doi.org'):
            with _PUBLISHER_LOCK:
                _PUBLISHER_RETRY_AT[host] = monotonic() + 120
        raise


def _read_publisher_details(url):
    with request_get(url, timeout=25, stream=True) as response:
        response.raise_for_status()
        if 'html' not in response.headers.get('Content-Type', '').lower():
            return {}
        chunks, size = [], 0
        for chunk in response.iter_content(65536):
            size += len(chunk)
            if size > 2 * 1024 * 1024:
                return {}
            chunks.append(chunk)
        html = b''.join(chunks).decode(response.encoding or 'utf-8', errors='replace')
    details = parse_article_page(html)
    details['abstract'] = details.get('abstract') or parse_publisher_abstract(html)
    return details


def crawl_journal_resumable(venue, year, existing, on_new, config, flush, dest):
    manifest = dest / 'bibliography-progress.json'
    scope = {'version': 1, 'issns': config['issns'], 'year': year}
    saved = {entry['start']: entry['ids'] for entry in load_records(manifest)
             if entry.get('scope') == scope and isinstance(entry.get('start'), str)
             and isinstance(entry.get('ids'), list) and all(isinstance(i, str) for i in entry['ids'])}
    if len(existing) < 200 and not saved:
        return crawl_journal(venue, year, None, existing, on_new, config, flush=flush,
                             defer_abstracts=True)
    segments = (('01-01', '03-31'), ('04-01', '06-30'),
                ('07-01', '09-30'), ('10-01', '12-31'))
    merged = {}
    for start, end in segments:
        ids = saved.get(start)
        if ids is not None and all(pid in existing for pid in ids):
            rows = [existing[pid] for pid in ids]
            logger.info(f'{venue} {year}: 跳过已完成书目分段 {start} 至 {end}，{len(rows)} 条')
        else:
            rows = crawl_journal(venue, year, None, existing, on_new, config, flush=flush,
                                 defer_abstracts=True, date_range=(start, end))
            flush()
            saved[start] = [row['id'] for row in rows]
            dump_records(manifest, [{'scope': scope, 'start': key, 'ids': value}
                                    for key, value in saved.items()])
            logger.info(f'{venue} {year}: 书目分段已保存 {start} 至 {end}，{len(rows)} 条')
        for row in rows:
            merged.setdefault(row['id'], row)
    return list(merged.values())


def crawl_journal(venue, year, limit, existing, on_new, config, *, flush=None, defer_abstracts=False,
                  date_range=('01-01', '12-31')):
    if limit is not None and limit <= 0:
        raise ValueError('limit必须为正整数')
    logger.info(f'期刊 {venue}: {config.get("title", venue)} {year}, ISSN={",".join(config["issns"])}')
    rows, seen = [], set()
    issns = config['issns']
    endpoint = f'https://api.crossref.org/journals/{issns[0]}/works'
    works = 'https://api.crossref.org/works'
    start, end = date_range
    params = {'filter':f'from-pub-date:{year}-{start},until-pub-date:{year}-{end},type:journal-article',
              'rows': min(limit, 100) if limit else 100, 'cursor':'*'}
    compact_sources = os.environ.get('CROSSREF_COMPACT_SOURCE_YEARS', '').split(',')
    if f'{venue}:{year}' in compact_sources:
        params['select'] = CROSSREF_NATURE_FIELDS + ',ISSN,issue,volume'
    if len(issns) > 1:
        endpoint = works
        params['filter'] += ',' + ','.join(f'issn:{issn}' for issn in issns)
    cursors = set()
    preview = None
    preview_rows = []

    def apply_preview(wait=False):
        nonlocal preview, preview_rows
        if preview is None or (not wait and not preview.done()):
            return
        try:
            abstracts = preview.result(timeout=5 if wait else 0)
        except TimeoutError:
            return
        except Exception as exc:
            logger.warning(f'{venue} {year}: OpenAlex 摘要预取中断: {exc}')
            preview = None
            preview_rows = []
            return
        hits = 0
        for row in preview_rows:
            abstract = abstracts.get(_doi_key(row.get('doi')))
            if abstract and not row.get('abstract'):
                row['abstract'] = abstract
                row['source'] = 'crossref.org+openalex.org'
                row['screening_status'] = ('needs_article_type' if row['article_type'] == 'unknown'
                                           else 'ready')
                on_new(dict(row))
                hits += 1
        if hits:
            if flush is not None:
                flush()
            logger.info(f'{venue} {year}: 书目采集中提前补到 {hits} 篇 OpenAlex 摘要')
        preview = None
        preview_rows = []

    while True:
        cursor = params['cursor']
        if cursor in cursors:
            raise RuntimeError(f'{venue}: Crossref重复游标，保留检查点后停止')
        cursors.add(cursor)
        while True:
            try:
                message = get_json(endpoint, params=dict(params), timeout=90, retries=6)['message']
                break
            except requests.HTTPError as exc:
                status = exc.response.status_code if exc.response is not None else None
                if status == 404 and endpoint != works:
                    endpoint = works
                    params['filter'] = f"issn:{issns[0]},{params['filter']}"
                elif status == 400 and 'select' in params:
                    params.pop('select')
                    logger.warning(f'{venue} {year}: Crossref 拒绝字段精简，本刊继续使用全字段')
                else:
                    raise
        apply_preview()
        items = message.get('items', [])
        if not items:
            break
        next_cursor = message.get('next-cursor') if len(items) >= params['rows'] else None
        if cursor == '*' and next_cursor and 'select' not in params:
            if not any(item.get('subtype') for item in items):
                params['select'] = CROSSREF_NATURE_FIELDS + ',ISSN,issue,volume'
                logger.info(f'{venue} {year}: Crossref 首页未见 subtype，后续页启用字段精简')
        jobs = []
        for item in items:
            if config.get('issue') and str(item.get('issue')) != config['issue']:
                continue
            if config.get('volume') and str(item.get('volume')) != config['volume']:
                continue
            item_issns = item.get('ISSN') or []
            issn = next((value for value in issns if value in item_issns), issns[0])
            row = record_from_crossref(item, venue, year, issn)
            if config.get('venue_type') == 'conference':
                row['venue_type'] = 'conference'
                row['conference_title'] = config['title']
            pid = row['id']
            if not pid or not row['title'] or pid in seen:
                continue
            if row.get('published') and int(row['published'][:4]) != year:
                continue
            seen.add(pid)
            cached = existing.get(pid)
            if cached:
                row.update({k:v for k,v in cached.items() if v is not None})
            if not row.get('article_type') or row['article_type'] == 'unknown':
                row['article_type'] = item.get('subtype') or 'unknown'
            url = item.get('resource', {}).get('primary', {}).get('URL') or item.get('URL') or row['url']
            if defer_abstracts and not row.get('abstract'):
                row['publisher_url'] = url
            jobs.append((row, url))
            if limit and len(rows) + len(jobs) >= limit:
                break
        missing = [r['doi'] for r, _ in jobs if r.get('doi') and not r.get('abstract')]
        for row, _ in jobs:
            row['screening_status'] = ('needs_abstract' if not row.get('abstract') else
                                       'needs_article_type' if row['article_type'] == 'unknown' else 'ready')
        changed = [row for row, _ in jobs if row != existing.get(row['id'])]
        for row in changed:
            on_new(row)
        if changed and missing and flush is not None:
            flush()
        if defer_abstracts:
            rows.extend(row for row, _ in jobs)
            if limit and len(rows) >= limit:
                apply_preview(wait=True)
                return rows
            if not next_cursor:
                break
            if preview is None:
                preview = _queue_openalex_preview(missing)
                preview_rows = [row for row, _ in jobs]
            params['cursor'] = next_cursor
            continue
        abstracts = fill_abstracts(missing, openalex_abstracts, include_openaire=True)
        def enrich(job):
            original, url = job
            row = dict(original)
            match = abstracts.get(_doi_key(row.get('doi')))
            if not row.get('abstract') and match:
                row['abstract'], host = match
                row['source'] = f'crossref.org+{host}'
            if not row.get('abstract'):
                try:
                    details = publisher_details(url)
                    for key in ('abstract', 'article_type', 'pdf_url'):
                        if details.get(key): row[key] = details[key]
                    if details.get('abstract'):
                        row['source'] = 'crossref.org+publisher'
                except Exception as exc:
                    logger.warning(f'{venue}: 公开摘要暂不可用 {row["id"]}: {exc}')
            row['screening_status'] = ('needs_abstract' if not row.get('abstract') else
                                       'needs_article_type' if row.get('article_type') == 'unknown' else 'ready')
            return row
        for (original, _), row in zip(jobs, map_details(enrich, jobs)):
            rows.append(row)
            if row != original:
                on_new(row)
        logger.info(f'{venue} {year}: 已读取 {len(rows)} 条，ISSN={",".join(issns)}')
        if limit and len(rows) >= limit:
            return rows
        if not next_cursor:
            break
        params['cursor'] = next_cursor
    apply_preview(wait=True)
    logger.info(f'{venue} {year}: ISSN检索完成，共{len(rows)}条；不代表出版社目录全量覆盖')
    return rows
