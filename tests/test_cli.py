"""Tests for Typer CLI commands using CliRunner."""

from unittest.mock import MagicMock, patch

from typer.testing import CliRunner

from llm_promptkit.cli import app

runner = CliRunner()


class TestHelperFunctions:
    def test_is_prompt_file_valid_md(self, tmp_path):
        from llm_promptkit.helpers import is_prompt_file

        prompt = tmp_path / "coding.md"
        prompt.touch()
        assert is_prompt_file(prompt) is True

    def test_is_prompt_file_readme_excluded(self, tmp_path):
        from llm_promptkit.helpers import is_prompt_file

        (tmp_path / "README.md").touch()
        assert is_prompt_file(tmp_path / "README.md") is False

    def test_is_prompt_file_readme_case_insensitive(self, tmp_path):
        from llm_promptkit.helpers import is_prompt_file

        (tmp_path / "readme.md").touch()
        assert is_prompt_file(tmp_path / "readme.md") is False

    def test_is_prompt_file_non_md(self, tmp_path):
        from llm_promptkit.helpers import is_prompt_file

        (tmp_path / "notes.txt").touch()
        assert is_prompt_file(tmp_path / "notes.txt") is False

    def test_get_prompt_files_filters_correctly(self, tmp_path):
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
        from llm_promptkit.helpers import count_prompts

        (tmp_path / "a.md").touch()
        (tmp_path / "b.md").touch()
        (tmp_path / "README.md").touch()
        assert count_prompts(tmp_path) == 2

    def test_get_prompts_dir_cwd_fallback(self, tmp_path, monkeypatch):
        from llm_promptkit.helpers import get_prompts_dir

        (tmp_path / "prompts").mkdir()
        monkeypatch.chdir(tmp_path)
        assert get_prompts_dir().exists()


class TestCopyToClipboard:
    @patch("llm_promptkit.helpers.subprocess.Popen")
    def test_copy_to_clipboard_xclip_success(self, mock_popen):
        from llm_promptkit.helpers import copy_to_clipboard

        mock_process = MagicMock()
        mock_process.communicate.return_value = (b"", b"")
        mock_process.returncode = 0
        mock_popen.return_value = mock_process
        copy_to_clipboard("test text")

    @patch("llm_promptkit.helpers.subprocess.Popen")
    def test_copy_to_clipboard_no_tool(self, mock_popen):
        from llm_promptkit.helpers import copy_to_clipboard

        mock_popen.side_effect = FileNotFoundError()
        copy_to_clipboard("test text")

    @patch("llm_promptkit.helpers.subprocess.Popen")
    def test_copy_to_clipboard_tool_fails(self, mock_popen):
        from llm_promptkit.helpers import copy_to_clipboard

        mock_process = MagicMock()
        mock_process.communicate.return_value = (b"", b"error")
        mock_process.returncode = 1
        mock_popen.return_value = mock_process
        copy_to_clipboard("test text")


class TestListCommand:
    def test_list_command_runs(self):
        result = runner.invoke(app, ["list"])
        assert result.exit_code == 0

    def test_list_command_shows_patterns(self):
        result = runner.invoke(app, ["list"])
        assert "chain-of-thought" in result.output


class TestBuildCommand:
    def test_build_with_persona_and_task(self):
        result = runner.invoke(app, ["build", "--persona", "Developer", "--task", "Review code"])
        assert result.exit_code == 0
        assert "Developer" in result.output
        assert "Review code" in result.output

    def test_build_with_pattern(self):
        result = runner.invoke(
            app,
            ["build", "--persona", "Developer", "--pattern", "chain-of-thought", "--task", "Test"],
        )
        assert result.exit_code == 0
        assert "step-by-step" in result.output.lower() or "step" in result.output.lower()

    def test_build_with_tokens(self):
        result = runner.invoke(
            app, ["build", "--persona", "Developer", "--task", "Test", "--tokens"]
        )
        assert result.exit_code == 0
        assert "token" in result.output.lower()

    def test_build_output_to_file(self, tmp_path):
        output_file = tmp_path / "output.txt"
        result = runner.invoke(
            app, ["build", "--persona", "Developer", "--task", "Test", "--output", str(output_file)]
        )
        assert result.exit_code == 0
        assert output_file.exists()
        content = output_file.read_text()
        assert "Developer" in content

    def test_build_invalid_pattern(self):
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

    def test_build_with_context(self):
        result = runner.invoke(
            app, ["build", "--persona", "Dev", "--task", "Review", "--context", "def foo(): pass"]
        )
        assert result.exit_code == 0
        assert "foo" in result.output

    def test_build_with_constraint(self):
        result = runner.invoke(
            app, ["build", "--persona", "Dev", "--task", "Test", "--constraint", "Max 100 words"]
        )
        assert result.exit_code == 0
        assert "Max 100 words" in result.output


class TestDoctorCommand:
    def test_doctor_with_text(self):
        result = runner.invoke(app, ["doctor", "You are a helpful assistant."])
        assert result.exit_code == 0

    def test_doctor_with_file(self, tmp_path):
        f = tmp_path / "test.md"
        f.write_text("You are a helpful assistant. Format your output as JSON.")
        result = runner.invoke(app, ["doctor", str(f)])
        assert result.exit_code == 0

    def test_doctor_shows_suggestions(self):
        result = runner.invoke(app, ["doctor", "Write something nice about whatever you want"])
        assert result.exit_code == 0
        assert "ambiguous" in result.output.lower() or "missing" in result.output.lower()


class TestPromptsCommand:
    def test_prompts_lists_providers(self):
        result = runner.invoke(app, ["prompts"])
        assert result.exit_code == 0


class TestSearchCommand:
    def test_search_with_query(self):
        result = runner.invoke(app, ["search", "security", "--limit", "3"])
        assert result.exit_code == 0

    def test_search_empty_query(self):
        result = runner.invoke(app, ["search", "xyznonexistent"])
        assert result.exit_code == 0

    def test_search_with_category(self):
        result = runner.invoke(app, ["search", "step", "--category", "reasoning"])
        assert result.exit_code == 0

    def test_search_limit_one(self):
        result = runner.invoke(app, ["search", "prompt", "--limit", "1"])
        assert result.exit_code == 0


class TestCLIHelp:
    def test_main_help(self):
        result = runner.invoke(app, ["--help"])
        assert result.exit_code == 0
        assert "promptkit" in result.output.lower() or "build" in result.output.lower()

    def test_build_help(self):
        result = runner.invoke(app, ["build", "--help"])
        assert result.exit_code == 0

    def test_doctor_help(self):
        result = runner.invoke(app, ["doctor", "--help"])
        assert result.exit_code == 0
