"""Reconcile publisher-audited Wang Wanting sources with the 2026 LFS annual file.

Run only with the complete annual papers.json fetched by Git LFS. This script
appends verified per-source records, never deletes or rewrites unrelated papers.
"""

import copy
import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SOURCES = {
    'cvpr': 4042,
    'ecai': 973,
    'natcomputsci': 142,
    'npjscilearn': 69,
    'j-f28cf1469d': 54,
    'j-9596fa43cd': 95,
    'j-3d73a601f6': 127,
    'nprot': 172,
    'nature-celldisc': 82,
}


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def write(path, data):
    with path.open('w', encoding='utf-8') as stream:
        json.dump(data, stream, ensure_ascii=False, indent=2)
        stream.write('\n')


def key(p):
    return (p['venue'], p['year'], p['id'].lower())


def digest(path):
    sha = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            sha.update(chunk)
    return {'sha256': sha.hexdigest(), 'bytes': path.stat().st_size}


def main():
    annual_path = ROOT / 'metadata/2026/papers.json'
    snapshot_path = ROOT / 'metadata/2026/snapshot.json'
    feedback_path = ROOT / 'reviews/2026/feedback/Blueblue1101.json'
    annual = read(annual_path)
    snapshot = read(snapshot_path)
    feedback = read(feedback_path)
    if len(annual) < 300000 or snapshot['year'] != 2026:
        raise RuntimeError('Complete 2026 LFS bibliography was not checked out')
    indexed = {key(p) for p in annual}
    # Unrelated venues may already have duplicate keys; audit only touched sources.
    added = 0
    changes = []
    for source, expected in SOURCES.items():
        path = ROOT / 'metadata' / source / '2026/papers.json'
        records = read(path)
        source_keys = {key(p) for p in records}
        if len(records) != expected or len(source_keys) != expected:
            raise RuntimeError(f'{source}: source count or unique identity differs from audited {expected}')
        annual_keys = {k for k in indexed if k[0] == source and k[1] == 2026}
        if not annual_keys.issubset(source_keys):
            raise RuntimeError(f'{source}: annual records not represented in current source bibliography')
        entries = [s for s in snapshot['sources'] if s['source'] == source]
        if len(entries) != 1 or entries[0]['papers'] != len(annual_keys):
            raise RuntimeError(f'{source}: snapshot count does not match annual bibliography')
        row_matches = [r for r in feedback if r['source_code'] == source]
        if len(row_matches) != 1:
            raise RuntimeError(f'{source}: owner feedback missing or duplicated')
        row = row_matches[0]
        if row.get('official_total') not in (None, expected):
            raise RuntimeError(f'{source}: official total conflicts with audited source count')
        if row.get('official_total') is None and source != 'natcomputsci':
            raise RuntimeError(f'{source}: publisher total has not been verified')
        for p in records:
            k = key(p)
            if k not in indexed:
                annual.append(copy.deepcopy(p))
                indexed.add(k)
                added += 1
        entry = entries[0]
        old_papers, old_with = entry['papers'], entry['with_abstract']
        entry['papers'] = expected
        entry['with_abstract'] = sum(bool(p.get('abstract')) for p in records)
        snapshot['totals']['papers'] += expected - old_papers
        snapshot['totals']['with_abstract'] += entry['with_abstract'] - old_with
        row['snapshot_papers'] = expected
        row['checked_at'] = '2026-11-26'
        note = f'年度LFS全量与逐源书目按唯一键对账：{expected}篇，2026-11-26。'
        if note not in (row.get('coverage_note') or ''):
            row['coverage_note'] = (row.get('coverage_note') or '') + ' ' + note
        # Keep unresolved publisher and candidate-metadata questions visible.
        if source in ('cvpr', 'ecai', 'j-3d73a601f6', 'nprot', 'nature-celldisc'):
            row['issues'] = [issue for issue in row.get('issues', []) if not (
                '年度快照' in issue or '年度聚合快照' in issue or '逐源题录待同步' in issue
            )]
            row['next_actions'] = [action for action in row.get('next_actions', []) if not (
                '年度快照' in action or '年度聚合快照' in action or '逐源papers.json' in action
            )]
        changes.append({'source': source, 'before': old_papers, 'after': expected})

    if added:
        write(annual_path, annual)
        snapshot['annual_files']['papers.json'] = digest(annual_path)
    snapshot['wangwanting_20261126_annual_reconciliation'] = {
        'base_snapshot_at': snapshot['captured_at'],
        'checked_at': '2026-11-26', 'annual_added': added,
        'sources': changes,
        'note': 'Only publisher-audited source records synchronized; other 2026 sources retain their original snapshot state.',
    }
    write(snapshot_path, snapshot)
    write(feedback_path, feedback)
    print(json.dumps({'annual_added': added, 'sources': changes}, ensure_ascii=False))


if __name__ == '__main__':
    main()
