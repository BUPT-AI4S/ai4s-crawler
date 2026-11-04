import requests

cookies = {
    'browser_timezone': 'Asia/Shanghai',
    'sessionid': 'kkv8c2wou6yfb9oi6mmk7yp1d4zrjgqq',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    # 'Cookie': 'browser_timezone=Asia/Shanghai; sessionid=kkv8c2wou6yfb9oi6mmk7yp1d4zrjgqq',
}
import json
import re
import time
from dataclasses import dataclass, asdict
from typing import List, Optional, Dict, Any
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from loguru import logger


@dataclass
class ThecvfItem:
    url: str
    canonical: Optional[str]
    title: Optional[str]
    authors: List[str]
    abstract: Optional[str]
    date_published: Optional[str]
    date_modified: Optional[str]
    event_type: Optional[str]          # Poster / Oral / etc.
    schedule: Optional[str]            # e.g. Tue, Oct 21, 2025 • 2:45 PM – 4:45 PM PDT
    location: Optional[str]            # e.g. Exhibit Hall I #244
    project_url: Optional[str]
    slides_url: Optional[str]
    poster_url: Optional[str]
    pdf_url: Optional[str]
    video_url: Optional[str]           # youtube embed
    image_url: Optional[str]           # from JSON-LD
    thumbnail_url: Optional[str]       # from JSON-LD


def _as_pdf_url(url: Optional[str]) -> Optional[str]:
    if not url:
        return None
    u = url.strip()
    if "arxiv.org/abs/" in u:
        return u.replace("/abs/", "/pdf/")
    if "openaccess.thecvf.com" in u and "/html/" in u:
        u = u.replace("/html/", "/papers/")
        if u.endswith(".html"):
            u = u[: -len(".html")] + ".pdf"
    return u


def _clean_text(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def fetch_html(url: str, timeout: int = 90, sleep_s: float = 0.8) -> str:
    r = requests.get(url, headers=headers, timeout=timeout)
    r.raise_for_status()
    time.sleep(sleep_s)
    return r.text


def _parse_jsonld(soup: BeautifulSoup) -> Dict[str, Any]:
    """
    返回页面里第一个看起来像 CreativeWork 的 JSON-LD（如果存在）。
    """
    for tag in soup.find_all("script", attrs={"type": "application/ld+json"}):
        txt = (tag.string or tag.get_text() or "").strip()
        if not txt:
            continue
        try:
            data = json.loads(txt)
        except Exception:
            continue

        # 可能是 dict 或 list
        candidates = data if isinstance(data, list) else [data]
        for obj in candidates:
            if isinstance(obj, dict) and obj.get("@type") in ("CreativeWork", "ScholarlyArticle", "Article"):
                return obj
    return {}


def parse_thecvf_virtual_page(html: str, url: str) -> ThecvfItem:
    soup = BeautifulSoup(html, "lxml")

    # canonical
    canonical = None
    can = soup.find("link", rel="canonical")
    if can and can.get("href"):
        canonical = can["href"].strip()

    base_url = canonical or url

    # JSON-LD（最稳定）
    j = _parse_jsonld(soup)
    title = j.get("name")
    authors = []
    for a in j.get("author", []) or []:
        if isinstance(a, dict) and a.get("name"):
            authors.append(a["name"].strip())
        elif isinstance(a, str):
            authors.append(a.strip())

    date_published = j.get("datePublished")
    date_modified = j.get("dateModified")

    image_url = j.get("image")
    if image_url:
        image_url = urljoin(base_url, image_url)

    thumbnail_url = j.get("thumbnailUrl")
    if thumbnail_url:
        thumbnail_url = urljoin(base_url, thumbnail_url)

    # 标题（DOM 兜底）
    if not title:
        h1 = soup.select_one("h1.event-title")
        if h1:
            title = _clean_text(h1.get_text(" ", strip=True))

    # 作者（DOM 兜底：Yuwei Yang · Zeyu Zhang · ...）
    if not authors:
        org = soup.select_one("div.event-organizers")
        if org:
            raw = org.get_text(" ", strip=True)
            # &middot; 会变成 “·”
            parts = [p.strip() for p in re.split(r"·|\u00b7|&middot;|,", raw) if p.strip()]
            authors = parts

    # abstract（DOM：div.abstract-text-inner p）
    abstract = None
    abs_p = soup.select_one("div.abstract-text-inner")
    if abs_p:
        abstract = _clean_text(abs_p.get_text(" ", strip=True))

    # event type（Poster 等）
    event_type = None
    badge = soup.select_one(".event-type-badge")
    if badge:
        event_type = _clean_text(badge.get_text(" ", strip=True))

    # schedule & location（meta-pill）
    schedule = None
    location = None
    pills = [p.get_text(" ", strip=True) for p in soup.select(".meta-pill")]
    # 你样例里 schedule 是包含日期时间的那条，location 包含 Exhibit Hall
    for t in pills:
        if re.search(r"\b(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)\b", t) and re.search(r"\d{1,2}:\d{2}", t):
            schedule = _clean_text(t)
        if "Exhibit" in t or "#" in t or "Hall" in t:
            location = _clean_text(t)

    # project / slides / poster / pdf 链接（action-buttons）
    project_url = None
    slides_url = None
    poster_url = None
    pdf_url = None

    for a in soup.select(".action-buttons a[href]"):
        href = a["href"].strip()
        text = _clean_text(a.get_text(" ", strip=True)).lower()

        full = urljoin(base_url, href)

        if "project" in text or "project page" in text:
            project_url = full
        # 你样例里 Slides / Poster 是按钮文字
        if "slides" in text:
            slides_url = full
        if "poster" in text:
            poster_url = full
        if "pdf" in text or text in ("paper", "paper pdf"):
            pdf_url = _as_pdf_url(full)

        # 有时通过 class 区分
        cls = " ".join(a.get("class", []))
        if "href_PDF" in cls and not slides_url:
            slides_url = full
        if "href_Poster" in cls and not poster_url:
            poster_url = full

    if not pdf_url:
        meta_pdf = soup.find("meta", attrs={"name": "citation_pdf_url"})
        if meta_pdf and meta_pdf.get("content"):
            pdf_url = _as_pdf_url(urljoin(base_url, meta_pdf["content"].strip()))

    # video（youtube nocookie embed）
    video_url = None
    iframe = soup.select_one('iframe[src*="youtube"]')
    if iframe and iframe.get("src"):
        video_url = iframe["src"].strip()

    return ThecvfItem(
        url=url,
        canonical=canonical,
        title=title.strip() if title else None,
        authors=authors,
        abstract=abstract,
        date_published=date_published,
        date_modified=date_modified,
        event_type=event_type,
        schedule=schedule,
        location=location,
        project_url=project_url,
        slides_url=slides_url,
        poster_url=poster_url,
        pdf_url=pdf_url,
        video_url=video_url,
        image_url=image_url,
        thumbnail_url=thumbnail_url,
    )


def parse_thecvf_openaccess(html: str, url: str) -> ThecvfItem:
    soup = BeautifulSoup(html, "lxml")
    meta_map: Dict[str, List[str]] = {}
    for m in soup.find_all("meta"):
        name = m.get("name")
        content = m.get("content")
        if name and content:
            meta_map.setdefault(name, []).append(content)

    title = (meta_map.get("citation_title") or [None])[0]
    authors = meta_map.get("citation_author", [])
    date_published = (meta_map.get("citation_publication_date") or [None])[0]
    pdf_url = (meta_map.get("citation_pdf_url") or [None])[0]
    pdf_url = _as_pdf_url(urljoin(url, pdf_url) if pdf_url else url)

    abstract = None
    abs_div = soup.select_one("#abstract")
    if abs_div:
        abstract = _clean_text(abs_div.get_text(" ", strip=True))

    return ThecvfItem(
        url=url,
        canonical=url,
        title=title.strip() if title else None,
        authors=[a.strip() for a in authors if a.strip()],
        abstract=abstract,
        date_published=date_published.strip() if date_published else None,
        date_modified=None,
        event_type=None,
        schedule=None,
        location=None,
        project_url=None,
        slides_url=None,
        poster_url=None,
        pdf_url=pdf_url,
        video_url=None,
        image_url=None,
        thumbnail_url=None,
    )


def fetch_thecvf_paper(url: str) -> ThecvfItem:
    html = fetch_html(url)
    if "openaccess.thecvf.com" in url:
        return parse_thecvf_openaccess(html, url)
    return parse_thecvf_virtual_page(html, url)


OPENACCESS_BASE = "https://openaccess.thecvf.com"
ECVA_PAPERS = "https://www.ecva.net/papers.php"
THECVF_VENUES = ("cvpr", "iccv", "eccv", "wacv")


def _parse_openaccess_index(html: str, page_url: str, venue: str, year: int) -> List[dict]:
    soup = BeautifulSoup(html, "lxml")
    items = []
    seen = set()
    for dt in soup.select("dt.ptitle"):
        a = dt.find("a", href=True)
        if not a:
            continue
        paper_url = urljoin(page_url, a["href"].strip())
        if paper_url in seen:
            continue
        seen.add(paper_url)
        title = _clean_text(a.get_text(" ", strip=True))
        authors = []
        pdf_url = None
        dd_authors = dt.find_next_sibling("dd")
        if dd_authors:
            for inp in dd_authors.select('input[name="query_author"]'):
                val = (inp.get("value") or "").strip()
                if val:
                    authors.append(val)
        dd_links = dd_authors.find_next_sibling("dd") if dd_authors else None
        bibtex = None
        if dd_links:
            for link in dd_links.find_all("a", href=True):
                href = link["href"]
                if "supplemental" in href or "-supp" in href:
                    continue
                if "/papers/" in href and href.lower().endswith(".pdf"):
                    pdf_url = urljoin(page_url, href)
                    break
            raw_links = dd_links.get_text("\n", strip=True)
            bib_match = re.search(r"@\w+\s*\{.*", raw_links, flags=re.S)
            if bib_match:
                bibtex = bib_match.group(0).strip()
        if not pdf_url:
            pdf_url = _as_pdf_url(paper_url)
        items.append({
            "url": paper_url,
            "title": title or None,
            "authors": authors,
            "pdf_url": pdf_url,
            "venue": venue,
            "year": year,
            "bibtex": bibtex,
        })
    return items


def _openaccess_list_urls(venue: str, year: int) -> List[str]:
    conf = venue.upper()
    bases = [
        f"{OPENACCESS_BASE}/{conf}{year}",
        f"{OPENACCESS_BASE}/{conf}{year}.py",
    ]
    last_error = None
    for base in bases:
        try:
            html = fetch_html(base, sleep_s=0.4)
        except Exception as e:
            last_error = e
            continue
        soup = BeautifulSoup(html, "lxml")
        all_papers = soup.select_one('a[href*="day=all"]')
        if all_papers and all_papers.get("href"):
            return [urljoin(base, all_papers["href"])]
        if soup.select("dt.ptitle"):
            return [base]
        day_links = []
        for a in soup.select('a[href*="day="]'):
            href = urljoin(base, a["href"])
            if href not in day_links:
                day_links.append(href)
        if day_links:
            return day_links
    raise RuntimeError(f"找不到 {venue.upper()} {year} 的 Open Access 列表页") from last_error


def list_eccv_ecva(year: int) -> List[dict]:
    html = fetch_html(ECVA_PAPERS, sleep_s=1.0)
    soup = BeautifulSoup(html, "lxml")
    token = f"eccv_{year}"
    items = []
    seen = set()
    links = soup.find_all("a", href=True)
    for i, a in enumerate(links):
        href = a["href"]
        if token not in href.lower() or "/html/" not in href:
            continue
        paper_url = urljoin(ECVA_PAPERS, href)
        if paper_url in seen:
            continue
        seen.add(paper_url)
        title = _clean_text(a.get_text(" ", strip=True))
        if not title or title.lower() in ("pdf", "doi"):
            continue
        pdf_url = None
        for b in links[i + 1 : i + 8]:
            h = b.get("href", "")
            text = b.get_text(" ", strip=True).lower()
            if token not in h.lower() or not h.lower().endswith(".pdf"):
                continue
            if "-supp" in h.lower() or "supp" in text or "supplement" in text:
                continue
            pdf_url = urljoin(ECVA_PAPERS, h)
            break
        items.append({
            "url": paper_url,
            "title": title,
            "authors": [],
            "pdf_url": pdf_url,
            "venue": "eccv",
            "year": year,
        })
    return items


def _openaccess_id(url: str) -> str:
    path = urlparse(url).path.rstrip("/")
    name = path.split("/")[-1] if path else url
    if name.endswith(".html"):
        name = name[: -len(".html")]
    return name or url


def _keywords_from_openaccess(html: str) -> List[str]:
    soup = BeautifulSoup(html, "lxml")
    keywords = []
    for meta in soup.find_all("meta"):
        if (meta.get("name") or "").lower() != "citation_keywords":
            continue
        content = (meta.get("content") or "").strip()
        if content:
            keywords.extend(part.strip() for part in re.split(r"\s*[;,]\s*", content) if part.strip())
    return keywords


def crawl_openaccess_metadata(
    venue: str,
    year: int,
    limit: Optional[int],
    existing: Dict[str, dict],
    on_new,
) -> List[dict]:
    """Open Access 列表补 BibTeX，再逐篇补摘要。已有 id 不重复请求。"""
    from fetch_util import is_transient
    from paper_record import bibtex_field, make_record

    papers = list_thecvf_papers(venue, year)
    if limit:
        papers = papers[:limit]
    records = []
    for index, paper in enumerate(papers, 1):
        pid = _openaccess_id(paper.get("url") or "")
        cached = existing.get(pid)
        if cached:
            records.append(cached)
            continue
        abstract = None
        published = None
        keywords: List[str] = []
        paper_url = paper.get("url")
        if paper_url:
            try:
                html = fetch_html(paper_url, timeout=90, sleep_s=0.25)
                detail = parse_thecvf_openaccess(html, paper_url)
                abstract = detail.abstract
                published = detail.date_published
                keywords = _keywords_from_openaccess(html)
            except Exception as exc:
                if is_transient(exc):
                    logger.warning(f"[{index}/{len(papers)}] 暂时失败，下次重试 {paper_url}: {exc}")
                    continue
                logger.warning(f"[{index}/{len(papers)}] 摘要失败 {paper_url}: {exc}")
        bibtex = paper.get("bibtex")
        record = make_record(
            id=pid,
            venue=venue,
            year=year,
            track="main",
            title=paper.get("title"),
            authors=paper.get("authors") or [],
            abstract=abstract,
            keywords=keywords,
            doi=bibtex_field(bibtex, "doi"),
            pages=bibtex_field(bibtex, "pages"),
            bibtex=bibtex,
            url=paper_url,
            pdf_url=paper.get("pdf_url"),
            published=published,
            source="openaccess.thecvf.com",
        )
        records.append(record)
        on_new(record)
        logger.info(f"[{index}/{len(papers)}] {record.get('title')}")
    return records


def list_thecvf_papers(venue: str, year: int) -> List[dict]:
    """按会议+年份列出 Open Access 论文（含 pdf_url），不用 paper_links。"""
    venue = venue.strip().lower()
    if venue not in THECVF_VENUES:
        raise ValueError(f"不支持的 TheCVF 会议: {venue}，可选: {', '.join(THECVF_VENUES)}")
    if venue == "eccv":
        try:
            items = []
            for page_url in _openaccess_list_urls(venue, year):
                items.extend(_parse_openaccess_index(fetch_html(page_url), page_url, venue, year))
            if items:
                return items
        except Exception:
            pass
        return list_eccv_ecva(year)

    items = []
    for page_url in _openaccess_list_urls(venue, year):
        items.extend(_parse_openaccess_index(fetch_html(page_url), page_url, venue, year))
    return items


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="TheCVF / Open Access 论文")
    parser.add_argument("--url", help="单篇 virtual 或 openaccess URL")
    parser.add_argument("-v", "--venue", default="cvpr", help="cvpr / iccv / eccv / wacv")
    parser.add_argument("-y", "--year", type=int, help="年份，列出该年全部论文")
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args()

    if args.url:
        item = fetch_thecvf_paper(args.url)
        print(json.dumps(asdict(item), ensure_ascii=False, indent=2))
    elif args.year:
        papers = list_thecvf_papers(args.venue, args.year)
        if args.limit:
            papers = papers[: args.limit]
        print(json.dumps(papers, ensure_ascii=False, indent=2))
    else:
        item = fetch_thecvf_paper("https://cvpr.thecvf.com/virtual/2025/poster/34787")
        print(json.dumps(asdict(item), ensure_ascii=False, indent=2))
