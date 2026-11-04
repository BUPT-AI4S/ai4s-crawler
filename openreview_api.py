import os
import re
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, List, Optional
from urllib.parse import parse_qs, urlparse

from loguru import logger

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None

_ENV_FILE = Path(__file__).resolve().parent / ".env"
_TOKEN_FILE = Path(__file__).resolve().parent / "store" / "openreview_token"
_env_loaded = False


def _load_env() -> None:
    global _env_loaded
    if _env_loaded:
        return
    if load_dotenv is not None and _ENV_FILE.exists():
        load_dotenv(_ENV_FILE, override=False)
    _env_loaded = True

try:
    import openreview
except ImportError as e:  # pragma: no cover
    raise ImportError("请先安装 openreview-py：pip install openreview-py") from e


API2_BASE = "https://api2.openreview.net"
API1_BASE = "https://api.openreview.net"
WEB_BASE = "https://openreview.net"
_API_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36"
)
TOKEN_EXPIRES_IN = 7 * 24 * 3600  # 最长一周，避免大批量下 PDF 中途过期


class OpenReviewBlocked(RuntimeError):
    """OpenReview 登录或列表接口被 403 / challenge 拦住。"""


def _blocked_error(exc: Exception) -> bool:
    text = str(exc)
    return "403" in text or "Forbidden" in text or "ChallengeRequired" in text or "challenge" in text.lower()


@dataclass
class OpenReviewPaper:
    forum_id: str
    url: str
    title: Optional[str]
    authors: List[str]
    abstract: Optional[str]
    pdf_url: Optional[str]
    venue: Optional[str]
    venueid: Optional[str]
    keywords: List[str]
    number: Optional[int]
    author_ids: List[str] = field(default_factory=list)
    tldr: Optional[str] = None
    primary_area: Optional[str] = None
    presentation: Optional[str] = None
    bibtex: Optional[str] = None
    code_url: Optional[str] = None
    project_url: Optional[str] = None
    published: Optional[str] = None


_client_v2 = None
_client_v1 = None
_logged_in = False


def note_content_value(content: Optional[dict], key: str, default=None):
    if not content or key not in content:
        return default
    val = content[key]
    if isinstance(val, dict) and "value" in val:
        return val["value"]
    return val


def extract_forum_id(url_or_id: str) -> str:
    s = (url_or_id or "").strip()
    if not s:
        raise ValueError("空的 OpenReview id/url")
    if s.startswith("http"):
        query = parse_qs(urlparse(s).query)
        if query.get("id"):
            return query["id"][0]
        raise ValueError(f"无法从 URL 解析 forum id: {s}")
    return s


def _credentials():
    _load_env()
    return (
        os.environ.get("OPENREVIEW_USERNAME") or os.environ.get("OPENREVIEW_USER"),
        os.environ.get("OPENREVIEW_PASSWORD"),
        os.environ.get("OPENREVIEW_TOKEN"),
    )


def is_logged_in() -> bool:
    return _logged_in


def _read_cached_token() -> Optional[str]:
    try:
        if _TOKEN_FILE.exists():
            token = _TOKEN_FILE.read_text(encoding="utf-8").strip()
            return token or None
    except OSError:
        return None
    return None


def _write_cached_token(token: Optional[str]) -> None:
    if not token:
        return
    try:
        _TOKEN_FILE.parent.mkdir(parents=True, exist_ok=True)
        _TOKEN_FILE.write_text(token, encoding="utf-8")
    except OSError:
        pass


def _apply_user_agent(client) -> None:
    headers = getattr(client, "headers", None)
    if isinstance(headers, dict):
        headers["User-Agent"] = _API_USER_AGENT


def get_openreview_client(api: str = "v2"):
    """
    登录后速率更高，而且现在匿名访问 api2 经常会碰到 ChallengeRequired。
    凭据从环境变量读取：OPENREVIEW_USERNAME / OPENREVIEW_PASSWORD，或 OPENREVIEW_TOKEN。
    登录成功后会把 token 缓存到 store/，避免反复 login 触发 429。
    """
    global _client_v2, _client_v1, _logged_in
    username, password, token = _credentials()
    cached = _read_cached_token()
    token = token or cached

    if api == "v1":
        if _client_v1 is None:
            kwargs = {"baseurl": API1_BASE}
            if token:
                kwargs["token"] = token
            elif username and password:
                kwargs["username"] = username
                kwargs["password"] = password
            _client_v1 = openreview.Client(**kwargs)
            _apply_user_agent(_client_v1)
        return _client_v1

    if _client_v2 is None:
        kwargs = {"baseurl": API2_BASE, "tokenExpiresIn": TOKEN_EXPIRES_IN}
        client = None
        if token:
            try:
                client = openreview.api.OpenReviewClient(baseurl=API2_BASE, token=token)
                logger.info("使用缓存 token 访问 OpenReview API v2")
            except Exception:
                logger.info("缓存 token 失效，改用账号密码登录")
                client = None
        if client is None and username and password:
            try:
                client = openreview.api.OpenReviewClient(
                    baseurl=API2_BASE,
                    username=username,
                    password=password,
                    tokenExpiresIn=TOKEN_EXPIRES_IN,
                )
                logger.info("已登录 OpenReview API v2")
            except Exception:
                logger.warning("OpenReview 登录失败")
                client = None
        if client is None:
            try:
                if not (username and password):
                    logger.warning("未设置 OpenReview 账号，改为匿名访问")
                client = openreview.api.OpenReviewClient(baseurl=API2_BASE)
            except Exception:
                raise OpenReviewBlocked("OpenReview 无法连接") from None
        _apply_user_agent(client)
        _client_v2 = client
        _logged_in = bool(getattr(client, "token", None) or token or (username and password))
        _write_cached_token(getattr(client, "token", None))
    return _client_v2


def _as_str_list(value) -> List[str]:
    if not value:
        return []
    if isinstance(value, str):
        return [part.strip() for part in re.split(r",| and |;", value) if part.strip()]
    if isinstance(value, list):
        out = []
        for item in value:
            if isinstance(item, str) and item.strip():
                out.append(item.strip())
        return out
    return []


def _as_text(value) -> Optional[str]:
    if value is None:
        return None
    if isinstance(value, list):
        parts = [str(item).strip() for item in value if str(item).strip()]
        return "; ".join(parts) or None
    text = str(value).strip()
    return text or None


def _first_http(*values) -> Optional[str]:
    for value in values:
        if isinstance(value, str) and value.strip().startswith("http"):
            return value.strip()
        if isinstance(value, dict):
            for key in ("value", "url"):
                inner = value.get(key)
                if isinstance(inner, str) and inner.strip().startswith("http"):
                    return inner.strip()
    return None


def _presentation(*texts: Optional[str]) -> Optional[str]:
    for text in texts:
        if not text:
            continue
        low = text.lower()
        for label in ("spotlight", "oral", "poster"):
            if re.search(rf"\b{label}\b", low):
                return label
    return None


def _ms_date(value) -> Optional[str]:
    if value is None:
        return None
    try:
        stamp = int(value) / 1000
    except (TypeError, ValueError):
        return None
    return datetime.fromtimestamp(stamp, tz=timezone.utc).strftime("%Y-%m-%d")


def _looks_rejected(venue_text: Optional[str]) -> bool:
    if not venue_text:
        return False
    low = venue_text.lower()
    return any(token in low for token in ("reject", "withdraw", "desk reject"))


def _parse_note(note: Any) -> OpenReviewPaper:
    content = getattr(note, "content", None) or {}
    forum_id = getattr(note, "id", None) or getattr(note, "forum", None)
    authors = _as_str_list(note_content_value(content, "authors", []) or [])
    keywords = _as_str_list(note_content_value(content, "keywords", []) or [])
    pdf_field = note_content_value(content, "pdf")
    pdf_url = f"{WEB_BASE}/pdf?id={forum_id}"
    if isinstance(pdf_field, str) and pdf_field.startswith("http"):
        pdf_url = pdf_field
    venue_text = _as_text(note_content_value(content, "venue"))
    primary = None
    for key in ("primary_area", "primary_subject_area", "subject_area", "research_area"):
        primary = _as_text(note_content_value(content, key))
        if primary:
            break
    tldr = None
    for key in ("TLDR", "tldr", "TL;DR", "summary"):
        tldr = _as_text(note_content_value(content, key))
        if tldr:
            break
    bibtex = _as_text(note_content_value(content, "_bibtex") or note_content_value(content, "bibtex"))
    return OpenReviewPaper(
        forum_id=forum_id,
        url=f"{WEB_BASE}/forum?id={forum_id}",
        title=_as_text(note_content_value(content, "title")),
        authors=authors,
        abstract=_as_text(note_content_value(content, "abstract")),
        pdf_url=pdf_url,
        venue=venue_text,
        venueid=_as_text(note_content_value(content, "venueid")),
        keywords=keywords,
        number=getattr(note, "number", None),
        author_ids=_as_str_list(note_content_value(content, "authorids", []) or []),
        tldr=tldr,
        primary_area=primary,
        presentation=_presentation(
            _as_text(note_content_value(content, "presentation_type")),
            venue_text,
        ),
        bibtex=bibtex,
        code_url=_first_http(
            note_content_value(content, "code"),
            note_content_value(content, "code_url"),
            note_content_value(content, "software"),
        ),
        project_url=_first_http(
            note_content_value(content, "project_url"),
            note_content_value(content, "website"),
            note_content_value(content, "project"),
        ),
        published=_ms_date(getattr(note, "pdate", None) or getattr(note, "cdate", None)),
    )


def _looks_like_challenge(exc: Exception) -> bool:
    text = str(exc)
    return "ChallengeRequired" in text or "challenge verification" in text.lower()


def fetch_openreview_paper(url_or_id: str, client=None) -> OpenReviewPaper:
    forum_id = extract_forum_id(url_or_id)
    client = client or get_openreview_client("v2")
    try:
        note = client.get_note(forum_id)
        return _parse_note(note)
    except Exception as e:
        if _looks_like_challenge(e) and not is_logged_in():
            raise RuntimeError(
                "OpenReview 匿名接口被 challenge 拦截，请设置环境变量 "
                "OPENREVIEW_USERNAME 和 OPENREVIEW_PASSWORD 后重试"
            ) from e
        logger.info(f"API v2 读取失败，回退 API v1: {e}")
        client_v1 = get_openreview_client("v1")
        note = client_v1.get_note(forum_id)
        return _parse_note(note)


def _query_accepted(client, venue_id: str, limit: Optional[int] = None):
    kwargs = {"content": {"venueid": venue_id}}
    if limit:
        return client.get_notes(**kwargs, limit=limit)
    return client.get_all_notes(**kwargs)


def fetch_openreview_accepted(
    venue_id: str,
    client=None,
    limit: Optional[int] = None,
) -> List[OpenReviewPaper]:
    """录用稿的 content.venueid 等于会议本体 id，例如 ICLR.cc/2025/Conference。"""
    client = client or get_openreview_client("v2")
    notes = []
    try:
        notes = _query_accepted(client, venue_id, limit)
    except Exception as e:
        if _looks_like_challenge(e) and not is_logged_in():
            raise RuntimeError(
                "OpenReview 匿名接口被 challenge 拦截，请先登录账号"
            ) from e
        if _blocked_error(e):
            raise OpenReviewBlocked("OpenReview API v2 不可用") from None
        logger.info(f"API v2 列表失败，回退 API v1: {e}")
    if not notes:
        try:
            notes = _query_accepted(get_openreview_client("v1"), venue_id, limit) or []
        except Exception as e:
            if _blocked_error(e):
                raise OpenReviewBlocked("OpenReview API v1 不可用") from None
            logger.info(f"API v1 也没有结果: {e}")
            notes = []
    papers = []
    for note in notes:
        paper = _parse_note(note)
        if paper.venueid and paper.venueid != venue_id:
            continue
        if _looks_rejected(paper.venue):
            continue
        papers.append(paper)
    return papers


def fetch_openreview_records(
    venue_id: str,
    venue: str,
    year: int,
    limit: Optional[int] = None,
    client=None,
) -> List[dict]:
    """录用稿转成统一元数据，不下载 PDF。"""
    from paper_record import bibtex_field, make_record

    papers = fetch_openreview_accepted(venue_id, client=client, limit=limit)
    records = []
    for paper in papers:
        records.append(make_record(
            id=paper.forum_id,
            venue=venue,
            year=year,
            track="main",
            title=paper.title,
            authors=paper.authors,
            author_ids=paper.author_ids,
            abstract=paper.abstract,
            keywords=paper.keywords,
            tldr=paper.tldr,
            primary_area=paper.primary_area,
            presentation=paper.presentation,
            doi=bibtex_field(paper.bibtex, "doi"),
            pages=bibtex_field(paper.bibtex, "pages"),
            bibtex=paper.bibtex,
            url=paper.url,
            pdf_url=paper.pdf_url,
            code_url=paper.code_url,
            project_url=paper.project_url,
            published=paper.published,
            source="openreview",
        ))
    return records


def download_openreview_pdf(forum_id: str, dest_path: str, client=None, skip_existing: bool = True) -> str:
    from pdf_download import write_pdf_bytes

    forum_id = extract_forum_id(forum_id)
    client = client or get_openreview_client("v2")
    try:
        data = client.get_attachment(field_name="pdf", id=forum_id)
        return write_pdf_bytes(data, dest_path, skip_existing=skip_existing)
    except Exception as e:
        if _looks_like_challenge(e) and not is_logged_in():
            raise RuntimeError(
                "下载 OpenReview PDF 需要登录。请设置 OPENREVIEW_USERNAME / OPENREVIEW_PASSWORD"
            ) from e
        raise


if __name__ == "__main__":
    import json
    import sys

    target = sys.argv[1] if len(sys.argv) > 1 else "https://openreview.net/forum?id=G7sIFXugTX"
    paper = fetch_openreview_paper(target)
    print(json.dumps(asdict(paper), ensure_ascii=False, indent=2))
