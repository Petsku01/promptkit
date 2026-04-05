from pathlib import Path

from llm_promptkit.pattern_loader import PatternLoader


def test_load_from_directory_extracts_template_section(tmp_path: Path):
    patterns_dir = tmp_path / "patterns"
    (patterns_dir / "reasoning").mkdir(parents=True)
    (patterns_dir / "reasoning" / "chain-of-thought.md").write_text(
        """# Chain of Thought

## When to Use
Complex tasks.

## Template
Think through this step-by-step.
1. Analyze
2. Solve
""",
        encoding="utf-8",
    )

    loaded = PatternLoader().load_from_directory(patterns_dir)

    assert "chain-of-thought" in loaded
    assert loaded["chain-of-thought"].startswith("Think through this step-by-step")
    assert "## When to Use" not in loaded["chain-of-thought"]


def test_pattern_name_extracted_from_filename(tmp_path: Path):
    patterns_dir = tmp_path / "patterns"
    patterns_dir.mkdir()
    (patterns_dir / "json-enforcer.md").write_text(
        """# JSON Enforcer

## Template
Return valid JSON only.
""",
        encoding="utf-8",
    )

    loaded = PatternLoader().load_from_directory(patterns_dir)

    assert list(loaded.keys()) == ["json-enforcer"]
    assert loaded["json-enforcer"] == "Return valid JSON only."


def test_subdirectory_loading_and_fallback_to_content_after_h1(tmp_path: Path):
    patterns_dir = tmp_path / "patterns"
    (patterns_dir / "code").mkdir(parents=True)
    (patterns_dir / "code" / "stack-trace-decoder.md").write_text(
        """# Stack Trace Decoder

Decode the stack trace and explain root cause.
""",
        encoding="utf-8",
    )

    loaded = PatternLoader().load_from_directory(patterns_dir)

    assert "stack-trace-decoder" in loaded
    assert loaded["stack-trace-decoder"] == "Decode the stack trace and explain root cause."
