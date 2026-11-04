"""DOI-matched public abstract fallbacks for journal and conference pages."""
import html
import re
import xml.etree.ElementTree as ET

from loguru import logger

from fetch_util import get_json, get_text
from kdd_meta import _doi_key, _strip_jats, semantic_scholar_abstracts
from paper_record import norm_space

PUBMED = 'https://eutils.ncbi.nlm.nih.gov/entrez/eutils/'
OPENAIRE = 'https://api.openaire.eu/search/publications'
OPENAIRE_BATCH = 50
OPENAIRE_BATCH_MIN = 10
OPENAIRE_MAX_RESULTS = 100
_HTML_TAG = re.compile(r'<[^>]+>')


def europe_pmc_abstracts(dois):
    keys = [doi for doi in dois if re.fullmatch(r'10\.\d+/[^"\\\s]+', doi)]
    found = {}
    for start in range(0, len(keys), 25):
        batch = keys[start:start + 25]
        try:
            data = get_json(
                'https://www.ebi.ac.uk/europepmc/webservices/rest/search',
                params={'query': '(' + ' OR '.join(f'DOI:"{doi}"' for doi in batch)
                        + ') AND HAS_ABSTRACT:y',
                        'format': 'json', 'resultType': 'core', 'pageSize': 100},
                timeout=15, retries=1, sleep_s=0,
            )
        except Exception as exc:
            logger.warning(f'Europe PMC 摘要查询中断: {exc}')
            break
        for record in data.get('resultList', {}).get('result', []):
            doi = _doi_key(record.get('doi'))
            abstract = _strip_jats(record.get('abstractText'))
            if doi in batch and abstract:
                found.setdefault(doi, abstract)
    return found


def pubmed_abstracts(dois):
    keys = [doi for doi in dois if re.fullmatch(r'10\.\d+/[^"\\\s]+', doi)]
    found = {}
    for start in range(0, len(keys), 25):
        batch = keys[start:start + 25]
        try:
            search = get_json(
                PUBMED + 'esearch.fcgi',
                params={'db': 'pubmed', 'retmode': 'json', 'retmax': 100,
                        'term': ' OR '.join(f'"{doi}"[AID]' for doi in batch)},
                timeout=12, retries=1, sleep_s=0,
            )
            result = search.get('esearchresult', {})
            ids = result.get('idlist')
            if not isinstance(ids, list):
                raise ValueError('PubMed ESearch 响应缺少有效 idlist，本批保留待重试')
            if not ids:
                continue
            xml = get_text(PUBMED + 'efetch.fcgi',
                           params={'db': 'pubmed', 'retmode': 'xml', 'id': ','.join(ids)},
                           timeout=12, retries=1, sleep_s=0)
            articles = ET.fromstring(xml).findall('PubmedArticle')
        except Exception as exc:
            logger.warning(f'PubMed 批量摘要查询中断: {exc}')
            break
        for article in articles:
            doi = _doi_key(article.findtext('PubmedData/ArticleIdList/ArticleId[@IdType="doi"]'))
            if doi not in batch:
                continue
            parts = []
            for section in article.findall('MedlineCitation/Article/Abstract/AbstractText'):
                content = norm_space(''.join(section.itertext()))
                if content:
                    label = section.get('Label')
                    parts.append(f'{label}: {content}' if label else content)
            if parts:
                found.setdefault(doi, ' '.join(parts))
    return found


def _openaire_text(value):
    """OpenAIRE 的 description 常带 JATS/HTML 片段，先还原实体再压平空白。"""
    return norm_space(html.unescape(_HTML_TAG.sub(' ', value or '')))


def _openaire_entities(data):
    response = (data or {}).get('response') or {}
    results = ((response.get('results') or {}).get('result')) or []
    for item in results:
        entity = (((item or {}).get('metadata') or {}).get('oaf:entity') or {}).get('oaf:result')
        if isinstance(entity, dict):
            yield entity


def _openaire_abstracts_of(batch):
    params = [('format', 'json'), ('size', str(OPENAIRE_MAX_RESULTS))]
    params.extend(('doi', doi) for doi in batch)
    data = get_json(OPENAIRE, params=params, timeout=40, retries=1, sleep_s=0)
    found = {}
    for entity in _openaire_entities(data):
        pids = entity.get('pid')
        doi = ''
        for pid in (pids if isinstance(pids, list) else [pids]):
            if isinstance(pid, dict) and pid.get('@classid') == 'doi':
                doi = _doi_key(pid.get('$'))
                break
        if doi not in batch:
            continue
        descriptions = entity.get('description')
        for item in (descriptions if isinstance(descriptions, list) else [descriptions]):
            if not isinstance(item, dict):
                continue
            abstract = _openaire_text(item.get('$'))
            if len(abstract) > 200:
                found.setdefault(doi, abstract)
                break
    return found


def openaire_abstracts(dois):
    """OpenAIRE 聚合机构库 green OA 副本，可补 Crossref/出版社缺失的 Elsevier 摘要。"""
    keys = [doi for doi in dois if re.fullmatch(r'10\.\d+/[^"\\\s]+', doi)]
    found = {}
    queue = [keys[start:start + OPENAIRE_BATCH] for start in range(0, len(keys), OPENAIRE_BATCH)]
    while queue:
        batch = queue.pop(0)
        try:
            found.update(_openaire_abstracts_of(batch))
        except Exception as exc:
            if len(batch) > OPENAIRE_BATCH_MIN:
                # 超长 doi 列表会触发 HTTP 409，折半重试而不是整条链路作废。
                half = len(batch) // 2
                queue[:0] = [batch[:half], batch[half:]]
                continue
            logger.warning(f'OpenAIRE 摘要查询中断: {exc}')
            break
    return found


def fill_abstracts(dois, openalex, include_openaire=False):
    """按 openalex → 欧洲PMC → PubMed →(可选)OpenAIRE → Semantic Scholar 顺序补齐摘要。

    OpenAIRE 每条查询要 5–30 秒且响应可达数 MB，只对摘要缺口集中的期刊链路开启。
    """
    remaining = list(dict.fromkeys(key for doi in dois if (key := _doi_key(doi))))
    results = {}
    lookups = [('openalex.org', openalex), ('europepmc.org', europe_pmc_abstracts),
               ('pubmed.ncbi.nlm.nih.gov', pubmed_abstracts)]
    if include_openaire:
        lookups.append(('openaire.eu', openaire_abstracts))
    lookups.append(('semanticscholar.org', semantic_scholar_abstracts))
    for host, lookup in lookups:
        if not remaining:
            break
        try:
            abstracts = lookup(remaining)
        except Exception as exc:
            logger.warning(f'{host} 批量摘要查询中断: {exc}')
            continue
        for doi in remaining:
            if abstracts.get(doi):
                results[doi] = abstracts[doi], host
        remaining = [doi for doi in remaining if doi not in results]
    return results
