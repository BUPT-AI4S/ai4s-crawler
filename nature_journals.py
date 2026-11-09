"""Nature 来源注册表。目录快照来自官方 siteindex，不按刊名猜测 URL。"""
import json
import re
from functools import lru_cache
from pathlib import Path

from bs4 import BeautifulSoup

from fetch_util import get_text

_CONFIG = json.loads(Path(__file__).with_name('nature_journals.json').read_text(encoding='utf-8'))
JOURNALS = {row['slug']: row for row in _CONFIG['journals']}
_NATURE_KEYS = set(JOURNALS)
JOURNALS.update({row['slug']: row for row in json.loads(
    Path(__file__).with_name('additional_journals.json').read_text(encoding='utf-8'))['journals']})
ALIASES = {'ncs': 'natcomputsci', 'nmi': 'natmachintell', 'nc': 'ncomms', 'natcomm': 'ncomms'}
for _key, _journal in JOURNALS.items():
    ALIASES[re.sub(r'[^a-z0-9]+', '-', _journal['title'].lower()).strip('-')] = _key

GROUPS = {f'nature-{series}': [k for k, row in JOURNALS.items() if row['series'] == series]
          for series in {row['series'] for row in JOURNALS.values()}}
GROUPS['nature-all'] = [key for key in JOURNALS if key in _NATURE_KEYS]
GROUPS['nature-core'] = ['nature', 'ncomms', 'natcomputsci', 'natmachintell', 'nmeth',
                         'sdata', 'npjcompumats', 'npjdigitalmed']


def expand_venues(venues: list[str]) -> list[str]:
    result = []
    for name in venues:
        key = name.strip() if '/' in name else name.strip().lower()
        for item in GROUPS.get(key, [ALIASES.get(key, key)]):
            if item not in result:
                result.append(item)
    return result


def parse_issn(html: str) -> str:
    soup = BeautifulSoup(html, 'lxml')
    for name in ('prism.issn', 'citation_issn'):
        meta = soup.find('meta', attrs={'name': name})
        match = re.search(r'\b\d{4}-\d{3}[\dX]\b', meta.get('content', '')) if meta else None
        if match:
            return match.group()
    text = soup.get_text(' ', strip=True)
    match = re.search(r'ISSN\s*(?:\([^)]*\)\s*)?(\d{4}-\d{3}[\dX])\s*\(online\)', text, re.I)
    if not match:
        raise ValueError('Nature 页面中未找到期刊 ISSN，可能遇到拦截或页面结构变化')
    return match.group(1)


@lru_cache(maxsize=None)
def resolve_issn(venue: str) -> str:
    return parse_issn(get_text(JOURNALS[venue]['homepage']))
