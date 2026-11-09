import json
import re
from functools import lru_cache
from pathlib import Path

from ai4s_taxonomy import classify_paper, has_ai_evidence, normalize_text, paper_text

_KEYWORDS = Path(__file__).resolve().parent / "ai4s_keywords.txt"
_VOCABULARY = Path(__file__).resolve().parent / 'skills/ai4s-paper-review/references/tag-vocabulary.json'
_SEARCH_FIELDS = ("title", "abstract", "tldr", "primary_area", "track")


def load_patterns(path: Path | None = None) -> list[tuple[str, re.Pattern]]:
    source = path or _KEYWORDS
    patterns = []
    for raw in source.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.lower().startswith("re:"):
            label = line[3:]
            patterns.append((label, re.compile(label, flags=re.I)))
            continue
        if " " not in line and len(line) <= 4:
            patterns.append((line, re.compile(rf"\b{re.escape(line)}\b", flags=re.I)))
            continue
        patterns.append((line, re.compile(re.escape(line), flags=re.I)))
    return patterns


@lru_cache(maxsize=1)
def load_review_vocabulary() -> tuple[tuple[str, str, re.Pattern], ...]:
    if not _VOCABULARY.exists():
        return ()
    data = json.loads(_VOCABULARY.read_text(encoding='utf-8-sig'))
    patterns = []
    for tag in data['tags']:
        forms = [tag['label'], tag['label_en'], *tag.get('aliases', [])]
        alternatives = []
        for value in sorted({normalize_text(form) for form in forms if form.strip()}, key=lambda v: (-len(v), v)):
            term = re.escape(value)
            # ASCII boundaries avoid substring hits such as GNN inside AGNN,
            # while permitting Chinese labels within unsegmented Chinese text.
            if value[0].isascii() and value[0].isalnum():
                term = r'(?<![A-Za-z0-9_])' + term
            if value[-1].isascii() and value[-1].isalnum():
                term += r'(?![A-Za-z0-9_])'
            alternatives.append(term)
        if alternatives:
            patterns.append((tag['axis'], tag['label'], re.compile('|'.join(alternatives), re.I)))
    return tuple(patterns)


def _search_text(paper: dict) -> str:
    parts = []
    for key in _SEARCH_FIELDS:
        value = paper.get(key)
        if isinstance(value, str) and value.strip():
            parts.append(value)
    keywords = paper.get("keywords") or []
    if isinstance(keywords, list):
        parts.extend(str(item) for item in keywords if str(item).strip())
    elif isinstance(keywords, str) and keywords.strip():
        parts.append(keywords)
    return "\n".join(parts)


def is_official_ai4s(paper: dict) -> bool:
    track = paper.get("track") or ""
    return "ai for science" in str(track).lower()


def match_hits(paper: dict, patterns: list[tuple[str, re.Pattern]] | None = None) -> list[str]:
    text = _search_text(paper)
    if not text:
        return []
    compiled = patterns if patterns is not None else load_patterns()
    hits = []
    for label, pattern in compiled:
        if pattern.search(text):
            hits.append(label)
    return hits


def select_ai4s(papers: list[dict], patterns: list[tuple[str, re.Pattern]] | None = None) -> list[dict]:
    compiled = patterns if patterns is not None else load_patterns()
    vocabulary = load_review_vocabulary()
    chosen = []
    for paper in papers:
        if paper.get('ccf_paper_status') == 'excluded':
            continue
        hits = match_hits(paper, compiled)
        official = is_official_ai4s(paper)
        classification = classify_paper(paper)
        if paper.get('venue_type') == 'journal':
            # 自然科学期刊中仅有 protein/molecule 等词不足以证明属于 AI4S。
            article_type = str(paper.get('article_type') or '').lower()
            if re.search(r'editorial|news|comment|correction|erratum|retraction|research briefing|'
                         r'research highlight|matters arising|correspondence|book review|obituary', article_type):
                continue
            if not has_ai_evidence(paper):
                continue
        text = paper_text(paper)
        vocabulary_matches = [(axis, label, pattern) for axis, label, pattern in vocabulary if pattern.search(text)]
        vocabulary_only = not (hits or official or classification['ai4s_tags'])
        if vocabulary_only:
            context = [pattern for axis, _, pattern in vocabulary_matches if axis in ('domain', 'task')]
            if not context:
                continue
            for pattern in context:
                text = pattern.sub(' ', text)
            if not has_ai_evidence({'title': text}):
                continue
        row = dict(paper)
        row["ai4s_hits"] = hits
        row["ai4s_reason"] = "official_track" if official else ("keyword" if hits else
                             "review_vocabulary" if vocabulary_only else "taxonomy_rule")
        if vocabulary_matches:
            row["ai4s_vocabulary_hits"] = list(dict.fromkeys(label for _, label, _ in vocabulary_matches))
        # 已经整理/人工复核的标签不被规则覆盖。
        for key, value in classification.items():
            if key not in row:
                row[key] = value
        chosen.append(row)
    return chosen
