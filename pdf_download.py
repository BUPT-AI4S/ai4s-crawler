import os
import re
from pathlib import Path
from typing import Optional
from urllib.parse import unquote, urlparse

import requests

DEFAULT_HEADERS = {
    "Accept": "application/pdf,application/octet-stream;q=0.9,*/*;q=0.8",
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
    ),
}


def normalize_pdf_url(url: Optional[str]) -> Optional[str]:
    if not url:
        return None
    u = url.strip()
    if "arxiv.org/abs/" in u:
        u = u.replace("/abs/", "/pdf/")
    if "openaccess.thecvf.com" in u and "/html/" in u:
        u = u.replace("/html/", "/papers/")
        if u.endswith(".html"):
            u = u[: -len(".html")] + ".pdf"
    return u


def safe_filename(name: str, max_len: int = 150) -> str:
    name = unquote(name or "")
    name = re.sub(r'[\\/:*?"<>|\r\n]+', "_", name)
    name = re.sub(r"\s+", " ", name).strip(" ._")
    if not name:
        return "paper"
    return name[:max_len]


def filename_from_detail(url: str, detail: dict) -> str:
    for key in ("anthology_id", "arxiv_id", "forum_id"):
        value = (detail or {}).get(key)
        if value:
            return safe_filename(str(value)) + ".pdf"

    pdf_url = (detail or {}).get("pdf_url") or ""
    base = os.path.basename(unquote(urlparse(pdf_url).path))
    if base.lower().endswith(".pdf") and len(base) > 8:
        return safe_filename(base)

    title = (detail or {}).get("title")
    if title:
        return safe_filename(title) + ".pdf"

    fallback = os.path.basename(unquote(urlparse(url).path)) or "paper"
    if not fallback.lower().endswith(".pdf"):
        fallback = fallback + ".pdf"
    return safe_filename(fallback)


def _looks_like_pdf(path: Path) -> bool:
    try:
        with path.open("rb") as f:
            return f.read(5) == b"%PDF-"
    except OSError:
        return False


def download_pdf(
    url: str,
    dest_path: str,
    headers: Optional[dict] = None,
    session: Optional[requests.Session] = None,
    timeout: int = 90,
    skip_existing: bool = True,
) -> str:
    dest = Path(dest_path)
    if skip_existing and dest.exists() and dest.stat().st_size > 1000 and _looks_like_pdf(dest):
        return str(dest)

    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(dest.suffix + ".part")
    http = session or requests
    r = http.get(url, headers=headers or DEFAULT_HEADERS, timeout=timeout, stream=True)
    r.raise_for_status()
    try:
        with tmp.open("wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
    finally:
        r.close()

    if not _looks_like_pdf(tmp):
        tmp.unlink(missing_ok=True)
        raise ValueError(f"下载结果不是 PDF: {url}")
    tmp.replace(dest)
    return str(dest)


def write_pdf_bytes(data: bytes, dest_path: str, skip_existing: bool = True) -> str:
    dest = Path(dest_path)
    if skip_existing and dest.exists() and dest.stat().st_size > 1000 and _looks_like_pdf(dest):
        return str(dest)
    if not data or not data.startswith(b"%PDF-"):
        raise ValueError("OpenReview 附件不是 PDF")
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp = dest.with_suffix(dest.suffix + ".part")
    tmp.write_bytes(data)
    tmp.replace(dest)
    return str(dest)
