"""Read-only crawler monitor. Only the secret route serves content."""
import hmac
import json
import os
import re
import subprocess
import threading
import time
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit


def read_counts(path):
    """Read one JSON array incrementally, without retaining all paper objects."""
    decoder = json.JSONDecoder()
    count = abstracts = missing = 0
    with Path(path).open(encoding='utf-8') as stream:
        buffer = ''
        eof = False

        def available():
            nonlocal buffer, eof
            buffer = buffer.lstrip()
            while not buffer and not eof:
                chunk = stream.read(65536)
                eof = not chunk
                buffer += chunk
                buffer = buffer.lstrip()
            return bool(buffer)

        if not available() or buffer[0] != '[':
            raise ValueError('Expected a JSON array')
        buffer = buffer[1:]
        first = True
        while available():
            if buffer[0] == ']':
                buffer = buffer[1:]
                if available():
                    raise ValueError('Unexpected trailing JSON')
                return count, abstracts, missing
            if not first:
                if buffer[0] != ',':
                    raise ValueError('Expected a comma')
                buffer = buffer[1:]
                if not available() or buffer[0] == ']':
                    raise ValueError('Missing record')
            while True:
                try:
                    row, end = decoder.raw_decode(buffer)
                    break
                except json.JSONDecodeError as exc:
                    chunk = stream.read(65536)
                    if not chunk or len(buffer) > 8 * 1024 * 1024:
                        raise ValueError('Invalid or oversized JSON record') from exc
                    buffer += chunk
            if not isinstance(row, dict):
                raise ValueError('Expected a paper object')
            count += 1
            abstracts += bool(row.get('abstract'))
            missing += bool(row.get('doi')) and not row.get('abstract')
            buffer = buffer[end:]
            first = False
    raise ValueError('Unfinished JSON array')


def redact(line):
    if re.search(r'authorization|password|passwd|bearer\s|(?:api[_-]?key|token|cookie)\s*[:=]', line, re.I):
        return '[包含敏感字段的日志已隐藏]'
    return re.sub(r'\x1b\[[0-9;]*m', '', line)


RETRY_ENTRY = re.compile(r'^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\.\d+ \| WARNING\s+\| '
                         r'conference_meta:_page_payload:\d+ - (\S+) \d{4}: DBLP 枚举第 (\d+) 次失败（(.+?)），')
RETRY_ROUND = re.compile(r'第 (\d+) 轮重试上游暂时不可用的来源（(\d+) 个）: (.+)$')
RETRY_GIVEUP = re.compile(r'以下来源上游持续不可用，已保留断点、下次运行优先重试: (.+)$')


def retry_evidence(lines):
    """Collect per-source upstream retry attempts from the crawler log tail."""
    evidence, round_no, waiting = {}, None, []
    for line in lines:
        match = RETRY_ENTRY.match(line)
        if match:
            stamp, source, attempt, error = match.groups()
            evidence[source] = {'attempt': int(attempt), 'error': error, 'at': stamp,
                                'epoch': _local_epoch(stamp)}
            continue
        match = RETRY_ROUND.search(line)
        if match:
            round_no = int(match.group(1))
            continue
        match = RETRY_GIVEUP.search(line)
        if match:
            waiting = [name.strip() for name in match.group(1).split(',') if name.strip()]
    return evidence, round_no, waiting


def _local_epoch(stamp):
    try:
        return datetime.strptime(stamp, '%Y-%m-%d %H:%M:%S').timestamp()
    except ValueError:
        return 0.0


def service_properties(unit="academic-crawler.service"):
    names = ['ActiveState', 'SubState', 'Result', 'ExecMainStatus', 'MemoryCurrent',
             'MemoryMax', 'CPUQuotaPerSecUSec',
             'ExecMainStartTimestampMonotonic', 'ExecMainExitTimestampMonotonic']
    result = subprocess.run(['systemctl', 'show', unit,
                             *['--property=' + name for name in names]],
                            capture_output=True, text=True, timeout=3, check=True)
    return dict(line.split('=', 1) for line in result.stdout.splitlines() if '=' in line)


class Collector:
    def __init__(self, root, manifest, log, service_reader=service_properties):
        self.root, self.manifest, self.log = Path(root), Path(manifest), Path(log)
        self.service_reader = service_reader
        self.cache = {}
        self.snapshot = {'loading': True, 'sources': [], 'logs': []}

    def counts(self, path):
        stat = path.stat()
        signature = (stat.st_ino, stat.st_mtime_ns, stat.st_size)
        cached = self.cache.get(path)
        if cached and cached[0] == signature:
            return cached[1]
        value = read_counts(path)
        self.cache[path] = (signature, value)
        return value

    def collect(self):
        manifest = json.loads(self.manifest.read_text(encoding='utf-8'))
        year = manifest['year']
        sources = manifest['sources']
        task_states = {}
        try:
            tasks = json.loads((self.root / str(year) / 'run-status.json').read_text(encoding='utf-8'))
            task_states = {task['source']: task['state'] for task in tasks}
        except (OSError, ValueError, TypeError, KeyError):
            pass
        service = self.service_reader()
        active = service.get('ActiveState', 'unknown')
        state = ('running' if active == 'active' else
                 'finished' if active == 'inactive' and service.get('Result') == 'success'
                 and service.get('ExecMainStatus') == '0' else
                 'failed' if active == 'failed' or service.get('Result') not in (None, 'success') else active)
        lines = []
        if self.log.exists():
            with self.log.open('rb') as stream:
                stream.seek(max(0, self.log.stat().st_size - 512 * 1024))
                data = stream.read(512 * 1024).decode('utf-8', errors='replace')
            data = data.rsplit('=== START ALL 2024:', 1)[-1]
            lines = data.splitlines()
        retries, retry_round, retry_waiting = retry_evidence(lines)
        now_epoch = time.time()
        failed = set(re.findall(r' - (\S+) 元数据抓取失败', '\n'.join(lines)))
        current = None
        for line in reversed(lines):
            match = re.search(r'CCF-[AB] (.+?) ' + str(year) + r':', line)
            if match:
                candidate = match[1].lower()
                if candidate in sources:
                    current = candidate
                break
        rows = []
        saved = abstracts = ai4s = completed = 0
        for source in sources:
            folder = self.root / source / str(year)
            papers_path, ai4s_path = folder / 'papers.json', folder / 'ai4s.json'
            row = {'source': source, 'title': manifest.get('source_titles', {}).get(source, source),
                   'status': 'pending', 'papers': 0, 'abstracts': 0, 'missing': 0,
                   'ai4s': 0, 'ai4s_ready': False, 'updated': None}
            try:
                if papers_path.exists():
                    row['papers'], row['abstracts'], row['missing'] = self.counts(papers_path)
                    row['updated'] = datetime.fromtimestamp(papers_path.stat().st_mtime, timezone.utc).isoformat()
                    row['status'] = 'collecting'
                if ai4s_path.exists():
                    row['ai4s'] = self.counts(ai4s_path)[0]
                    row['ai4s_ready'] = True
                    row['status'] = 'completed'
                elif current == source and state == 'running':
                    row['status'] = 'collecting'
                if source in failed:
                    row['status'] = 'failed'
                if task_states.get(source) == 'not_held':
                    row['status'] = 'not_held'
                elif task_states.get(source) == 'running' and state == 'running':
                    row['status'] = 'collecting'
                elif task_states.get(source) == 'failed':
                    row['status'] = 'failed'
                elif task_states.get(source) == 'completed' and ai4s_path.exists() and papers_path.exists():
                    row['status'] = 'completed'
                elif task_states.get(source) in ('abstract_queued', 'backfilling', 'abstract_incomplete'):
                    row['status'] = task_states[source]
                elif task_states.get(source) == 'pending':
                    row['status'] = 'pending'
                retry = retries.get(source)
                if retry:
                    row['retry_attempt'] = retry['attempt']
                    row['retry_error'] = retry['error']
                    row['retry_at'] = retry['at']
                    fresh = not retry['epoch'] or now_epoch - retry['epoch'] <= 3600
                    if fresh and (task_states.get(source) in ('running', 'retryable')
                                  or (not task_states and state == 'running')):
                        row['status'] = 'retrying'
                if task_states.get(source) == 'retryable':
                    row['status'] = 'retrying'
            except (OSError, ValueError):
                row['status'] = 'unreadable'
                row['papers'] = row['abstracts'] = row['missing'] = row['ai4s'] = 0
            saved += row['papers']
            abstracts += row['abstracts']
            ai4s += row['ai4s']
            completed += row['status'] in ('completed', 'not_held', 'abstract_incomplete')
            rows.append(row)
        in_progress = [row for row in rows if row['status'] == 'collecting']
        if in_progress:
            current = max(in_progress, key=lambda r: r['updated'] or '')['source']
        elif state != 'running':
            current = None
        current_sources = ([source for source, task in task_states.items() if task == 'running']
                           if task_states else [row['source'] for row in in_progress])
        if state != 'running':
            current_sources = []
        try:
            memory = int(service.get('MemoryCurrent', ''))
        except ValueError:
            memory = None
        try:
            memory_limit = int(service.get('MemoryMax', ''))
        except ValueError:
            memory_limit = None
        cpu_quota = re.fullmatch(r'(\d+(?:\.\d+)?)s', service.get('CPUQuotaPerSecUSec', ''))
        elapsed = None
        try:
            started = int(service['ExecMainStartTimestampMonotonic']) / 1e6
            ended = int(service.get('ExecMainExitTimestampMonotonic', '0')) / 1e6
            now = float(Path('/proc/uptime').read_text().split()[0])
            elapsed = max(0, int((ended if ended >= started else now) - started)) if started else None
        except (OSError, KeyError, ValueError):
            pass
        disk = os.statvfs(self.root) if hasattr(os, 'statvfs') else None
        retrying = [row for row in rows if row['status'] == 'retrying']
        conference_jobs = [row for row in rows if not row['source'].startswith('j-')
                           and task_states.get(row['source']) in ('running', 'retryable')]
        backfill = self.backfill_report(rows) if year == 2024 else None
        return {'loading': False, 'year': year, 'updated_at': datetime.now(timezone.utc).isoformat(),
                'service': {'state': state, 'detail': service.get('SubState', ''),
                            'memory_bytes': memory, 'memory_limit_bytes': memory_limit,
                            'cpu_limit_cores': float(cpu_quota[1]) if cpu_quota else None,
                            'elapsed_seconds': elapsed},
                'current_source': current, 'current_sources': current_sources,
                'total_sources': len(sources), 'completed_sources': completed,
                'failed_sources': sum(row['status'] == 'failed' for row in rows),
                'retrying_sources': [{'source': row['source'], 'title': row['title'],
                                      'status': ('queued' if task_states.get(row['source']) == 'retryable'
                                                 else row['status']),
                                      'attempt': row.get('retry_attempt'), 'error': row.get('retry_error'),
                                      'at': row.get('retry_at'), 'papers': row['papers'],
                                      'abstracts': row['abstracts'], 'updated': row['updated']}
                                     for row in {row['source']: row for row in retrying + conference_jobs}.values()],
                'retry_round': retry_round, 'retry_waiting': retry_waiting,
                'backfill': backfill,
                'missing_with_doi': sum(row['missing'] for row in rows),
                'saved_papers': saved, 'papers_with_abstract': abstracts, 'ai4s_candidates': ai4s,
                'disk_available_bytes': disk.f_bavail * disk.f_frsize if disk else None,
                'sources': rows, 'logs': [redact(line) for line in lines[-60:]],
                'recent_warnings': sum(bool(re.search(r'\|\s*WARNING\s*\|', line)) for line in lines[-60:]),
                'recent_errors': sum(bool(re.search(r'\|\s*ERROR\s*\|', line)) for line in lines[-60:]),
                'outputs': {'papers': str(self.root / str(year) / 'papers.json'),
                            'ai4s': str(self.root / str(year) / 'ai4s.json')},
                'annual_merge_exists': (self.root / str(year) / 'papers.json').exists()}

    def cache_stats(self):
        """Read the shared abstract cache without blocking the writer."""
        path = self.root / 'journal-abstract-cache.sqlite3'
        try:
            stat = path.stat()
        except OSError:
            return None
        signature = (stat.st_mtime_ns, stat.st_size)
        cached = self.cache.get(path)
        if cached and cached[0] == signature:
            return cached[1]
        value = {'rows': None, 'by_source': {}, 'size_bytes': stat.st_size,
                 'updated_at': datetime.fromtimestamp(stat.st_mtime, timezone.utc).isoformat()}
        try:
            import sqlite3
            conn = sqlite3.connect('file:' + path.as_posix() + '?mode=ro', uri=True, timeout=1.0)
            try:
                value['rows'] = conn.execute('SELECT COUNT(*) FROM abstracts').fetchone()[0]
                value['by_source'] = dict(conn.execute('SELECT source, COUNT(*) FROM abstracts'
                                                       ' GROUP BY source ORDER BY 2 DESC'))
            finally:
                conn.close()
        except Exception:
            value['rows'] = None
        self.cache[path] = (signature, value)
        return value

    def backfill_row(self, source, title, start, current, start_epoch, updated):
        start, current = int(start or 0), int(current or 0)
        updated_epoch = 0.0
        if updated:
            try:
                updated_epoch = datetime.fromisoformat(updated).timestamp()
            except ValueError:
                updated_epoch = 0.0
        status = ('done' if start and current == 0 else
                  'idle' if not start_epoch else
                  'running' if updated_epoch > start_epoch else 'queued')
        filled = max(0, start - current)
        return {'source': source, 'title': title, 'missing_start': start, 'missing_now': current,
                'filled': filled, 'percent': (filled / start) if start else 0.0,
                'status': status, 'updated': updated}

    def backfill_report(self, rows):
        """Summarise the journal abstract backfill run behind backfill-jobs.json."""
        missing = {row['source']: row.get('missing', 0) for row in rows}
        updated = {row['source']: row['updated'] for row in rows}
        titles = {row['source']: row['title'] for row in rows}
        jobs, started, origin = [], None, 'file'
        try:
            payload = json.loads((self.root / 'backfill-jobs.json').read_text(encoding='utf-8'))
            started = payload.get('started_at') or payload.get('generated_at')
            start_epoch = _local_epoch(started) if started else 0.0
            for job in payload.get('folders', []):
                source = job.get('source')
                if source not in missing:
                    continue
                row = self.backfill_row(source, job.get('title') or titles.get(source, source),
                                        job.get('missing_start'), missing[source],
                                        start_epoch, updated.get(source))
                if job.get('status') in ('running', 'queued', 'done', 'failed', 'stopped'):
                    row['status'] = job['status']
                jobs.append(row)
        except (OSError, ValueError, AttributeError, TypeError):
            origin = 'derived'
            ranked = sorted(((value, source) for source, value in missing.items()
                             if value and source.startswith('j-')), reverse=True)[:10]
            for value, source in ranked:
                jobs.append(self.backfill_row(source, titles.get(source, source), value, value, 0.0,
                                              updated.get(source)))
        total_start = sum(job['missing_start'] for job in jobs)
        total_now = sum(job['missing_now'] for job in jobs)
        return {'origin': origin, 'started_at': started, 'jobs': jobs,
                'total_missing_start': total_start, 'total_missing_now': total_now,
                'total_filled': max(0, total_start - total_now),
                'folders_done': sum(job['status'] == 'done' for job in jobs),
                'cache': self.cache_stats()}

    def refresh_forever(self):
        while True:
            try:
                self.snapshot = self.collect()
            except Exception as exc:
                self.snapshot = {**self.snapshot, 'monitor_error': type(exc).__name__}
            time.sleep(15)


def make_handler(secret, collector, collector_2026=None):
    asset_root = Path(__file__).resolve().parent
    assets = {'': ('index.html', 'text/html; charset=utf-8'),
              'app.js': ('app.js', 'text/javascript; charset=utf-8'),
              'style.css': ('style.css', 'text/css; charset=utf-8')}

    class Handler(BaseHTTPRequestHandler):
        server_version = 'Monitor'
        sys_version = ''

        def setup(self):
            super().setup()
            self.connection.settimeout(5)

        def log_message(self, *args):
            pass  # Do not log the bearer URL.

        def respond(self, status, body, content_type='text/plain; charset=utf-8'):
            self.send_response(status)
            self.send_header('Content-Type', content_type)
            self.send_header('Content-Length', str(len(body)))
            self.send_header('Cache-Control', 'no-store')
            self.send_header('Referrer-Policy', 'no-referrer')
            self.send_header('X-Robots-Tag', 'noindex, nofollow, noarchive')
            self.send_header('X-Content-Type-Options', 'nosniff')
            self.send_header('Content-Security-Policy', "default-src 'none'; script-src 'self'; style-src 'self'; connect-src 'self'; base-uri 'none'; frame-ancestors 'none'")
            self.end_headers()
            if self.command != 'HEAD':
                self.wfile.write(body)

        def authorized_route(self):
            parts = urlsplit(self.path).path.split('/')
            if len(parts) < 4 or parts[1] != 'academic-watch':
                return None
            if not hmac.compare_digest(parts[2].encode(), secret.encode()):
                return None
            if len(parts) == 4:
                return 2024, parts[3]
            if len(parts) == 5 and parts[3] == '2026' and collector_2026 is not None:
                return 2026, parts[4]
            return None

        def do_GET(self):
            authorized = self.authorized_route()
            if authorized is None:
                self.respond(404, b'Not found')
                return
            year, route = authorized
            if route == 'status':
                selected = collector_2026 if year == 2026 else collector
                self.respond(200, json.dumps(selected.snapshot, ensure_ascii=False).encode(), 'application/json; charset=utf-8')
            elif route in assets:
                name, content_type = assets[route]
                body = (asset_root / name).read_bytes()
                if name == 'index.html' and year == 2026:
                    body = body.replace(b'2024', b'2026').replace(
                        b'<a href="2026/">2026</a>', b'<a href="../">2024</a>')
                self.respond(200, body, content_type)
            else:
                self.respond(404, b'Not found')

        do_HEAD = do_GET

        def do_POST(self):
            self.respond(405 if self.authorized_route() is not None else 404, b'Method not allowed')

    return Handler


if __name__ == '__main__':
    secret = os.environ.get('MONITOR_SECRET', '')
    if not re.fullmatch(r'[A-Za-z0-9_-]{32,128}', secret):
        raise SystemExit('MONITOR_SECRET must contain at least 32 URL-safe characters')
    data = Path(os.environ.get('ACADEMIC_DATA', '/mnt/figure/academic'))
    collector = Collector(data / 'metadata', data / 'run-manifest-2024.json', data / 'logs/crawl.log')
    collector_2026 = Collector(data / 'metadata', data / 'run-manifest-2026.json',
                               data / 'logs/crawl-2026.log',
                               lambda: service_properties('academic-crawler-2026.service'))
    for dashboard in (collector, collector_2026):
        threading.Thread(target=dashboard.refresh_forever, daemon=True).start()
    server = ThreadingHTTPServer(('127.0.0.1', int(os.environ.get('MONITOR_PORT', '18765'))),
                                 make_handler(secret, collector, collector_2026))
    server.daemon_threads = True
    server.serve_forever()
