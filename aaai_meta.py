import re
import xml.etree.ElementTree as ET
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
from loguru import logger

from fetch_util import get_text, is_transient
from paper_record import make_record, norm_space

OAI_URL = "https://ojs.aaai.org/index.php/AAAI/oai"
ARCHIVE_URL = "https://ojs.aaai.org/index.php/AAAI/issue/archive"
SKIP_TOKENS = (
    "student abstract",
    "student research",
    "demonstration",
    "demonstrations",
    "tutorial",
    "doctoral consortium",
    "undergraduate",
    "new faculty",
    "model ai assignment",
    "teaching",
    "eaai",
    "iaai",
)


def _keep_label(label: str) -> bool:
    low = (label or "").lower()
    return not any(token in low for token in SKIP_TOKENS)


def _local_texts(node: ET.Element, name: str) -> list[str]:
    found = []
    for child in node.iter():
        tag = child.tag.split("}")[-1]
        if tag == name and child.text and child.text.strip():
            found.append(norm_space(child.text) or "")
    return [item for item in found if item]


def _oai_error(root: ET.Element) -> str | None:
    for child in root.iter():
        if child.tag.split("}")[-1] == "error":
            return norm_space(" ".join(part for part in (child.get("code"), child.text) if part))
    return None


def _iter_oai(year: int):
    params: dict = {
        "verb": "ListRecords",
        "metadataPrefix": "oai_dc",
        "from": f"{year}-01-01",
        "until": f"{year}-12-31",
    }
    while True:
        text = get_text(OAI_URL, params=params, timeout=120, sleep_s=0.2)
        root = ET.fromstring(text)
        error = _oai_error(root)
        if error:
            raise RuntimeError(error)
        records = [node for node in root.iter() if node.tag.split("}")[-1] == "record"]
        for record in records:
            yield record
        token = None
        for node in root.iter():
            if node.tag.split("}")[-1] == "resumptionToken" and node.text and node.text.strip():
                token = node.text.strip()
        if not token:
            break
        params = {"verb": "ListRecords", "resumptionToken": token}


def _record_from_oai(node: ET.Element, year: int) -> dict | None:
    header = None
    metadata = None
    for child in list(node):
        name = child.tag.split("}")[-1]
        if name == "header":
            header = child
        elif name == "metadata":
            metadata = child
    if header is not None:
        status = (header.get("status") or "").lower()
        if status == "deleted":
            return None
    if metadata is None:
        return None
    titles = _local_texts(metadata, "title")
    creators = _local_texts(metadata, "creator")
    descriptions = _local_texts(metadata, "description")
    identifiers = _local_texts(metadata, "identifier")
    dates = _local_texts(metadata, "date")
    sources = _local_texts(metadata, "source")
    subjects = _local_texts(metadata, "subject")
    label = " ".join(sources)
    volume = year - 1986
    doi_hint = " ".join(identifiers).lower()
    year_hit = f"aaai.v{volume}" in doi_hint or f"aaai-{year % 100:02d}" in label.lower() or f"({year})" in label
    if not year_hit:
        return None
    if not _keep_label(label or " ".join(titles)):
        return None
    doi = None
    url = None
    pdf_url = None
    for item in identifiers:
        low = item.lower()
        if "doi.org/" in low or low.startswith("10."):
            doi = item.split("doi.org/")[-1]
        elif low.endswith(".pdf"):
            pdf_url = item
        elif item.startswith("http") and url is None:
            url = item
    pid = doi or url
    if not pid or not titles:
        return None
    abstract = max(descriptions, key=len) if descriptions else None
    track = None
    for src in sources:
        low = src.lower()
        if "track" in low or "aaai-" in low:
            track = src
            break
    if track is None:
        for src in sources:
            if not re.fullmatch(r"[\d\-xX]+", src):
                track = src
                break
    return make_record(
        id=pid,
        venue="aaai",
        year=year,
        track=track,
        title=titles[0],
        authors=creators,
        abstract=abstract,
        keywords=subjects,
        doi=doi,
        url=url,
        pdf_url=pdf_url,
        published=dates[0] if dates else None,
        source="ojs.aaai.org",
    )


def _issue_links(year: int) -> list[dict]:
    issues = []
    seen_issues = set()
    seen_pages = set()
    page_url = ARCHIVE_URL
    pages = 0
    while page_url and page_url not in seen_pages and pages < 40:
        seen_pages.add(page_url)
        pages += 1
        html = get_text(page_url, timeout=90, sleep_s=0.3)
        soup = BeautifulSoup(html, "lxml")
        for link in soup.find_all("a", href=True):
            href = urljoin(page_url, link["href"])
            if "/issue/view/" not in href:
                continue
            label = norm_space(link.get_text(" ", strip=True)) or ""
            parent = link.find_parent(["div", "li", "h2", "h3", "td"])
            blob = norm_space(parent.get_text(" ", strip=True)) if parent else label
            if str(year) not in blob and f"aaai-{str(year)[-2:]}" not in blob.lower():
                continue
            if href in seen_issues:
                continue
            seen_issues.add(href)
            issues.append({"url": href, "label": blob or label})
        nxt = soup.select_one("a.next")
        page_url = urljoin(page_url, nxt["href"]) if nxt and nxt.get("href") else None
    return issues


def _article_links(issue_url: str) -> list[str]:
    html = get_text(issue_url, timeout=90, sleep_s=0.2)
    soup = BeautifulSoup(html, "lxml")
    urls = []
    seen = set()
    for link in soup.find_all("a", href=True):
        href = urljoin(issue_url, link["href"].split("#", 1)[0])
        if "/article/view/" not in href or "/pdf" in href.lower():
            continue
        if href in seen:
            continue
        seen.add(href)
        urls.append(href)
    return urls


def _record_from_article(url: str, year: int, track: str | None) -> dict | None:
    html = get_text(url, timeout=60, sleep_s=0.25)
    soup = BeautifulSoup(html, "lxml")
    meta: dict[str, list[str]] = {}
    for tag in soup.find_all("meta"):
        name = tag.get("name")
        content = tag.get("content")
        if name and content:
            meta.setdefault(name, []).append(content.strip())
    title = (meta.get("citation_title") or [None])[0]
    authors = meta.get("citation_author") or []
    doi = (meta.get("citation_doi") or [None])[0]
    pdf_url = (meta.get("citation_pdf_url") or [None])[0]
    published = (meta.get("citation_publication_date") or meta.get("citation_date") or [None])[0]
    keywords = []
    for item in meta.get("citation_keywords", []):
        keywords.extend(part.strip() for part in re.split(r"\s*[;,]\s*", item) if part.strip())
    abstract = None
    block = soup.select_one("section.item.abstract")
    if block:
        abstract = norm_space(block.get_text(" ", strip=True))
        if abstract and abstract.lower().startswith("abstract"):
            abstract = abstract.split(" ", 1)[-1].strip()
    pid = doi or url.rstrip("/").split("/")[-1]
    if not title:
        return None
    return make_record(
        id=pid,
        venue="aaai",
        year=year,
        track=track,
        title=title,
        authors=authors,
        abstract=abstract,
        keywords=keywords,
        doi=doi,
        url=url,
        pdf_url=pdf_url,
        published=published,
        source="ojs.aaai.org",
    )


def _crawl_html(year: int, limit: int | None, existing: dict, on_new) -> list[dict]:
    records = []
    for issue in _issue_links(year):
        if not _keep_label(issue["label"]):
            continue
        if limit is not None and len(records) >= limit:
            break
        for article_url in _article_links(issue["url"]):
            if limit is not None and len(records) >= limit:
                break
            pid_hint = article_url.rstrip("/").split("/")[-1]
            cached = existing.get(pid_hint)
            if cached:
                records.append(cached)
                continue
            try:
                record = _record_from_article(article_url, year, issue["label"])
            except Exception as exc:
                if is_transient(exc):
                    logger.warning(f"暂时失败，下次重试 {article_url}: {exc}")
                    continue
                logger.warning(f"AAAI 文章失败 {article_url}: {exc}")
                continue
            if not record:
                continue
            already = existing.get(record["id"])
            if already:
                records.append(already)
                continue
            records.append(record)
            on_new(record)
            logger.info(f"[{len(records)}] {record.get('title')}")
    return records


def crawl_aaai(year: int, limit: int | None, existing: dict, on_new) -> list[dict]:
    try:
        records = []
        for node in _iter_oai(year):
            if limit is not None and len(records) >= limit:
                break
            record = _record_from_oai(node, year)
            if not record:
                continue
            cached = existing.get(record["id"])
            if cached:
                records.append(cached)
                continue
            records.append(record)
            on_new(record)
        if records:
            logger.info(f"AAAI {year} 从 OAI-PMH 得到 {len(records)} 篇")
            return records
        logger.info("OAI-PMH 没有可用的 AAAI 记录，改抓 issue 页面")
    except Exception as exc:
        logger.warning(f"AAAI OAI-PMH 不可用，改抓 issue 页面: {exc}")
    return _crawl_html(year, limit, existing, on_new)
