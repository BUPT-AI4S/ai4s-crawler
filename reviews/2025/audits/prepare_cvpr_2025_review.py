#!/usr/bin/env python3
"""Apply individually reviewed CVPR 2025 decisions and official catalogue recovery."""

import concurrent.futures
import copy
import difflib
import json
from datetime import date
from pathlib import Path

from bs4 import BeautifulSoup

from reconcile_cvpr_2025 import get

ROOT = Path(__file__).resolve().parents[3]
YEAR = ROOT / 'metadata/2025/ai4s.json'
SOURCE = ROOT / 'metadata/cvpr/2025/ai4s.json'
PAPERS = ROOT / 'metadata/cvpr/2025/papers.json'
REVIEW = ROOT / 'reviews/2025/Blueblue1101.json'
FEEDBACK = ROOT / 'reviews/2025/feedback/Blueblue1101.json'
AUDIT = ROOT / 'reviews/2025/audits/wangwanting-cvpr-2025-official-diff.json'
SNAPSHOT = '2026-11-09T10:51:18+08:00'
BATCH = 'wangwanting-2025-cvpr-20261128'

# Numbering follows the immutable original 22 candidates in metadata/cvpr/2025/ai4s.json.
DECISIONS = {
    1: ('exclude', '仅改进通用文生图模型的创意生成，没有具体科学研究任务。', None),
    2: ('exclude', '任意尺度通用图像超分辨，没有可确认的科学任务。', None),
    3: ('include', '显微图像问答基准评估科研层面的图像理解、假设生成与实验建议。', 'AI 用于生命科学'),
    4: ('include', '病理切片与基因组数据用于癌症患者生存预测。', 'AI 用于生命科学'),
    5: ('exclude', '跨航拍与地面视频行人重识别是通用视觉识别任务。', None),
    6: ('include', '从欠采样 MRI 测量中重建人体影像以缩短扫描时间。', '医学影像重建'),
    7: ('include', '隐式神经表示解析空间转录组中的基因表达空间分布。', 'AI 用于生命科学'),
    8: ('include', '时空模型缓解大气湍流导致的远距离成像失真。', 'AI 用于工程科学'),
    9: ('include', '从动态视频估计速度场与物体运动的底层物理。', 'AI 用于数理科学'),
    10: ('include', '病理全切片图像预测空间转录组基因表达。', 'AI 用于生命科学'),
    11: ('include', '提出神经场微分算子用于物理 PDE 模拟所需的空间导数。', 'AI 用于数理科学'),
    12: ('include', '从科学文献构建生物医学图文资源并训练生物医学视觉语言模型。', '科学数据'),
    13: ('include', '自监督 3D 断层扫描配准帮助冷冻电镜重建大分子结构。', 'AI 用于生命科学'),
    14: ('exclude', '通用图像生成分辨率扩展，未验证科学任务。', None),
    15: ('include', '病理图像预测空间基因表达并融合基因相似性。', 'AI 用于生命科学'),
    16: ('include', '个性化联邦模型处理低剂量 CT 图像降噪。', '医学影像重建'),
    17: ('include', '学习成像系统的点扩散函数并进行物理约束的模糊估计。', 'AI 用于工程科学'),
    18: ('exclude', '量子退火框架用于计算机视觉优化，摘要无明确科学研究任务。', None),
    19: ('include', '从病理切片推断 3D 空间转录组表达以降低实验采集成本。', 'AI 用于生命科学'),
    20: ('include', '卫星观测引导气象状态降尺度与高分辨率场重建。', '气象水文预测'),
    21: ('include', '利用雷达序列预测降水临近变化。', '气象水文预测'),
    22: ('exclude', '通用多模态模型跨域泛化评估，医学和分子图像仅为测试域。', None),
}

# Numbering follows the official missing-in-snapshot audit. All other recovered
# proceedings papers remain in the full source bibliography, not AI4S candidates.
RECOVERED = {
    4: ('医学视觉语言模型结合医学图像问答、定位和临床语义分析。', 'AI 用于生命科学'),
    5: ('神经物体表示学习电磁属性以改进无线电传播物理仿真。', 'AI 用于工程科学'),
    13: ('多实例学习对病理全切片进行疾病图像分类。', '医学影像分类'),
    17: ('卫星影像和机载 LiDAR 构建树冠高度及变化监测基准。', 'AI 用于地球宇宙科学'),
    25: ('3D 蠕虫显微图像的多图匹配用于生物成像配准。', 'AI 用于生命科学'),
    57: ('细胞表型与分子数据的多模态对比学习支持药物发现。', '药物筛选'),
    88: ('超高分辨率遥感影像基准评估模型对地球观测图像的理解。', 'AI 用于地球宇宙科学'),
}


def write(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def key(p):
    return (p['venue'], p['year'], p['id'])


def official(row):
    soup = BeautifulSoup(get(row['url']), 'html.parser')
    def meta(name):
        tag = soup.find('meta', attrs={'name': name})
        return tag.get('content', '').strip() if tag else None
    title = meta('citation_title')
    score = difflib.SequenceMatcher(None, title.lower(), row['title'].lower()).ratio()
    if score < .95:
        raise ValueError(f'Official title mismatch: {row["id"]}: {score:.2f}')
    authors = [x.get('content', '').strip() for x in soup.find_all('meta', attrs={'name': 'citation_author'})]
    if not authors:
        raise ValueError(f'Official authors missing: {row["id"]}')
    return row['id'], {'title': title, 'authors': authors, 'url': row['url'],
                       'pdf_url': meta('citation_pdf_url'), 'evidence_urls': [row['url']],
                       'checked_at': str(date.today())}


def review(p, decision, rationale, label, verified=None):
    value = {'schema_version': 2, 'batch_id': BATCH, 'owner': '王婉婷',
             'snapshot_at': SNAPSHOT, 'decision': decision, 'rationale': rationale,
             'verified_metadata': verified or {}, 'tags': []}
    if decision == 'include':
        tag = next(x for x in json.loads((ROOT / 'skills/ai4s-paper-review/references/tag-vocabulary.json').read_text())['tags']
                   if x['label'] == label)
        value['tags'] = [{'axis': tag['axis'], 'label': label, 'label_en': tag['label_en'],
                          'evidence_location': '输入摘要', 'rationale': rationale}]
    p['ai4s_review'] = value
    return p


def main():
    audit = json.loads(AUDIT.read_text())
    assert (audit['official_count'], audit['local_count'], audit['missing_count'], audit['extra_count']) == (2871, 2755, 116, 0)
    assert len(audit['official_missing_in_snapshot']) == 116 and not audit['unresolved']
    initial = json.loads(SOURCE.read_text())
    assert len(initial) == len(DECISIONS) == 22
    assert len(RECOVERED) == 7
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        verified = dict(pool.map(official, initial))
    existing = json.loads(REVIEW.read_text()) if REVIEW.exists() else []
    if not existing:
        assigned = {x['code'] for x in json.loads((ROOT / 'reviews/source-assignments-2025.json').read_text())['sources']
                    if x['owner'] == '王婉婷'}
        existing = [review(copy.deepcopy(p), 'unreviewed', None, None) for p in json.loads(YEAR.read_text())
                    if p['venue'] in assigned]
    bykey = {key(p): p for p in existing}
    assert len(bykey) == len(existing)
    for i, p in enumerate(initial, 1):
        decision, rationale, label = DECISIONS[i]
        review(bykey[key(p)], decision, rationale, label, verified[p['id']] if decision == 'include' else None)
    source_papers = json.loads(PAPERS.read_text())
    source_keys = {p['id'] for p in source_papers}
    year_candidates = json.loads(YEAR.read_text())
    year_keys = {key(p) for p in year_candidates}
    source_candidates = list(initial)
    for i, r in enumerate(audit['official_missing_in_snapshot'], 1):
        assert r['title'] and r['authors'] and r['abstract'] and r['pdf_url']
        assert r['id'] not in source_keys
        raw = {'id': r['id'], 'venue': 'cvpr', 'year': 2025, 'track': 'main',
               'title': r['title'], 'authors': r['authors'], 'author_ids': [],
               'abstract': r['abstract'], 'keywords': [], 'tldr': None,
               'primary_area': None, 'presentation': None, 'doi': None,
               'pages': f'{r["firstpage"]}-{r["lastpage"]}' if r['firstpage'] and r['lastpage'] else None,
               'bibtex': None, 'url': r['url'], 'pdf_url': r['pdf_url'],
               'code_url': None, 'project_url': None, 'published': '2025',
               'source': 'CVF official proceedings; 2026-11-28 reconciliation'}
        source_papers.append(raw)
        if i in RECOVERED:
            rationale, label = RECOVERED[i]
            assert key(raw) not in year_keys and key(raw) not in bykey
            candidate = copy.deepcopy(raw)
            candidate['ai4s_hits'] = []
            candidate['ai4s_reason'] = '官网漏采补录：摘要确认具体 AI4S 任务'
            source_candidates.append(candidate)
            year_candidates.append(candidate)
            meta = {'title': r['title'], 'authors': r['authors'], 'url': r['url'],
                    'pdf_url': r['pdf_url'], 'evidence_urls': [r['url']], 'checked_at': str(date.today())}
            bykey[key(raw)] = review(copy.deepcopy(candidate), 'include',
                                     '官网漏采补录；' + rationale, label, meta)
    assert len(source_papers) == 2871
    write(PAPERS, source_papers)
    write(SOURCE, source_candidates)
    write(YEAR, year_candidates)
    write(REVIEW, list(bykey.values()))
    feedback = json.loads(FEEDBACK.read_text()) if FEEDBACK.exists() else []
    if not any(x['source_code'] == 'cvpr' for x in feedback):
        feedback.append({'year': 2025, 'source_code': 'cvpr', 'snapshot_at': SNAPSHOT,
                         'official_total': 2871, 'official_scope': 'CVF 2025 年主会正式论文 HTML，去重官方 ID；全届目录',
                         'coverage_note': '官网 2871，固定快照 2755；缺失 116 篇已核对官网摘要并补入逐源书目，7 篇 AI4S 漏筛纳入候选和审核。原候选 22 篇逐篇审核。年度 LFS 全量与快照尚需重建，不能将 116 篇差额视为已核销。',
                         'evidence_urls': [audit['directory']],
                         'issues': ['固定年度快照仍为 2755 篇；逐源已补 116 篇，年度 LFS 全量与快照尚未重建。'],
                         'next_actions': ['将逐源 2871 篇与年度 LFS 全量及快照同步，按官网 ID 对账后核销总量。'],
                         'checked_at': str(date.today())})
    write(FEEDBACK, feedback)
    print(json.dumps({'reviewed_cvpr': 29, 'included_cvpr': 23,
                      'recovered_full': 116, 'unreviewed_other_sources': sum(p['ai4s_review']['decision']=='unreviewed' for p in bykey.values())}, ensure_ascii=False))


if __name__ == '__main__':
    main()
