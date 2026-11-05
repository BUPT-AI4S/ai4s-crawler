"""Supplement completed journal bibliographies without holding source slots."""
import os
import sqlite3
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from contextlib import closing
from itertools import islice
from time import monotonic

from loguru import logger

from abstract_sources import europe_pmc_abstracts, fill_abstracts, pubmed_abstracts
from ai4s_filter import select_ai4s
from fetch_util import map_details
from journal_meta import publisher_details
from kdd_meta import OPENALEX_BATCH, _doi_key, openalex_abstracts
from paper_record import dump_records, load_records

_OPENALEX_WORKERS = max(1, int(os.environ.get('OPENALEX_FETCH_WORKERS', '12')))
_OPENALEX_POOL = ThreadPoolExecutor(max_workers=_OPENALEX_WORKERS, thread_name_prefix='abstract-openalex')


def _parallel_openalex(dois, on_batch=None, *, pending_limit=None):
    batches = (dois[start:start + OPENALEX_BATCH] for start in range(0, len(dois), OPENALEX_BATCH))
    found = {}
    futures = {_OPENALEX_POOL.submit(openalex_abstracts, batch)
               for batch in islice(batches, pending_limit or _OPENALEX_WORKERS)}
    try:
        while futures:
            done, futures = wait(futures, return_when=FIRST_COMPLETED)
            for future in done:
                hits = future.result()
                found.update(hits)
                if on_batch is not None:
                    on_batch(hits)
            futures.update(_OPENALEX_POOL.submit(openalex_abstracts, batch)
                           for batch in islice(batches, len(done)))
    finally:
        for future in futures:
            future.cancel()
    return found


def _has_abstract(row):
    return bool(str(row.get('abstract') or '').strip())


def _abstract_gap(root, year, folder):
    rows = load_records(root / folder / str(year) / 'papers.json')
    missing = [row for row in rows if not _has_abstract(row)]
    large = len(missing) >= 20 or (len(missing) >= 5 and len(missing) * 10 >= len(rows))
    return large, any(_doi_key(row.get('doi')) for row in missing)


def complete_abstracts(root, year, folders, update):
    pending = list(folders)
    for round_no, options in enumerate(({'openalex_only': True}, {'biomedical_only': True}, {}), 1):
        eligible = []
        for folder in pending:
            large, has_doi = _abstract_gap(root, year, folder)
            if large and has_doi:
                eligible.append(folder)
                update(folder, 'backfilling')
            else:
                update(folder, 'abstract_incomplete' if large else 'completed')
        if not eligible:
            return
        logger.info(f'{year} 摘要补查第 {round_no}/3 轮，{len(eligible)} 个来源')
        try:
            backfill_journal_abstracts(root, year, eligible, **options)
        except Exception as exc:
            logger.warning(f'{year} 第 {round_no}/3 轮摘要补查中断：{type(exc).__name__}')
        pending = eligible
    for folder in pending:
        large, _ = _abstract_gap(root, year, folder)
        update(folder, 'abstract_incomplete' if large else 'completed')


def backfill_journal_abstracts(root, year, folders, *, openalex_only=False, biomedical_only=False):
    pending = {}
    sources = {}
    for folder in folders:
        dest = root / folder / str(year)
        rows = load_records(dest / 'papers.json')
        sources[dest] = rows
        for row in rows:
            doi = _doi_key(row.get('doi'))
            if doi and not _has_abstract(row):
                pending.setdefault(doi, []).append(row)
    if not pending:
        return

    keys = list(pending)
    found = {}
    changed = set()
    last_write = 0.0

    def publish(force=False):
        nonlocal last_write
        if not changed or (not force and monotonic() - last_write < 5):
            return
        for dest, rows in sources.items():
            if any(id(row) in changed for row in rows):
                dump_records(dest / 'papers.json', rows)
                dump_records(dest / 'ai4s.json', select_ai4s(rows))
        changed.clear()
        last_write = monotonic()

    def apply_hits(hits):
        for doi, (abstract, host) in hits.items():
            for row in pending.get(doi, ()):
                if not _has_abstract(row):
                    row['abstract'] = abstract
                    row['source'] = f'{row.get("source") or "metadata"}+{host}'
                    row['screening_status'] = ('needs_article_type' if row.get('article_type') in (None, 'unknown')
                                               else 'ready')
                    changed.add(id(row))

    with closing(sqlite3.connect(root / 'journal-abstract-cache.sqlite3')) as cache:
        cache.execute('CREATE TABLE IF NOT EXISTS abstracts (doi TEXT PRIMARY KEY, abstract TEXT, source TEXT)')
        for start in range(0, len(keys), 90):
            batch = keys[start:start + 90]
            placeholders = ','.join('?' for _ in batch)
            cached = {doi: (abstract, source) for doi, abstract, source in cache.execute(
                f'SELECT doi, abstract, source FROM abstracts WHERE doi IN ({placeholders})', batch
            )}
            found.update(cached)
        apply_hits(found)
        publish(force=True)

        def save(hits):
            with cache:
                cache.executemany('INSERT OR IGNORE INTO abstracts VALUES (?, ?, ?)',
                                  [(doi, abstract, source) for doi, (abstract, source) in hits.items()])
            apply_hits(hits)

        def lookup_openalex(dois):
            def save_batch(hits):
                if hits:
                    save({doi: (abstract, 'openalex.org') for doi, abstract in hits.items()})
                    publish()

            hits = _parallel_openalex(dois, on_batch=save_batch,
                                      pending_limit=None)
            publish(force=True)
            logger.info(f'OpenAlex 摘要首轮: {len(folders)} 个来源，查 {len(dois)} 个 DOI，命中 {len(hits)} 个')
            return hits

        missing = [doi for doi in keys if doi not in found]
        if biomedical_only:
            for host, lookup in (('europepmc.org', europe_pmc_abstracts),
                                 ('pubmed.ncbi.nlm.nih.gov', pubmed_abstracts)):
                remaining = [doi for doi in missing if doi not in found]
                for start in range(0, len(remaining), 100):
                    batch = remaining[start:start + 100]
                    hits = {doi: (abstract, host) for doi, abstract in lookup(batch).items()}
                    if hits:
                        found.update(hits)
                        save(hits)
                        publish()
                publish(force=True)
            return
        if missing:
            if openalex_only:
                lookup_openalex(missing)
                return
            fetched = fill_abstracts(missing, lookup_openalex, include_openaire=True)
            found.update(fetched)
            save(fetched)
            publish(force=True)

    if openalex_only:
        return

    def publisher(doi):
        row = pending[doi][0]
        try:
            return doi, publisher_details(row.get('publisher_url') or row.get('url') or '')
        except Exception as exc:
            logger.warning(f'公开摘要暂不可用 {doi}: {exc}')
            return doi, {}

    publisher_hits = dict(map_details(publisher, [doi for doi in keys if doi not in found]))
    for doi, details in publisher_hits.items():
        if not details:
            continue
        records = pending[doi]
        for row in records:
            for field in ('abstract', 'article_type', 'pdf_url'):
                if details.get(field):
                    row[field] = details[field]
            if row.get('abstract'):
                row['source'] = f'{row.get("source") or "metadata"}+publisher'
            row['screening_status'] = ('needs_abstract' if not row.get('abstract') else
                                       'needs_article_type' if row.get('article_type') in (None, 'unknown')
                                       else 'ready')
            changed.add(id(row))

    publish(force=True)
    logger.info(f'期刊摘要回填: {len(folders)} 个来源，{len(keys)} 个 DOI，'
                f'补到 {len(found) + sum(bool(d.get("abstract")) for d in publisher_hits.values())} 个')
