"""P0 补丁：OpenAlex 批量 20->90、Semantic Scholar 支持 500/批 key、Crossref mailto。

用法：python3 p0_patch_20261104.py <目标目录>
脚本对 kdd_meta.py、fetch_util.py 做定点替换，已打过补丁时只报告不重复写。
"""
import pathlib
import re
import sys


NEW_S2 = '''def _s2_api_key() -> str | None:
    return os.environ.get("SEMANTIC_SCHOLAR_API_KEY") or os.environ.get("S2_API_KEY") or None


def semantic_scholar_abstracts(dois: list[str]) -> dict[str, str]:
    from fetch_util import request_post

    found = {}
    url = "https://api.semanticscholar.org/graph/v1/paper/batch"
    api_key = _s2_api_key()
    batch = SEMANTIC_SCHOLAR_BATCH if api_key else SEMANTIC_SCHOLAR_BATCH_ANONYMOUS
    headers = {"User-Agent": SEMANTIC_SCHOLAR_UA}
    if api_key:
        headers["x-api-key"] = api_key
    keys = [doi for doi in (_doi_key(item) for item in dois) if doi]
    for start in range(0, len(keys), batch):
        chunk = keys[start : start + batch]
        body = {"ids": [f"DOI:{doi}" for doi in chunk]}
        try:
            http = request_post(
                url,
                params={"fields": "externalIds,abstract"},
                json=body,
                timeout=60,
                headers=headers,
            )
            if http.status_code == 429:
                if not api_key:
                    logger.warning("Semantic Scholar 速率受限且未配置 API key，摘要可能不完整")
                    break
                time.sleep(3)
                http = request_post(
                    url,
                    params={"fields": "externalIds,abstract"},
                    json=body,
                    timeout=60,
                    headers=headers,
                )
                if http.status_code == 429:
                    logger.warning("Semantic Scholar 速率受限，摘要可能不完整")
                    break
            http.raise_for_status()
            rows = http.json()
        except Exception as exc:
            logger.warning(f"Semantic Scholar 摘要失败: {exc}")
            break
        if not isinstance(rows, list):
            continue
        for work in rows:
            if not isinstance(work, dict):
                continue
            doi = _doi_key((work.get("externalIds") or {}).get("DOI"))
            abstract = norm_space(work.get("abstract"))
            if doi and abstract:
                found[doi] = abstract
    return found
'''

NEW_OPENALEX = '''SEMANTIC_SCHOLAR_BATCH = 500
SEMANTIC_SCHOLAR_BATCH_ANONYMOUS = 50
OPENALEX_BATCH = 90
OPENALEX_BATCH_MIN = 10
SEMANTIC_SCHOLAR_UA = "academic-crawler/1.0 (mailto:academic-crawler@localhost)"


def _openalex_page(chunk: list[str], headers: dict | None) -> list[dict]:
    payload = get_json(
        OPENALEX,
        headers=headers,
        params={
            "filter": "doi:" + "|".join(chunk),
            "per-page": len(chunk),
            "select": "doi,abstract_inverted_index",
        },
        timeout=45,
        sleep_s=0.2,
        retries=1,
    )
    return payload.get("results") or []


def _openalex_pages(chunk: list[str], headers: dict | None) -> list[dict]:
    """失败的批次折半重试；只对可重试错误（限流/5xx/400 过滤过长）拆分。"""
    try:
        return _openalex_page(chunk, headers)
    except Exception as exc:
        status = getattr(getattr(exc, "response", None), "status_code", None)
        retryable = is_transient(exc) or status == 400
        if len(chunk) <= OPENALEX_BATCH_MIN or not retryable:
            logger.warning(f"OpenAlex 摘要中断: {exc}")
            return []
        middle = len(chunk) // 2
        logger.warning(f"OpenAlex 批量失败，拆分 {len(chunk)} 条为 {middle}+{len(chunk) - middle} 条: {exc}")
        return _openalex_pages(chunk[:middle], headers) + _openalex_pages(chunk[middle:], headers)


def openalex_abstracts(dois: list[str]) -> dict[str, str]:
    found = {}
    api_key = os.environ.get("OPENALEX_API_KEY")
    headers = {"Authorization": f"Bearer {api_key}"} if api_key else None
    keys = [doi for doi in (_doi_key(item) for item in dois) if doi]
    for start in range(0, len(keys), OPENALEX_BATCH):
        chunk = keys[start : start + OPENALEX_BATCH]
        for work in _openalex_pages(chunk, headers):
            doi = _doi_key(work.get("doi"))
            abstract = _reconstruct_abstract(work.get("abstract_inverted_index"))
            if doi and abstract:
                found[doi] = abstract
    return found
'''

MAILTO_BLOCK = '''_CROSSREF_MAILTO = os.environ.get('CROSSREF_MAILTO', 'academic-crawler@users.noreply.github.com')


def _with_politeness(host, kwargs):
    """Crossref 公共池靠 mailto 进 polite pool，避免被当作匿名突发流量。"""
    if host != 'api.crossref.org':
        return kwargs
    params = dict(kwargs.get('params') or {})
    if not params.get('mailto'):
        params['mailto'] = _CROSSREF_MAILTO
    kwargs = dict(kwargs, params=params)
    return kwargs


'''


def _read(path):
    raw = path.read_bytes()
    crlf = b'\r\n' in raw
    return raw.decode('utf-8').replace('\r\n', '\n'), crlf


def _write(path, text, crlf):
    if crlf:
        text = text.replace('\n', '\r\n')
    path.write_bytes(text.encode('utf-8'))


def patch_kdd_meta(path):
    text, crlf = _read(path)
    if 'OPENALEX_BATCH = 90' in text:
        print(f'{path.name}: 已打过补丁，跳过')
        return False
    text = text.replace('import os\nimport re\nimport xml.etree.ElementTree as ET',
                        'import os\nimport re\nimport time\nimport xml.etree.ElementTree as ET', 1)
    text, count_s2 = re.subn(
        r'def semantic_scholar_abstracts\(dois: list\[str\]\) -> dict\[str, str\]:.*?(?=\ndef openalex_abstracts\()',
        NEW_S2 + '\n', text, count=1, flags=re.S)
    text, count_oa = re.subn(
        r'def openalex_abstracts\(dois: list\[str\]\) -> dict\[str, str\]:.*?(?=\ndef crawl_kdd\()',
        NEW_OPENALEX + '\n', text, count=1, flags=re.S)
    if (count_s2, count_oa) != (1, 1):
        raise SystemExit(f'{path.name}: 定位失败 s2={count_s2} openalex={count_oa}')
    _write(path, text, crlf)
    print(f'{path.name}: 已替换 semantic_scholar_abstracts、openalex_abstracts，新增 time 导入')
    return True


def patch_fetch_util(path):
    text, crlf = _read(path)
    if '_with_politeness' in text:
        print(f'{path.name}: 已打过补丁，跳过')
        return False
    anchor = 'def _request(send, url, **kwargs):\n    host = urlparse(url).hostname\n'
    if text.count(anchor) != 1:
        raise SystemExit(f'{path.name}: 定位失败，_request 锚点出现 {text.count(anchor)} 次')
    text = text.replace(anchor, MAILTO_BLOCK + anchor + '    kwargs = _with_politeness(host, kwargs)\n', 1)
    _write(path, text, crlf)
    print(f'{path.name}: 已注入 Crossref mailto（polite pool）')
    return True


def main():
    root = pathlib.Path(sys.argv[1]).resolve()
    changed = patch_kdd_meta(root / 'kdd_meta.py')
    changed = patch_fetch_util(root / 'fetch_util.py') or changed
    for name in ('kdd_meta.py', 'fetch_util.py'):
        compile((root / name).read_text(encoding='utf-8'), str(root / name), 'exec')
    print('语法检查通过；变更文件数:', int(changed))


if __name__ == '__main__':
    main()
