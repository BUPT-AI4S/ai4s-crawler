import hashlib
import re
from html import unescape
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from loguru import logger

from fetch_util import get_json, get_text
from paper_record import bibtex_field, make_record, norm_space, norm_title

ACCEPTED_URL = "https://eccv.ecva.net/Conferences/{year}/AcceptedPapers"
CROSSREF = "https://api.crossref.org/works"


def _presentation(schedule: str | None) -> str | None:
    if not schedule:
        return None
    low = schedule.lower()
    for label in ("spotlight", "oral", "poster"):
        if re.search(rf"\b{label}\b", low):
            return label
    return None


def _split_keywords(text: str | None) -> list[str]:
    if not text:
        return []
    parts = re.split(r"\s*(?:⋅|·|\u00b7|;|,)\s*", text)
    return [part.strip() for part in parts if part.strip()]


def parse_accepted_html(html: str, page_url: str) -> list[dict]:
    soup = BeautifulSoup(html, "lxml")
    rows = []
    for tr in soup.select("table tr"):
        cells = tr.find_all(["td", "th"])
        if len(cells) < 2:
            continue
        title_cell = cells[0]
        if title_cell.name == "th":
            continue
        title_link = None
        project_url = None
        for link in title_cell.find_all("a", href=True):
            label = norm_space(link.get_text(" ", strip=True)) or ""
            href = urljoin(page_url, link["href"].strip())
            if "project" in label.lower():
                project_url = href
                continue
            if title_link is None and label and label.lower() not in ("pdf", "doi", "abs"):
                title_link = link
        title = norm_space(title_link.get_text(" ", strip=True)) if title_link else None
        if not title or title.lower() in ("title", "paper"):
            continue
        author_node = title_cell.select_one("div.indented") or title_cell.select_one("i")
        authors = _split_keywords(norm_space(author_node.get_text(" ", strip=True)) if author_node else None)
        keywords = _split_keywords(norm_space(cells[1].get_text(" ", strip=True)))
        schedule = norm_space(cells[2].get_text(" ", strip=True)) if len(cells) > 2 else None
        paper_url = urljoin(page_url, title_link["href"].strip()) if title_link and title_link.get("href") else page_url
        rows.append({
            "title": title,
            "authors": authors,
            "keywords": keywords,
            "presentation": _presentation(schedule),
            "project_url": project_url,
            "url": paper_url,
        })
    return rows


def _strip_markup(text: str | None) -> str | None:
    if not text:
        return None
    cleaned = re.sub(r"<[^>]+>", " ", text)
    return norm_space(unescape(cleaned))


def _crossref_items(year: int) -> list[dict]:
    queries = [
        {
            "query.container-title": f"ECCV {year}",
            "filter": f"type:book-chapter,from-pub-date:{year}-01-01,until-pub-date:{year}-12-31",
        },
        {
            "query.bibliographic": f"Computer Vision ECCV {year}",
            "filter": f"type:book-chapter,from-pub-date:{year}-01-01,until-pub-date:{year}-12-31",
        },
    ]
    best: list[dict] = []
    for params in queries:
        params = dict(params)
        params.update({
            "rows": 1000,
            "select": "title,author,abstract,DOI,page,URL,container-title",
            "mailto": "academic-crawler@localhost",
        })
        offset = 0
        found = []
        total = None
        for _page in range(25):
            params["offset"] = offset
            try:
                payload = get_json(CROSSREF, params=params, timeout=90, sleep_s=0.2)
            except Exception as exc:
                logger.warning(f"Crossref 查询失败: {exc}")
                break
            message = payload.get("message") or {}
            if total is None:
                total = int(message.get("total-results") or 0)
            items = message.get("items") or []
            if not items:
                break
            found.extend(items)
            offset += len(items)
            if total and offset >= total:
                break
        kept = []
        for item in found:
            container = " ".join(item.get("container-title") or []).lower()
            if "eccv" in container or "european conference on computer vision" in container:
                kept.append(item)
        if len(kept) > len(best):
            best = kept
        if len(best) >= 2500:
            break
    return best


def _crossref_by_title(items: list[dict], require_eccv: bool = True) -> dict[str, dict]:
    mapped = {}
    for item in items:
        titles = item.get("title") or []
        if not titles:
            continue
        container = " ".join(item.get("container-title") or [])
        blob = container.lower()
        if require_eccv and "eccv" not in blob and "european conference on computer vision" not in blob:
            continue
        mapped.setdefault(norm_title(titles[0]), item)
    return mapped


def _paper_id(title: str) -> str:
    digest = hashlib.sha1(norm_title(title).encode("utf-8")).hexdigest()[:16]
    return f"eccv-{digest}"


def _crossref_for_titles(year: int, titles: list[str]) -> dict[str, dict]:
    mapped = {}
    for title in titles:
        params = {
            "query.bibliographic": title,
            "filter": f"from-pub-date:{year}-01-01,until-pub-date:{year}-12-31",
            "rows": 5,
            "select": "title,author,abstract,DOI,page,URL,container-title",
            "mailto": "academic-crawler@localhost",
        }
        try:
            payload = get_json(CROSSREF, params=params, timeout=60, sleep_s=0.2)
        except Exception as exc:
            logger.warning(f"Crossref 单篇查询失败: {exc}")
            continue
        items = (payload.get("message") or {}).get("items") or []
        mapped.update(_crossref_by_title(items, require_eccv=False))
    return mapped


def crawl_eccv(year: int, limit: int | None, existing: dict, on_new) -> list[dict]:
    page_url = ACCEPTED_URL.format(year=year)
    html = get_text(page_url, timeout=120, sleep_s=0.3)
    listed = parse_accepted_html(html, page_url)
    if not listed:
        logger.warning(f"ECCV {year} 录用表没有解析出论文")
        return []
    if limit:
        listed = listed[:limit]
    logger.info(f"ECCV {year} 录用表 {len(listed)} 篇，开始对 Crossref 摘要")
    if limit is not None and limit <= 30:
        crossref = _crossref_for_titles(year, [paper["title"] for paper in listed])
    else:
        crossref = _crossref_by_title(_crossref_items(year))
    records = []
    matched = 0
    for paper in listed:
        pid = _paper_id(paper["title"])
        cached = existing.get(pid)
        if cached:
            records.append(cached)
            if cached.get("abstract"):
                matched += 1
            continue
        hit = crossref.get(norm_title(paper["title"]))
        abstract = None
        doi = None
        pages = None
        pdf_url = None
        if hit:
            abstract = _strip_markup(hit.get("abstract"))
            doi = hit.get("DOI")
            pages = hit.get("page")
            pdf_url = hit.get("URL")
            if abstract:
                matched += 1
            authors = paper["authors"]
            if not authors:
                authors = []
                for person in hit.get("author") or []:
                    name = norm_space(" ".join(part for part in (person.get("given"), person.get("family")) if part))
                    if name:
                        authors.append(name)
                paper = dict(paper)
                paper["authors"] = authors
        record = make_record(
            id=pid,
            venue="eccv",
            year=year,
            track="main",
            title=paper["title"],
            authors=paper["authors"],
            abstract=abstract,
            keywords=paper["keywords"],
            presentation=paper["presentation"],
            doi=doi,
            pages=pages,
            url=paper["url"],
            pdf_url=pdf_url,
            project_url=paper.get("project_url"),
            source="eccv.ecva.net",
        )
        if record.get("bibtex"):
            record["doi"] = record["doi"] or bibtex_field(record["bibtex"], "doi")
        records.append(record)
        on_new(record)
    missing = [row["doi"] for row in records if row.get("doi") and not row.get("abstract")]
    if missing:
        from kdd_meta import semantic_scholar_abstracts

        found = semantic_scholar_abstracts(missing)
        for row in records:
            doi = (row.get("doi") or "").lower().split("doi.org/")[-1]
            if row.get("abstract") or doi not in found:
                continue
            row["abstract"] = found[doi]
            matched += 1
    logger.info(f"ECCV 摘要覆盖 {matched}/{len(records)}")
    return records
