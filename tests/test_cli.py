"""Tests for Typer CLI commands using CliRunner."""

from unittest.mock import MagicMock, patch

from typer.testing import CliRunner

from llm_promptkit.cli import app

runner = CliRunner()


# =============================================================================
# Helper Function Tests (imported from helpers module)
# =============================================================================


class TestHelperFunctions:
    """Tests for utility/helper functions."""

    def test_is_prompt_file_valid_md(self, tmp_path):
        """Valid .md files should be detected as prompts."""
        from llm_promptkit.helpers import is_prompt_file

        prompt = tmp_path / "coding.md"
        prompt.touch()
        assert is_prompt_file(prompt) is True

    def test_is_prompt_file_readme_excluded(self, tmp_path):
        """README.md should not be a prompt file."""
        from llm_promptkit.helpers import is_prompt_file

        readme = tmp_path / "README.md"
        readme.touch()
        assert is_prompt_file(readme) is False

    def test_is_prompt_file_readme_case_insensitive(self, tmp_path):
        """readme.md (lowercase) should also be excluded."""
        from llm_promptkit.helpers import is_prompt_file

        readme = tmp_path / "readme.md"
        readme.touch()
        assert is_prompt_file(readme) is False

    def test_is_prompt_file_non_md(self, tmp_path):
        """Non-.md files should not be prompt files."""
        from llm_promptkit.helpers import is_prompt_file

        txt_file = tmp_path / "notes.txt"
        txt_file.touch()
        assert is_prompt_file(txt_file) is False

    def test_get_prompt_files_filters_correctly(self, tmp_path):
        """get_prompt_files should return only valid prompt files."""
        from llm_promptkit.helpers import get_prompt_files

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
        from llm_promptkit.helpers import count_prompts

        (tmp_path / "a.md").touch()
        (tmp_path / "b.md").touch()
        (tmp_path / "README.md").touch()

        assert count_prompts(tmp_path) == 2

    def test_get_prompts_dir_cwd_fallback(self, tmp_path, monkeypatch):
        """Should find prompts dir in cwd if package dir doesn't have it."""
        from llm_promptkit.helpers import get_prompts_dir

        prompts_dir = tmp_path / "prompts"
        prompts_dir.mkdir()
        monkeypatch.chdir(tmp_path)

        result = get_prompts_dir()
        assert result.exists()


class TestCopyToClipboard:
    """Tests for clipboard functionality."""

    @patch("llm_promptkit.helpers.subprocess.Popen")
    def test_copy_to_clipboard_xclip_success(self, mock_popen):
        """Should use xclip when available."""
        from llm_promptkit.helpers import copy_to_clipboard

        mock_process = MagicMock()
        mock_process.communicate.return_value = (b"", b"")
        mock_process.returncode = 0
        mock_popen.return_value = mock_process

        # Should not raise
        copy_to_clipboard("test text")

    @patch("llm_promptkit.helpers.subprocess.Popen")
    def test_copy_to_clipboard_no_tool(self, mock_popen):
        """Should handle missing clipboard tool gracefully."""
        from llm_promptkit.helpers import copy_to_clipboard

        mock_popen.side_effect = FileNotFoundError()

        # Should not raise, just print warning
        copy_to_clipboard("test text")

    @patch("llm_promptkit.helpers.subprocess.Popen")
    def test_copy_to_clipboard_tool_fails(self, mock_popen):
        """Should handle clipboard tool failure gracefully."""
        from llm_promptkit.helpers import copy_to_clipboard

        mock_process = MagicMock()
        mock_process.communicate.return_value = (b"", b"error")
        mock_process.returncode = 1
        mock_popen.return_value = mock_process

        # Should not raise
        copy_to_clipboard("test text")


# =============================================================================
# CLI Command Tests using CliRunner
# =============================================================================


class TestListCommand:
    """Tests for the list command."""

    def test_list_command_runs(self):
        """List command should run without error."""
        result = runner.invoke(app, ["list"])
        # May have no patterns dir in test, but should not crash
        assert result.exit_code == 0


class TestBuildCommand:
    """Tests for the build command."""

    def test_build_with_persona_and_task(self):
        """Build command should accept persona and task."""
        result = runner.invoke(app, ["build", "--persona", "Developer", "--task", "Review code"])
        assert result.exit_code == 0

    def test_build_with_pattern(self):
        """Build command should accept pattern."""
        result = runner.invoke(
            app,
            ["build", "--persona", "Developer", "--pattern", "chain-of-thought", "--task", "Test"],
        )
        assert result.exit_code == 0

    def test_build_with_tokens(self):
        """Build command should show token estimate."""
        result = runner.invoke(
            app, ["build", "--persona", "Developer", "--task", "Test", "--tokens"]
        )
        assert result.exit_code == 0

    def test_build_output_to_file(self, tmp_path):
        """Build command should write output to file."""
        output_file = tmp_path / "output.txt"
        result = runner.invoke(
            app, ["build", "--persona", "Developer", "--task", "Test", "--output", str(output_file)]
        )
        assert result.exit_code == 0
        assert output_file.exists()

    def test_build_invalid_pattern(self):
        """Build command should handle invalid pattern gracefully."""
        result = runner.invoke(
            app,
            [
                "build",
                "--persona",
                "Developer",
                "--pattern",
                "nonexistent-pattern",
                "--task",
                "Test",
            ],
        )
        assert result.exit_code == 1


class TestDoctorCommand:
    """Tests for the doctor command."""

    def test_doctor_with_text(self):
        """Doctor command should analyze text prompt."""
        result = runner.invoke(app, ["doctor", "You are a helpful assistant."])
        assert result.exit_code == 0

    def test_doctor_with_file(self, tmp_path):
        """Doctor command should analyze a prompt file."""
        f = tmp_path / "test.md"
        f.write_text("You are a helpful assistant. Format your output as JSON.")
        result = runner.invoke(app, ["doctor", str(f)])
        assert result.exit_code == 0


class TestPromptsCommand:
    """Tests for the prompts command."""

    def test_prompts_lists_providers(self):
        """Prompts command should list providers."""
        result = runner.invoke(app, ["prompts"])
        # Should list providers without crashing
        assert result.exit_code == 0


class TestSearchCommand:
    """Tests for the search command."""

    def test_search_with_query(self):
        """Search command should search prompts."""
        result = runner.invoke(app, ["search", "security", "--limit", "3"])
        assert result.exit_code == 0

    def test_search_empty_query(self):
        """Search with empty query should still work."""
        result = runner.invoke(app, ["search", "xyznonexistent"])
        assert result.exit_code == 0


class TestCLIHelp:
    """Tests for CLI help and version output."""

    def test_main_help(self):
        """Main --help should work."""
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "promptkit" in result.output.lower() or "build" in result.output.lower()

    def test_build_help(self):
        """Build --help should work."""
        result = runner.invoke(app, ["build", "--help"])
        assert result.exit_code == 0

    def test_doctor_help(self):
        """Doctor --help should work."""
        result = runner.invoke(app, ["doctor", "--help"])
        assert result.exit_code == 0
