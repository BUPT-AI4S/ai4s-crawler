import requests

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}
import re
import time
import json
from dataclasses import dataclass, asdict
from typing import List, Optional, Dict
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup


@dataclass
class NeuripsPaper:
    url: str
    title: Optional[str]
    authors: List[str]
    journal: Optional[str]          # citation_journal_title
    volume: Optional[str]           # citation_volume
    publication_date: Optional[str] # citation_publication_date
    doi: Optional[str]              # citation_doi
    firstpage: Optional[str]
    lastpage: Optional[str]
    pdf_url: Optional[str]          # citation_pdf_url
    abstract: Optional[str]
    bibtex_url: Optional[str]       # 页面上的 Bibtex 按钮（相对链接转绝对）


def _clean_text(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def fetch_html(url: str, timeout: int = 30, sleep_s: float = 0.6) -> str:
    r = requests.get(url, headers=headers, timeout=timeout)
    r.raise_for_status()
    time.sleep(sleep_s)
    return r.text

def extract_abstract(soup: BeautifulSoup) -> str | None:
    # A) 优先：class 方式（你原来的）
    node = soup.select_one(".paper-abstract")
    if node:
        txt = _clean_text(node.get_text(" ", strip=True))
        if txt:
            return txt

    # B) 兜底1：找到 “Abstract” 标题所在 section，然后取 section 内第一个 <p>
    for h2 in soup.select("h2.section-label"):
        if _clean_text(h2.get_text()) == "Abstract":
            section = h2.find_parent("section")
            if section:
                p = section.find("p")
                if p:
                    txt = _clean_text(p.get_text(" ", strip=True))
                    if txt:
                        return txt

            # C) 兜底2：取 p 的下一个 <p>（相邻/后继）
            p2 = p.find_next("p")
            if p2:
                txt = _clean_text(p2.get_text(" ", strip=True))
                if txt:
                    return txt
    return None


def parse_neurips_paper(html: str, base_url: str) -> NeuripsPaper:
    soup = BeautifulSoup(html, "lxml")

    # 1) 解析 meta citation_*
    meta_map: Dict[str, List[str]] = {}
    for m in soup.find_all("meta"):
        name = m.get("name")
        content = m.get("content")
        if name and content:
            meta_map.setdefault(name, []).append(content)

    title = (meta_map.get("citation_title") or [None])[0]
    authors = meta_map.get("citation_author", [])
    journal = (meta_map.get("citation_journal_title") or [None])[0]
    volume = (meta_map.get("citation_volume") or [None])[0]
    publication_date = (meta_map.get("citation_publication_date") or [None])[0]
    doi = (meta_map.get("citation_doi") or [None])[0]
    firstpage = (meta_map.get("citation_firstpage") or [None])[0]
    lastpage = (meta_map.get("citation_lastpage") or [None])[0]
    pdf_url = (meta_map.get("citation_pdf_url") or [None])[0]
    pdf_url = urljoin(base_url, pdf_url) if pdf_url else None

    # 2) Abstract：你样例里在 <section> 内，且 class="paper-abstract"
    abstract = extract_abstract(soup)

    # 3) Bibtex 链接：按钮里通常是 /paper_files/paper/xxxxx-/bibtex
    bibtex_url = None
    bib_a = soup.select_one('a[href*="/bibtex"]')
    if bib_a and bib_a.get("href"):
        bibtex_url = urljoin(base_url, bib_a["href"])

    return NeuripsPaper(
        url=base_url,
        title=title.strip() if title else None,
        authors=[a.strip() for a in authors if a.strip()],
        journal=journal.strip() if journal else None,
        volume=volume.strip() if volume else None,
        publication_date=publication_date.strip() if publication_date else None,
        doi=doi.strip() if doi else None,
        firstpage=firstpage.strip() if firstpage else None,
        lastpage=lastpage.strip() if lastpage else None,
        pdf_url=pdf_url,
        abstract=abstract,
        bibtex_url=bibtex_url,
    )


def fetch_neurips_paper(url: str) -> NeuripsPaper:
    html = fetch_html(url)
    return parse_neurips_paper(html, url)


if __name__ == "__main__":
    u = "https://proceedings.neurips.cc/paper_files/paper/2024/hash/07fbde96bee50f4e09303fd4f877c2f3-Abstract.html"
    paper = fetch_neurips_paper(u)
    print(json.dumps(asdict(paper), ensure_ascii=False, indent=2))
