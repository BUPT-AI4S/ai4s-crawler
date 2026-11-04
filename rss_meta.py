"""RSS 2024 official proceedings independent of the DBLP endpoint."""
import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup

from fetch_util import get_text, map_details
from paper_record import make_record

BASE = 'https://www.roboticsproceedings.org/rss20/'


def crawl_rss(limit, existing, on_new):
    if limit is not None and limit <= 0:
        raise ValueError('limit 必须为正整数')
    index = BeautifulSoup(get_text(BASE + 'index.html', timeout=20), 'lxml')
    pages = list(dict.fromkeys(link['href'] for link in index.select('a[href]')
                               if re.fullmatch(r'p\d{3}\.html', link['href'])))
    if len(pages) != 134:
        raise RuntimeError(f'RSS 2024 官网目录应有 134 篇，实际解析 {len(pages)} 篇')

    def detail(name):
        url = urljoin(BASE, name)
        doi = '10.15607/rss.2024.xx.' + name[1:4]
        cached = existing.get(doi)
        if cached and cached.get('abstract') and cached.get('authors'):
            return cached
        html = get_text(url, timeout=20)
        page = BeautifulSoup(html, 'lxml')
        title = page.select_one('meta[name=citation_title][content]')
        authors = [tag['content'] for tag in page.select('meta[name=citation_author][content]')]
        heading = page.find('b', string='Abstract:')
        paragraph = heading.parent.find_next_sibling('p') if heading else None
        abstract = paragraph.get_text(' ', strip=True) if paragraph else ''
        if doi not in html.lower() or not title or not authors or not abstract:
            raise RuntimeError(f'RSS 官网元数据不完整: {url}')
        return make_record(id=doi, doi=doi, title=title['content'], authors=authors,
                           abstract=abstract, venue='rss', venue_type='conference',
                           conference_title='Robotics: Science and Systems', year=2024,
                           url=url, source='www.roboticsproceedings.org',
                           article_type='Conference Paper', screening_status='ready')

    rows = []
    for row in map_details(detail, pages[:limit]):
        rows.append(row)
        on_new(row)
    return rows
