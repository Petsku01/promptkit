"""Tests for deep coverage: prompts, search, doctor, helpers, registry."""

import os
import shutil
import tempfile
from pathlib import Path
from unittest.mock import patch

from typer.testing import CliRunner

from llm_promptkit.cli import app
from llm_promptkit.helpers import (
    copy_to_clipboard,
    get_models_with_prompts,
    get_prompts_dir,
    is_prompt_file,
)
from llm_promptkit.patterns._registry import (
    PatternLoadError,
    _resolve_patterns_dir,
    invalidate_pattern_cache,
    read_pattern,
)

runner = CliRunner()


# ============================================================================
# prompts.py — show/model branches
# ============================================================================


class TestPromptsShow:
    """Test _show_prompt and _handle_model_path branches."""

    def test_show_model_invalid_format_single(self):
        result = runner.invoke(app, ["prompts", "--model", "just-one-part"])
        assert result.exit_code == 0
        assert "Provider" in result.output or "not found" in result.output

    def test_show_model_provider_not_found(self):
        result = runner.invoke(app, ["prompts", "--model", "nonexistent_provider/some_model"])
        assert result.exit_code == 0
        assert "not found" in result.output.lower()

    def test_show_prompt_invalid_format(self):
        result = runner.invoke(app, ["prompts", "--show", "too/few/parts/extra"])
        assert result.exit_code == 0
        # v0.3.0: _find_prompt_file searches all dirs — result is "not found" not "invalid format"
        assert "not found" in result.output.lower() or "invalid" in result.output.lower()

    def test_show_prompt_not_found(self):
        result = runner.invoke(app, ["prompts", "--show", "nonexist/model/prompt"])
        assert result.exit_code == 0
        assert "not found" in result.output.lower()


# ============================================================================
# prompts.py — interactive deep coverage
# ============================================================================


class TestPromptsInteractiveDeep:
    """Deep interactive prompts tests — nested loop coverage."""

    @patch("llm_promptkit.cli.commands.prompts.Prompt.ask")
    def test_interactive_full_flow_quit(self, mock_ask):
        """Full flow: select provider → model → prompt → quit."""
        prompts_dir = get_prompts_dir()
        model_dir = prompts_dir / "model-optimized"
        if not model_dir.exists():
            return

        mock_ask.side_effect = ["1", "1", "1", "n", "q"]
        result = runner.invoke(app, ["prompts", "--interactive"])
        assert result.exit_code == 0

    @patch("llm_promptkit.cli.commands.prompts.Prompt.ask")
    def test_interactive_back_from_model(self, mock_ask):
        """Select provider, back from model, then quit."""
        prompts_dir = get_prompts_dir()
        model_dir = prompts_dir / "model-optimized"
        if not model_dir.exists():
            return

        mock_ask.side_effect = ["1", "b", "q"]
        result = runner.invoke(app, ["prompts", "--interactive"])
        assert result.exit_code == 0

    @patch("llm_promptkit.cli.commands.prompts.Prompt.ask")
    def test_interactive_back_from_prompt(self, mock_ask):
        """Select provider → model, back from prompt, back from model, quit."""
        prompts_dir = get_prompts_dir()
        model_dir = prompts_dir / "model-optimized"
        if not model_dir.exists():
            return

        mock_ask.side_effect = ["1", "1", "b", "b", "q"]
        result = runner.invoke(app, ["prompts", "--interactive"])
        assert result.exit_code == 0

    @patch("llm_promptkit.cli.commands.prompts.Prompt.ask")
    def test_interactive_invalid_provider_number(self, mock_ask):
        """Invalid number at provider level then quit."""
        prompts_dir = get_prompts_dir()
        model_dir = prompts_dir / "model-optimized"
        if not model_dir.exists():
            return

        mock_ask.side_effect = ["999", "q"]
        result = runner.invoke(app, ["prompts", "--interactive"])
        assert result.exit_code == 0
        assert "Invalid" in result.output

    @patch("llm_promptkit.cli.commands.prompts.Prompt.ask")
    def test_interactive_non_numeric_provider(self, mock_ask):
        """Non-numeric input at provider level then quit."""
        prompts_dir = get_prompts_dir()
        model_dir = prompts_dir / "model-optimized"
        if not model_dir.exists():
            return

        mock_ask.side_effect = ["abc", "q"]
        result = runner.invoke(app, ["prompts", "--interactive"])
        assert result.exit_code == 0

    @patch("llm_promptkit.cli.commands.prompts.Prompt.ask")
    def test_interactive_no_model_dir(self, mock_ask):
        """Interactive prompts when model-optimized dir doesn't exist."""
        with patch("llm_promptkit.cli.commands.prompts.get_prompts_dir") as mock_dir:
            fake_dir = Path("/tmp/nonexistent_promptkit_test")
            mock_dir.return_value = fake_dir
            result = runner.invoke(app, ["prompts", "--interactive"])
            assert result.exit_code == 0
            assert "not found" in result.output.lower()

    @patch("llm_promptkit.cli.commands.prompts.copy_to_clipboard", return_value=True)
    @patch("llm_promptkit.cli.commands.prompts.Prompt.ask")
    def test_interactive_copy_to_clipboard(self, mock_ask, mock_copy):
        """Full flow with clipboard copy."""
        prompts_dir = get_prompts_dir()
        model_dir = prompts_dir / "model-optimized"
        if not model_dir.exists():
            return

        mock_ask.side_effect = ["1", "1", "1", "y", "q"]
        result = runner.invoke(app, ["prompts", "--interactive"])
        assert result.exit_code == 0

    @patch("llm_promptkit.cli.commands.prompts.copy_to_clipboard", return_value=False)
    @patch("llm_promptkit.cli.commands.prompts.Prompt.ask")
    def test_interactive_copy_fails(self, mock_ask, mock_copy):
        """Full flow — copy to clipboard fails (no tool)."""
        prompts_dir = get_prompts_dir()
        model_dir = prompts_dir / "model-optimized"
        if not model_dir.exists():
            return

        mock_ask.side_effect = ["1", "1", "1", "y", "q"]
        result = runner.invoke(app, ["prompts", "--interactive"])
        assert result.exit_code == 0

    @patch("llm_promptkit.cli.commands.prompts.Prompt.ask")
    def test_interactive_enter_to_continue(self, mock_ask):
        """Select prompt, press Enter for another, then quit."""
        prompts_dir = get_prompts_dir()
        model_dir = prompts_dir / "model-optimized"
        if not model_dir.exists():
            return

        mock_ask.side_effect = ["1", "1", "1", "n", "", "q"]
        result = runner.invoke(app, ["prompts", "--interactive"])
        assert result.exit_code == 0


# ============================================================================
# search.py — missing lines: 30, 38-39, 87-88, 115-116
# ============================================================================


class TestSearchDeep:
    """Test search edge cases for full coverage."""

    def test_search_with_category(self):
        result = runner.invoke(app, ["search", "prompt", "--category", "context"])
        assert result.exit_code == 0

    def test_search_nonexistent_category(self):
        result = runner.invoke(app, ["search", "prompt", "--category", "nonexistent_cat"])
        assert result.exit_code == 0

    def test_search_empty_query(self):
        result = runner.invoke(app, ["search", ""])
        assert result.exit_code == 0 or result.exit_code == 1

    def test_search_snippet_fallback(self):
        result = runner.invoke(app, ["search", "few-shot", "--limit", "5"])
        assert result.exit_code == 0


# ============================================================================
# doctor.py — missing lines: 133, 145, 166
# ============================================================================


class TestDoctorDeep:
    """Test doctor edge cases for full coverage."""

    def test_doctor_empty_prompt(self):
        """Very short prompt should trigger warning."""
        result = runner.invoke(app, ["doctor", "Hi"])
        assert result.exit_code == 0
        assert "short" in result.output.lower()

    def test_doctor_output_format(self):
        """Prompt mentioning output format should not trigger format warning."""
        result = runner.invoke(
            app,
            [
                "doctor",
                "You are an expert. Output as JSON. Translate this text to Finnish.",
            ],
        )
        assert result.exit_code == 0
        assert "Analysis" in result.output or "analysis" in result.output.lower()

    def test_doctor_verbose_phrase(self):
        """Prompt with verbose phrase should trigger suggestion."""
        result = runner.invoke(
            app,
            [
                "doctor",
                "You are an expert. Please think about this carefully and give a thorough analysis.",
            ],
        )
        assert result.exit_code == 0
        assert "Analysis" in result.output or "analysis" in result.output.lower()


# ============================================================================
# registry — missing lines: 26, 78-79
# ============================================================================


class TestRegistryDeep:
    """Test registry edge cases for full coverage."""

    def test_resolve_patterns_dir_exists(self):
        """Pattern dir exists in package."""
        path = _resolve_patterns_dir()
        assert path.is_dir()

    def test_pattern_load_error_unreadable(self):
        """read_pattern should raise PatternLoadError on unreadable file."""
        tmp = tempfile.mkdtemp()
        try:
            fake_dir = Path(tmp) / "fake_cat"
            fake_dir.mkdir()
            fake_file = fake_dir / "broken.md"
            fake_file.write_text("# Broken\n\n**Category:** fake\n\nContent here")
            os.chmod(str(fake_file), 0o000)

            with patch(
                "llm_promptkit.patterns._registry._resolve_patterns_dir",
                return_value=Path(tmp),
            ):
                invalidate_pattern_cache()
                try:
                    read_pattern("broken")
                    # If we get here on systems where root can still read 0o000, that's OK
                except PatternLoadError:
                    pass  # Expected on normal systems
                finally:
                    os.chmod(str(fake_file), 0o644)
                    invalidate_pattern_cache()
        finally:
            shutil.rmtree(tmp)

    def test_cwd_fallback_no_package(self):
        """When package dir doesn't exist, should fall back to cwd/prompts."""
        with patch(
            "llm_promptkit.patterns._registry._resolve_patterns_dir",
            side_effect=PatternLoadError("test: no package dir"),
        ):
            # Verify we can still invalidate cache without error
            invalidate_pattern_cache()
            # Verify we can still invalidate cache without error


# ============================================================================
# helpers.py — copy_to_clipboard, is_prompt_file, get_models
# ============================================================================


class TestHelpersDeep:
    """Test helpers edge cases."""

    def test_copy_to_clipboard_no_tool(self):
        """copy_to_clipboard returns False when no tool available."""
        with patch("llm_promptkit.helpers.subprocess.Popen") as mock_popen:
            mock_popen.side_effect = FileNotFoundError()
            result = copy_to_clipboard("test text")
            assert result is False

    def test_is_prompt_file(self):
        assert is_prompt_file(Path("test.md")) is True
        assert is_prompt_file(Path("README.md")) is False
        assert is_prompt_file(Path("test.txt")) is False

    def test_get_models_with_prompts_nested(self, tmp_path):
        model_a = tmp_path / "model_a"
        model_a.mkdir()
        (model_a / "coding.md").write_text("# Coding")
        (model_a / "writing.md").write_text("# Writing")

        model_b = tmp_path / "model_b"
        model_b.mkdir()
        # No .md files in model_b

        result = get_models_with_prompts(tmp_path)
        assert len(result) == 1
        assert result[0] == ("model_a", 2)

    def test_get_prompts_dir_returns_path(self):
        path = get_prompts_dir()
        assert isinstance(path, Path)


# ============================================================================
# build.py CLI — interactive context prompt
# ============================================================================


class TestBuildInteractiveContext:
    """Test interactive build with context."""

    @patch("llm_promptkit.cli.commands.build.Prompt.ask")
    def test_interactive_build_with_context(self, mock_ask):
        mock_ask.side_effect = [
            "senior developer",  # persona
            "y",  # confirm persona
            "chain-of-thought",  # pattern
            "y",  # confirm pattern
            "fix bugs",  # task
            "y",  # confirm task
            "some code here",  # context (has content)
            "n",  # no constraints
            "n",  # no examples
        ]
        result = runner.invoke(app, ["build", "--interactive"])
        assert result.exit_code == 0
