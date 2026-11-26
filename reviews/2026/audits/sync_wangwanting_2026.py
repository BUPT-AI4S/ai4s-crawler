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


def main():
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
