import re
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from loguru import logger

from acl import parse_paper_page
from fetch_util import get_text, is_transient
from paper_record import make_record

EVENT_URL = "https://aclanthology.org/events/{venue}-{year}/"
SKIP_TOKENS = ("demo", "tutorial", "srw", "industry", "student", "workshop")
KEEP_TOKENS = ("-long", "-short", "-main", "findings")


def _volume_track(volume_id: str) -> str | None:
    slug = volume_id.split(".", 1)[-1].lower()
    if any(token in slug for token in SKIP_TOKENS):
        return None
    if "findings" in slug:
        return "findings"
    if "-long" in slug:
        return "long"
    if "-short" in slug:
        return "short"
    if "-main" in slug:
        return "main"
    if any(token in slug for token in KEEP_TOKENS):
        return slug
    return None


def _volume_links(html: str, page_url: str, year: int) -> list[dict]:
    soup = BeautifulSoup(html, "lxml")
    found = []
    seen = set()
    for link in soup.find_all("a", href=True):
        href = urljoin(page_url, link["href"].strip())
        path = urlparse(href).path.strip("/")
        match = re.fullmatch(rf"volumes/({year}\.[a-z0-9]+(?:-[a-z0-9]+)+)", path)
        if not match:
            continue
        volume_id = match.group(1)
        if volume_id in seen:
            continue
        track = _volume_track(volume_id)
        if not track:
            continue
        seen.add(volume_id)
        found.append({"id": volume_id, "track": track, "url": f"https://aclanthology.org/volumes/{volume_id}/"})
    return found


def _paper_urls(html: str, page_url: str) -> list[str]:
    soup = BeautifulSoup(html, "lxml")
    urls = []
    seen = set()
    for link in soup.find_all("a", href=True):
        href = urljoin(page_url, link["href"].strip())
        path = urlparse(href).path.strip("/")
        if not re.fullmatch(r"\d{4}\.[a-z0-9]+(?:-[a-z0-9]+)+\.[1-9]\d*", path):
            continue
        if path in seen:
            continue
        seen.add(path)
        urls.append(f"https://aclanthology.org/{path}/")
    return urls


def crawl_anthology(venue: str, year: int, limit: int | None, existing: dict, on_new) -> list[dict] | None:
    """返回 None 表示 Anthology 没有这一年的事件页。"""
    event_url = EVENT_URL.format(venue=venue, year=year)
    try:
        html = get_text(event_url, timeout=90, sleep_s=0.2)
    except requests.HTTPError as exc:
        status = exc.response.status_code if exc.response is not None else None
        if status == 404:
            logger.info(f"Anthology 没有 {venue} {year}: {event_url}")
            return None
        raise
    volumes = _volume_links(html, event_url, year)
    if not volumes:
        logger.info(f"Anthology {venue} {year} 没有 long/short/main/findings 卷")
        return None
    records = []
    for volume in volumes:
        if limit is not None and len(records) >= limit:
            break
        volume_html = get_text(volume["url"], timeout=120, sleep_s=0.2)
        for paper_url in _paper_urls(volume_html, volume["url"]):
            if limit is not None and len(records) >= limit:
                break
            anthology_id = urlparse(paper_url).path.strip("/")
            cached = existing.get(anthology_id)
            if cached:
                records.append(cached)
                continue
            try:
                page = get_text(paper_url, timeout=60, sleep_s=0.25)
                parsed = parse_paper_page(page, paper_url)
            except Exception as exc:
                if is_transient(exc):
                    logger.warning(f"暂时失败，下次重试 {paper_url}: {exc}")
                    continue
                logger.warning(f"解析失败 {paper_url}: {exc}")
                continue
            record = make_record(
                id=parsed.anthology_id or anthology_id,
                venue=venue,
                year=year,
                track=volume["track"],
                title=parsed.title,
                authors=parsed.authors,
                abstract=parsed.abstract,
                doi=parsed.doi,
                url=parsed.url,
                pdf_url=parsed.pdf_url,
                published=parsed.publication_date,
                source="aclanthology.org",
            )
            records.append(record)
            on_new(record)
            logger.info(f"[{len(records)}] {record.get('title')}")
    return records
