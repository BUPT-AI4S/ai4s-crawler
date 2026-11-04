import itertools
import os
import re
import time
import xml.etree.ElementTree as ET

from loguru import logger

from fetch_util import get_json, get_text, is_transient
from paper_record import make_record, norm_space, norm_title

DBLP_API = "https://dblp.org/search/publ/api"
CROSSREF = "https://api.crossref.org/works"
OPENALEX = "https://api.openalex.org/works"
_OPENALEX_KEY_NAMES = ("OPENALEX_API_KEY", "OPENALEX_PREVIEW_API_KEY")
_OPENALEX_ROTATION = itertools.count()


def openalex_keys() -> list[str]:
    """所有可用的 OpenAlex key：两把 key 各自有独立配额，轮转使用才能都吃满。"""
    keys = []
    for name in _OPENALEX_KEY_NAMES:
        value = (os.environ.get(name) or "").strip()
        if value and value not in keys:
            keys.append(value)
    return keys


def next_openalex_key() -> str | None:
    keys = openalex_keys()
    if not keys:
        return None
    return keys[next(_OPENALEX_ROTATION) % len(keys)]

ACM_PROCEEDINGS_2026 = (
    "https://dl.acm.org/doi/proceedings/10.1145/3770854",
    "https://dl.acm.org/doi/proceedings/10.1145/3770855",
)


def _dblp_authors(info: dict) -> list[str]:
    authors = (info.get("authors") or {}).get("author")
    if authors is None:
        return []
    if isinstance(authors, dict):
        authors = [authors]
    names = []
    for author in authors:
        if isinstance(author, str):
            names.append(author.strip())
        elif isinstance(author, dict):
            names.append(str(author.get("text") or author.get("#text") or "").strip())
    return [name for name in names if name]


def _clean_title(title) -> str | None:
    if isinstance(title, dict):
        title = title.get("text") or title.get("#text")
    text = norm_space(title if isinstance(title, str) else None)
    if text and text.endswith("."):
        text = text[:-1].strip()
    return text or None


def _dblp_query(query: str) -> list[dict]:
    rows = []
    offset = 0
    while True:
        payload = get_json(
            DBLP_API,
            params={"q": query, "h": 1000, "f": offset, "format": "json"},
            timeout=90,
            sleep_s=0.2,
        )
        hits_block = (payload.get("result") or {}).get("hits") or {}
        total = int(hits_block.get("@total") or 0)
        hits = hits_block.get("hit") or []
        if isinstance(hits, dict):
            hits = [hits]
        if not hits:
            break
        for hit in hits:
            info = hit.get("info") or {}
            title = _clean_title(info.get("title"))
            if not title:
                continue
            doi = info.get("doi")
            if isinstance(doi, str):
                doi = doi.strip() or None
            ee = info.get("ee")
            if isinstance(ee, dict):
                ee = ee.get("text") or ee.get("#text")
            rows.append({
                "title": title,
                "authors": _dblp_authors(info),
                "pages": info.get("pages"),
                "doi": doi,
                "url": ee if isinstance(ee, str) else None,
                "year": info.get("year"),
            })
        offset += len(hits)
        if offset >= total:
            break
    return rows


def _dblp_xml(year: int) -> list[dict]:
    rows = []
    names = [f"kdd{year}-1", f"kdd{year}-2", f"kdd{year}"]
    for name in names:
        url = f"https://dblp.org/db/conf/kdd/{name}.xml"
        try:
            text = get_text(url, timeout=90, sleep_s=0.2, headers={"Accept": "application/xml,text/xml,*/*"})
        except Exception as exc:
            logger.info(f"DBLP XML 不可用 {url}: {exc}")
            continue
        try:
            root = ET.fromstring(text)
        except ET.ParseError as exc:
            logger.info(f"DBLP XML 解析失败 {url}: {exc}")
            continue
        for node in root:
            if node.tag not in ("inproceedings", "incollection"):
                continue
            title = _clean_title("".join(node.findtext("title") or ""))
            authors = [norm_space(author.text) for author in node.findall("author")]
            authors = [author for author in authors if author]
            ee = node.findtext("ee")
            doi = None
            if ee and "doi.org/" in ee:
                doi = ee.split("doi.org/")[-1]
            if not title:
                continue
            rows.append({
                "title": title,
                "authors": authors,
                "pages": node.findtext("pages"),
                "doi": doi,
                "url": ee,
                "year": node.findtext("year"),
            })
    return rows


def _crossref_kdd(year: int) -> list[dict]:
    params = {
        "query.container-title": "SIGKDD",
        "filter": f"from-pub-date:{year}-01-01,until-pub-date:{year}-12-31,type:proceedings-article",
        "rows": 1000,
        "select": "title,author,abstract,DOI,page,URL,container-title",
        "mailto": "academic-crawler@localhost",
    }
    offset = 0
    rows = []
    total = None
    for page in range(10):
        params["offset"] = offset
        payload = get_json(CROSSREF, params=params, timeout=90, sleep_s=0.2)
        message = payload.get("message") or {}
        if total is None:
            total = int(message.get("total-results") or 0)
        items = message.get("items") or []
        logger.info(f"Crossref KDD 第 {page + 1} 页 {len(items)} 条，合计 {total}")
        if not items:
            break
        for item in items:
            container = " ".join(item.get("container-title") or []).lower()
            if "kdd" not in container and "knowledge discovery" not in container:
                continue
            titles = item.get("title") or []
            title = _clean_title(titles[0] if titles else None)
            if not title:
                continue
            authors = []
            for person in item.get("author") or []:
                name = norm_space(" ".join(part for part in (person.get("given"), person.get("family")) if part))
                if name:
                    authors.append(name)
            rows.append({
                "title": title,
                "authors": authors,
                "pages": item.get("page"),
                "doi": item.get("DOI"),
                "url": item.get("URL"),
                "abstract": _strip_jats(item.get("abstract")),
                "year": str(year),
            })
        offset += len(items)
        if total is not None and offset >= total:
            break
    return rows


def _strip_jats(text) -> str | None:
    if not isinstance(text, str) or not text.strip():
        return None
    cleaned = re.sub(r"<[^>]+>", " ", text)
    return norm_space(cleaned)


def list_kdd_bibliography(year: int) -> tuple[list[dict], str]:
    queries = [
        f"toc:db/conf/kdd/kdd{year}-1.bht:",
        f"toc:db/conf/kdd/kdd{year}-2.bht:",
        f"toc:db/conf/kdd/kdd{year}.bht:",
    ]
    rows = []
    for query in queries:
        try:
            found = _dblp_query(query)
        except Exception as exc:
            logger.info(f"DBLP API 失败 {query}: {exc}")
            found = []
        rows.extend(found)
    if rows:
        return _dedupe(rows), "dblp"
    xml_rows = _dblp_xml(year)
    if xml_rows:
        return _dedupe(xml_rows), "dblp"
    logger.warning("DBLP 没有 KDD 书目，改用 Crossref")
    return _dedupe(_crossref_kdd(year)), "crossref"


def _dedupe(rows: list[dict]) -> list[dict]:
    seen = set()
    out = []
    for row in rows:
        key = (row.get("doi") or "").lower() or norm_title(row.get("title"))
        if not key or key in seen:
            continue
        seen.add(key)
        out.append(row)
    return out


def _doi_key(doi: str | None) -> str | None:
    if not doi:
        return None
    text = doi.strip().lower()
    text = text.split("doi.org/")[-1]
    return text or None


def _clean_track(text: str) -> str:
    cleaned = re.sub(r"^session:\s*", "", text.strip(), flags=re.I)
    return re.sub(r"\s+", " ", cleaned).strip()


def acm_tracks(year: int) -> dict[str, str]:
    if year != 2026:
        return {}
    mapping = {}
    blocked = False
    for url in ACM_PROCEEDINGS_2026:
        try:
            html = get_text(url, timeout=90, sleep_s=0.4)
        except Exception as exc:
            logger.warning(f"ACM 会议录目录不可用 {url}: {exc}")
            blocked = True
            continue
        from bs4 import BeautifulSoup

        soup = BeautifulSoup(html, "lxml")
        current = None
        for el in soup.find_all(["h1", "h2", "h3", "h4", "h5", "a"]):
            if el.name != "a":
                text = _clean_track(el.get_text(" ", strip=True))
                if text and "track" in text.lower():
                    current = text
                continue
            href = el.get("href") or ""
            match = re.search(r"(10\.1145/\d+\.\d+)", href, flags=re.I)
            if match and current:
                mapping[_doi_key(match.group(1))] = current
    if not mapping:
        logger.warning("ACM 目录没有解析出分轨。KDD 书目仍会保存，官方 AI for Sciences 标签可能缺失")
        if blocked:
            logger.warning("ACM 目录请求被拦截")
    else:
        logger.info(f"ACM 分轨映射 {len(mapping)} 篇")
    return mapping


def _reconstruct_abstract(inverted: dict | None) -> str | None:
    if not inverted:
        return None
    positions = []
    for word, indexes in inverted.items():
        for index in indexes:
            positions.append((index, word))
    if not positions:
        return None
    positions.sort()
    return " ".join(word for _, word in positions)


SEMANTIC_SCHOLAR_BATCH = 500
OPENALEX_BATCH = 90
OPENALEX_BATCH_MIN = 10
SEMANTIC_SCHOLAR_UA = "academic-crawler/1.0 (mailto:academic-crawler@localhost)"


def _s2_api_key() -> str | None:
    return os.environ.get("SEMANTIC_SCHOLAR_API_KEY") or os.environ.get("S2_API_KEY") or None


def semantic_scholar_abstracts(dois: list[str]) -> dict[str, str]:
    from fetch_util import request_post

    found = {}
    url = "https://api.semanticscholar.org/graph/v1/paper/batch"
    api_key = _s2_api_key()
    if not api_key:
        return {}
    batch = SEMANTIC_SCHOLAR_BATCH
    headers = {"User-Agent": SEMANTIC_SCHOLAR_UA, "x-api-key": api_key}
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


def openalex_abstracts(dois: list[str], *, api_key: str | None = None) -> dict[str, str]:
    found = {}
    api_key = api_key or next_openalex_key()
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


def crawl_kdd(year: int, limit: int | None, existing: dict, on_new) -> list[dict]:
    bibliography, origin = list_kdd_bibliography(year)
    if limit:
        bibliography = bibliography[:limit]
    if not bibliography:
        logger.warning(f"没有找到 KDD {year} 论文")
        return []
    logger.info(f"KDD {year} 书目 {len(bibliography)} 篇，来源 {origin}")
    tracks = acm_tracks(year) if year == 2026 else {}
    missing = []
    records = []
    for paper in bibliography:
        doi = _doi_key(paper.get("doi"))
        pid = doi or ("kdd-" + norm_title(paper["title"])[:80].replace(" ", "-"))
        cached = existing.get(pid)
        if cached:
            records.append(cached)
            continue
        if doi and not paper.get("abstract"):
            missing.append(doi)
        records.append({
            "paper": paper,
            "id": pid,
            "doi": doi,
            "track": tracks.get(doi) if doi else None,
        })
    abstracts = openalex_abstracts(missing) if missing else {}
    if missing and len(abstracts) < len(missing):
        still = [doi for doi in missing if doi not in abstracts]
        abstracts.update(semantic_scholar_abstracts(still))
    final = []
    for item in records:
        if "paper" not in item:
            final.append(item)
            continue
        paper = item["paper"]
        doi = item["doi"]
        abstract = paper.get("abstract") or (abstracts.get(doi) if doi else None)
        record = make_record(
            id=item["id"],
            venue="kdd",
            year=year,
            track=item["track"],
            title=paper.get("title"),
            authors=paper.get("authors") or [],
            abstract=abstract,
            doi=doi,
            pages=paper.get("pages"),
            url=paper.get("url"),
            pdf_url=paper.get("url"),
            published=str(paper.get("year") or year),
            source=origin,
        )
        final.append(record)
        on_new(record)
    filled = sum(1 for row in final if row.get("abstract"))
    logger.info(f"KDD 摘要覆盖 {filled}/{len(final)}")
    return final
