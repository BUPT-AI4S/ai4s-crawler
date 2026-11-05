import argparse
import json
import os
import random
import sys
import threading
import time
from itertools import zip_longest
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict
from pathlib import Path

from loguru import logger

logger.remove()
logger.add(sys.stderr, diagnose=False)

from aaai_meta import crawl_aaai
from approved_sources import APPROVED_SOURCES
from ai4s_filter import select_ai4s
from anthology_meta import crawl_anthology
from ccf_venues import (CONFERENCES, ALIASES as CCF_ALIASES, GROUPS as CCF_GROUPS,
                        canonical_venue, expand_ccf_venues, annotate_ccf_record)
from conference_meta import crawl_conference
from eccv_meta import crawl_eccv
from kdd_meta import crawl_kdd
from nature_journals import ALIASES as NATURE_ALIASES, GROUPS as NATURE_GROUPS, JOURNALS, expand_venues
from nature_meta import crawl_nature
from openreview_api import (
    OpenReviewBlocked,
    download_openreview_pdf,
    fetch_openreview_accepted,
    fetch_openreview_records,
    get_openreview_client,
)
from virtual_meta import crawl_virtual
from paper_record import RecordCheckpoint, dump_records, load_records
from pdf_download import download_pdf, filename_from_detail
from thecvf import THECVF_VENUES, crawl_openaccess_metadata, list_thecvf_papers
from fetch_util import HostCooldown, is_transient

# 走 OpenReview 的会议。venueid 模板：{year} 会替换成年份。
VENUES = {
    "iclr": "ICLR.cc/{year}/Conference",
    "neurips": "NeurIPS.cc/{year}/Conference",
    "nips": "NeurIPS.cc/{year}/Conference",
    "icml": "ICML.cc/{year}/Conference",
    "acl": "aclweb.org/ACL/{year}/Conference",
    "emnlp": "EMNLP/{year}/Conference",
    "naacl": "aclweb.org/NAACL/{year}/Conference",
}

OPENREVIEW_MAIN = {"iclr", "neurips", "nips", "icml"}
ANTHOLOGY_VENUES = {"acl", "naacl", "emnlp"}
_SPECIALIZED_CONFERENCES = set(VENUES) | set(THECVF_VENUES) | {'aaai', 'kdd'}
META_ONLY_VENUES = {"aaai", "kdd"} | set(JOURNALS) | (set(CONFERENCES) - _SPECIALIZED_CONFERENCES)
OPENACCESS_META = {"cvpr", "iccv", "wacv"}
_OPENREVIEW_LOCK = threading.Lock()


def _folder_name(venue: str) -> str:
    key = canonical_venue(venue)
    key = NATURE_ALIASES.get(key, key)
    if key == "nips":
        return "neurips"
    if key in VENUES or key in THECVF_VENUES or key in META_ONLY_VENUES:
        return key
    return venue.strip().replace("/", "_")


def resolve_venue_id(name: str, year: int) -> str:
    raw = name.strip()
    if "/" in raw:
        return raw.replace("{year}", str(year))
    key = raw.lower()
    if key not in VENUES:
        known = ", ".join(sorted(known_venues()))
        raise SystemExit(f"未知会议 {name!r}，可选: {known}")
    return VENUES[key].format(year=year)


def known_venues() -> set[str]:
    return ({'teacher-approved'} | {k for k in VENUES if k != "nips"} | set(THECVF_VENUES) | set(META_ONLY_VENUES)
            | set(NATURE_ALIASES) | set(NATURE_GROUPS) | set(CCF_ALIASES) | set(CCF_GROUPS))


def _write_result(dest_root: Path, result: list[dict]) -> None:
    dest_root.mkdir(parents=True, exist_ok=True)
    out = dest_root / "papers.json"
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    logger.info(f"元数据已写入 {out}")


def crawl_thecvf_venue(venue: str, year: int, limit: int | None, pdf_dir: Path) -> list[dict]:
    logger.info(f"从 TheCVF Open Access 拉取 {venue.upper()} {year}")
    papers = list_thecvf_papers(venue, year)
    if limit:
        papers = papers[:limit]
    logger.info(f"{venue.upper()} {year} 共 {len(papers)} 篇")
    if not papers:
        logger.warning("没有论文。该年 Open Access 可能还没上线")
        return []

    dest_root = pdf_dir / _folder_name(venue) / str(year)
    dest_root.mkdir(parents=True, exist_ok=True)
    result = []
    for i, paper in enumerate(papers, 1):
        item = dict(paper)
        item["pdf_path"] = None
        pdf_url = paper.get("pdf_url")
        try:
            if not pdf_url:
                raise ValueError("没有 pdf_url")
            dest = dest_root / filename_from_detail(paper.get("url") or pdf_url, paper)
            item["pdf_path"] = download_pdf(pdf_url, str(dest))
            logger.info(f"[{i}/{len(papers)}] {paper.get('title')}")
        except Exception as e:
            logger.warning(f"[{i}/{len(papers)}] 下载失败 {paper.get('url')}: {e}")
        result.append(item)
        time.sleep(0.5 + random.random() * 0.4)

    _write_result(dest_root, result)
    return result


def crawl_openreview_venue(venue: str, year: int, limit: int | None, pdf_dir: Path) -> list[dict]:
    venue_id = resolve_venue_id(venue, year)
    logger.info(f"从 OpenReview 拉取录用稿: {venue_id}")
    papers = fetch_openreview_accepted(venue_id, limit=limit)
    logger.info(f"{venue_id} 共 {len(papers)} 篇")
    if not papers:
        logger.warning("没有论文。可能该年还没公开，或没有使用 OpenReview")
        return []

    dest_root = pdf_dir / _folder_name(venue) / str(year)
    dest_root.mkdir(parents=True, exist_ok=True)
    result = []
    for i, paper in enumerate(papers, 1):
        item = asdict(paper)
        item["pdf_path"] = None
        try:
            dest = dest_root / f"{paper.forum_id}.pdf"
            item["pdf_path"] = download_openreview_pdf(paper.forum_id, str(dest))
            logger.info(f"[{i}/{len(papers)}] {paper.title}")
        except Exception as e:
            logger.warning(f"[{i}/{len(papers)}] 下载失败 {paper.forum_id}: {e}")
        result.append(item)
        time.sleep(0.3 + random.random() * 0.3)

    _write_result(dest_root, result)
    return result


def crawl_venue(venue: str, year: int, limit: int | None, pdf_dir: Path) -> list[dict]:
    key = venue.strip().lower()
    if key in META_ONLY_VENUES:
        raise SystemExit(f"{key} 只支持 --metadata-only")
    if key in THECVF_VENUES:
        return crawl_thecvf_venue(key, year, limit, pdf_dir)
    return crawl_openreview_venue(venue, year, limit, pdf_dir)


def _needs_openreview_now(venues: list[str], metadata_only: bool) -> bool:
    for venue in venues:
        if "/" in venue:
            return True
        key = venue.strip().lower()
        if key in OPENREVIEW_MAIN:
            return True
        if key in ANTHOLOGY_VENUES and not metadata_only:
            return True
    return False


def _crawl_one_metadata(venue: str, year: int, limit: int | None, existing: dict, on_new, *,
                        flush=None, defer_abstracts=False) -> list[dict]:
    if venue == 'eccb' and year == 2024:
        from journal_meta import crawl_journal
        return crawl_journal(venue, year, limit, existing, on_new, {
            'issns':['1367-4803','1367-4811'], 'volume':'40','issue':'Supplement_2',
            'title':'European Conference on Computational Biology', 'venue_type':'conference'}, flush=flush)
    raw = venue.strip()
    if "/" in raw:
        venue_id = resolve_venue_id(raw, year)
        folder = _folder_name(raw)
        with _OPENREVIEW_LOCK:
            return fetch_openreview_records(venue_id, folder, year, limit=limit)

    key = canonical_venue(NATURE_ALIASES.get(raw.lower(), raw.lower()))
    folder = _folder_name(key)
    if key == 'iccv' and year == 2024:
        logger.info('ICCV 在 2024 年未举办，记录为空结果，不请求不存在的会议页面')
        return []
    if key in JOURNALS:
        return crawl_nature(key, year, limit, existing, on_new, flush=flush,
                            defer_abstracts=defer_abstracts)
    if key in OPENREVIEW_MAIN:
        try:
            # The SDK has a shared authenticated client; public fallbacks run outside this lock.
            with _OPENREVIEW_LOCK:
                return fetch_openreview_records(resolve_venue_id(key, year), folder, year, limit=limit)
        except OpenReviewBlocked:
            logger.warning(f"{folder} {year} 的 OpenReview 不可用，改用公开会议页面")
            return crawl_virtual(folder, year, limit, existing, on_new)
    if key == "eccv":
        return crawl_eccv(year, limit, existing, on_new)
    if key in OPENACCESS_META:
        return crawl_openaccess_metadata(key, year, limit, existing, on_new)
    if key in ANTHOLOGY_VENUES:
        found = crawl_anthology(key, year, limit, existing, on_new)
        if found:
            return found
        logger.warning(f"{key} {year} 的 Anthology 没有卷，改走 OpenReview")
        try:
            with _OPENREVIEW_LOCK:
                return fetch_openreview_records(resolve_venue_id(key, year), folder, year, limit=limit)
        except OpenReviewBlocked:
            logger.warning(f"{key} {year} 的 OpenReview 也不可用")
            return []
    if key == "aaai":
        return crawl_aaai(year, limit, existing, on_new)
    if key == "kdd":
        return crawl_kdd(year, limit, existing, on_new)
    if key == "mlsys" and year == 2024:
        from mlsys_meta import crawl_mlsys
        return crawl_mlsys(year, limit, existing, on_new)
    if key == "rss" and year == 2024:
        from rss_meta import crawl_rss
        return crawl_rss(limit, existing, on_new)
    if key in CONFERENCES:
        return crawl_conference(key, year, limit, existing, on_new)
    if key in THECVF_VENUES:
        return crawl_openaccess_metadata(key, year, limit, existing, on_new)
    known = ", ".join(sorted(known_venues()))
    raise SystemExit(f"未知会议 {venue!r}，可选: {known}")


def crawl_metadata_venue(venue: str, year: int, limit: int | None, root: Path, *,
                         defer_abstracts=False, resume_bibliography=False) -> list[dict]:
    dest = root / _folder_name(venue) / str(year)
    dest.mkdir(parents=True, exist_ok=True)
    papers_path = dest / "papers.json"
    if limit is not None and papers_path.exists():
        raise ValueError('--limit 试抓不能覆盖已有元数据，请使用独立的 --metadata-dir')
    checkpoint = RecordCheckpoint(papers_path, resume=limit is None)

    def on_new(row: dict) -> None:
        checkpoint.add(annotate_ccf_record(row, venue))

    try:
        key = canonical_venue(NATURE_ALIASES.get(venue.lower(), venue.lower()))
        config = JOURNALS.get(key, {})
        if resume_bibliography and defer_abstracts and limit is None and config.get('provider') == 'crossref':
            from journal_meta import crawl_journal_resumable
            records = crawl_journal_resumable(key, year, checkpoint.by_id, on_new, config,
                                              checkpoint.flush, dest)
        else:
            options = {'defer_abstracts': True} if defer_abstracts else {}
            records = _crawl_one_metadata(venue, year, limit, checkpoint.by_id, on_new,
                                          flush=checkpoint.flush, **options)
        if (venue in CONFERENCES and CONFERENCES[venue]['rank'] == '未收录'
                and not records and not checkpoint.rows):
            raise RuntimeError(f'{venue}: 新增会议书目检索为空，需核对当届论文集，不能认定采集完整')
    except Exception:
        checkpoint.flush()
        # A partial crawl still has useful papers; retain its failure state.
        dump_records(dest / "ai4s.json", select_ai4s(checkpoint.rows))
        raise
    finally:
        # API 中断也保存不足20条的尾批，供下次断点恢复。
        checkpoint.flush()
    if not records and checkpoint.rows:
        logger.warning(f"{venue} {year} 本次没有拉到论文，保留已有元数据")
        records = list(checkpoint.rows)
    else:
        records = [annotate_ccf_record(row, venue) for row in records]
        checkpoint.replace(records)
    ai4s = select_ai4s(records)
    dump_records(dest / "ai4s.json", ai4s)
    logger.info(f"{_folder_name(venue)} {year}: 全量 {len(records)} 篇，AI4S {len(ai4s)} 篇")
    return records


def write_merged(root: Path, year: int, venues=None) -> None:
    papers = []
    ai4s = []
    if not root.exists():
        return
    folders = {_folder_name(v) for v in venues} if venues is not None else None
    for venue_dir in sorted(path for path in root.iterdir() if path.is_dir() and not path.name.isdigit()):
        if folders is not None and venue_dir.name not in folders:
            continue
        papers.extend(load_records(venue_dir / str(year) / "papers.json"))
        ai4s.extend(load_records(venue_dir / str(year) / "ai4s.json"))
    dest = root / str(year)
    dump_records(dest / "papers.json", papers)
    dump_records(dest / "ai4s.json", ai4s)
    logger.info(f"汇总 {dest}: 全量 {len(papers)} 篇，AI4S {len(ai4s)} 篇")


def write_run_status(root: Path, year: int, states: dict) -> None:
    dump_records(root / str(year) / 'run-status.json',
                 [{'source': source, 'state': state} for source, state in states.items()])


def schedule_venues(venues: list[str]) -> list[str]:
    preferred = [venue for venue in venues if venue in OPENREVIEW_MAIN]
    conferences = [venue for venue in venues if venue not in OPENREVIEW_MAIN and venue not in JOURNALS]
    journals = [venue for venue in venues if venue in JOURNALS]
    return preferred + [venue for pair in zip_longest(conferences, journals) for venue in pair if venue]


def _is_retryable_upstream(exc: Exception) -> bool:
    """上游暂时不可用（DBLP 503、限流冷却、网络抖动）时延后重试，不判定来源失败。"""
    if isinstance(exc, HostCooldown):
        return True
    message = str(exc)
    if isinstance(exc, RuntimeError) and ('冷却至' in message or '保留断点' in message):
        return True
    return is_transient(exc)


def main():
    known = ", ".join(sorted(known_venues()))
    parser = argparse.ArgumentParser(
        description="按会议/期刊+年份下载论文 PDF，或只导出元数据（Nature 仅元数据）"
    )
    parser.add_argument("-v", "--venue", required=True, help=f"会议/期刊/期刊组，逗号分隔。可选: {known}")
    parser.add_argument("-y", "--year", type=int, required=True, help="年份，例如 2026")
    parser.add_argument("--limit", type=int, default=None, help="只拉前 N 篇，试跑用")
    parser.add_argument("--pdf-dir", default="pdfs", help="PDF 根目录，实际落到 pdfs/<venue>/<year>/")
    parser.add_argument("--metadata-only", action="store_true", help="只写元数据，不下载 PDF")
    parser.add_argument("--metadata-dir", default="metadata", help="元数据根目录，落到 metadata/<venue>/<year>/")
    parser.add_argument("--workers", type=int, default=1, help="同时采集的来源数，默认 1；仅元数据模式")
    parser.add_argument("--skip-completed", action="store_true", help="跳过同年已完成且结果文件齐全的来源")
    parser.add_argument("--defer-journal-abstracts", action="store_true", help="期刊书目与摘要分开采集")
    args = parser.parse_args()

    requested = [item.strip() for item in args.venue.split(',') if item.strip()]
    expanded = [v for item in requested for v in (APPROVED_SOURCES if item == 'teacher-approved' else [item])]
    venues = expand_ccf_venues(expand_venues(expanded))
    disabled = [v for v in venues if v not in APPROVED_SOURCES]
    if disabled:
        logger.warning(f'教师建议清单未启用的来源已跳过：{", ".join(disabled)}')
    venues = [v for v in venues if v in APPROVED_SOURCES]
    if not venues:
        parser.error('至少指定一个会议或期刊')
    if args.limit is not None and args.limit <= 0:
        parser.error('--limit 必须为正整数')
    if args.workers <= 0:
        parser.error('--workers 必须为正整数')
    if args.workers != 1 and not args.metadata_only:
        parser.error('--workers 仅支持 --metadata-only')
    if args.defer_journal_abstracts and not args.metadata_only:
        parser.error('--defer-journal-abstracts 仅支持 --metadata-only')
    if not args.metadata_only and any(v in JOURNALS for v in venues):
        parser.error('Nature 期刊目前仅支持 --metadata-only')
    if args.metadata_only:
        root = Path(args.metadata_dir)
        failed = []
        # Start the supported official OpenReview sources first.
        venues = schedule_venues(venues)
        states = dict.fromkeys(venues, 'pending')
        retry_sources = set()
        if args.skip_completed:
            try:
                previous = load_records(root / str(args.year) / 'run-status.json')
                for row in previous:
                    venue = row.get('source')
                    if venue in states and row.get('state') in ('failed', 'running', 'retryable'):
                        retry_sources.add(venue)
                    folder = root / _folder_name(venue) / str(args.year) if venue in states else None
                    if folder and row.get('state') in ('completed', 'not_held', 'abstract_queued', 'backfilling', 'abstract_incomplete') and all(
                            (folder / name).exists() for name in ('papers.json', 'ai4s.json')):
                        states[venue] = row['state']
            except OSError:
                logger.warning('旧来源状态暂不可读，将按论文断点继续')
        venues.sort(key=lambda venue: venue not in retry_sources)
        status_lock = threading.Lock()
        deferred = {v for v in venues if args.defer_journal_abstracts
                    and JOURNALS.get(v, {}).get('provider') == 'crossref'}

        def update(venue, state):
            with status_lock:
                states[venue] = state
                write_run_status(root, args.year, states)

        def crawl_one(venue):
            if states[venue] in ('completed', 'not_held', 'abstract_queued', 'backfilling', 'abstract_incomplete'):
                return 'ok'
            update(venue, 'running')
            try:
                if venue in ('iccv', 'ipmi') and args.year % 2 == 0:
                    dest = root / _folder_name(venue) / str(args.year)
                    dest.mkdir(parents=True, exist_ok=True)
                    dump_records(dest / 'papers.json', [])
                    dump_records(dest / 'ai4s.json', [])
                    update(venue, 'not_held')
                    return 'ok'
                options = {'defer_abstracts': True} if venue in deferred else {}
                if venue in deferred and args.skip_completed:
                    options['resume_bibliography'] = True
                crawl_metadata_venue(venue, args.year, args.limit, root, **options)
            except Exception as exc:
                logger.exception(f"{venue} 元数据抓取失败")
                if _is_retryable_upstream(exc):
                    update(venue, 'retryable')
                    return 'retryable'
                update(venue, 'failed')
                return 'failed'
            update(venue, 'not_held' if venue == 'iccv' and args.year == 2024 else 'completed')
            return 'ok'

        logger.info(f'元数据来源 {len(venues)} 个，同时处理 {min(args.workers, len(venues))} 个')
        from journal_abstract_backfill import complete_abstracts
        batch, backfills = [], []
        def supplement(group):
            by_folder = {_folder_name(venue): venue for venue in group}
            complete_abstracts(root, args.year, list(by_folder),
                               lambda folder, state: update(by_folder[folder], state))

        with ThreadPoolExecutor(max_workers=min(args.workers, len(venues))) as pool, \
                ThreadPoolExecutor(max_workers=1) as backfill_pool:
            pending_retry: list[str] = []

            def note(venue, status):
                if status == 'ok':
                    if args.limit is None and states[venue] in ('completed', 'abstract_queued', 'backfilling'):
                        batch.append(venue)
                        if len(batch) == 8:
                            backfills.append(backfill_pool.submit(supplement, batch[:]))
                            del batch[:]
                elif status == 'retryable':
                    pending_retry.append(venue)
                else:
                    failed.append(venue)

            futures = {pool.submit(crawl_one, venue): venue for venue in venues}
            for future in as_completed(futures):
                venue = futures[future]
                note(venue, future.result())
            rounds = max(0, int(os.environ.get('CRAWL_RETRY_ROUNDS', '2')))
            pause = max(0.0, float(os.environ.get('CRAWL_RETRY_DELAY', '60')))
            for round_no in range(1, rounds + 1):
                if not pending_retry:
                    break
                pending = pending_retry[:]
                del pending_retry[:]
                logger.warning(f'第 {round_no} 轮重试上游暂时不可用的来源（{len(pending)} 个）: {", ".join(pending)}')
                if pause:
                    time.sleep(pause)
                with ThreadPoolExecutor(max_workers=max(1, min(args.workers, len(pending)))) as retry_pool:
                    for venue, status in zip(pending, retry_pool.map(crawl_one, pending)):
                        note(venue, status)
            if pending_retry:
                logger.error(f'以下来源上游持续不可用，已保留断点、下次运行优先重试: {", ".join(pending_retry)}')
                failed.extend(pending_retry)
                del pending_retry[:]
            if batch:
                backfills.append(backfill_pool.submit(supplement, batch[:]))
            for future in backfills:
                future.result()
        write_merged(root, args.year, venues)
        if failed:
            logger.error(f'以下来源抓取失败: {", ".join(failed)}')
            raise SystemExit(1)
        return

    if _needs_openreview_now(venues, metadata_only=False):
        get_openreview_client("v2")

    pdf_dir = Path(args.pdf_dir)
    total = 0
    for venue in venues:
        total += len(crawl_venue(venue, args.year, args.limit, pdf_dir))
    logger.info(f"完成，共 {total} 篇")


if __name__ == "__main__":
    main()
