"""Official MLSys proceedings, independent of DBLP indexing."""
from urllib.parse import urljoin, urlparse

from bs4 import BeautifulSoup

from fetch_util import get_text, map_details
from paper_record import make_record


def crawl_mlsys(year, limit, existing, on_new):
    if limit is not None and limit <= 0:
        raise ValueError('limit 必须为正整数')
    base = f'https://proceedings.mlsys.org/paper_files/paper/{year}'
    soup = BeautifulSoup(get_text(base, timeout=20), 'lxml')
    urls = list(dict.fromkeys(
        urljoin(base, link['href']) for link in soup.select('a[href]')
        if link['href'].endswith('-Abstract-Conference.html')
        and urlparse(urljoin(base, link['href'])).hostname == 'proceedings.mlsys.org'
    ))
    if year == 2024 and len(urls) != 37:
        raise RuntimeError(f'MLSys 2024 官网目录应有 37 篇，实际解析 {len(urls)} 篇')
    if not urls:
        raise RuntimeError(f'MLSys {year} 官网目录未解析到论文')

    def detail(url):
        cached = existing.get(url)
        if cached and cached.get('abstract') and cached.get('authors'):
            return cached
        page = BeautifulSoup(get_text(url, timeout=20), 'lxml')
        title = page.select_one('meta[name=citation_title]')
        authors = [tag['content'] for tag in page.select('meta[name=citation_author][content]')]
        heading = page.find('h2', string=lambda value: value and value.strip() == 'Abstract')
        abstract = ' '.join(p.get_text(' ', strip=True)
                            for p in heading.parent.find_all('p')) if heading else ''
        if not title or not title.get('content') or not authors or not abstract:
            raise RuntimeError(f'MLSys 官网元数据不完整: {url}')
        return make_record(id=url, title=title['content'], authors=authors, abstract=abstract,
                           venue='mlsys', venue_type='conference', year=year,
                           conference_title='Conference on Machine Learning and Systems',
                           url=url, source='proceedings.mlsys.org',
                           article_type='Conference Paper', screening_status='ready')

    rows = []
    for row in map_details(detail, urls[:limit]):
        rows.append(row)
        on_new(row)
    return rows
