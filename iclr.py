import json
import re
from dataclasses import asdict, dataclass
from typing import List, Optional
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from nips import fetch_html, parse_neurips_paper
from openreview_api import OpenReviewPaper, fetch_openreview_accepted, fetch_openreview_paper

ICLR_VENUE_ID = "ICLR.cc/{year}/Conference"


@dataclass
class IclrPaper:
    url: str
    title: Optional[str]
    authors: List[str]
    journal: Optional[str]
    volume: Optional[str]
    publication_date: Optional[str]
    doi: Optional[str]
    firstpage: Optional[str]
    lastpage: Optional[str]
    pdf_url: Optional[str]
    abstract: Optional[str]
    bibtex_url: Optional[str]
    forum_id: Optional[str] = None
    venueid: Optional[str] = None


def _from_proceedings(url: str) -> IclrPaper:
    paper = parse_neurips_paper(fetch_html(url), url)
    return IclrPaper(
        url=paper.url,
        title=paper.title,
        authors=paper.authors,
        journal=paper.journal,
        volume=paper.volume,
        publication_date=paper.publication_date,
        doi=paper.doi,
        firstpage=paper.firstpage,
        lastpage=paper.lastpage,
        pdf_url=paper.pdf_url,
        abstract=paper.abstract,
        bibtex_url=paper.bibtex_url,
    )


def _from_openreview(paper: OpenReviewPaper) -> IclrPaper:
    return IclrPaper(
        url=paper.url,
        title=paper.title,
        authors=paper.authors,
        journal=paper.venue,
        volume=None,
        publication_date=None,
        doi=None,
        firstpage=None,
        lastpage=None,
        pdf_url=paper.pdf_url,
        abstract=paper.abstract,
        bibtex_url=None,
        forum_id=paper.forum_id,
        venueid=paper.venueid,
    )


def fetch_iclr_paper(url: str) -> IclrPaper:
    if "openreview.net" in url:
        return _from_openreview(fetch_openreview_paper(url))
    return _from_proceedings(url)


def list_iclr_proceedings(year: int) -> List[dict]:
    """从 proceedings.iclr.cc 列出当年论文页（带 camera-ready PDF 链接）。"""
    index_url = f"https://proceedings.iclr.cc/paper_files/paper/{year}"
    html = fetch_html(index_url, sleep_s=1.0)
    soup = BeautifulSoup(html, "lxml")
    items = []
    seen = set()
    for a in soup.select("a[href*='-Abstract']"):
        href = urljoin(index_url, a.get("href", "").strip())
        if href in seen:
            continue
        if not re.search(r"-Abstract(?:-Conference)?\.html$", href):
            continue
        seen.add(href)
        title = re.sub(r"\s+", " ", a.get_text(" ", strip=True)).strip()
        pdf_url = href.replace("/hash/", "/file/").replace("-Abstract", "-Paper")
        pdf_url = re.sub(r"\.html$", ".pdf", pdf_url)
        items.append({"url": href, "title": title or None, "pdf_url": pdf_url, "year": year})
    return items


def list_iclr_openreview(year: int) -> List[IclrPaper]:
    venue_id = ICLR_VENUE_ID.format(year=year)
    return [_from_openreview(p) for p in fetch_openreview_accepted(venue_id)]


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="抓取 ICLR 论文元数据（proceedings 或 OpenReview）")
    parser.add_argument("--url", help="单篇 URL：proceedings.iclr.cc 或 openreview.net")
    parser.add_argument("--year", type=int, help="按年份列出 proceedings 论文")
    parser.add_argument("--openreview", action="store_true", help="按年份从 OpenReview 拉录用稿（需要登录）")
    args = parser.parse_args()

    if args.url:
        paper = fetch_iclr_paper(args.url)
        print(json.dumps(asdict(paper), ensure_ascii=False, indent=2))
    elif args.year and args.openreview:
        papers = list_iclr_openreview(args.year)
        print(json.dumps([asdict(p) for p in papers], ensure_ascii=False, indent=2))
    elif args.year:
        print(json.dumps(list_iclr_proceedings(args.year), ensure_ascii=False, indent=2))
    else:
        u = "https://proceedings.iclr.cc/paper_files/paper/2024/hash/00153f90d9177dd3a872133972bc8dea-Abstract-Conference.html"
        paper = fetch_iclr_paper(u)
        print(json.dumps(asdict(paper), ensure_ascii=False, indent=2))
