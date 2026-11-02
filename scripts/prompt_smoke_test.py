#!/usr/bin/env python3
"""Smoke-test promptkit catalog files against an OpenAI-compatible chat API.

Each selected markdown prompt is parsed, variables are filled from the file's
own Variables table/examples (or short defaults), and sent as a single user
message (temperature 0.2). Responses are graded mechanically:

  FOLLOWED  structurally on-task / respects an obvious requested format
  PARTIAL   started but incomplete or off-spec
  FAILED    empty, refusal, or clearly the wrong task

Environment (never flags or source files):
  OLLAMA_API_KEY    required
  OLLAMA_BASE_URL   default https://ollama.com/v1

Results are appended as JSONL (one file per model) plus a checkpoint so reruns
skip completed (model, file) ids.

Examples:
  python scripts/prompt_smoke_test.py --models glm-5.3-flash,deepseek-v4.1-flash:1017 \\
      --category code --limit 2 --out ./smoke --concurrency 6

  python scripts/prompt_smoke_test.py --pilot --out /tmp/promptkit-smoke
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import threading
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

REPO_ROOT = Path(__file__).resolve().parent.parent
PROMPTS_ROOT = REPO_ROOT / "src" / "llm_promptkit" / "prompts"
DEFAULT_BASE = "https://ollama.com/v1"
DEFAULT_TEMPERATURE = 0.2
DEFAULT_CONCURRENCY = 6
MAX_TRIES = 4
REQUEST_TIMEOUT_S = 600
# Probe 2026-11-02 (glm-5.3-flash + deepseek-v4.1-flash:1017 @ ollama.com/v1):
# chat param think:false is accepted (HTTP 200) but not honored — reasoning
# still occupies the completion budget. Keep think:false (cheap when a model
# does honor it) and raise max_tokens so visible tokens can still land.
DEFAULT_MAX_TOKENS = 16384
SEND_THINK_FALSE = True
HARD_FAIL_STREAK_LIMIT = 5
PROGRESS_EVERY = 25
PREFERRED_MODELS = ("glm-5.3-flash", "deepseek-v4.1-flash:1017")
PILOT_CATEGORIES = ("code", "reasoning", "system", "debug", "defensive")
MODEL_ALIASES = {
    "deepseek-v4.1-flash-1017": "deepseek-v4.1-flash:1017",
    "deepseek-v4.1-flash:1017": "deepseek-v4.1-flash:1017",
}

# Bracket / ${name} slots whose example values are not in a Variables table.
DEFAULTS: Dict[str, str] = {
    "question": "What is 247 * 38?",
    "question/task": "What is 247 * 38?",
    "language": "Python",
    "purpose": "validates email addresses",
    "jobdescription": (
        "Senior Backend Engineer (Python/FastAPI), 5+ years, REST APIs, PostgreSQL."
    ),
    "resume": (
        "Alex Rivera. Backend engineer, 6 years Python. FastAPI services, "
        "PostgreSQL, pytest. B.Sc. CS 2018."
    ),
    "instrument": "AAPL (equity); evidence cutoff 2026-10-01",
    "evidence bundle": (
        "Market: AAPL 10-K excerpt (locator M1). Sentiment: mixed (S1). "
        "News: product launch 2026-09 (N1). Fundamentals: present (F1)."
    ),
    "round cap": "1",
    "nodes": (
        "worker (drafts artifact), reviewer (acceptance checks), "
        "controller (routes), escalation (dead-letter)"
    ),
    "state schema": (
        "run_id, artifact_version, current_artifact, acceptance_criteria, "
        "cycle_count, remaining_budget, reviewer_verdict, status"
    ),
    "max cycles": "3",
    "web search": "authorized, cap 2",
    "retry budgets": "2 rewrites / 2 regenerations / 8 tool calls",
    "corpus": (
        "Internal docs 2024-2026: billing FAQ and API guides; exclude marketing."
    ),
    "surface": (
        "Public REST API for a todo-list SaaS: create/list/update/delete items; "
        "no billing in v1."
    ),
    "consumers": "First-party web app and third-party API-key integrations.",
    "style rest/graphql/rpc": "REST, OpenAPI 3.1",
    "openapi document or versioned consumer contract": (
        '{"openapi":"3.0.0","info":{"title":"Todos","version":"1.0.0"},'
        '"paths":{"/todos":{"get":{"responses":{"200":{"description":"ok"}}}}}}'
    ),
    "client paths, operations and required test behaviors": (
        "GET /todos happy path plus 401; no live upstream calls."
    ),
    "language, test runner and existing mock tooling": "Python, pytest, respx",
    "stub, fixture, test and setup documentation paths": (
        "tests/mocks/todos.py, tests/test_todos_mock.py"
    ),
    "local binding, blocked upstream hosts and synthetic credentials": (
        "127.0.0.1, block api.example.com, token=test-token"
    ),
    "runtime": "CPython 3.12, single FastAPI worker, no sidecar",
    "workload": "100 req/s GET /todos, 5-minute steady, synthetic fixtures",
    "perf metric": "p95 latency ms; target <80ms; error rate must not rise",
    "websiteurl": "https://example.com",
    "website": "https://example.com",
}

REFUSAL_RE = re.compile(
    r"(?i)\b("
    r"i (cannot|can't|won't|am unable|will not) (help|assist|comply|provide|do that)"
    r"|as an ai( language model)?"
    r"|i'm (not |un)able to"
    r"|i am not able to"
    r"|refuse to"
    r"|against (my|our) (guidelines|policies)"
    r")\b"
)
FENCE_RE = re.compile(r"```(?:text|markdown|md|prompt)?\n(.*?)```", re.DOTALL)
VAR_TABLE_ROW_RE = re.compile(
    r"^\|\s*`?(\[[^\]]+\]|\$\{[^}]+\}|[A-Za-z0-9_./ -]+)`?\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|",
    re.MULTILINE,
)
VAR_BULLET_RE = re.compile(
    r"^[-*]\s+`?(\[[^\]]+\]|\$\{[^}]+\})`?\s*[:—-]\s*(.+)$",
    re.MULTILINE,
)
DOLLAR_RE = re.compile(r"\$\{([^{}]+)\}")
BRACKET_RE = re.compile(r"\[([^\[\]]{1,120})\]")
HINT_RETURN_RE = re.compile(
    r"(?im)^(?:return|respond with|format(?: your response)? as|output(?: format)?[: ]+)\s*(.+)$"
)
JSONL_LOCK = threading.Lock()


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def stamp_now() -> str:
    return utc_now().strftime("%Y%m%d")


def iso_now() -> str:
    return utc_now().replace(microsecond=0).isoformat().replace("+00:00", "Z")


def die(message: str, code: int = 2) -> None:
    print(message, file=sys.stderr)
    raise SystemExit(code)


def normalize_base(url: str) -> str:
    url = url.rstrip("/")
    if url.endswith("/chat/completions"):
        url = url[: -len("/chat/completions")]
    if not url.endswith("/v1"):
        url = url + "/v1"
    return url


def safe_model_name(model: str) -> str:
    return re.sub(r"[^A-Za-z0-9._+-]+", "-", model).strip("-")


def record_id(model: str, rel: str) -> str:
    return f"{model}::{rel}"


def section_after(text: str, heading: str) -> str:
    match = re.search(rf"(?im)^## {re.escape(heading)}\s*$", text)
    if not match:
        return ""
    rest = text[match.end() :]
    nxt = re.search(r"(?im)^## ", rest)
    return rest[: nxt.start()] if nxt else rest


def _strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[2]
    return text


def extract_prompt_body(text: str) -> str:
    """Take the first fenced block after ## The Prompt (body may contain ## headings).

    Model-optimized / multi-prompt files often omit ## The Prompt; fall back to
    the first fenced block, then the body after frontmatter.
    """
    match = re.search(r"(?im)^## The Prompt\s*$", text)
    if not match:
        fenced = FENCE_RE.search(text)
        if fenced:
            return fenced.group(1).strip()
        fallback = _strip_frontmatter(text).strip()
        if not fallback:
            raise ValueError("missing ## The Prompt and no fenced prompt body")
        return fallback
    rest = text[match.end() :]
    lines = rest.splitlines()
    idx = 0
    while idx < len(lines) and not lines[idx].strip():
        idx += 1
    if idx < len(lines) and lines[idx].strip().startswith("```"):
        idx += 1
        body: List[str] = []
        while idx < len(lines):
            if lines[idx].strip() == "```":
                break
            body.append(lines[idx])
            idx += 1
        return "\n".join(body).strip()
    fenced = FENCE_RE.search(rest)
    if fenced:
        return fenced.group(1).strip()
    nxt = re.search(r"(?im)^## ", rest)
    block = rest[: nxt.start()] if nxt else rest
    return block.strip()


def _strip_ticks(value: str) -> str:
    value = value.strip()
    if value.startswith("`") and value.endswith("`") and len(value) >= 2:
        return value[1:-1].strip()
    return value


def _slot_key(raw: str) -> str:
    raw = raw.strip()
    if raw.startswith("[") and raw.endswith("]") and len(raw) >= 2:
        raw = raw[1:-1]
    if raw.startswith("${") and raw.endswith("}") and len(raw) >= 3:
        raw = raw[2:-1]
    if ":" in raw and re.match(r"^[A-Za-z0-9_]+\:", raw):
        raw = raw.split(":", 1)[0]
    return raw.strip().lower()


def parse_variable_examples(text: str) -> Dict[str, str]:
    """Map slot key -> example/default from the Variables section (or prompt)."""
    found: Dict[str, str] = {}
    section = section_after(text, "Variables")
    for match in VAR_TABLE_ROW_RE.finditer(section):
        name, _desc, example = match.groups()
        if name.lower().strip(" `") in {"variable", "----------"}:
            continue
        example = _strip_ticks(example)
        if example and example.lower() not in {"example", "---", "---------"}:
            found[_slot_key(name)] = example
    for match in VAR_BULLET_RE.finditer(section):
        name, desc = match.groups()
        key = _slot_key(name)
        if key not in found:
            # bullets rarely have examples; keep description for defaults later
            found.setdefault(f"__desc__{key}", desc.strip())
    # ${name:default} declarations inside the prompt itself
    body = extract_prompt_body(text)
    for inner in DOLLAR_RE.findall(body):
        if ":" in inner:
            name, default = inner.split(":", 1)
            default = default.strip()
            if default:
                found[_slot_key(name)] = default
    return found


def default_for(name: str, desc: str = "") -> str:
    key = _slot_key(name)
    if key in DEFAULTS:
        return DEFAULTS[key]
    for known, value in DEFAULTS.items():
        if known in key or key in known:
            return value
    if desc:
        return f"example {desc[:72]}"
    return f"example {name.strip()[:72]}"


def is_bracket_slot(inner: str) -> bool:
    inner = inner.strip()
    if not inner or len(inner) > 80:
        return False
    if re.fullmatch(r"\d+", inner):
        return False
    if inner.lower().endswith((".md", ".py", ".json")):
        return False
    if "http://" in inner.lower() or "https://" in inner.lower():
        return False
    if inner.count(" ") > 12:
        return False
    return bool(re.search(r"[A-Za-z]", inner))


def fill_variables(prompt: str, examples: Dict[str, str]) -> Tuple[str, Dict[str, str], List[str]]:
    """Replace [slots] and ${slots}; return (text, filled, leftover_slots)."""
    filled: Dict[str, str] = {}

    def value_for(raw: str) -> str:
        key = _slot_key(raw)
        desc = examples.get(f"__desc__{key}", "")
        if key in examples:
            val = examples[key]
        elif raw in examples:
            val = examples[raw]
        else:
            val = default_for(raw, desc)
        filled[key] = val
        return val

    def repl_dollar(match: re.Match[str]) -> str:
        inner = match.group(1)
        if ":" in inner:
            name, default = inner.split(":", 1)
            key = _slot_key(name)
            if key in examples:
                filled[key] = examples[key]
                return examples[key]
            if default.strip():
                filled[key] = default.strip()
                return default.strip()
            return value_for(name)
        return value_for(inner)

    text = DOLLAR_RE.sub(repl_dollar, prompt)

    def repl_bracket(match: re.Match[str]) -> str:
        inner = match.group(1)
        if not is_bracket_slot(inner):
            return match.group(0)
        return value_for(inner)

    text = BRACKET_RE.sub(repl_bracket, text)

    leftovers: List[str] = []
    leftovers.extend(f"${{{m}}}" for m in DOLLAR_RE.findall(text))
    leftovers.extend(f"[{m}]" for m in BRACKET_RE.findall(text) if is_bracket_slot(m))
    return text, filled, leftovers


def format_hints(prompt: str) -> List[str]:
    hints: List[str] = []
    for match in HINT_RETURN_RE.finditer(prompt):
        hints.append(match.group(1).strip()[:160])
    for token in (
        "READY FOR CONTRACT REVIEW",
        "PROVISIONAL",
        "BLOCKED",
        "ANSWERED",
        "ABSTAIN",
        "ESCALATE",
        "SPECIFICATION-ONLY",
        "INSUFFICIENT EVIDENCE",
        "INCONCLUSIVE",
        "JSON",
    ):
        if token.lower() in prompt.lower() and token not in hints:
            hints.append(token)
    return hints


def grade(prompt: str, response: str, finish_reason: str, reasoning: str = "") -> str:
    text = (response or "").strip()
    if not text:
        # Reasoning models may exhaust max_tokens on hidden thinking.
        if (reasoning or "").strip():
            return "PARTIAL"
        return "FAILED"
    if REFUSAL_RE.search(text) and len(text) < 1200:
        return "FAILED"
    lowered = text.lower()
    off_task = (
        "what would you like me to do" in lowered
        or "please provide the" in lowered and len(text) < 200
        or lowered.startswith("i'm ready")
        and len(text) < 120
    )
    hints = format_hints(prompt)
    if hints:
        hits = 0
        blob = text.lower()
        for hint in hints:
            token = hint.split(",")[0].split(";")[0].strip()
            if len(token) >= 4 and token.lower() in blob:
                hits += 1
            elif any(part.strip().lower() in blob for part in re.split(r"[/,;]", hint) if len(part.strip()) >= 4):
                hits += 1
        if hits == 0:
            return "PARTIAL"
        if finish_reason == "length":
            return "PARTIAL"
        return "FOLLOWED"
    if off_task:
        return "PARTIAL"
    if len(text) < 40:
        return "PARTIAL"
    if finish_reason == "length" and len(text) < 200:
        return "PARTIAL"
    return "FOLLOWED"


def http_json(
    method: str,
    url: str,
    api_key: str,
    payload: Optional[dict] = None,
    timeout: int = REQUEST_TIMEOUT_S,
) -> Tuple[int, Any]:
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Authorization", f"Bearer {api_key}")
    req.add_header("Accept", "application/json")
    if data is not None:
        req.add_header("Content-Type", "application/json")
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            raw = resp.read().decode("utf-8", "replace")
            try:
                parsed: Any = json.loads(raw) if raw else {}
            except json.JSONDecodeError:
                parsed = raw
            return int(resp.status), parsed
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", "replace")
        try:
            parsed = json.loads(raw) if raw else {"error": str(exc)}
        except json.JSONDecodeError:
            parsed = {"error": raw or str(exc)}
        return int(exc.code), parsed
    except urllib.error.URLError as exc:
        return 0, {"error": str(exc.reason if getattr(exc, "reason", None) else exc)}
    except TimeoutError as exc:
        return 0, {"error": f"TimeoutError: {exc}"}


def list_models(base: str, api_key: str) -> List[str]:
    status, body = http_json("GET", f"{base}/models", api_key, timeout=30)
    if status != 200:
        die(f"model probe failed HTTP {status}: {body!r}"[:400])
    names: List[str] = []
    if isinstance(body, dict):
        rows = body.get("data") or body.get("models") or []
        if isinstance(rows, list):
            for row in rows:
                if isinstance(row, dict):
                    name = row.get("id") or row.get("name") or row.get("model")
                    if name:
                        names.append(str(name))
                elif isinstance(row, str):
                    names.append(row)
    return names


def resolve_models(requested: Sequence[str], available: Sequence[str]) -> List[str]:
    catalog = list(available)
    catalog_l = {name.lower(): name for name in catalog}
    resolved: List[str] = []
    missing: List[str] = []
    for raw in requested:
        raw = raw.strip()
        if not raw:
            continue
        alias = MODEL_ALIASES.get(raw, raw)
        if alias in catalog:
            resolved.append(alias)
            continue
        if alias.lower() in catalog_l:
            resolved.append(catalog_l[alias.lower()])
            continue
        # hyphen/colon swap (deepseek-v4.1-flash-1017 vs :1017)
        swapped = alias.replace("-", ":", 1) if alias.count(":") == 0 and "-" in alias else alias.replace(":", "-")
        if swapped in catalog:
            resolved.append(swapped)
            continue
        if swapped.lower() in catalog_l:
            resolved.append(catalog_l[swapped.lower()])
            continue
        missing.append(raw)
    if missing:
        die("requested models not in API catalog: " + ", ".join(missing) + "\navailable: " + ", ".join(catalog))
    # de-dupe, preserve order
    out: List[str] = []
    for name in resolved:
        if name not in out:
            out.append(name)
    return out


def pick_preferred(available: Sequence[str]) -> List[str]:
    return resolve_models(PREFERRED_MODELS, available)


def resolve_file_filter(spec: str) -> set[Path]:
    """Read comma-separated paths and/or text lists; reject invalid prompt paths.

    Prompt paths are relative to PROMPTS_ROOT or REPO_ROOT. Text-list paths
    are relative to the working directory (absolute paths are also accepted).
    Lists contain one prompt path per line; blank lines and # comments are ignored.
    """
    entries: List[str] = []
    for token in spec.split(","):
        token = token.strip()
        if not token:
            continue
        source = Path(token).expanduser()
        if source.suffix.lower() != ".md" and source.is_file():
            try:
                entries.extend(
                    line.strip()
                    for line in source.read_text(encoding="utf-8").splitlines()
                    if line.strip() and not line.lstrip().startswith("#")
                )
            except (OSError, UnicodeError) as exc:
                die(f"cannot read --files list {token}: {exc}")
        else:
            entries.append(token)
    if not entries:
        die("--files must select at least one prompt")
    selected: set[Path] = set()
    for entry in entries:
        relative = Path(entry)
        if relative.is_absolute() or ".." in relative.parts:
            die(f"--files requires relative prompt paths without '..': {entry}")
        candidates = (PROMPTS_ROOT / relative, REPO_ROOT / relative)
        matched = False
        for candidate in candidates:
            path = candidate.resolve()
            if (
                PROMPTS_ROOT.resolve() in path.parents
                and path.is_file()
                and path.suffix == ".md"
                and path.name.lower() != "readme.md"
            ):
                selected.add(path)
                matched = True
                break
        if not matched:
            die(f"unknown prompt in --files: {entry}")
    return selected


def discover_prompts(
    categories: Optional[Sequence[str]],
    limit: Optional[int],
    per_category: Optional[int],
    files: Optional[str] = None,
) -> List[Path]:
    if not PROMPTS_ROOT.is_dir():
        die(f"prompts root missing: {PROMPTS_ROOT}")
    wanted = [c.strip() for c in (categories or []) if c.strip()]
    if wanted:
        dirs = []
        for cat in wanted:
            path = PROMPTS_ROOT / cat
            if not path.is_dir():
                die(f"unknown category: {cat}")
            dirs.append(path)
    else:
        dirs = sorted(p for p in PROMPTS_ROOT.iterdir() if p.is_dir())
    file_filter = resolve_file_filter(files) if files is not None else None
    selected: List[Path] = []
    for folder in dirs:
        category_files = sorted(
            p for p in folder.rglob("*.md")
            if p.name.lower() != "readme.md"
            and (file_filter is None or p.resolve() in file_filter)
        )
        if per_category is not None:
            category_files = category_files[:per_category]
        selected.extend(category_files)
    if limit is not None:
        selected = selected[:limit]
    return selected


def load_checkpoint(path: Path) -> set:
    if not path.is_file():
        return set()
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return set()
    done = data.get("done") if isinstance(data, dict) else None
    if isinstance(done, list):
        return set(str(x) for x in done)
    return set()


def save_checkpoint(path: Path, done: Iterable[str]) -> None:
    payload = {
        "updated": iso_now(),
        "done": sorted(set(done)),
    }
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def load_jsonl_ids(path: Path) -> set:
    ids: set[str] = set()
    if not path.is_file():
        return ids
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            try:
                row = json.loads(line)
            except json.JSONDecodeError:
                continue
            rid = row.get("id")
            if rid:
                ids.add(str(rid))
            elif row.get("model") and row.get("file"):
                ids.add(record_id(str(row["model"]), str(row["file"])))
    return ids


def append_jsonl(path: Path, row: dict) -> None:
    line = json.dumps(row, ensure_ascii=False) + "\n"
    with JSONL_LOCK:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as handle:
            handle.write(line)
            handle.flush()
            os.fsync(handle.fileno())


def chat_completion(
    base: str,
    api_key: str,
    model: str,
    content: str,
    temperature: float,
    max_tokens: int,
    think: Optional[bool] = False,
) -> Tuple[int, dict, int]:
    """Return (http_status, body, retries_used). Retries 429 with exponential backoff."""
    url = f"{base}/chat/completions"
    payload: Dict[str, Any] = {
        "model": model,
        "messages": [{"role": "user", "content": content}],
        "temperature": temperature,
        "max_tokens": max_tokens,
        "stream": False,
    }
    if think is not None:
        payload["think"] = think
    delay = 1.0
    last_status = 0
    last_body: Any = {}
    retries = 0
    for attempt in range(MAX_TRIES):
        status, body = http_json("POST", url, api_key, payload)
        last_status, last_body = status, body if isinstance(body, dict) else {"error": body}
        if status != 429:
            return status, last_body, retries
        retries += 1
        if attempt == MAX_TRIES - 1:
            break
        time.sleep(delay)
        delay *= 2
    return last_status, last_body, retries


def usage_tokens(body: dict) -> Tuple[Optional[int], Optional[int]]:
    usage = body.get("usage") if isinstance(body, dict) else None
    if not isinstance(usage, dict):
        return None, None
    prompt = usage.get("prompt_tokens")
    completion = usage.get("completion_tokens")
    try:
        p = int(prompt) if prompt is not None else None
    except (TypeError, ValueError):
        p = None
    try:
        c = int(completion) if completion is not None else None
    except (TypeError, ValueError):
        c = None
    return p, c


def _flatten_text(value: Any) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, list):
        parts = []
        for item in value:
            if isinstance(item, dict) and isinstance(item.get("text"), str):
                parts.append(item["text"])
            elif isinstance(item, str):
                parts.append(item)
        return "".join(parts)
    return str(value or "")


def response_text(body: dict) -> Tuple[str, str, str]:
    choices = body.get("choices") if isinstance(body, dict) else None
    if not isinstance(choices, list) or not choices:
        err = body.get("error") if isinstance(body, dict) else None
        if isinstance(err, dict):
            return "", str(err.get("message") or err), ""
        return "", str(err or ""), ""
    choice = choices[0] if isinstance(choices[0], dict) else {}
    finish = str(choice.get("finish_reason") or "")
    raw_msg = choice.get("message")
    message: dict = raw_msg if isinstance(raw_msg, dict) else {}
    content = _flatten_text(message.get("content"))
    reasoning = _flatten_text(message.get("reasoning") or message.get("reasoning_content") or "")
    return content, finish, reasoning


def estimate_tokens(text: str) -> int:
    # ~4 chars/token fallback when the API omits usage
    return max(1, (len(text) + 3) // 4)


def jsonl_path(out_dir: Path, model: str, stamp: str) -> Path:
    return out_dir / f"promptkit-smoke-results-{safe_model_name(model)}-{stamp}.jsonl"


def run_one(
    *,
    path: Path,
    model: str,
    base: str,
    api_key: str,
    temperature: float,
    max_tokens: int,
    think: Optional[bool] = False,
) -> dict:
    rel = path.relative_to(PROMPTS_ROOT).as_posix()
    category = path.parent.name
    raw = path.read_text(encoding="utf-8")
    body = extract_prompt_body(raw)
    examples = parse_variable_examples(raw)
    filled_prompt, filled, leftovers = fill_variables(body, examples)
    t0 = time.perf_counter()
    status, payload, retries = chat_completion(
        base, api_key, model, filled_prompt, temperature, max_tokens, think=think
    )
    latency = round(time.perf_counter() - t0, 3)
    if isinstance(payload, dict):
        text, finish, reasoning = response_text(payload)
    else:
        text, finish, reasoning = "", "", ""
    prompt_tokens, completion_tokens = usage_tokens(payload if isinstance(payload, dict) else {})
    if prompt_tokens is None:
        prompt_tokens = estimate_tokens(filled_prompt)
    if completion_tokens is None:
        completion_tokens = estimate_tokens(text) if text else 0
    error = None
    if status != 200:
        error = payload.get("error") if isinstance(payload, dict) else payload
        if isinstance(error, dict):
            error = error.get("message") or json.dumps(error)
        grade_status = "FAILED"
        text = text or ""
    else:
        grade_status = grade(filled_prompt, text, finish, reasoning)
    preview = re.sub(r"\s+", " ", text).strip()[:400]
    return {
        "id": record_id(model, rel),
        "file": rel,
        "category": category,
        "model": model,
        "status": grade_status,
        "latency_s": latency,
        "prompt_tokens": prompt_tokens,
        "completion_tokens": completion_tokens,
        "timestamp": iso_now(),
        "http_status": status,
        "retries": retries,
        "finish_reason": finish,
        "unfilled": leftovers,
        "filled_keys": sorted(filled.keys()),
        "error": error,
        "response_preview": preview,
        "prompt_chars": len(filled_prompt),
        "response_chars": len(text),
        "reasoning_chars": len(reasoning or ""),
        "max_tokens": max_tokens,
        "think": think,
    }


def summarize(rows: Sequence[dict], models: Sequence[str], available: Sequence[str]) -> dict:
    counts = {"FOLLOWED": 0, "PARTIAL": 0, "FAILED": 0}
    tokens_in = 0
    tokens_out = 0
    latency = 0.0
    retries_429 = 0
    unfilled_files = []
    for row in rows:
        counts[row.get("status", "FAILED")] = counts.get(row.get("status", "FAILED"), 0) + 1
        tokens_in += int(row.get("prompt_tokens") or 0)
        tokens_out += int(row.get("completion_tokens") or 0)
        latency += float(row.get("latency_s") or 0)
        retries_429 += int(row.get("retries") or 0)
        if row.get("unfilled"):
            unfilled_files.append({"file": row.get("file"), "unfilled": row.get("unfilled")})
    n = max(len(rows), 1)
    per_call_in = tokens_in / n
    per_call_out = tokens_out / n
    per_call_s = latency / n
    sweep_calls = 374 * len(models)
    return {
        "models": list(models),
        "available_count": len(available),
        "available": list(available),
        "pilot_calls": len(rows),
        "counts": counts,
        "prompt_tokens": tokens_in,
        "completion_tokens": tokens_out,
        "total_tokens": tokens_in + tokens_out,
        "latency_s": round(latency, 3),
        "retries_429": retries_429,
        "unfilled": unfilled_files,
        "est_full_sweep_calls": sweep_calls,
        "est_full_sweep_prompt_tokens": int(per_call_in * sweep_calls),
        "est_full_sweep_completion_tokens": int(per_call_out * sweep_calls),
        "est_full_sweep_total_tokens": int((per_call_in + per_call_out) * sweep_calls),
        "est_full_sweep_wall_s_at_concurrency_6": round(per_call_s * sweep_calls / 6, 1),
    }


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Smoke-test promptkit prompts against Ollama Cloud (or any OpenAI-compatible chat API).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=(
            "Env: OLLAMA_API_KEY (required), OLLAMA_BASE_URL (default https://ollama.com/v1).\n"
            "Checkpoint + JSONL under --out make reruns idempotent."
        ),
    )
    parser.add_argument("--models", default="", help="Comma-separated model ids")
    parser.add_argument("--limit", type=int, default=None, help="Max prompts (not calls)")
    parser.add_argument(
        "--files",
        default=None,
        help=(
            "Comma-separated prompt paths (relative to src/llm_promptkit/prompts or repo root) "
            "and/or text-list paths (one prompt per line); intersects category filters "
            "before --per-category and --limit"
        ),
    )
    parser.add_argument(
        "--category",
        default="",
        help="Category filter; comma-separated (code,reasoning,...)",
    )
    parser.add_argument("--out", default="-", help="Output directory for JSONL + checkpoint")
    parser.add_argument(
        "--concurrency",
        type=int,
        default=DEFAULT_CONCURRENCY,
        help=f"Thread-pool size (default {DEFAULT_CONCURRENCY})",
    )
    parser.add_argument(
        "--per-category",
        type=int,
        default=None,
        help="Take the first N prompts alphabetically from each category",
    )
    parser.add_argument(
        "--pilot",
        action="store_true",
        help="10-prompt pilot: 2 per code/reasoning/system/debug/defensive, preferred model pair",
    )
    parser.add_argument("--probe", action="store_true", help="List API models and exit")
    parser.add_argument("--temperature", type=float, default=DEFAULT_TEMPERATURE)
    parser.add_argument("--max-tokens", type=int, default=DEFAULT_MAX_TOKENS)
    parser.add_argument("--stamp", default="", help="Filename date stamp (default UTC YYYYMMDD)")
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = parse_args(argv)
    api_key = os.environ.get("OLLAMA_API_KEY", "").strip()
    if not api_key:
        die("OLLAMA_API_KEY is not set")
    base = normalize_base(os.environ.get("OLLAMA_BASE_URL", DEFAULT_BASE).strip() or DEFAULT_BASE)
    available = list_models(base, api_key)
    print(
        f"probe: {len(available)} models at {base} "
        f"(preferred present: "
        + ", ".join(
            f"{m}={'yes' if m in available else 'NO'}" for m in PREFERRED_MODELS
        )
        + ")"
    )
    if args.probe:
        for name in available:
            print(name)
        return 0

    if args.pilot:
        categories = list(PILOT_CATEGORIES)
        per_category = 2
        limit = args.limit if args.files is not None else None
        requested = [m.strip() for m in args.models.split(",") if m.strip()] or list(
            PREFERRED_MODELS
        )
    else:
        categories = [c.strip() for c in args.category.split(",") if c.strip()]
        per_category = args.per_category
        limit = args.limit
        requested = [m.strip() for m in args.models.split(",") if m.strip()]
        if not requested:
            die("--models is required (or pass --pilot)")

    models = resolve_models(requested, available)
    if len(models) < 1:
        die("no models resolved")

    prompts = discover_prompts(categories or None, limit, per_category, files=args.files)
    if not prompts:
        die("no prompts selected")

    stamp = args.stamp or stamp_now()
    if args.out in {"", "-"}:
        die("--out DIR is required")
    out_dir = Path(args.out).expanduser().resolve()
    out_dir.mkdir(parents=True, exist_ok=True)
    checkpoint_path = out_dir / f"promptkit-smoke-checkpoint-{stamp}.json"

    done = load_checkpoint(checkpoint_path)
    for model in models:
        done |= load_jsonl_ids(jsonl_path(out_dir, model, stamp))

    jobs: List[Tuple[str, Path]] = []
    skipped = 0
    for path in prompts:
        rel = path.relative_to(PROMPTS_ROOT).as_posix()
        for model in models:
            if record_id(model, rel) in done:
                skipped += 1
                continue
            jobs.append((model, path))

    print(
        f"selected {len(prompts)} prompts × {len(models)} models; "
        f"{len(jobs)} calls queued, {skipped} skipped (checkpoint)"
    )
    if not jobs:
        print("nothing to do")
        return 0

    think_param: Optional[bool] = False if SEND_THINK_FALSE else None
    print(
        "think:false probe (2026-11-02): accepted=yes honored=no; "
        f"sending think={think_param!r} max_tokens={args.max_tokens}",
        file=sys.stderr,
        flush=True,
    )

    rows: List[dict] = []
    checkpoint_done = set(done)
    stop_event = threading.Event()
    hard_streak = 0
    hard_fail_rows: List[dict] = []
    completed = 0
    paused = False
    status_counts = {"FOLLOWED": 0, "PARTIAL": 0, "FAILED": 0}

    def worker(job: Tuple[str, Path]) -> Optional[dict]:
        if stop_event.is_set():
            return None
        model, path = job
        try:
            return run_one(
                path=path,
                model=model,
                base=base,
                api_key=api_key,
                temperature=args.temperature,
                max_tokens=args.max_tokens,
                think=think_param,
            )
        except Exception as exc:  # keep sweep alive; record as FAILED
            rel = path.relative_to(PROMPTS_ROOT).as_posix()
            return {
                "id": record_id(model, rel),
                "file": rel,
                "category": path.parent.name,
                "model": model,
                "status": "FAILED",
                "latency_s": 0.0,
                "prompt_tokens": 0,
                "completion_tokens": 0,
                "timestamp": iso_now(),
                "http_status": 0,
                "retries": 0,
                "finish_reason": "",
                "unfilled": [],
                "filled_keys": [],
                "error": f"{type(exc).__name__}: {exc}",
                "response_preview": "",
                "prompt_chars": 0,
                "response_chars": 0,
                "reasoning_chars": 0,
                "max_tokens": args.max_tokens,
                "think": think_param,
            }

    concurrency = max(1, int(args.concurrency))
    with ThreadPoolExecutor(max_workers=concurrency) as pool:
        futures = [pool.submit(worker, job) for job in jobs]
        for fut in as_completed(futures):
            if stop_event.is_set() and fut.cancelled():
                continue
            try:
                row = fut.result()
            except Exception as exc:
                print(f"worker crashed: {exc}", file=sys.stderr)
                continue
            if row is None:
                continue
            append_jsonl(jsonl_path(out_dir, str(row["model"]), stamp), row)
            checkpoint_done.add(row["id"])
            save_checkpoint(checkpoint_path, checkpoint_done)
            rows.append(row)
            completed += 1
            status_counts[row.get("status", "FAILED")] = (
                status_counts.get(row.get("status", "FAILED"), 0) + 1
            )
            print(
                f"{row['status']:8} {row['model']} {row['file']} "
                f"{row['latency_s']}s in={row['prompt_tokens']} out={row['completion_tokens']}"
                + (f" unfilled={row['unfilled']}" if row.get("unfilled") else "")
                + (f" err={row['error']}" if row.get("error") else "")
            )
            http_status = int(row.get("http_status") or 0)
            if http_status != 200:
                hard_streak += 1
                hard_fail_rows.append(row)
                if hard_streak >= HARD_FAIL_STREAK_LIMIT:
                    stop_event.set()
                    paused = True
                    last_ids = ", ".join(
                        str(r.get("id")) for r in hard_fail_rows[-HARD_FAIL_STREAK_LIMIT:]
                    )
                    print(
                        f"PAUSE: {hard_streak} consecutive hard failures "
                        f"(http != 200). Last ids: {last_ids}",
                        file=sys.stderr,
                        flush=True,
                    )
                    for pending in futures:
                        pending.cancel()
                    break
            else:
                hard_streak = 0
            if completed % PROGRESS_EVERY == 0:
                print(
                    f"progress: {completed}/{len(jobs)} calls "
                    f"FOLLOWED={status_counts.get('FOLLOWED', 0)} "
                    f"PARTIAL={status_counts.get('PARTIAL', 0)} "
                    f"FAILED={status_counts.get('FAILED', 0)} "
                    f"hard_streak={hard_streak}",
                    file=sys.stderr,
                    flush=True,
                )

    if paused:
        print(
            f"paused after {completed}/{len(jobs)} new calls; "
            f"rerun resumes from checkpoint {checkpoint_path}",
            file=sys.stderr,
            flush=True,
        )

    # rebuild from JSONL so summary includes skipped-already-done rows from this stamp
    all_rows: List[dict] = []
    for model in models:
        path = jsonl_path(out_dir, model, stamp)
        if not path.is_file():
            continue
        with path.open(encoding="utf-8") as handle:
            for line in handle:
                line = line.strip()
                if line:
                    try:
                        all_rows.append(json.loads(line))
                    except json.JSONDecodeError:
                        continue
    summary = summarize(all_rows, models, available)
    summary_path = out_dir / f"promptkit-smoke-summary-{stamp}.json"
    summary_path.write_text(json.dumps(summary, indent=2) + "\n", encoding="utf-8")
    print(
        f"summary {summary['counts']} tokens {summary['total_tokens']} "
        f"(in {summary['prompt_tokens']} / out {summary['completion_tokens']}) "
        f"429s={summary['retries_429']}"
    )
    print(f"artifacts: {out_dir}")
    return 3 if paused else 0


if __name__ == "__main__":
    raise SystemExit(main())
