"""Metadata, byte preservation and deterministic documentation regression tests."""

import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

from llm_promptkit.patterns import _registry as registry

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("generate_docs", ROOT / "scripts/generate_docs.py")
generator = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(generator)


def test_yaml_frontmatter_is_removed_from_template(tmp_path):
    path = tmp_path / "test.md"
    path.write_text('---\ncategory: reasoning\ntitle: "Example: safe"\n---\n# Example\n\nBody $task\n')
    assert registry._parse_pattern_body(path) == "Body $task"


def test_metadata_getters_read_frontmatter(tmp_path, monkeypatch):
    path = tmp_path / "test.md"
    path.write_text('---\ncategory: output\nsource: prompts.chat\nlicense: CC0\n---\n# Test\nBody\n')
    monkeypatch.setattr(registry, "_scan_pattern", lambda *_: (path, "custom"))
    assert registry.get_pattern_category("test") == "output"
    assert registry.get_pattern_attribution("test") == "prompts.chat"
    assert registry.get_pattern_license("test") == "CC0"
    assert registry.get_pattern_source("test") == "custom"  # existing API: origin, not attribution


def test_unknown_license_is_absent():
    metadata = registry.get_pattern_metadata("chain-of-thought")
    assert metadata["category"] == "reasoning"
    assert "license" not in metadata
    assert registry.get_pattern_license("chain-of-thought") is None
    assert registry.get_pattern_attribution("chain-of-thought") is None


def test_missing_pattern_metadata_raises():
    with pytest.raises(registry.PatternNotFoundError):
        registry.get_pattern_metadata("not-a-real-pattern")


def test_legacy_pattern_category_fallback(tmp_path, monkeypatch):
    path = tmp_path / "legacy.md"
    path.write_text("# Legacy\n\n**Category:** reasoning\n\nBody\n")
    monkeypatch.setattr(registry, "_scan_pattern", lambda *_: (path, "custom"))
    assert registry.get_pattern_category("legacy") == tmp_path.name
    assert registry._parse_pattern_body(path) == "Body"


@pytest.mark.parametrize("header", ["category: [a, b]", "!!python/object:builtins.object {}", "- not-a-map"])
def test_invalid_yaml_is_load_error(tmp_path, header):
    path = tmp_path / "bad.md"
    path.write_text(f"---\n{header}\n---\nBody\n")
    with pytest.raises(registry.PatternLoadError):
        registry._parse_pattern_body(path)


def test_every_content_file_has_path_metadata():
    from llm_promptkit.metadata import split_frontmatter

    for kind in ("prompts", "patterns"):
        base = ROOT / "src/llm_promptkit" / kind
        files = [p for p in base.rglob("*.md") if p.name.lower() != "readme.md"]
        assert len(files) >= 19  # sanity floor: catalog keeps growing, not shrinking
        for path in files:
            metadata, _, _ = split_frontmatter(path.read_bytes())
            parts = path.relative_to(base).parts
            assert metadata["category"] == parts[0]
            assert metadata["title"]
            if len(parts) > 2:
                assert metadata["subcategory"] == parts[1]
            if len(parts) == 4:
                assert metadata["model"] == parts[2]
            assert metadata.get("license") in (None, "MIT", "CC0")


def test_source_content_bytes_unchanged_from_head():
    from llm_promptkit.metadata import split_frontmatter

    for kind in ("prompts", "patterns"):
        for path in (ROOT / "src/llm_promptkit" / kind).rglob("*.md"):
            relative = path.relative_to(ROOT)
            in_head = subprocess.run(
                ["git", "cat-file", "-e", f"HEAD:{relative}"], cwd=ROOT
            ).returncode == 0
            if not in_head:
                continue  # files added after HEAD are new-era additions by design
            before = subprocess.check_output(["git", "show", f"HEAD:{relative}"], cwd=ROOT)
            assert split_frontmatter(before)[2] == split_frontmatter(path.read_bytes())[2], relative


def test_all_docs_are_frontmatter_nav_and_exact_source_body():
    from llm_promptkit.metadata import split_frontmatter

    rendered = generator.render_docs()
    for kind in ("prompts", "patterns"):
        base = ROOT / "src/llm_promptkit" / kind
        for source in base.rglob("*.md"):
            if source.name.lower() == "readme.md":
                continue
            destination = generator.doc_path(source, kind)
            _, front, body = split_frontmatter(source.read_bytes())
            actual = rendered[destination]
            assert actual.startswith(front + "[← Back to ".encode())
            assert actual.split(b"\n\n", 1)[1] == body
            assert destination.read_bytes() == actual


def test_render_preserves_crlf_body():
    content = b'---\r\ncategory: code\r\n---\r\n# Title\r\n\r\nBody\r\n'
    rendered = generator.with_navigation(content, "code")
    assert rendered.startswith(b'---\r\ncategory: code\r\n---\r\n')
    assert rendered.endswith(b'# Title\r\n\r\nBody\r\n')


def test_check_detects_modified_missing_and_orphan_docs_without_writes(tmp_path):
    target = tmp_path / "docs/prompts/code/test.md"
    target.parent.mkdir(parents=True)
    expected = {target: b"expected\n"}
    assert generator.sync_docs(expected, check=True, roots=[tmp_path / "docs/prompts"]) == 1
    assert not target.exists()
    assert generator.sync_docs(expected, check=False, roots=[tmp_path / "docs/prompts"]) == 0
    assert target.read_bytes() == b"expected\n"
    assert generator.sync_docs(expected, check=True, roots=[tmp_path / "docs/prompts"]) == 0
    target.write_bytes(b"drift\n")
    orphan = target.with_name("orphan.md")
    orphan.write_bytes(b"orphan\n")
    assert generator.sync_docs(expected, check=True, roots=[tmp_path / "docs/prompts"]) == 1
    assert target.read_bytes() == b"drift\n"
    assert orphan.exists()
    generator.sync_docs(expected, check=False, roots=[tmp_path / "docs/prompts"])
    assert target.read_bytes() == b"expected\n"
    assert not orphan.exists()


def test_generate_docs_check_cli():
    result = subprocess.run([sys.executable, "scripts/generate_docs.py", "--check"], cwd=ROOT, capture_output=True)
    assert result.returncode == 0, result.stdout + result.stderr
    assert b"drift=0" in result.stdout
    import re as _re
    mirrors = int(_re.search(rb"(\d+) content mirrors checked", result.stdout).group(1))
    assert mirrors >= 300  # dynamic floor: mirror count grows with the catalog
