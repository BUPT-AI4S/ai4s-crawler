"""CCF 第七版 A/B 会议注册表；等级属于来源，不等同于单篇论文认证。"""
import json
import re
from pathlib import Path

_CONFIG = json.loads(Path(__file__).with_name('ccf_conferences.json').read_text(encoding='utf-8'))
CATALOG_VERSION = _CONFIG['catalog_version']
CONFERENCES = {row['code']: row for row in _CONFIG['conferences']}
CONFERENCES.update({row['code']: row for row in json.loads(
    Path(__file__).with_name('additional_conferences.json').read_text(encoding='utf-8'))['conferences']})
ALIASES = {alias.lower(): code for code, row in CONFERENCES.items() for alias in row['aliases']}
for _code, _row in CONFERENCES.items():
    if _code != 'fse-crypto':
        ALIASES[_row['acronym'].lower()] = _code
GROUPS = {
    'ccf-a': [code for code, row in CONFERENCES.items() if row['rank'] == 'A'],
    'ccf-b': [code for code, row in CONFERENCES.items() if row['rank'] == 'B'],
    'ccf-ab': [code for code, row in CONFERENCES.items() if row['rank'] in ('A', 'B')],
}


def canonical_venue(name: str) -> str:
    raw = name.strip()
    if '/' in raw:
        return raw
    return ALIASES.get(raw.lower(), raw.lower())


def expand_ccf_venues(names: list[str]) -> list[str]:
    result = []
    for name in names:
        key = canonical_venue(name)
        for code in GROUPS.get(key, [key]):
            if code not in result:
                result.append(code)
    return result


def annotate_ccf_record(paper: dict, venue: str) -> dict:
    key = canonical_venue(venue)
    if key not in CONFERENCES:
        return paper
    row = dict(paper)
    config = CONFERENCES[key]
    if config['rank'] not in ('A', 'B'):
        return row
    row.update(ccf_rank=config['rank'], ccf_field=config['field'], ccf_catalog_version=CATALOG_VERSION)
    if not row.get('ccf_paper_status'):
        row['ccf_paper_status'] = 'unverified'
    if re.search(r'\b(?:extended abstract|short paper|short|findings|workshops?|companion|adjunct|demo|poster|doctoral|tutorial)\b',
                 ' '.join(str(row.get(k) or '') for k in ('track', 'article_type', 'dblp_toc')), re.I) or \
            re.search(r'\((?:extended abstract|short paper|demo|poster)\)', str(row.get('title') or ''), re.I):
        row['ccf_paper_status'] = 'excluded'
    return row
