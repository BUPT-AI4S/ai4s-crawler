#!/usr/bin/env python3
"""Close only verified bibliographic-metadata feedback for this owner."""

import json
from collections import defaultdict
from datetime import date
from pathlib import Path

REVIEW = Path('reviews/2026/Blueblue1101.json')
FEEDBACK = Path('reviews/2026/feedback/Blueblue1101.json')
UNFINISHED = Path('reviews/2026/audits/wangwanting-2026-metadata-unfinished.json')
AUDIT_URL = 'reviews/2026/audits/wangwanting-2026-metadata-verification.json'
ISSUE = '纳入结论基于原摘要及已记录的正文补证；除verified_metadata已明确记录者，正式元数据在线核验仍未完成。'


def main():
    papers = json.loads(REVIEW.read_text())
    feedback = json.loads(FEEDBACK.read_text())
    by_source = defaultdict(list)
    for p in papers:
        if p.get('ai4s_review', {}).get('decision') == 'include':
            by_source[p['venue']].append(p)
    updated = 0
    actions_updated = 0
    unfinished = []
    for row in feedback:
        has_issue = ISSUE in row.get('issues', [])
        has_action = any('正式元数据' in x for x in row.get('next_actions', []))
        if not (has_issue or has_action):
            continue
        source = row['source_code']
        items = by_source[source]
        missing = []
        for p in items:
            v = p['ai4s_review'].get('verified_metadata') or {}
            fields = ['title', 'authors', 'url', 'evidence_urls'] + ([] if source == 'cvpr' else ['doi'])
            if any(not v.get(k) for k in fields) or v.get('checked_at') != str(date.today()):
                missing.append({'id': p['id'], 'missing': [k for k in fields if not v.get(k)], 'checked_at': v.get('checked_at')})
        if missing:
            unfinished.append({'source_code': source, 'included': len(items), 'unverified': missing})
            continue
        if has_issue:
            row['issues'] = [x for x in row['issues'] if x != ISSUE]
            row['coverage_note'] = (row.get('coverage_note', '').rstrip() + f' 2026-11-28：本来源纳入 {len(items)} 篇，逐篇以出版社登记的 Crossref DOI、题名、作者、正式落地页（CVPR 为 CVF 官方论文页）在线核验；结果写入 verified_metadata，未匹配 0 篇。证据见 {AUDIT_URL}。')
            row['checked_at'] = str(date.today())
            updated += 1
        if has_action:
            row['next_actions'] = [
                '从出版社补齐候选原摘要。' if x == '从出版社补齐候选原摘要并核对纳入条目的正式元数据。' else x
                for x in row.get('next_actions', []) if x != '核对纳入条目的正式元数据。'
            ]
            actions_updated += 1
    FEEDBACK.write_text(json.dumps(feedback, ensure_ascii=False, indent=2) + '\n')
    UNFINISHED.write_text(json.dumps({'checked_at': str(date.today()), 'sources': unfinished}, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'metadata_issues_closed': updated, 'metadata_actions_updated': actions_updated, 'remaining_sources': len(unfinished), 'remaining_papers': sum(len(x['unverified']) for x in unfinished)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
