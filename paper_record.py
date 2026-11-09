import json
import re
from pathlib import Path

FIELDS = (
    "id",
    "venue",
    "year",
    "track",
    "title",
    "authors",
    "author_ids",
    "abstract",
    "keywords",
    "tldr",
    "primary_area",
    "presentation",
    "doi",
    "pages",
    "bibtex",
    "url",
    "pdf_url",
    "code_url",
    "project_url",
    "published",
    "source",
    "venue_type",
    "journal_title",
    "issn",
    "article_type",
    "screening_status",
    "conference_title",
    "ccf_rank",
    "ccf_field",
    "ccf_catalog_version",
    "ccf_paper_status",
    "dblp_key",
    "dblp_toc",
    "booktitle",
)

_LIST_FIELDS = ("authors", "author_ids", "keywords")


def norm_space(text: str | None) -> str | None:
    if text is None:
        return None
    cleaned = re.sub(r"\s+", " ", text).strip()
    return cleaned or None


def norm_title(text: str | None) -> str:
    raw = (text or "").lower()
    raw = re.sub(r"[^a-z0-9]+", " ", raw)
    return " ".join(raw.split())


def bibtex_field(bibtex: str | None, name: str) -> str | None:
    if not bibtex:
        return None
    braced = re.search(rf"{re.escape(name)}\s*=\s*\{{([^}}]*)\}}", bibtex, flags=re.I)
    if braced:
        return norm_space(braced.group(1))
    quoted = re.search(rf'{re.escape(name)}\s*=\s*"([^"]*)"', bibtex, flags=re.I)
    if quoted:
        return norm_space(quoted.group(1))
    return None


def make_record(**kwargs) -> dict:
    row = {key: None for key in FIELDS}
    for key in _LIST_FIELDS:
        row[key] = []
    for key, value in kwargs.items():
        if key not in row:
            continue
        if key in _LIST_FIELDS:
            row[key] = _as_list(value)
        elif key == "year":
            row[key] = int(value) if value is not None else None
        elif isinstance(value, str):
            row[key] = norm_space(value)
        else:
            row[key] = value
    return row


def _as_list(value) -> list:
    if value is None:
        return []
    if isinstance(value, str):
        parts = re.split(r"\s*[;|]\s*", value)
        return [part.strip() for part in parts if part.strip()]
    if isinstance(value, list):
        out = []
        for item in value:
            if isinstance(item, str) and item.strip():
                out.append(item.strip())
        return out
    return []


def load_records(path: Path) -> list[dict]:
    if not path.exists():
        return []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []
    if not isinstance(data, list):
        return []
    return [row for row in data if isinstance(row, dict)]


def dump_records(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(path)


class RecordCheckpoint:
    """按论文 id 断点续写。limit 试跑不读取旧文件。"""

    def __init__(self, path: Path, resume: bool):
        self.path = path
        self.rows = load_records(path) if resume else []
        self.by_id = {row["id"]: row for row in self.rows if row.get("id")}
        self._dirty = 0

    def add(self, row: dict) -> None:
        pid = row.get("id")
        if pid and pid in self.by_id:
            self.by_id[pid] = row
            self.rows = [row if item.get("id") == pid else item for item in self.rows]
        else:
            self.rows.append(row)
            if pid:
                self.by_id[pid] = row
        self._dirty += 1
        if self._dirty >= 20:
            self.flush()

    def flush(self) -> None:
        dump_records(self.path, self.rows)
        self._dirty = 0

    def replace(self, rows: list[dict]) -> None:
        self.rows = rows
        self.by_id = {row["id"]: row for row in rows if row.get("id")}
        self.flush()
