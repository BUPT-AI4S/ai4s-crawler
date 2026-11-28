"""Remove eight verified IJCAI-2024 workshop papers from the 2025 annual LFS file.

Run only after git lfs pull retrieved the complete annual file. The source-level
IJCAI 2025 catalogue, the official proceedings, and the archived eight records
are checked before modifying the annual bibliography or its snapshot manifest.
"""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ANNUAL = ROOT / 'metadata/2025/papers.json'
SNAPSHOT = ROOT / 'metadata/2025/snapshot.json'
SOURCE = ROOT / 'metadata/ijcai/2025/papers.json'
ARCHIVE = ROOT / 'reviews/2025/audits/dinglijun-ijcai-2025-reconciliation.json'
FEEDBACK = ROOT / 'reviews/2025/feedback/dinglijun.json'


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def write(path, data):
    with path.open('w', encoding='utf-8') as stream:
        json.dump(data, stream, ensure_ascii=False, indent=2)
        stream.write('\n')


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(chunk)
    return {'sha256': h.hexdigest(), 'bytes': path.stat().st_size}


def key(p):
    return p['venue'], p['year'], p['id'].lower()


def main():
    annual = read(ANNUAL)
    snapshot = read(SNAPSHOT)
    source = read(SOURCE)
    archive = read(ARCHIVE)
    feedback = read(FEEDBACK)
    # The existing annual JSON has 308,425 globally deduplicated records,
    # while the manifest sums 308,909 source records. Preserve this preexisting
    # difference and validate the IJCAI subset by exact identity below.
    if len(annual) != 308425 or snapshot['totals']['papers'] != 308909:
        raise RuntimeError(
            f'Unexpected baseline: annual={len(annual)}, '
            f'source_sum={snapshot["totals"]["papers"]}'
        )
    if len(source) != 1280 or archive['official_total'] != 1280:
        raise RuntimeError('IJCAI source or official proceedings count changed')
    source_keys = {key(p) for p in source}
    expected = {key(p) for p in archive['removed_papers']}
    old = [p for p in annual if p['venue'] == 'ijcai' and p['year'] == 2025]
    old_keys = {key(p) for p in old}
    if len(old) != 1288 or len(old_keys) != 1288 or old_keys != source_keys | expected or source_keys & expected:
        raise RuntimeError('Annual IJCAI identities differ from the audited 1280+8 split')
    old_extra = [p for p in old if key(p) in expected]
    if len(old_extra) != 8 or sum(bool(p.get('abstract')) for p in old) != 1269:
        raise RuntimeError('Annual IJCAI abstract counts differ from the snapshot')
    entry = next(x for x in snapshot['sources'] if x['source'] == 'ijcai')
    if (entry['papers'], entry['with_abstract']) != (1288, 1269):
        raise RuntimeError('Snapshot IJCAI counts differ from the audited state')
    remaining = [p for p in annual if key(p) not in expected]
    if len(remaining) != len(annual) - 8:
        raise RuntimeError('Unexpected removal count')
    write(ANNUAL, remaining)
    removed_abstracts = sum(bool(p.get('abstract')) for p in old_extra)
    entry['papers'] = 1280
    entry['with_abstract'] = sum(bool(p.get('abstract')) for p in source)
    if entry['with_abstract'] != 1269 - removed_abstracts:
        raise RuntimeError('Remaining source abstracts do not match the annual aggregate')
    snapshot['totals']['papers'] -= 8
    snapshot['totals']['with_abstract'] -= removed_abstracts
    snapshot['annual_files']['papers.json'] = digest(ANNUAL)
    snapshot['dinglijun_ijcai_2025_annual_reconciliation'] = {
        'checked_at': '2026-11-28',
        'official_proceedings_url': archive['official_proceedings_url'],
        'previous_count': 1288, 'current_count': 1280,
        'removed_ids': sorted(p['id'] for p in old_extra),
        'reason': 'These eight papers belong to IJCAI 2024 workshops, not IJCAI-25 proceedings.',
        'preexisting_annual_vs_source_sum_difference': 484,
    }
    write(SNAPSHOT, snapshot)
    row = next(x for x in feedback if x['source_code'] == 'ijcai')
    row['updated_at'] = '2026-11-28'
    row['snapshot_papers'] = 1280
    row['coverage_note'] += ' 年度 Git LFS 全量文件已与来源级正式论文集对齐，剔除归档的 8 篇 IJCAI 2024 工作坊论文；snapshot.json 对应计数及文件哈希已更新。'
    row['issues'] = [x for x in row['issues'] if '年度 snapshot.json' not in x]
    row['next_actions'] = [x for x in row['next_actions'] if '年度采集快照' not in x]
    write(FEEDBACK, feedback)
    print(json.dumps({'removed': 8, 'remaining_ijcai': 1280, 'annual_count': len(remaining)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
