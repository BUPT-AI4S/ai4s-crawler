#!/usr/bin/env python3
"""Apply evidence-based 2025 screening for the listed small assigned sources."""

import concurrent.futures
import difflib
import html
import json
import re
import urllib.parse
import urllib.request
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
REVIEW = ROOT / 'reviews/2025/Blueblue1101.json'
FEEDBACK = ROOT / 'reviews/2025/feedback/Blueblue1101.json'
VOCAB = ROOT / 'skills/ai4s-paper-review/references/tag-vocabulary.json'
SNAPSHOT = '2026-11-09T10:51:18+08:00'
BATCH = 'wangwanting-2025-small-sources-20261128'

# Source order is checked against the fixed 2025 candidate snapshot. I = include,
# E = exclude; positive decisions each carry the scientific contribution and a
# shared-vocabulary tag. These 25 records were read individually from abstracts.
DECISIONS = {
    'j-216eba8f80': [('E', '综述讨论代谢衰老的细胞异质性，AI 仅作为未来数据整合工具提及。')],
    'j-96be195ee8': [('E', '综述诱发地震机理与风险，机器学习仅为多种预测方法之一，未给出实质 AI 研究。')],
    'j-b65bc153a0': [('E', 'Viewpoint 倡导低碳抗凝照护，AI 只是数字医疗愿景中的一项。')],
    'j-1a2d106b4b': [
        ('E', '呼吸化学感受的神经生物学综述，未研究 AI 方法。'),
        ('E', '神经回路与习惯行为的综述，仅类比 Transformer 注意力。'),
    ],
    'j-1c0b582639': [
        ('E', '肌骨疾病负担与健康照护综述，AI 只在数字医疗方案中提及。'),
        ('I', '系统综述 AI 从多器官医学影像估计生物年龄及健康风险的研究。', 'AI 用于生命科学'),
    ],
    'j-c702b0c2a4': [
        ('E', '肺癌人群队列关联分析使用传统回归，没有实质 AI 模型研究。'),
        ('E', '背痛与 MRI 肌肉组成的流行病学关联为核心；既有分割工具仅辅助测量。'),
    ],
    'j-3d73a601f6': [
        ('I', '机器学习功能遗传筛选识别 DDX55，随后用实验揭示 T 细胞稳态机制。', 'AI 用于生命科学'),
        ('I', '以系统疫苗学案例评估 LLM 的生物学假设与实验设计能力。', '科学评测'),
        ('E', '一段短讯介绍 AI 辅助抗体设计，属于新闻/评论而非研究正文。'),
    ],
    'j-6f25cc9655': [
        ('E', '综述癌症与心血管疾病的共有机制及药物再利用，未展开 AI。'),
        ('E', '离子通道药理学综述仅将 AI 作为新药发现趋势之一。'),
        ('I', '综述用多组学与机器学习识别动脉粥样硬化特征并支持个体化诊疗。', 'AI 用于生命科学'),
    ],
    'j-c2843d80b8': [
        ('E', '胰腺癌前病变多组学标志物综述，未见实质 AI 方法。'),
        ('E', '胰腺癌表观遗传机制及临床应用综述，未见实质 AI 方法。'),
        ('I', '综述 AI 整合遗传、临床与影像数据用于胰腺癌风险分层。', 'AI 用于生命科学'),
    ],
    'j-f28cf1469d': [
        ('E', '问卷调查 ChatGPT 辅助语言学习的态度与影响因素，未研究 AI 对科学任务的作用。'),
        ('E', '学习科学定义的文献综述仅提及 AI 是未来相关技术。'),
        ('I', '设计 ChatGPT 数学辅导系统并以准实验检验学生解题效果。', 'AI 用于社会科学'),
    ],
    'j-72172ba21c': [
        ('E', 'Opinion 评论癌症诊断 AI 进展和未来愿景，缺乏实质研究综述。'),
        ('E', '结节性硬化症性别差异的生物学评论，未研究 AI。'),
        ('E', 'Opinion 讨论代谢组学与 AI 的前景，不是实质学术综述。'),
        ('E', '通用禽流感疫苗进展综述中 AI 仅作为辅助技术提及。'),
    ],
}


def verify(p):
    doi = p.get('doi') or (p['id'] if p['id'].startswith('10.') else None)
    if not doi:
        raise ValueError(f'No DOI for included paper: {p["id"]}')
    url = 'https://api.crossref.org/works/' + urllib.parse.quote(doi, safe='/')
    req = urllib.request.Request(url, headers={'User-Agent': 'BUPT-AI4S metadata verification (academic bibliography)'})
    with urllib.request.urlopen(req, timeout=25) as response:
        m = json.load(response)['message']
    title = html.unescape((m.get('title') or [''])[0])
    norm = lambda s: re.sub(r'[^a-z0-9]', '', s.lower())
    if m.get('DOI', '').lower() != doi.lower() or difflib.SequenceMatcher(None, norm(title), norm(p['title'])).ratio() < .9:
        raise ValueError(f'DOI/title mismatch: {doi}: {title}')
    authors = [' '.join(filter(None, [x.get('given'), x.get('family')])) for x in m.get('author', [])]
    if not authors:
        raise ValueError(f'No authors registered: {doi}')
    landing = m.get('resource', {}).get('primary', {}).get('URL') or p.get('url') or m.get('URL')
    return p['id'], {'doi': doi, 'title': title, 'authors': authors, 'url': landing,
                     'checked_at': str(date.today()), 'evidence_urls': [url]}


def main():
    rows = json.loads(REVIEW.read_text())
    feedback = json.loads(FEEDBACK.read_text())
    tags = {x['label']: x for x in json.loads(VOCAB.read_text())['tags']}
    selected = [(p, decision) for code, spec in DECISIONS.items()
                for p, decision in zip([p for p in rows if p['venue'] == code], spec)]
    assert sum(len(v) for v in DECISIONS.values()) == len(selected)
    assert all(len([p for p in rows if p['venue'] == c]) == len(v) for c,v in DECISIONS.items())
    assert all(p['ai4s_review']['decision'] == 'unreviewed' and p.get('abstract') for p, _ in selected)
    includes = [p for p, rule in selected if rule[0] == 'I']
    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
        verified = dict(pool.map(verify, includes))
    for p, rule in selected:
        state, rationale, *label = rule
        v = p['ai4s_review']
        v.update({'decision': 'include' if state == 'I' else 'exclude', 'rationale': rationale, 'batch_id': BATCH})
        if state == 'I':
            t = tags[label[0]]
            v['verified_metadata'] = verified[p['id']]
            v['tags'] = [{'axis': t['axis'], 'label': t['label'], 'label_en': t['label_en'],
                          'evidence_location': '输入摘要', 'rationale': rationale}]
    known = {f['source_code'] for f in feedback}
    snapshot = json.loads((ROOT / 'metadata/2025/snapshot.json').read_text())
    bysource = {x['source']: x for x in snapshot['sources']}
    for source, spec in DECISIONS.items():
        if source in known:
            raise ValueError(f'Feedback already exists for {source}')
        feedback.append({'year': 2025, 'source_code': source, 'snapshot_at': SNAPSHOT,
                         'official_total': None, 'official_scope': None,
                         'coverage_note': f'{len(spec)} 条候选已按原摘要与文献类型逐篇精筛；纳入论文 DOI、题名、作者和正式页面经 Crossref 出版社登记核对。全量采集快照 {bysource[source]["papers"]} 篇，官网同口径年度目录仍待核对。',
                         'evidence_urls': [], 'issues': ['官网同口径年度总量尚未核对。'],
                         'next_actions': ['按出版社年度目录与固定快照逐项核对全量，处理差异。'],
                         'checked_at': str(date.today())})
    REVIEW.write_text(json.dumps(rows, ensure_ascii=False, indent=2) + '\n')
    FEEDBACK.write_text(json.dumps(feedback, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'sources': len(DECISIONS), 'reviewed': len(selected), 'included': len(includes)}, ensure_ascii=False))


if __name__ == '__main__':
    main()
