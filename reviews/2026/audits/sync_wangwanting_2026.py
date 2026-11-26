"""Idempotently sync verified Wang Wanting 2026 review additions to candidate/source data.

The yearly candidate file is too large for the GitHub web uploader. This small,
review-scoped job runs in the repository's existing action-list workflow.
"""

import copy
import json
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
YEAR = 2026
REVIEW = ROOT / 'reviews/2026/Blueblue1101.json'
AGGREGATE = ROOT / 'metadata/2026/ai4s.json'


def key(p):
    return (p['venue'], p['year'], p['id'].lower())


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def write(path, records, compact=False):
    if compact:
        body = '[\n' + ',\n'.join(json.dumps(p, ensure_ascii=False, separators=(',', ':')) for p in records) + '\n]\n'
    else:
        body = json.dumps(records, ensure_ascii=False, indent=2) + '\n'
    path.write_text(body, encoding='utf-8')


def ensure_nprot_review():
    """Retain publisher-verified source omissions and explicit owner decisions."""
    audit = read(ROOT / 'reviews/2026/audits/wangwanting-2026-nprot-official-catalogue.json')
    papers = audit['new_articles']
    catalogue_ids = [x['doi'].lower() for x in audit['official_catalogue']]
    if (len(catalogue_ids) != 172 or len(set(catalogue_ids)) != 171
            or catalogue_ids.count('10.1038/s41596-026-01418-x') != 2
            or len(papers) != 11):
        raise RuntimeError('Nature Protocols catalogue changed; review the discrepancy')
    review = read(REVIEW)
    old = {key(p) for p in review}
    changed = False
    for item in papers:
        doi = item['doi'].lower()
        k = ('nprot', YEAR, doi)
        if k in old:
            continue
        paper = {
            'id': doi, 'venue': 'nprot', 'year': YEAR, 'track': None,
            'title': item['title'], 'authors': item['authors'],
            'author_ids': [], 'abstract': item['abstract'], 'keywords': [],
            'doi': doi, 'url': item['url'], 'pdf_url': item['url'] + '.pdf',
            'published': item['date'], 'source': 'nature.com',
            'venue_type': 'journal', 'journal_title': 'Nature Protocols',
            'issn': '1750-2799', 'article_type': item['article_type'],
            'screening_status': 'ready' if item['abstract'] else 'needs_abstract',
            'ai4s_review': {
                'schema_version': 2, 'batch_id': 'wangwanting-2026-nprot-catalogue-20261126',
                'owner': '王婉婷', 'snapshot_at': audit['checked_at'],
                'decision': 'exclude', 'rationale': item['screening_rationale'],
                'verified_metadata': {'url': item['url'], 'doi': doi,
                                      'article_type': item['article_type'],
                                      'evidence_urls': [item['url'], audit['official_url']],
                                      'checked_at': audit['checked_at']},
                'tags': [],
            },
        }
        review.append(paper)
        old.add(k)
        changed = True
    if changed:
        write(REVIEW, review)

    path = ROOT / 'reviews/2026/feedback/Blueblue1101.json'
    feedback = read(path)
    row = next(x for x in feedback if x['source_code'] == 'nprot')
    row['official_total'] = 172
    row['official_scope'] = 'Nature Protocols 官网 articles?year=2026，2026-11-26 在线发表目录172行，重复 DOI 10.1038/s41596-026-01418-x 一次，去重后171篇；另加官网独立可核实的2026更正页 DOI 10.1038/s41596-026-01462-7 一篇，同口径唯一正式页面共172篇。'
    row['coverage_note'] = '目录171个唯一DOI，原逐源书目161条；目录11条漏采已逐篇按原摘要和类型审核补录。原书目额外一条更正公告经官网正式页面核实，因此补录后的逐源书目172条与可核实正式页面集合一致。年度快照仍需同步。候选6篇均已审。'
    row['evidence_urls'] = list(dict.fromkeys(row['evidence_urls'] + [audit['official_url']] + [x['url'] for x in papers]))
    row['issues'] = ['年度快照仍为旧版本，待与补录后的逐源书目同步对账。']
    row['next_actions'] = ['按172个官网可核实正式页面口径完成年度快照同步。']
    write(path, feedback)


def ensure_cell_discovery_review():
    """Record four verified publisher omissions, including one highlight."""
    audit = read(ROOT / 'reviews/2026/audits/wangwanting-2026-cell-discovery-catalogue.json')
    catalog = audit['official_catalogue']
    papers = audit['new_articles']
    ids = [x['doi'].lower() for x in catalog]
    if len(ids) != 82 or len(set(ids)) != 82 or len(papers) != 4:
        raise RuntimeError('Cell Discovery catalogue changed; review the discrepancy')
    review = read(REVIEW)
    old = {key(p) for p in review}
    changed = False
    for item in papers:
        doi = item['doi'].lower()
        if doi not in ids or item['article_type'] not in ('Article', 'Research Highlight'):
            raise RuntimeError(f'Unverified Cell Discovery article: {doi}')
        k = ('nature-celldisc', YEAR, doi)
        if k in old:
            continue
        paper = {
            'id': doi, 'venue': 'nature-celldisc', 'year': YEAR, 'track': None,
            'title': item['title'], 'authors': item['authors'],
            'author_ids': [], 'abstract': item['abstract'], 'keywords': [],
            'doi': doi, 'url': item['url'], 'pdf_url': item['url'] + '.pdf',
            'published': item['date'], 'source': 'nature.com',
            'venue_type': 'journal', 'journal_title': 'Cell Discovery',
            'issn': '2056-5968', 'article_type': item['article_type'],
            'screening_status': 'ready' if item['abstract'] else 'non_research_no_abstract',
            'ai4s_review': {
                'schema_version': 2, 'batch_id': 'wangwanting-2026-cell-discovery-catalogue-20261126',
                'owner': '王婉婷', 'snapshot_at': audit['checked_at'],
                'decision': 'exclude', 'rationale': item['screening_rationale'],
                'verified_metadata': {'url': item['url'], 'doi': doi,
                                      'article_type': item['article_type'],
                                      'evidence_urls': [item['url'], audit['official_url']],
                                      'checked_at': audit['checked_at']},
                'tags': [],
            },
        }
        review.append(paper)
        old.add(k)
        changed = True
    if changed:
        write(REVIEW, review)

    path = ROOT / 'reviews/2026/feedback/Blueblue1101.json'
    feedback = read(path)
    row = next(x for x in feedback if x['source_code'] == 'nature-celldisc')
    row['official_total'] = 82
    row['official_scope'] = 'Cell Discovery 官网 articles?year=2026，2026-11-26 在线发表目录5页82个唯一 DOI，包含 Article 与 Research Highlight。'
    row['coverage_note'] = '官网82篇，原逐源书目78篇；4篇漏采按官网原摘要与文章类型逐篇核实，3篇实验生物学研究与1篇 Research Highlight 均排除；补录后逐源书目82篇。原5篇候选结论保留。年度快照仍需同步。'
    row['evidence_urls'] = list(dict.fromkeys(row['evidence_urls'] + [audit['official_url']] + [x['url'] for x in papers]))
    row['issues'] = ['年度快照仍为旧版本，待与补录后的逐源书目同步对账。', '原有5篇候选的正式元数据仍需逐篇在线复核。']
    row['next_actions'] = ['按82个官网唯一 DOI 口径完成年度快照同步。', '逐篇复核原有候选正式元数据。']
    write(path, feedback)


def main():
    ensure_nprot_review()
    ensure_cell_discovery_review()
    review = read(REVIEW)
    candidate = read(AGGREGATE)
    by_key = {key(p): p for p in candidate}
    # The annual aggregate already contains three unrelated ECCV duplicate keys.
    # Preserve them as-is and enforce uniqueness only for the review keys touched here.

    additions = defaultdict(list)
    markers = defaultdict(list)
    source_backfills = defaultdict(list)
    for paper in review:
        rv = paper.get('ai4s_review') or {}
        if paper['year'] != YEAR or rv.get('owner') != '王婉婷':
            continue
        k = key(paper)
        if rv.get('batch_id') == 'wangwanting-2026-npjscilearn-catalog-20261119':
            # An official catalogue comparison found two source omissions. Only
            # one is AI4S; both belong in the source bibliography.
            if not paper.get('abstract') or not rv.get('verified_metadata', {}).get('url'):
                raise RuntimeError(f'Catalogue backfill lacks publisher evidence: {k}')
            source_backfills[paper['venue']].append(
                {name: copy.deepcopy(value) for name, value in paper.items() if name != 'ai4s_review'}
            )
        marker = rv.get('abstract_requirement')
        if marker and rv.get('decision') == 'exclude':
            if marker.get('status') != 'not_required' or not marker.get('evidence_urls'):
                raise RuntimeError(f'Incomplete abstract requirement for {k}')
            markers[paper['venue']].append((k, marker))
            if k not in by_key:
                raise RuntimeError(f'Existing excluded candidate missing: {k}')
            by_key[k]['abstract_requirement'] = copy.deepcopy(marker)
        if rv.get('decision') != 'include' or k in by_key:
            continue
        abstract = paper.get('abstract') or rv.get('verified_metadata', {}).get('abstract')
        if not abstract or len(abstract) < 80:
            raise RuntimeError(f'Inclusion has no verified original abstract: {k}')
        plain = {name: copy.deepcopy(value) for name, value in paper.items() if name != 'ai4s_review'}
        plain['abstract'] = abstract
        plain['screening_status'] = 'ready'
        additions[paper['venue']].append(plain)
        by_key[k] = plain
        candidate.append(plain)

    # Older official directory comparisons were audited before the source
    # bibliography could be uploaded through GitHub. Complete those two source
    # catalogues from the exact publisher-verified review records.
    cvpr_recovered = read(ROOT / 'reviews/2026/audits/wangwanting-2026-cvpr-recovered.json')
    for evidence in cvpr_recovered:
        matched = [p for p in review if p['venue'] == 'cvpr' and p.get('url') == evidence['url']]
        if len(matched) != 1 or matched[0].get('abstract') != evidence['abstract']:
            raise RuntimeError(f'CVPR catalogue evidence mismatch: {evidence["url"]}')
        source_backfills['cvpr'].append(
            {name: copy.deepcopy(value) for name, value in matched[0].items() if name != 'ai4s_review'}
        )
    ecai_gap = read(ROOT / 'reviews/2026/audits/wangwanting-2026-ecai-catalogue-diff.json')
    for evidence in ecai_gap['missing']:
        doi = '10.24963/ijcai.2026/' + evidence['id'].removeprefix('paper')
        matched = [p for p in review if p['venue'] == 'ecai' and p.get('id', '').lower() == doi]
        if len(matched) != 1 or not matched[0].get('abstract'):
            raise RuntimeError(f'IJCAI-ECAI catalogue evidence mismatch: {doi}')
        source_backfills['ecai'].append(
            {name: copy.deepcopy(value) for name, value in matched[0].items() if name != 'ai4s_review'}
        )
    nature_gap = read(ROOT / 'reviews/2026/audits/wangwanting-2026-natcomputsci-official-seven.json')
    for evidence in nature_gap['new_articles']:
        doi = evidence['doi'].lower()
        matched = [p for p in review if p['venue'] == 'natcomputsci' and p.get('id', '').lower() == doi]
        if len(matched) != 1 or matched[0].get('title') != evidence['title']:
            raise RuntimeError(f'Nature Computational Science catalogue mismatch: {doi}')
        source_backfills['natcomputsci'].append(
            {name: copy.deepcopy(value) for name, value in matched[0].items() if name != 'ai4s_review'}
        )

    sle_gap = read(ROOT / 'reviews/2026/audits/wangwanting-2026-smart-learning-catalogue.json')
    for evidence in sle_gap['new_articles']:
        doi = evidence['doi'].lower()
        matched = [p for p in review if p['venue'] == 'j-f28cf1469d' and p.get('id', '').lower() == doi]
        if len(matched) != 1 or matched[0].get('title') != evidence['title'] or not matched[0].get('abstract'):
            raise RuntimeError(f'Smart Learning Environments catalogue mismatch: {doi}')
        source_backfills['j-f28cf1469d'].append(
            {name: copy.deepcopy(value) for name, value in matched[0].items() if name != 'ai4s_review'}
        )

    mnd_gap = read(ROOT / 'reviews/2026/audits/wangwanting-2026-molecular-neurodegeneration-catalogue.json')
    for evidence in mnd_gap['new_articles']:
        doi = evidence['id'].lower()
        matched = [p for p in review if p['venue'] == 'j-9596fa43cd' and p.get('id', '').lower() == doi]
        if (len(matched) != 1 or matched[0].get('title') != evidence['title']
                or matched[0].get('abstract') != evidence['abstract']):
            raise RuntimeError(f'Molecular Neurodegeneration catalogue mismatch: {doi}')
        source_backfills['j-9596fa43cd'].append(
            {name: copy.deepcopy(value) for name, value in matched[0].items() if name != 'ai4s_review'}
        )

    sci_gap = read(ROOT / 'reviews/2026/audits/wangwanting-2026-science-immunology-catalogue.json')
    for evidence in sci_gap['new_articles']:
        doi = evidence['id'].lower()
        matched = [p for p in review if p['venue'] == 'j-3d73a601f6' and p.get('id', '').lower() == doi]
        if (len(matched) != 1 or matched[0].get('title') != evidence['title']
                or matched[0].get('abstract') != evidence['abstract']
                or matched[0].get('ai4s_review', {}).get('decision') != 'exclude'):
            raise RuntimeError(f'Science Immunology catalogue mismatch: {doi}')
        source_backfills['j-3d73a601f6'].append(
            {name: copy.deepcopy(value) for name, value in matched[0].items() if name != 'ai4s_review'}
        )

    nprot_gap = read(ROOT / 'reviews/2026/audits/wangwanting-2026-nprot-official-catalogue.json')
    for evidence in nprot_gap['new_articles']:
        doi = evidence['doi'].lower()
        matched = [p for p in review if p['venue'] == 'nprot' and p.get('id', '').lower() == doi]
        if (len(matched) != 1 or matched[0].get('title') != evidence['title']
                or matched[0].get('abstract') != evidence['abstract']
                or matched[0].get('ai4s_review', {}).get('decision') != 'exclude'):
            raise RuntimeError(f'Nature Protocols catalogue mismatch: {doi}')
        source_backfills['nprot'].append(
            {name: copy.deepcopy(value) for name, value in matched[0].items() if name != 'ai4s_review'}
        )

    cd_gap = read(ROOT / 'reviews/2026/audits/wangwanting-2026-cell-discovery-catalogue.json')
    for evidence in cd_gap['new_articles']:
        doi = evidence['doi'].lower()
        matched = [p for p in review if p['venue'] == 'nature-celldisc' and p.get('id', '').lower() == doi]
        if (len(matched) != 1 or matched[0].get('title') != evidence['title']
                or matched[0].get('abstract') != evidence['abstract']
                or matched[0].get('ai4s_review', {}).get('decision') != 'exclude'):
            raise RuntimeError(f'Cell Discovery catalogue mismatch: {doi}')
        source_backfills['nature-celldisc'].append(
            {name: copy.deepcopy(value) for name, value in matched[0].items() if name != 'ai4s_review'}
        )

    if sum(map(len, markers.values())) != 6:
        raise RuntimeError('Expected six reviewed non-research abstract exceptions')

    # Source files are explicitly checked out in the workflow. Keep their original
    # records and modify only the exact reviewed keys, then add verified omissions.
    updated = Counter()
    for source in sorted(set(additions) | set(markers) | set(source_backfills)):
        base = ROOT / 'metadata' / source / str(YEAR)
        for filename in ('papers.json', 'ai4s.json'):
            path = base / filename
            if not path.is_file():
                raise RuntimeError(f'Missing sparse-checkout source file: {path}')
            records = read(path)
            lookup = {key(x): x for x in records}
            changed = False
            for k, marker in markers[source]:
                if k in lookup and lookup[k].get('abstract_requirement') != marker:
                    lookup[k]['abstract_requirement'] = copy.deepcopy(marker)
                    changed = True
            for plain in additions[source]:
                k = key(plain)
                if k in lookup:
                    if not lookup[k].get('abstract'):
                        lookup[k]['abstract'] = plain['abstract']
                        lookup[k]['screening_status'] = 'ready'
                        changed = True
                    if lookup[k].get('article_type') in (None, '', 'unknown') and plain.get('article_type') not in (None, '', 'unknown'):
                        lookup[k]['article_type'] = plain['article_type']
                        changed = True
                else:
                    records.append(copy.deepcopy(plain))
                    lookup[k] = records[-1]
                    changed = True
            if filename == 'papers.json':
                for plain in source_backfills[source]:
                    k = key(plain)
                    if k not in lookup:
                        records.append(copy.deepcopy(plain))
                        lookup[k] = records[-1]
                        changed = True
            if changed:
                write(path, records)
                updated[filename] += 1

    annual_changed = sum(map(len, additions.values())) > 0
    # Existing six candidate records may gain markers without new additions.
    if annual_changed or markers:
        write(AGGREGATE, candidate, compact=True)

    print(json.dumps({'candidate_total': len(candidate), 'new_inclusions': sum(map(len, additions.values())),
                      'official_catalog_source_backfills': sum(map(len, source_backfills.values())),
                      'non_research_markers': sum(map(len, markers.values())),
                      'changed_source_files': updated}, ensure_ascii=False))


if __name__ == '__main__':
    main()
