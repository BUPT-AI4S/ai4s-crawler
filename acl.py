import requests

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'If-Modified-Since': 'Tue, 03 Feb 2026 00:11:13 GMT',
    'If-None-Match': '"8e3d-649e0470fd90f-gzip"',
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
from typing import List, Optional, Dict, Any

import requests
from bs4 import BeautifulSoup


@dataclass
class AclPaper:
    anthology_id: Optional[str]
    url: str
    title: Optional[str]
    authors: List[str]
    venue: Optional[str]
    publication_date: Optional[str]
    doi: Optional[str]
    pdf_url: Optional[str]
    abstract: Optional[str]


def _clean_text(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def fetch_html(url: str, timeout: int = 30, sleep_s: float = 0.8) -> str:
    r = requests.get(url, headers=headers, timeout=timeout)
    r.raise_for_status()
    time.sleep(sleep_s)  # 友好一点，避免过快请求
    return r.text


def parse_paper_page(html: str, url: str) -> AclPaper:
    soup = BeautifulSoup(html, "lxml")

    # 1) 优先从 meta citation_* 取（稳定）
    metas = soup.find_all("meta")
    meta_map: Dict[str, List[str]] = {}
    for m in metas:
        name = m.get("name")
        content = m.get("content")
        if name and content:
            meta_map.setdefault(name, []).append(content)

    title = (meta_map.get("citation_title") or [None])[0]
    authors = meta_map.get("citation_author", [])  # 可能多个 meta 同名
    venue = (meta_map.get("citation_conference_title") or [None])[0]
    publication_date = (meta_map.get("citation_publication_date") or [None])[0]
    doi = (meta_map.get("citation_doi") or [None])[0]
    pdf_url = (meta_map.get("citation_pdf_url") or [None])[0]

    # 2) Anthology ID：页面里通常有 <dd>2025.acl-long.387</dd> 或 JS paper_params
    anthology_id = None
    # 从页面中找 "Anthology ID:" 对应的 dd
    for dt in soup.find_all("dt"):
        if _clean_text(dt.get_text()) == "Anthology ID:":
            dd = dt.find_next_sibling("dd")
            if dd:
                anthology_id = _clean_text(dd.get_text())
            break

    # 3) Abstract：页面正文里有 <div class="card-body acl-abstract"> ... <span>ABSTRACT</span>
    abstract = None
    abs_div = soup.select_one("div.card-body.acl-abstract span")
    if abs_div and abs_div.get_text(strip=True):
        abstract = _clean_text(abs_div.get_text(" ", strip=True))
    else:
        # 兜底：有些页会把 abstract 放在 BibTeX 或 JS paper_params 里
        # a) BibTeX 里通常含 abstract = "..."
        bib = soup.select_one("#citeBibtexContent")
        if bib:
            m = re.search(r'abstract\s*=\s*[{"](.+?)[}"],\s*$', bib.get_text("\n"), flags=re.M | re.S)
            if m:
                abstract = _clean_text(m.group(1))

        # b) JS paper_params = { ... abstract: "..." }
        if abstract is None:
            scripts_text = "\n".join(s.get_text("\n") for s in soup.find_all("script"))
            m2 = re.search(r'paper_params\s*=\s*\{.*?abstract:\s*"(.+?)"\s*\}', scripts_text, flags=re.S)
            if m2:
                abstract = _clean_text(m2.group(1))

    if abstract and ("paper_params" in abstract or "function showMetadataDialog" in abstract):
        abstract = None

    return AclPaper(
        anthology_id=anthology_id,
        url=url,
        title=title.strip() if title else None,
        authors=[a.strip() for a in authors if a.strip()],
        venue=venue.strip() if venue else None,
        publication_date=publication_date.strip() if publication_date else None,
        doi=doi.strip() if doi else None,
        pdf_url=pdf_url.strip() if pdf_url else None,
        abstract=abstract,
    )


def fetch_acl_paper(url: str) -> AclPaper:
    html = fetch_html(url)
    return parse_paper_page(html, url)

def main():
    paper = fetch_acl_paper("https://aclanthology.org/2025.acl-long.387/")
    print(json.dumps(asdict(paper), ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
