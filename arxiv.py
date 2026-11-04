import requests

cookies = {
    'arxiv_labs': '{%22sameSite%22:%22strict%22%2C%22expires%22:365}',
}

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-CN,zh;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6',
    'cache-control': 'max-age=0',
    'priority': 'u=0, i',
    'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'cross-site',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
    # 'cookie': 'arxiv_labs={%22sameSite%22:%22strict%22%2C%22expires%22:365}',
}
import re
import time
import json
from dataclasses import dataclass, asdict
from typing import List, Optional, Dict

import requests
from bs4 import BeautifulSoup


@dataclass
class ArxivPaper:
    arxiv_id: Optional[str]
    url: str
    title: Optional[str]
    authors: List[str]
    abstract: Optional[str]
    date: Optional[str]          # citation_date，如 2025/10/09
    pdf_url: Optional[str]
    doi: Optional[str]           # 页面里通常有 DataCite DOI: 10.48550/arXiv.xxxx


def _clean_text(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def fetch_html(url: str, timeout: int = 30, sleep_s: float = 0.8) -> str:
    r = requests.get(url, headers=headers, timeout=timeout, allow_redirects=True)
    r.raise_for_status()
    time.sleep(sleep_s)
    return r.text


def parse_arxiv_abs(html: str, url: str) -> ArxivPaper:
    soup = BeautifulSoup(html, "lxml")

    # 1) meta citation_*（首选）
    meta_map: Dict[str, List[str]] = {}
    for m in soup.find_all("meta"):
        name = m.get("name")
        content = m.get("content")
        if name and content:
            meta_map.setdefault(name, []).append(content)

    title = (meta_map.get("citation_title") or [None])[0]
    authors = meta_map.get("citation_author", [])
    abstract = (meta_map.get("citation_abstract") or [None])[0]
    date = (meta_map.get("citation_date") or [None])[0]
    pdf_url = (meta_map.get("citation_pdf_url") or [None])[0]
    arxiv_id = (meta_map.get("citation_arxiv_id") or [None])[0]

    # 2) DOI：页面正文里一般有 <a id="arxiv-doi-link" href="https://doi.org/10.48550/arXiv.2510.08177">
    doi = None
    doi_a = soup.select_one("#arxiv-doi-link")
    if doi_a and doi_a.get("href"):
        # 把 https://doi.org/xxx 转成 xxx
        m = re.search(r"doi\.org/(.+)$", doi_a["href"])
        doi = m.group(1) if m else doi_a["href"]

    # 3) 兜底：若 meta 没有 abstract，可从 blockquote.abstract 取
    if not abstract:
        abs_block = soup.select_one("blockquote.abstract")
        if abs_block:
            text = abs_block.get_text(" ", strip=True)
            text = re.sub(r"^Abstract:\s*", "", text).strip()
            abstract = _clean_text(text) if text else None

    # 4) 兜底：若 meta 没有作者，可从 div.authors a 取
    if not authors:
        author_links = soup.select("div.authors a")
        authors = [_clean_text(a.get_text()) for a in author_links if a.get_text(strip=True)]

    # 5) 兜底：若 meta 没有 title，可从 h1.title 取
    if not title:
        h1 = soup.select_one("h1.title")
        if h1:
            text = h1.get_text(" ", strip=True)
            text = re.sub(r"^Title:\s*", "", text).strip()
            title = _clean_text(text) if text else None

    return ArxivPaper(
        arxiv_id=arxiv_id.strip() if arxiv_id else None,
        url=url,
        title=title.strip() if title else None,
        authors=[a.strip() for a in authors if a.strip()],
        abstract=_clean_text(abstract) if abstract else None,
        date=date.strip() if date else None,
        pdf_url=pdf_url.strip() if pdf_url else None,
        doi=doi.strip() if doi else None,
    )


def fetch_arxiv_paper(abs_url_or_id: str) -> ArxivPaper:
    # 允许传入 "2510.08177" 或 "https://arxiv.org/abs/2510.08177"
    if abs_url_or_id.startswith("http"):
        url = abs_url_or_id
    else:
        url = f"https://arxiv.org/abs/{abs_url_or_id}"

    html = fetch_html(url)
    return parse_arxiv_abs(html, url)


if __name__ == "__main__":
    p = fetch_arxiv_paper("https://arxiv.org/abs/2510.08177")
    print(json.dumps(asdict(p), ensure_ascii=False, indent=2))
