"""Era 2: executable CLI, configuration and lossless-fix contracts."""

import json
from pathlib import Path
from unittest.mock import patch

import pytest

from llm_promptkit import PromptBuilder
from llm_promptkit import config as config_module
from llm_promptkit.cli import app
from llm_promptkit.cli.commands import doctor, prompts
from llm_promptkit.config import PromptKitConfig
from tests._cli_runner import make_runner, visible_text

runner = make_runner()


def test_show_readme_route():
    result = runner.invoke(app, ["prompts", "--show", "openai/gpt-4o/coding"])
    assert result.exit_code == 0
    assert "not found" not in result.output.lower()
    assert "Estimated tokens" in result.output


@pytest.mark.parametrize("args", [["--show", "no-such-prompt"], ["--show", "missing/nope"], ["--model", "missing"], ["--model", "openai/missing"]])
def test_prompt_missing_exit_one(args):
    assert runner.invoke(app, ["prompts", *args]).exit_code == 1


def test_show_resolution_order_and_fuzzy(tmp_path, monkeypatch):
    direct = tmp_path / "vendor/model/code.md"
    model = tmp_path / "model-optimized/vendor/model/code.md"
    for file in (direct, model):
        file.parent.mkdir(parents=True, exist_ok=True)
        file.write_text("DIRECT" if file == direct else "MODEL")
    monkeypatch.setattr(prompts, "get_all_prompt_dirs", lambda: [tmp_path])
    assert prompts._find_prompt_file(["vendor", "model", "code"])[0] == direct
    direct.unlink()
    assert prompts._find_prompt_file(["vendor", "model", "code"])[0] == model
    result = runner.invoke(app, ["prompts", "--show", "code"])
    assert result.exit_code == 0 and "MODEL" in result.output


def test_prompt_read_error_exit_two():
    with patch.object(Path, "read_text", side_effect=OSError("unreadable")):
        result = runner.invoke(app, ["prompts", "--show", "openai/gpt-4o/coding"])
    assert result.exit_code == 2
    assert "unreadable" in visible_text(result)


@pytest.mark.parametrize("fmt", ["table", "json"])
def test_empty_file_exit_two(tmp_path, fmt):
    file = tmp_path / "empty.md"
    file.write_text(" \n\t")
    result = runner.invoke(app, ["doctor", "--file", str(file), "--format", fmt])
    assert result.exit_code == 2
    if fmt == "json":
        assert json.loads(result.output) == {"error": "empty"}
    else:
        assert "tyhjä prompt — mitään analyysoitavissa" in visible_text(result)


@pytest.mark.parametrize("fmt", ["table", "json"])
def test_doctor_either_or(tmp_path, fmt):
    file = tmp_path / "prompt.md"
    file.write_text("Review this code.")
    result = runner.invoke(app, ["doctor", "text", "--file", str(file), "--format", fmt])
    assert result.exit_code == 2
    message = json.loads(result.output)["error"] if fmt == "json" else visible_text(result)
    assert "Anna EITHER text TAI --file" in message


def test_positional_file_same_json(tmp_path):
    file = tmp_path / "prompt.md"
    file.write_text("You are a reviewer. Return JSON. Example: {}")
    positional = runner.invoke(app, ["doctor", str(file), "--format", "json"])
    explicit = runner.invoke(app, ["doctor", "--file", str(file), "--format", "json"])
    assert positional.exit_code == explicit.exit_code == 0
    assert json.loads(positional.output) == json.loads(explicit.output)


@pytest.mark.parametrize("fence", ["```", "~~~", "````"])
def test_fix_preserves_fenced_bytes(tmp_path, fence):
    code = f'{fence}python\r\n    PLEASE  keep = "  "  \r\n\tTask:\r\n{fence}\r\n'
    file = tmp_path / "prompt.md"
    file.write_bytes(("PLEASE review.\r\n\r\nTask:\r\n\r\n" + code + "\r\nPLEASE finish.").encode())
    result = runner.invoke(app, ["doctor", str(file), "--fix", "--format", "json"])
    assert result.exit_code == 0
    fixed = file.read_bytes().decode()
    assert code in fixed
    assert fixed.startswith("review.") and fixed.endswith("finish.")
    assert "Task:" not in fixed.replace(code, "")


def test_backup_rotation_and_atomic_replace(tmp_path):
    file = tmp_path / "prompt.md"
    file.write_text("PLEASE review this code.")
    bak = Path(str(file) + ".bak")
    bak.write_text("old backup")
    Path(str(bak) + ".1").write_text("older backup")
    import os
    with patch.object(doctor.os, "replace", wraps=os.replace) as replace:
        result = runner.invoke(app, ["doctor", "--file", str(file), "--fix"])
    assert result.exit_code == 0
    replace.assert_called_once()
    assert bak.read_text() == "old backup"
    assert Path(str(bak) + ".1").read_text() == "older backup"
    assert Path(str(bak) + ".2").read_text() == "PLEASE review this code."
    assert file.read_text() == "review this code."


@pytest.mark.parametrize("toml,field", [
    ('promptkit = "bad"', "promptkit"),
    ('[promptkit]\npaths = false', "promptkit.paths"),
    ('[promptkit]\ndefault_persona = 3', "promptkit.default_persona"),
    ('[promptkit]\ndefault_model = true', "promptkit.default_model"),
    ('[promptkit.paths]\nextra_prompt_dirs = "bad"', "promptkit.paths.extra_prompt_dirs"),
    ('[promptkit.paths]\nextra_pattern_dirs = [42]', "promptkit.paths.extra_pattern_dirs[0]"),
])
def test_config_types_and_cli(tmp_path, monkeypatch, toml, field):
    (tmp_path / "config.toml").write_text(toml)
    with pytest.raises(config_module.ConfigError, match=field.replace("[", r"\[").replace("]", r"\]")):
        PromptKitConfig(config_dir=tmp_path)
    monkeypatch.setenv("PROMPTKIT_CONFIG_DIR", str(tmp_path))
    monkeypatch.setattr(config_module, "_config", None)
    result = runner.invoke(app, ["build", "--task", "Review"])
    assert result.exit_code == 2
    assert field in visible_text(result)


def test_variables_kwargs_changelog_signature():
    builder = PromptBuilder()
    assert builder.variables(role="reviewer", task="audit") is builder
    assert builder._substitute_variables("$role: ${task}") == "reviewer: audit"
    builder.variable("role", "writer")
    assert builder._substitute_variables("$role: $task") == "writer: audit"


@pytest.mark.parametrize("fence", ["```", "~~~"])
def test_unclosed_fence_is_untouched(fence):
    code = f"{fence}python\n    PLEASE  keep\n\tTask:  \n"
    assert doctor._apply_safe_fixes(code) == code


def test_failed_atomic_replace_keeps_original(tmp_path):
    file = tmp_path / "prompt.md"
    original = "PLEASE review this code."
    file.write_text(original)
    with patch.object(doctor.os, "replace", side_effect=OSError("replace failed")):
        result = runner.invoke(app, ["doctor", str(file), "--fix", "--format", "json"])
    assert result.exit_code == 2
    assert "replace failed" in json.loads(result.output)["error"]
    assert file.read_text() == original
    assert Path(str(file) + ".bak").read_text() == original
    assert sorted(path.name for path in tmp_path.iterdir()) == ["prompt.md", "prompt.md.bak"]


def test_doctor_invalid_utf8_is_json_error(tmp_path):
    file = tmp_path / "prompt.md"
    file.write_bytes(b"\xff")
    result = runner.invoke(app, ["doctor", str(file), "--format", "json"])
    assert result.exit_code == 2
    assert "Error reading prompt" in json.loads(result.output)["error"]


def test_json_dry_run_warning_is_stderr_only():
    result = runner.invoke(app, ["doctor", "Review this code.", "--dry-run", "--format", "json"])
    assert result.exit_code == 0
    assert "issues" in json.loads(result.stdout)
    assert "requires --fix" in result.stderr


@pytest.mark.parametrize("category", ["reasoning", "no-such-category"])
def test_list_categories_and_sources(category):
    result = runner.invoke(app, ["list", "--category", category, "--sources"])
    assert result.exit_code == 0
    assert "built-in" in result.output if category == "reasoning" else "No patterns found" in result.output


def test_list_empty_registry(monkeypatch):
    from llm_promptkit.cli.commands import list as list_module
    monkeypatch.setattr(list_module, "list_patterns_with_categories", lambda: [])
    result = runner.invoke(app, ["list"])
    assert result.exit_code == 0 and "No patterns found" in result.output


def test_list_custom_sources(tmp_path, monkeypatch):
    from llm_promptkit.patterns._registry import invalidate_pattern_cache
    custom = tmp_path / "patterns"
    custom.mkdir()
    (custom / "era2-custom.md").write_text("Review carefully.")
    (tmp_path / "config.toml").write_text(f'[promptkit.paths]\nextra_pattern_dirs = ["{custom}"]\n')
    monkeypatch.setenv("PROMPTKIT_CONFIG_DIR", str(tmp_path))
    monkeypatch.setattr(config_module, "_config", None)
    invalidate_pattern_cache()
    try:
        result = runner.invoke(app, ["list", "--sources"])
        assert result.exit_code == 0
        assert "era2-custom" in result.output and "[custom]" in result.output
        assert "Custom pattern dirs:" in result.output
    finally:
        invalidate_pattern_cache()
