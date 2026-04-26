"""Tests for interactive CLI commands using mocked Prompt.ask."""

from unittest.mock import patch

from typer.testing import CliRunner

from llm_promptkit.cli import app

runner = CliRunner()


class TestBuildInteractive:
    """Test build --interactive by mocking Prompt.ask."""

    @patch("llm_promptkit.cli.commands.build.Prompt.ask")
    def test_interactive_build_with_persona_and_task(self, mock_ask):
        # Persona, Patterns (empty), Task, Context (empty)
        mock_ask.side_effect = ["Senior Dev", "", "Review this code", ""]
        result = runner.invoke(app, ["build", "--interactive", "-i"])
        assert result.exit_code == 0
        assert "Senior Dev" in result.output

    @patch("llm_promptkit.cli.commands.build.Prompt.ask")
    def test_interactive_build_with_pattern(self, mock_ask):
        # Persona, Patterns, Task, Context
        mock_ask.side_effect = ["Developer", "chain-of-thought", "Test task", ""]
        result = runner.invoke(app, ["build", "--interactive"])
        assert result.exit_code == 0
        assert "step-by-step" in result.output.lower() or "step" in result.output.lower()

    @patch("llm_promptkit.cli.commands.build.Prompt.ask")
    def test_interactive_build_invalid_pattern_warns(self, mock_ask):
        # Persona, invalid pattern, Task, Context
        mock_ask.side_effect = ["Dev", "nonexistent-xyz", "Task", ""]
        result = runner.invoke(app, ["build", "--interactive"])
        assert result.exit_code == 0
        assert "warning" in result.output.lower() or "unknown" in result.output.lower()

    @patch("llm_promptkit.cli.commands.build.Prompt.ask")
    def test_interactive_build_empty_persona(self, mock_ask):
        # Empty persona, no patterns, Task, no context
        mock_ask.side_effect = ["", "", "Simple task", ""]
        result = runner.invoke(app, ["build", "--interactive"])
        assert result.exit_code == 0
        assert "Simple task" in result.output


class TestPromptsNonInteractive:
    """Test prompts command non-interactive branches."""

    def test_prompts_show_invalid_format(self):
        result = runner.invoke(app, ["prompts", "--show", "invalid"])
        assert result.exit_code == 0
        assert "invalid" in result.output.lower() or "format" in result.output.lower()

    def test_prompts_model_invalid_format(self):
        result = runner.invoke(app, ["prompts", "--model", "a/b/c"])
        assert result.exit_code == 0
        assert "invalid" in result.output.lower() or "format" in result.output.lower()

    def test_prompts_show_not_found(self):
        result = runner.invoke(app, ["prompts", "--show", "fake/model/prompt"])
        assert result.exit_code == 0
        assert "not found" in result.output.lower()

    def test_prompts_model_not_found(self):
        result = runner.invoke(app, ["prompts", "--model", "nonexistent_provider"])
        assert result.exit_code == 0
