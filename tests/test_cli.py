"""Comprehensive tests for CLI module."""
import argparse
from pathlib import Path
from unittest.mock import MagicMock, patch, mock_open

import pytest

from llm_promptkit import cli
from llm_promptkit.cli import (
    build_prompt,
    copy_to_clipboard,
    count_prompts,
    get_prompt_files,
    get_prompts_dir,
    is_prompt_file,
    list_model_prompts,
    list_patterns,
    list_providers,
    main,
    prompts_command,
    search_command,
    search_prompts,
    show_prompt,
)


# =============================================================================
# Helper Function Tests
# =============================================================================

class TestHelperFunctions:
    """Tests for utility/helper functions."""

    def test_is_prompt_file_valid_md(self, tmp_path):
        """Valid .md files should be detected as prompts."""
        prompt = tmp_path / "coding.md"
        prompt.touch()
        assert is_prompt_file(prompt) is True

    def test_is_prompt_file_readme_excluded(self, tmp_path):
        """README.md should not be a prompt file."""
        readme = tmp_path / "README.md"
        readme.touch()
        assert is_prompt_file(readme) is False

    def test_is_prompt_file_readme_case_insensitive(self, tmp_path):
        """readme.md (lowercase) should also be excluded."""
        readme = tmp_path / "readme.md"
        readme.touch()
        assert is_prompt_file(readme) is False

    def test_is_prompt_file_non_md(self, tmp_path):
        """Non-.md files should not be prompt files."""
        txt_file = tmp_path / "notes.txt"
        txt_file.touch()
        assert is_prompt_file(txt_file) is False

    def test_get_prompt_files_filters_correctly(self, tmp_path):
        """get_prompt_files should return only valid prompt files."""
        (tmp_path / "coding.md").touch()
        (tmp_path / "review.md").touch()
        (tmp_path / "README.md").touch()
        (tmp_path / "notes.txt").touch()

        files = get_prompt_files(tmp_path)
        names = [f.name for f in files]

        assert "coding.md" in names
        assert "review.md" in names
        assert "README.md" not in names
        assert "notes.txt" not in names
        assert len(files) == 2

    def test_count_prompts(self, tmp_path):
        """count_prompts should count only valid prompt files."""
        (tmp_path / "a.md").touch()
        (tmp_path / "b.md").touch()
        (tmp_path / "README.md").touch()

        assert count_prompts(tmp_path) == 2

    def test_get_prompts_dir_cwd_fallback(self, tmp_path, monkeypatch):
        """Should find prompts dir in cwd if package dir doesn't have it."""
        prompts_dir = tmp_path / "prompts"
        prompts_dir.mkdir()
        monkeypatch.chdir(tmp_path)

        result = get_prompts_dir()
        assert result.exists()


class TestCopyToClipboard:
    """Tests for clipboard functionality."""

    @patch("llm_promptkit.cli.subprocess.Popen")
    def test_copy_to_clipboard_xclip_success(self, mock_popen):
        """Should use xclip when available."""
        mock_process = MagicMock()
        mock_process.returncode = 0
        mock_popen.return_value = mock_process

        result = copy_to_clipboard("test text")

        assert result is True
        mock_popen.assert_called()

    @patch("llm_promptkit.cli.subprocess.Popen")
    def test_copy_to_clipboard_no_tool(self, mock_popen):
        """Should return False when no clipboard tool is available."""
        mock_popen.side_effect = FileNotFoundError

        result = copy_to_clipboard("test text")

        assert result is False

    @patch("llm_promptkit.cli.subprocess.Popen")
    def test_copy_to_clipboard_tool_fails(self, mock_popen):
        """Should try next tool when one fails."""
        mock_process = MagicMock()
        mock_process.returncode = 1
        mock_popen.return_value = mock_process

        result = copy_to_clipboard("test text")

        # All tools fail with returncode 1
        assert result is False


# =============================================================================
# List Command Tests
# =============================================================================

class TestListPatterns:
    """Tests for the list command."""

    @patch("llm_promptkit.cli.console")
    def test_list_patterns_outputs_table(self, mock_console):
        """list_patterns should output a table of patterns."""
        list_patterns()

        mock_console.print.assert_called()
        # Should have called print at least once with a Table
        call_args = mock_console.print.call_args_list
        assert len(call_args) > 0


# =============================================================================
# Build Command Tests
# =============================================================================

class MockBuildArgs:
    """Mock args for build command."""

    def __init__(
        self,
        persona=None,
        pattern=None,
        task=None,
        context=None,
        constraint=None,
        tokens=False,
        output=None,
    ):
        self.persona = persona
        self.pattern = pattern or []
        self.task = task
        self.context = context
        self.constraint = constraint
        self.tokens = tokens
        self.output = output


class TestBuildPrompt:
    """Tests for the build command."""

    @patch("llm_promptkit.cli.console.print")
    def test_build_prompt_basic(self, mock_print):
        """Basic build with persona and task."""
        args = MockBuildArgs(persona="Developer", task="Review code")
        build_prompt(args)
        assert mock_print.called

    @patch("llm_promptkit.cli.console.print")
    def test_build_prompt_with_pattern(self, mock_print):
        """Build with a valid pattern."""
        args = MockBuildArgs(
            persona="Developer",
            pattern=["chain-of-thought"],
            task="Analyze this"
        )
        build_prompt(args)
        assert mock_print.called

    @patch("llm_promptkit.cli.console.print")
    def test_build_prompt_invalid_pattern(self, mock_print):
        """Invalid pattern should show error."""
        args = MockBuildArgs(pattern=["invalid-pattern-xyz"])
        build_prompt(args)

        # Should have printed an error
        calls = [str(c) for c in mock_print.call_args_list]
        assert any("Error" in str(c) or "red" in str(c) for c in calls)

    @patch("llm_promptkit.cli.console.print")
    def test_build_prompt_with_context(self, mock_print):
        """Build with context included."""
        args = MockBuildArgs(
            task="Review",
            context="def hello(): pass"
        )
        build_prompt(args)
        assert mock_print.called

    @patch("llm_promptkit.cli.console.print")
    def test_build_prompt_with_constraints(self, mock_print):
        """Build with multiple constraints."""
        args = MockBuildArgs(
            task="Write code",
            constraint=["Max 100 lines", "Use Python 3.10+"]
        )
        build_prompt(args)
        assert mock_print.called

    @patch("llm_promptkit.cli.console.print")
    def test_build_prompt_with_tokens(self, mock_print):
        """Build with token estimation."""
        args = MockBuildArgs(
            persona="Dev",
            task="Test",
            tokens=True
        )
        build_prompt(args)

        # Should mention tokens in output
        calls = [str(c) for c in mock_print.call_args_list]
        assert any("token" in str(c).lower() for c in calls)

    def test_build_prompt_output_to_file(self, tmp_path):
        """Build with output to file."""
        output_file = tmp_path / "prompt.txt"
        args = MockBuildArgs(
            persona="Dev",
            task="Test task",
            output=str(output_file)
        )

        with patch("llm_promptkit.cli.console.print"):
            build_prompt(args)

        assert output_file.exists()
        content = output_file.read_text()
        assert "Dev" in content or "Test task" in content

    @patch("llm_promptkit.cli.console.print")
    def test_build_prompt_multiple_patterns(self, mock_print):
        """Build with multiple patterns."""
        args = MockBuildArgs(
            pattern=["chain-of-thought", "few-shot"],
            task="Analyze"
        )
        build_prompt(args)
        assert mock_print.called


# =============================================================================
# Prompts Command Tests
# =============================================================================

class MockPromptsArgs:
    """Mock args for prompts command."""

    def __init__(self, model=None, show=None, interactive=False):
        self.model = model
        self.show = show
        self.interactive = interactive


class TestPromptsCommand:
    """Tests for the prompts command."""

    @patch("llm_promptkit.cli.list_providers")
    def test_prompts_no_args_lists_providers(self, mock_list):
        """prompts with no args should list providers."""
        args = MockPromptsArgs()
        prompts_command(args)
        mock_list.assert_called_once()

    @patch("llm_promptkit.cli.list_model_prompts")
    def test_prompts_with_model(self, mock_list):
        """prompts --model should list model prompts."""
        args = MockPromptsArgs(model="openai")
        prompts_command(args)
        mock_list.assert_called_once_with("openai")

    @patch("llm_promptkit.cli.show_prompt")
    def test_prompts_with_show(self, mock_show):
        """prompts --show should show specific prompt."""
        args = MockPromptsArgs(show="openai/gpt-4o/coding")
        prompts_command(args)
        mock_show.assert_called_once_with("openai/gpt-4o/coding")

    @patch("llm_promptkit.cli.interactive_prompts")
    def test_prompts_interactive(self, mock_interactive):
        """prompts --interactive should start interactive mode."""
        args = MockPromptsArgs(interactive=True)
        prompts_command(args)
        mock_interactive.assert_called_once()


class TestListProviders:
    """Tests for list_providers function."""

    @patch("llm_promptkit.cli.console.print")
    @patch("llm_promptkit.cli.get_prompts_dir")
    def test_list_providers_no_dir(self, mock_get_dir, mock_print, tmp_path):
        """Should show error when model-optimized dir doesn't exist."""
        mock_get_dir.return_value = tmp_path / "nonexistent"

        list_providers()

        calls = [str(c) for c in mock_print.call_args_list]
        assert any("not found" in str(c).lower() for c in calls)

    @patch("llm_promptkit.cli.console.print")
    @patch("llm_promptkit.cli.get_prompts_dir")
    def test_list_providers_with_providers(self, mock_get_dir, mock_print, tmp_path):
        """Should list providers that have prompts."""
        prompts_dir = tmp_path / "prompts"
        model_dir = prompts_dir / "model-optimized"
        provider_dir = model_dir / "openai" / "gpt-4o"
        provider_dir.mkdir(parents=True)
        (provider_dir / "coding.md").write_text("# Coding prompt")

        mock_get_dir.return_value = prompts_dir

        list_providers()

        assert mock_print.called


class TestListModelPrompts:
    """Tests for list_model_prompts function."""

    @patch("llm_promptkit.cli.console.print")
    @patch("llm_promptkit.cli.get_prompts_dir")
    def test_list_model_prompts_provider_not_found(self, mock_get_dir, mock_print, tmp_path):
        """Should show error for unknown provider."""
        prompts_dir = tmp_path / "prompts"
        (prompts_dir / "model-optimized").mkdir(parents=True)
        mock_get_dir.return_value = prompts_dir

        list_model_prompts("nonexistent-provider")

        calls = [str(c) for c in mock_print.call_args_list]
        assert any("not found" in str(c).lower() for c in calls)

    @patch("llm_promptkit.cli.console.print")
    @patch("llm_promptkit.cli.get_prompts_dir")
    def test_list_model_prompts_model_not_found(self, mock_get_dir, mock_print, tmp_path):
        """Should show error for unknown model."""
        prompts_dir = tmp_path / "prompts"
        (prompts_dir / "model-optimized" / "openai").mkdir(parents=True)
        mock_get_dir.return_value = prompts_dir

        list_model_prompts("openai/unknown-model")

        calls = [str(c) for c in mock_print.call_args_list]
        assert any("not found" in str(c).lower() for c in calls)

    @patch("llm_promptkit.cli.console.print")
    @patch("llm_promptkit.cli.get_prompts_dir")
    def test_list_model_prompts_invalid_format(self, mock_get_dir, mock_print, tmp_path):
        """Should show error for invalid path format."""
        mock_get_dir.return_value = tmp_path

        list_model_prompts("too/many/parts/here")

        calls = [str(c) for c in mock_print.call_args_list]
        assert any("invalid" in str(c).lower() for c in calls)


class TestShowPrompt:
    """Tests for show_prompt function."""

    @patch("llm_promptkit.cli.console.print")
    @patch("llm_promptkit.cli.get_prompts_dir")
    def test_show_prompt_invalid_format(self, mock_get_dir, mock_print, tmp_path):
        """Should show error for invalid path format."""
        mock_get_dir.return_value = tmp_path

        show_prompt("only-two/parts")

        calls = [str(c) for c in mock_print.call_args_list]
        assert any("invalid" in str(c).lower() for c in calls)

    @patch("llm_promptkit.cli.console.print")
    @patch("llm_promptkit.cli.get_prompts_dir")
    def test_show_prompt_not_found(self, mock_get_dir, mock_print, tmp_path):
        """Should show error when prompt doesn't exist."""
        prompts_dir = tmp_path / "prompts"
        (prompts_dir / "model-optimized" / "openai" / "gpt-4o").mkdir(parents=True)
        mock_get_dir.return_value = prompts_dir

        show_prompt("openai/gpt-4o/nonexistent")

        calls = [str(c) for c in mock_print.call_args_list]
        assert any("not found" in str(c).lower() for c in calls)

    @patch("llm_promptkit.cli.console.print")
    @patch("llm_promptkit.cli.get_prompts_dir")
    def test_show_prompt_displays_content(self, mock_get_dir, mock_print, tmp_path):
        """Should display prompt content."""
        prompts_dir = tmp_path / "prompts"
        prompt_path = prompts_dir / "model-optimized" / "openai" / "gpt-4o"
        prompt_path.mkdir(parents=True)
        (prompt_path / "coding.md").write_text("# Coding Prompt\n\nWrite clean code.")

        mock_get_dir.return_value = prompts_dir

        show_prompt("openai/gpt-4o/coding")

        assert mock_print.called


# =============================================================================
# Search Command Tests
# =============================================================================

class MockSearchArgs:
    """Mock args for search command."""

    def __init__(self, query, limit=10, category=None):
        self.query = query if isinstance(query, list) else [query]
        self.limit = limit
        self.category = category


class TestSearchPrompts:
    """Tests for search_prompts function."""

    def test_search_prompts_finds_matches(self, tmp_path):
        """Should find prompts matching query."""
        prompts_dir = tmp_path / "prompts"
        prompts_dir.mkdir()
        (prompts_dir / "coding.md").write_text("# Coding\n\nWrite Python code.")
        (prompts_dir / "review.md").write_text("# Review\n\nReview Java code.")

        with patch("llm_promptkit.cli.get_prompts_dir", return_value=tmp_path):
            results = search_prompts("Python")

        assert len(results) >= 1
        assert any("coding" in r["title"].lower() for r in results)

    def test_search_prompts_no_results(self, tmp_path):
        """Should return empty list for no matches."""
        prompts_dir = tmp_path / "prompts"
        prompts_dir.mkdir()
        (prompts_dir / "coding.md").write_text("# Coding prompt")

        with patch("llm_promptkit.cli.get_prompts_dir", return_value=tmp_path):
            results = search_prompts("xyznonexistent123")

        assert len(results) == 0

    def test_search_prompts_respects_limit(self, tmp_path):
        """Should respect limit parameter."""
        prompts_dir = tmp_path / "prompts"
        prompts_dir.mkdir()
        for i in range(20):
            (prompts_dir / f"prompt{i}.md").write_text(f"# Prompt {i}\n\nTest content.")

        with patch("llm_promptkit.cli.get_prompts_dir", return_value=tmp_path):
            results = search_prompts("Test", limit=5)

        assert len(results) <= 5

    def test_search_prompts_filename_matches(self, tmp_path):
        """Should match on filename."""
        prompts_dir = tmp_path / "prompts"
        prompts_dir.mkdir()
        (prompts_dir / "security-audit.md").write_text("# Audit\n\nGeneric content.")

        with patch("llm_promptkit.cli.get_prompts_dir", return_value=tmp_path):
            results = search_prompts("security")

        assert len(results) >= 1


class TestSearchCommand:
    """Tests for search_command function."""

    @patch("llm_promptkit.cli.console.print")
    def test_search_command_empty_query(self, mock_print):
        """Should show error for empty query."""
        args = MockSearchArgs(query=[""])
        search_command(args)

        calls = [str(c) for c in mock_print.call_args_list]
        assert any("provide" in str(c).lower() or "query" in str(c).lower() for c in calls)

    @patch("llm_promptkit.cli.search_prompts")
    @patch("llm_promptkit.cli.console.print")
    def test_search_command_no_results(self, mock_print, mock_search):
        """Should show message when no results found."""
        mock_search.return_value = []

        args = MockSearchArgs(query=["nonexistent"])
        search_command(args)

        calls = [str(c) for c in mock_print.call_args_list]
        assert any("no" in str(c).lower() and "found" in str(c).lower() for c in calls)

    @patch("llm_promptkit.cli.search_prompts")
    @patch("llm_promptkit.cli.console.print")
    def test_search_command_with_results(self, mock_print, mock_search):
        """Should display results table."""
        mock_search.return_value = [
            {"path": "test/prompt.md", "title": "Test", "score": 10, "snippet": "Test content"}
        ]

        args = MockSearchArgs(query=["test"])
        search_command(args)

        assert mock_print.called


# =============================================================================
# Main Entry Point Tests
# =============================================================================

class TestMain:
    """Tests for main() entry point."""

    @patch("llm_promptkit.cli.list_patterns")
    def test_main_list_command(self, mock_list):
        """main() with 'list' should call list_patterns."""
        with patch("sys.argv", ["promptkit", "list"]):
            main()
        mock_list.assert_called_once()

    @patch("llm_promptkit.cli.build_prompt")
    def test_main_build_command(self, mock_build):
        """main() with 'build' should call build_prompt."""
        with patch("sys.argv", ["promptkit", "build", "--task", "Test"]):
            main()
        mock_build.assert_called_once()

    @patch("llm_promptkit.cli.prompts_command")
    def test_main_prompts_command(self, mock_prompts):
        """main() with 'prompts' should call prompts_command."""
        with patch("sys.argv", ["promptkit", "prompts"]):
            main()
        mock_prompts.assert_called_once()

    @patch("llm_promptkit.cli.search_command")
    def test_main_search_command(self, mock_search):
        """main() with 'search' should call search_command."""
        with patch("sys.argv", ["promptkit", "search", "test"]):
            main()
        mock_search.assert_called_once()

    @patch("sys.argv", ["promptkit"])
    def test_main_no_command_prints_help(self, capsys):
        """main() with no command should print help."""
        # This should not raise, just print help
        main()


# =============================================================================
# Integration Tests
# =============================================================================

class TestCLIIntegration:
    """Integration tests using actual CLI flow."""

    @patch("llm_promptkit.cli.console.print")
    def test_full_build_flow(self, mock_print):
        """Test complete build flow from args to output."""
        args = MockBuildArgs(
            persona="Senior Security Engineer",
            pattern=["chain-of-thought"],
            task="Review this code for vulnerabilities",
            context="def login(user, pw): return db.query(f'SELECT * FROM users WHERE name={user}')",
            constraint=["Focus on SQL injection", "Be specific"],
            tokens=True
        )

        build_prompt(args)

        # Verify print was called multiple times
        assert mock_print.call_count >= 1

    def test_build_output_file_contains_all_parts(self, tmp_path):
        """Output file should contain all specified parts."""
        output_file = tmp_path / "output.txt"

        args = MockBuildArgs(
            persona="Expert Reviewer",
            task="Analyze the architecture",
            context="class Service: pass",
            output=str(output_file)
        )

        with patch("llm_promptkit.cli.console.print"):
            build_prompt(args)

        content = output_file.read_text()
        assert "Expert Reviewer" in content
        assert "Analyze" in content or "architecture" in content
