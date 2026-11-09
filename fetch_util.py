import math
import hashlib
import os
import time
import threading
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor
from collections import deque
from itertools import islice
from pathlib import Path
from tempfile import NamedTemporaryFile

import requests
from loguru import logger

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}

# Shared across source workers, not multiplied by --workers.
_HOST_INTERVALS = {'api.crossref.org': 1.0, 'api.openalex.org': 0.5, 'sparql.dblp.org': 1.0,
                   'aclanthology.org': 0.5, 'www.aclanthology.org': 0.5}
_HOST_CONCURRENCY = {'api.crossref.org': 1, 'api.openalex.org': 2, 'sparql.dblp.org': 1,
                     'aclanthology.org': 2, 'www.aclanthology.org': 2}
# OpenAlex 的配额是按 key 算的：每把 key 单独一套速率/并发预算，
# 两把 key 才能同时放行两份请求；无 key 时退回按主机（匿名）的预算。
_OPENALEX_KEY_RPS = float(os.environ.get('OPENALEX_KEY_RPS', '6'))
_OPENALEX_KEY_SLOTS = int(os.environ.get('OPENALEX_KEY_SLOTS', '6'))
if os.environ.get('CROSSREF_MAILTO', '').strip():
    _HOST_INTERVALS['api.crossref.org'] = 1 / 3
    _HOST_CONCURRENCY['api.crossref.org'] = 3
for _host in ('www.ebi.ac.uk', 'api.semanticscholar.org', 'proceedings.mlsys.org',
              'www.roboticsproceedings.org', 'eutils.ncbi.nlm.nih.gov', 'api.openaire.eu'):
    _HOST_INTERVALS[_host] = 1.0
    _HOST_CONCURRENCY[_host] = 1
_HOST_LOCKS = {host: threading.Lock() for host in _HOST_INTERVALS}
_HOST_SLOTS = {host: threading.BoundedSemaphore(count) for host, count in _HOST_CONCURRENCY.items()}
_REGISTRY_LOCK = threading.Lock()
_NEXT_ALLOWED = {}
_ACCOUNT_COOLDOWNS = {}
_COOLDOWN_DIR = os.environ.get('ACADEMIC_HTTP_COOLDOWN_DIR')
_MAX_INLINE_WAIT = 60
_HTTP_LOCAL = threading.local()
_DETAIL_POOL = ThreadPoolExecutor(max_workers=32, thread_name_prefix='paper-detail')


def map_details(function, rows):
    """Keep at most four pending details per source; write results in source order."""
    iterator = iter(rows)
    pending = deque(_DETAIL_POOL.submit(function, row) for row in islice(iterator, 4))
    try:
        while pending:
            result = pending.popleft().result()
            for row in islice(iterator, 1):
                pending.append(_DETAIL_POOL.submit(function, row))
            yield result
    finally:
        for future in pending:
            future.cancel()


def _session_get(url, **kwargs):
    if not hasattr(_HTTP_LOCAL, 'session'):
        _HTTP_LOCAL.session = requests.Session()
    return _HTTP_LOCAL.session.get(url, **kwargs)


def _session_post(url, **kwargs):
    if not hasattr(_HTTP_LOCAL, 'session'):
        _HTTP_LOCAL.session = requests.Session()
    return _HTTP_LOCAL.session.post(url, **kwargs)


def _retry_after(response) -> float:
    value = response.headers.get('Retry-After', '')
    try:
        seconds = float(value)
        return max(0.0, seconds) if math.isfinite(seconds) else 5.0
    except ValueError:
        try:
            moment = parsedate_to_datetime(value)
            if moment.tzinfo is None:
                moment = moment.replace(tzinfo=timezone.utc)
            return max(0.0, (moment - datetime.now(timezone.utc)).total_seconds())
        except (TypeError, ValueError, OverflowError):
            return 5.0


class HostCooldown(RuntimeError):
    """The source can be retried after the upstream deadline."""


def _cooldown_file(host):
    if not _COOLDOWN_DIR or not host:
        return None
    return Path(_COOLDOWN_DIR) / (host.encode('utf-8').hex() + '.deadline')


def _read_cooldown(host):
    path = _cooldown_file(host)
    if path is None:
        return 0.0
    try:
        deadline = float(path.read_text(encoding='ascii'))
    except FileNotFoundError:
        return 0.0
    if not math.isfinite(deadline):
        raise ValueError(f'Invalid persisted cooldown for {host}')
    return deadline


def _save_cooldown(host, deadline):
    path = _cooldown_file(host)
    if path is None:
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with NamedTemporaryFile(mode='w', encoding='ascii', dir=path.parent, delete=False) as temp:
        temp.write(str(deadline))
    try:
        os.replace(temp.name, path)
    finally:
        Path(temp.name).unlink(missing_ok=True)


def _check_long_wait(host, delay, deadline, *, max_wait=_MAX_INLINE_WAIT):
    if delay > max_wait:
        resume = datetime.fromtimestamp(deadline, timezone.utc).isoformat()
        raise HostCooldown(f'{host} 冷却至 {resume}，剩余 {delay:.0f} 秒，保留断点后退出本次来源采集')


def _openalex_account_scope(host, headers):
    token = (headers or {}).get('Authorization', '')
    if host != 'api.openalex.org' or not token.startswith('Bearer '):
        return None
    return host + ':key:' + hashlib.sha256(token.encode()).hexdigest()[:24]


def _budget_interval(budget_key, host):
    if budget_key != host:
        return 1.0 / _OPENALEX_KEY_RPS
    return _HOST_INTERVALS.get(host, 0.25)


def _budget_slots(budget_key, host):
    if budget_key != host:
        return _OPENALEX_KEY_SLOTS
    return _HOST_CONCURRENCY.get(host, 4)


def _openalex_account_limited(response):
    try:
        if float(response.headers.get('X-RateLimit-Remaining', '').lstrip('$')) == 0:
            return True
    except (TypeError, ValueError):
        pass
    try:
        payload = response.json()
    except ValueError:
        return False
    if not isinstance(payload, dict):
        return False
    message = str(payload.get('message') or payload.get('error') or '').lower()
    return any(text in message for text in ('daily budget', 'daily quota', 'new account',
                                            'new-account', 'first $1'))


def request_get(url, **kwargs):
    return _request(_session_get, url, **kwargs)


def request_post(url, **kwargs):
    return _request(_session_post, url, **kwargs)


_CROSSREF_MAILTO = os.environ.get('CROSSREF_MAILTO', 'academic-crawler@users.noreply.github.com')


def _with_politeness(host, kwargs):
    """Crossref 公共池靠 mailto 进 polite pool，避免被当作匿名突发流量。"""
    if host != 'api.crossref.org':
        return kwargs
    params = dict(kwargs.get('params') or {})
    if not params.get('mailto'):
        params['mailto'] = _CROSSREF_MAILTO
    kwargs = dict(kwargs, params=params)
    return kwargs


def _request(send, url, **kwargs):
    host = urlparse(url).hostname
    account_scope = _openalex_account_scope(host, kwargs.get('headers'))
    budget = account_scope or host
    kwargs = _with_politeness(host, kwargs)
    with _REGISTRY_LOCK:
        _HOST_LOCKS.setdefault(budget, threading.Lock())
        _HOST_SLOTS.setdefault(budget, threading.BoundedSemaphore(_budget_slots(budget, host)))
    with _HOST_SLOTS[budget]:
        with _HOST_LOCKS[budget]:
            deadline = _read_cooldown(host)
            backlog = max(_NEXT_ALLOWED.get(host, 0), _NEXT_ALLOWED.get(budget, 0))
            delay = max(backlog - time.monotonic(), deadline - time.time())
            if account_scope:
                # 账号级冷却只来自 429 的配额告警：按 key 独立，另一把 key 不受影响。
                account_deadline = max(_read_cooldown(account_scope),
                                       _ACCOUNT_COOLDOWNS.get(account_scope, 0))
                account_delay = account_deadline - time.time()
                if account_delay > 1:
                    _check_long_wait(host, account_delay, account_deadline, max_wait=0)
            _check_long_wait(host, delay, max(deadline, time.time() + delay))
            if delay > 0:
                time.sleep(delay)
            _NEXT_ALLOWED[budget] = time.monotonic() + _budget_interval(budget, host)
        # Do not hold the scheduling lock during network I/O.
        response = send(url, **kwargs)
        if response.status_code in (429, 503):
            with _HOST_LOCKS[host]:
                seconds = _retry_after(response)
                scope = host
                if account_scope and response.status_code == 429 and _openalex_account_limited(response):
                    scope = account_scope
                if host == 'api.semanticscholar.org' and response.status_code == 429 and not response.headers.get('Retry-After'):
                    seconds = 300
                now = time.time()
                deadline = max(_read_cooldown(scope), now + seconds)
                delay = max(0.0, deadline - now)
                _NEXT_ALLOWED[scope] = max(_NEXT_ALLOWED.get(scope, 0), time.monotonic() + delay)
                _save_cooldown(scope, deadline)
                if scope != host:
                    _ACCOUNT_COOLDOWNS[scope] = deadline
                resume = datetime.fromtimestamp(deadline, timezone.utc).isoformat()
                retry_after = response.headers.get('Retry-After', '')[:120]
                response_url = response.url
                upstream = urlparse(response_url).hostname if isinstance(response_url, str) else host
                logger.warning(f'上游冷却 host={host} upstream={upstream} HTTP={response.status_code} '
                               f'Retry-After={retry_after!r} wait={delay:.0f}s resume={resume} '
                               f'scope={"account" if scope != host else "host"}')
                max_wait = 0 if scope != host else _MAX_INLINE_WAIT
                if delay > max_wait:
                    response.close()
                    _check_long_wait(host, delay, deadline, max_wait=max_wait)
        return response


def is_transient(exc: Exception) -> bool:
    if isinstance(exc, (requests.Timeout, requests.ConnectionError)):
        return True
    if isinstance(exc, requests.HTTPError) and exc.response is not None:
        return exc.response.status_code in (429, 500, 502, 503, 504)
    return False


def get_response(
    url: str,
    *,
    params: dict | None = None,
    timeout: int = 60,
    sleep_s: float = 0.2,
    headers: dict | None = None,
    retries: int = 3,
) -> requests.Response:
    hdrs = dict(HEADERS)
    if headers:
        hdrs.update(headers)
    last: Exception | None = None
    for attempt in range(retries):
        try:
            response = request_get(url, params=params, headers=hdrs, timeout=timeout)
            if response.status_code in (429, 503) and attempt + 1 < retries:
                time.sleep(5 * (attempt + 1))
                continue
            response.raise_for_status()
            if sleep_s:
                time.sleep(sleep_s)
            return response
        except (requests.Timeout, requests.ConnectionError) as exc:
            last = exc
            time.sleep(2 * (attempt + 1))
    if last:
        raise last
    raise RuntimeError(f"请求失败: {url}")


def get_text(url: str, **kwargs) -> str:
    response = get_response(url, **kwargs)
    response.encoding = response.encoding or "utf-8"
    return response.text


def get_json(url: str, **kwargs):
    retries = kwargs.pop("retries", 3)
    last: Exception | None = None
    for attempt in range(retries):
        try:
            return get_response(url, retries=1, **kwargs).json()
        except (
            requests.HTTPError,
            requests.exceptions.ChunkedEncodingError,
            requests.exceptions.ConnectionError,
            requests.exceptions.Timeout,
            requests.exceptions.JSONDecodeError,
        ) as exc:
            if isinstance(exc, requests.HTTPError) and not is_transient(exc):
                raise
            last = exc
            if attempt + 1 < retries:
                if (urlparse(url).hostname == 'api.crossref.org'
                        and isinstance(exc, requests.HTTPError) and exc.response is not None
                        and exc.response.status_code == 429):
                    delay = min(120, 15 * 2**attempt)
                    logger.warning(f'Crossref 限流，退避 {delay} 秒后重试 ({attempt + 1}/{retries})')
                    time.sleep(delay)
                else:
                    time.sleep(2 * (attempt + 1))
    if last:
        raise last
    raise RuntimeError(f"JSON 请求失败: {url}")
