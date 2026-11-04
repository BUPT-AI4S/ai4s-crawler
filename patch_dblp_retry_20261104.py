"""补丁：DBLP 枚举页重试 + 上游暂时失败不判定来源失败（1+2）。

用法：python patch_dblp_retry_20261104.py <目标目录>
幂等：已打过的文件会跳过。
"""
import sys
from pathlib import Path

CONF_HELPER = '''ENDPOINT = 'https://sparql.dblp.org/sparql'
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
'''

CONF_CALL_OLD = '''        payload = get_json(ENDPOINT, params={'query': build_query(venue, year, size, offset)},
                           headers={'Accept': 'application/sparql-results+json'}, timeout=60,
                           sleep_s=0.5, retries=2)
'''
CONF_CALL_NEW = '''        payload = _page_payload(venue, year, size, offset)
'''

ACADEMIC_HELPER = '''def _is_retryable_upstream(exc: Exception) -> bool:
    """上游暂时不可用（DBLP 503、限流冷却、网络抖动）时延后重试，不判定来源失败。"""
    if isinstance(exc, HostCooldown):
        return True
    message = str(exc)
    if isinstance(exc, RuntimeError) and ('冷却至' in message or '保留断点' in message):
        return True
    return is_transient(exc)


def main():
'''

CRAWL_ONE_OLD = '''        def crawl_one(venue):
            if states[venue] in ('completed', 'not_held'):
                return True
            update(venue, 'running')
            try:
                if venue in ('iccv', 'ipmi') and args.year % 2 == 0:
                    dest = root / _folder_name(venue) / str(args.year)
                    dest.mkdir(parents=True, exist_ok=True)
                    dump_records(dest / 'papers.json', [])
                    dump_records(dest / 'ai4s.json', [])
                    update(venue, 'not_held')
                    return True
                options = {'defer_abstracts': True} if venue in deferred else {}
                if venue in deferred and args.skip_completed:
                    options['resume_bibliography'] = True
                crawl_metadata_venue(venue, args.year, args.limit, root, **options)
            except Exception:
                logger.exception(f"{venue} 元数据抓取失败")
                update(venue, 'failed')
                return False
            update(venue, 'not_held' if venue == 'iccv' and args.year == 2024 else 'completed')
            return True
'''

CRAWL_ONE_NEW = '''        def crawl_one(venue):
            if states[venue] in ('completed', 'not_held'):
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
'''

LOOP_OLD = '''            futures = {pool.submit(crawl_one, venue): venue for venue in venues}
            for future in as_completed(futures):
                venue = futures[future]
                if not future.result():
                    failed.append(venue)
                elif venue in deferred and states[venue] == 'completed':
                    batch.append(_folder_name(venue))
                    if len(batch) == 8:
                        backfills.append(backfill_pool.submit(backfill_journal_abstracts, root, args.year, batch))
                        batch = []
            if batch:
'''

LOOP_NEW = '''            pending_retry: list[str] = []

            def note(venue, status):
                if status == 'ok':
                    if venue in deferred and states[venue] == 'completed':
                        batch.append(_folder_name(venue))
                        if len(batch) == 8:
                            backfills.append(backfill_pool.submit(backfill_journal_abstracts, root, args.year, batch))
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
'''


def patch(conf_path: Path, acad_path: Path) -> int:
    changed = 0

    raw = conf_path.read_bytes()
    crlf = b'\r\n' in raw
    text = raw.decode('utf-8').replace('\r\n', '\n')
    if 'def _page_payload(' not in text:
        assert text.count('ENDPOINT = \'https://sparql.dblp.org/sparql\'\nPAGE_SIZE = 100\n') == 1
        text = text.replace("import re\nimport json\nimport time\n", "import os\nimport re\nimport json\nimport time\n", 1)
        text = text.replace("ENDPOINT = 'https://sparql.dblp.org/sparql'\nPAGE_SIZE = 100\n", CONF_HELPER, 1)
        assert text.count(CONF_CALL_OLD) == 1, '枚举调用锚点不唯一'
        text = text.replace(CONF_CALL_OLD, CONF_CALL_NEW, 1)
        conf_path.write_bytes((text.replace('\n', '\r\n') if crlf else text).encode('utf-8'))
        changed += 1

    raw = acad_path.read_bytes()
    crlf = b'\r\n' in raw
    text = raw.decode('utf-8').replace('\r\n', '\n')
    if '_is_retryable_upstream' not in text:
        assert text.count('import argparse\nimport json\n') == 1
        text = text.replace('import argparse\nimport json\n', 'import argparse\nimport json\nimport os\n', 1)
        assert text.count('from thecvf import THECVF_VENUES, crawl_openaccess_metadata, list_thecvf_papers\n') == 1
        text = text.replace('from thecvf import THECVF_VENUES, crawl_openaccess_metadata, list_thecvf_papers\n',
                            'from thecvf import THECVF_VENUES, crawl_openaccess_metadata, list_thecvf_papers\n'
                            'from fetch_util import HostCooldown, is_transient\n', 1)
        assert text.count('\ndef main():\n') == 1
        text = text.replace('\ndef main():\n', '\n' + ACADEMIC_HELPER, 1)
        assert text.count("in ('failed', 'running'):") == 1
        text = text.replace("in ('failed', 'running'):", "in ('failed', 'running', 'retryable'):", 1)
        assert text.count(CRAWL_ONE_OLD) == 1, 'crawl_one 锚点不唯一'
        text = text.replace(CRAWL_ONE_OLD, CRAWL_ONE_NEW, 1)
        assert text.count(LOOP_OLD) == 1, '主循环锚点不唯一'
        text = text.replace(LOOP_OLD, LOOP_NEW, 1)
        acad_path.write_bytes((text.replace('\n', '\r\n') if crlf else text).encode('utf-8'))
        changed += 1

    return changed


def main() -> int:
    target = Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
    conf = target / 'conference_meta.py'
    acad = target / 'academic.py'
    for path in (conf, acad):
        if not path.exists():
            raise SystemExit(f'缺少文件: {path}')
    changed = patch(conf, acad)
    for path in (conf, acad):
        compile(path.read_text(encoding='utf-8'), str(path), 'exec')
    print(f'语法检查通过；变更文件数: {changed}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
