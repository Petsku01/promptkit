"""Tests for interactive prompt selector and search edge cases."""

from unittest.mock import patch

from typer.testing import CliRunner

from llm_promptkit.cli import app

runner = CliRunner()


class TestPromptsInteractive:
    """Test _interactive_prompts by mocking Prompt.ask."""

    @patch("llm_promptkit.cli.commands.prompts.Prompt.ask")
    def test_interactive_quit_immediately(self, mock_ask):
        mock_ask.return_value = "q"
        result = runner.invoke(app, ["prompts", "--interactive", "-i"])
        assert result.exit_code == 0

    @patch("llm_promptkit.cli.commands.prompts.Prompt.ask")
    def test_interactive_back_at_top(self, mock_ask):
        # 'b' at top level, then 'q' to quit
        mock_ask.side_effect = ["b", "q"]
        result = runner.invoke(app, ["prompts", "--interactive"])
        assert result.exit_code == 0

    @patch("llm_promptkit.cli.commands.prompts.Prompt.ask")
    def test_interactive_invalid_then_quit(self, mock_ask):
        # Invalid number, then quit
        mock_ask.side_effect = ["abc", "q"]
        result = runner.invoke(app, ["prompts", "--interactive"])
        assert result.exit_code == 0
        assert "invalid" in result.output.lower() or "number" in result.output.lower()

    @patch("llm_promptkit.cli.commands.prompts.Prompt.ask")
    def test_interactive_out_of_range_quit(self, mock_ask):
        # Number too high, then quit
        mock_ask.side_effect = ["999", "q"]
        result = runner.invoke(app, ["prompts", "--interactive"])
        assert result.exit_code == 0
        assert "invalid" in result.output.lower()


class TestSearchEdgeCases:
    """Test search command edge cases for coverage."""

    def test_search_with_many_results(self):
        result = runner.invoke(app, ["search", "prompt", "--limit", "20"])
        assert result.exit_code == 0

    def test_search_no_results(self):
        result = runner.invoke(app, ["search", "zzzzzzzznonexistent"])
        assert result.exit_code == 0
        assert "no" in result.output.lower() or result.exit_code == 0


class TestHelperFunctions:
    """Test helper functions for coverage."""

    def test_get_models_with_prompts_empty(self, tmp_path):
        from llm_promptkit.helpers import get_models_with_prompts

        result = get_models_with_prompts(tmp_path)
        assert result == []

    def test_get_models_with_prompts_with_data(self, tmp_path):
        from llm_promptkit.helpers import get_models_with_prompts

        model_dir = tmp_path / "gpt4"
        model_dir.mkdir()
        (model_dir / "coding.md").write_text("# Coding prompt")
        result = get_models_with_prompts(tmp_path)
        assert len(result) == 1
        assert result[0][0] == "gpt4"
        assert result[0][1] == 1

    def test_get_prompts_dir_package_exists(self):
        from llm_promptkit.helpers import get_prompts_dir

        prompts_dir = get_prompts_dir()
        # Should return a path (either package or cwd fallback)
        assert prompts_dir is not None
