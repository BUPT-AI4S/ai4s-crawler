"""可解释的规则候选标签；不将关键词命中冒充为人工语义复核。"""
import json
import re
import unicodedata
from pathlib import Path

_CONFIG = json.loads(Path(__file__).with_suffix('.json').read_text(encoding='utf-8'))
CATEGORIES = tuple(row['name'] for row in _CONFIG['categories'])
_RULES = [(row['name'], row['axis'], row.get('fields'), [(label, re.compile(pattern, re.I))
           for label, pattern in row['keywords'].items()]) for row in _CONFIG['categories']]
_AI = [re.compile(pattern, re.I) for pattern in _CONFIG['ai_evidence']]
_METHODS = [(label, re.compile(pattern, re.I)) for label, pattern in _CONFIG.get('method_keywords', {}).items()]
_DASHES = str.maketrans({ch: '-' for ch in '\u2010\u2011\u2012\u2013\u2014\u2212'})
_EXPLICIT_SCIENCE = re.compile(r'\b(?:AI for science|ai4s(?:cience)?|scientific|SciML|autonomous laborator(?:y|ies)|self[- ]driving laborator(?:y|ies))\b|科学数据|科学知识模型|科学基础模型|科学智能体|科研智能体|自主实验室|科学发现|科学推理', re.I)


def paper_text(paper: dict) -> str:
    parts = [paper.get(k) for k in ('title', 'abstract', 'tldr', 'primary_area', 'track')]
    keywords = paper.get('keywords') or []
    parts.extend(keywords if isinstance(keywords, list) else [keywords])
    return '\n'.join(normalize_text(v) for v in parts if isinstance(v, str) and v.strip())


def normalize_text(text: str) -> str:
    return re.sub(r'\s+', ' ', unicodedata.normalize('NFKC', text).translate(_DASHES)).strip()


def has_ai_evidence(paper: dict) -> bool:
    text = paper_text(paper)
    return any(pattern.search(text) for pattern in _AI)


def classify_paper(paper: dict) -> dict:
    text = paper_text(paper)
    matches = []
    for name, axis, fields, rules in _RULES:
        category_text = '\n'.join(normalize_text(str(paper.get(k) or '')) for k in fields) if fields else text
        matches.append((name, axis, [label for label, pattern in rules if pattern.search(category_text)]))
    scientific = any(hits for _, axis, hits in matches if axis == 'discipline') or bool(_EXPLICIT_SCIENCE.search(text))
    evidence = {name: hits for name, axis, hits in matches if hits and (axis == 'discipline' or scientific)}
    keywords = list(dict.fromkeys(hit for hits in evidence.values() for hit in hits))
    if scientific:
        methods = [label for label, pattern in _METHODS if pattern.search(text)]
        keywords = list(dict.fromkeys(keywords + methods))
    else:
        methods = []
    return {
        'ai4s_tags': list(evidence), 'ai4s_keywords': keywords,
        'ai4s_tagging': {'taxonomy_version': _CONFIG['version'], 'basis': 'metadata_rules',
                         'status': 'needs_review' if evidence else 'unclassified', 'evidence': evidence,
                         'method_evidence': methods},
    }
