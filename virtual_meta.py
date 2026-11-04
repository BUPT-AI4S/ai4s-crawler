import re
from urllib.parse import parse_qs, urlparse

from loguru import logger

from fetch_util import get_json, is_transient
from iclr import list_iclr_proceedings
from nips import fetch_html, parse_neurips_paper
from paper_record import make_record, norm_space

_PRESENTATION_RANK = {"spotlight": 3, "oral": 2, "poster": 1}


def _forum_id(url: str | None) -> str | None:
    if not url or "openreview.net" not in url:
        return None
    query = parse_qs(urlparse(url).query)
    if query.get("id"):
        return query["id"][0]
    return None


def _presentation(item: dict) -> str | None:
    blob = " ".join(
        str(item.get(key) or "")
        for key in ("eventtype", "event_type", "decision", "session")
    ).lower()
    for label in ("spotlight", "oral", "poster"):
        if re.search(rf"\b{label}\b", blob):
            return label
    return None


def _is_paper(item: dict) -> bool:
    source = (item.get("sourceurl") or "").lower()
    if "workshop" in source:
        return False
    event_type = (item.get("eventtype") or "").lower()
    if any(token in event_type for token in ("tutorial", "invited", "affinity", "social", "expo")):
        return False
    decision = (item.get("decision") or "").lower()
    if "reject" in decision or "withdraw" in decision:
        return False
    if item.get("paper_url") or item.get("paper_pdf_url"):
        return True
    return any(token in event_type for token in ("poster", "oral", "spotlight"))


def _authors(item: dict) -> tuple[list[str], list[str]]:
    names = []
    ids = []
    for author in item.get("authors") or []:
        if isinstance(author, str):
            names.append(author.strip())
            continue
        if not isinstance(author, dict):
            continue
        name = norm_space(author.get("fullname") or author.get("name"))
        if name:
            names.append(name)
        if author.get("id") is not None:
            ids.append(str(author["id"]))
    return names, ids


def _keywords(item: dict) -> list[str]:
    raw = item.get("keywords") or []
    if isinstance(raw, str):
        return [part.strip() for part in re.split(r"\s*[;,]\s*", raw) if part.strip()]
    found = []
    for entry in raw:
        if isinstance(entry, str) and entry.strip():
            found.append(entry.strip())
        elif isinstance(entry, dict):
            name = entry.get("name") or entry.get("keyword")
            if isinstance(name, str) and name.strip():
                found.append(name.strip())
    return found


def _media_url(item: dict, needles: tuple[str, ...]) -> str | None:
    for media in item.get("eventmedia") or []:
        uri = media.get("uri") or ""
        name = (media.get("name") or "").lower()
        if not isinstance(uri, str) or not uri.startswith("http"):
            continue
        if any(needle in name or needle in uri.lower() for needle in needles):
            return uri
    return None


def _load_virtual(venue: str, year: int) -> tuple[list[dict], dict] | None:
    papers_url = f"https://{venue}.cc/static/virtual/data/{venue}-{year}-orals-posters.json"
    abstracts_url = f"https://{venue}.cc/static/virtual/data/{venue}-{year}-abstracts.json"
    if venue == "neurips":
        papers_url = f"https://neurips.cc/static/virtual/data/neurips-{year}-orals-posters.json"
        abstracts_url = f"https://neurips.cc/static/virtual/data/neurips-{year}-abstracts.json"
    try:
        payload = get_json(papers_url, timeout=120, sleep_s=0.1)
    except Exception as exc:
        logger.info(f"{venue} {year} 没有 virtual JSON: {exc}")
        return None
    abstracts = {}
    try:
        raw = get_json(abstracts_url, timeout=120, sleep_s=0.1)
        if isinstance(raw, dict):
            abstracts = {str(key): value for key, value in raw.items() if isinstance(value, str)}
    except Exception as exc:
        logger.warning(f"{venue} {year} 摘要 JSON 不可用: {exc}")
    results = payload.get("results") if isinstance(payload, dict) else None
    if not isinstance(results, list):
        return None
    return results, abstracts


def _records_from_virtual(venue: str, year: int, results: list[dict], abstracts: dict, limit: int | None) -> list[dict]:
    grouped: dict[str, dict] = {}
    for item in results:
        if not isinstance(item, dict) or not _is_paper(item):
            continue
        title = norm_space(item.get("name"))
        if not title:
            continue
        forum = _forum_id(item.get("paper_url"))
        key = forum or item.get("uid") or title.lower()
        presentation = _presentation(item)
        bucket = grouped.get(key)
        if bucket is None:
            bucket = {"item": item, "presentation": presentation, "ids": [], "forum": forum}
            grouped[key] = bucket
        bucket["ids"].append(item.get("id"))
        old_rank = _PRESENTATION_RANK.get(bucket["presentation"] or "", 0)
        new_rank = _PRESENTATION_RANK.get(presentation or "", 0)
        if new_rank >= old_rank:
            bucket["item"] = item
            bucket["presentation"] = presentation
            bucket["forum"] = forum or bucket["forum"]
    records = []
    for key, bucket in grouped.items():
        item = bucket["item"]
        abstract = None
        for event_id in bucket["ids"]:
            text = abstracts.get(str(event_id))
            if text and text.strip():
                abstract = norm_space(text)
                break
        authors, author_ids = _authors(item)
        forum = bucket["forum"]
        pdf_url = item.get("paper_pdf_url") or (_media_url(item, ("pdf",)) if item else None)
        if not pdf_url and forum:
            pdf_url = f"https://openreview.net/pdf?id={forum}"
        site = "https://neurips.cc" if venue == "neurips" else f"https://{venue}.cc"
        virtual_path = item.get("virtualsite_url") or ""
        url = item.get("paper_url") or (site + virtual_path if virtual_path else None)
        published = item.get("starttime")
        if isinstance(published, str) and "T" in published:
            published = published.split("T", 1)[0]
        records.append(make_record(
            id=forum or str(key),
            venue=venue,
            year=year,
            track="main",
            title=item.get("name"),
            authors=authors,
            author_ids=author_ids,
            abstract=abstract,
            keywords=_keywords(item),
            primary_area=norm_space(item.get("topic")) if isinstance(item.get("topic"), str) else None,
            presentation=bucket["presentation"],
            url=url,
            pdf_url=pdf_url,
            code_url=_media_url(item, ("code", "github")),
            project_url=_media_url(item, ("project",)),
            published=published,
            source=f"{venue}.cc",
        ))
        if limit is not None and len(records) >= limit:
            break
    logger.info(f"{venue} {year} virtual 去重后 {len(grouped)} 篇，写出 {len(records)} 篇")
    return records


def _iclr_proceedings(year: int, limit: int | None, existing: dict, on_new) -> list[dict]:
    listed = list_iclr_proceedings(year)
    if limit:
        listed = listed[:limit]
    records = []
    for item in listed:
        url = item["url"]
        match = re.search(r"/([0-9a-f]{8,})-", url)
        pid = match.group(1) if match else url
        cached = existing.get(pid)
        if cached:
            records.append(cached)
            continue
        try:
            paper = parse_neurips_paper(fetch_html(url, sleep_s=0.25), url)
        except Exception as exc:
            if is_transient(exc):
                logger.warning(f"暂时失败，下次重试 {url}: {exc}")
                continue
            logger.warning(f"ICLR proceedings 解析失败 {url}: {exc}")
            continue
        record = make_record(
            id=pid,
            venue="iclr",
            year=year,
            track="main",
            title=paper.title or item.get("title"),
            authors=paper.authors,
            abstract=paper.abstract,
            doi=paper.doi,
            pages="-".join(part for part in (paper.firstpage, paper.lastpage) if part) or None,
            url=paper.url,
            pdf_url=paper.pdf_url or item.get("pdf_url"),
            published=paper.publication_date,
            source="proceedings.iclr.cc",
        )
        records.append(record)
        on_new(record)
        logger.info(f"[{len(records)}] {record.get('title')}")
    return records


def crawl_virtual(venue: str, year: int, limit: int | None, existing: dict, on_new) -> list[dict]:
    loaded = _load_virtual(venue, year)
    if loaded:
        results, abstracts = loaded
        records = _records_from_virtual(venue, year, results, abstracts, limit)
        if records:
            return records
    if venue == "iclr":
        logger.info(f"ICLR {year} 改从 proceedings.iclr.cc 拉摘要")
        return _iclr_proceedings(year, limit, existing, on_new)
    logger.warning(f"没有 {venue} {year} 的公开会议页面")
    return []
