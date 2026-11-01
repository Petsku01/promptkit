"""Safe string-valued YAML frontmatter, retaining the original body bytes."""

from typing import Dict, Tuple

import yaml


def split_frontmatter(content: bytes) -> Tuple[Dict[str, str], bytes, bytes]:
    """Return (metadata, original frontmatter, original body), without normalization.

    Missing frontmatter is supported for legacy/custom templates. Malformed YAML,
    non-mappings and non-string values raise ValueError; no Python tags are loaded.
    """
    lines = content.splitlines(keepends=True)
    if not lines or lines[0].rstrip(b"\r\n") != b"---":
        return {}, b"", content
    for index, line in enumerate(lines[1:], 1):
        if line.rstrip(b"\r\n") == b"---":
            try:
                metadata = yaml.safe_load(b"".join(lines[1:index]).decode("utf-8"))
            except (yaml.YAMLError, UnicodeDecodeError) as exc:
                raise ValueError(f"Invalid YAML frontmatter: {exc}") from exc
            if not isinstance(metadata, dict) or not all(
                isinstance(key, str) and isinstance(value, str)
                for key, value in metadata.items()
            ):
                raise ValueError("Frontmatter must be a mapping of strings to strings")
            return metadata, b"".join(lines[:index + 1]), b"".join(lines[index + 1:])
    raise ValueError("Unclosed YAML frontmatter")
