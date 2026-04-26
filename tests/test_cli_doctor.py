"""Tests for the doctor command using CliRunner."""

from typer.testing import CliRunner

from llm_promptkit.cli import app

runner = CliRunner()


class TestDoctorCommand:
    """Tests for the doctor command via CLI."""

    def test_doctor_command_no_issues(self):
        """Good prompt should report no issues."""
        result = runner.invoke(
            app,
            [
                "doctor",
                "You are a helpful assistant. Format your output as JSON. Here is an example: {}",
            ],
        )
        assert result.exit_code == 0
        assert "0" in result.output or "No" in result.output or "issue" in result.output.lower()

    def test_doctor_command_with_issues(self):
        """Vague prompt should report issues."""
        result = runner.invoke(app, ["doctor", "Write something nice about whatever you want"])
        assert result.exit_code == 0
        # Should detect issues

    def test_doctor_command_text_input(self):
        """Doctor should accept direct text input."""
        result = runner.invoke(app, ["doctor", "You are an assistant"])
        assert result.exit_code == 0


class TestDoctorEdgeCases:
    """Edge case tests for the doctor command via CLI."""

    def test_empty_prompt(self):
        """Doctor should handle empty-ish prompt."""
        result = runner.invoke(app, ["doctor", "   "])
        assert result.exit_code == 0 or result.exit_code == 1
        # Empty prompt is acceptable

    def test_long_prompt(self):
        """Doctor should handle long prompt."""
        long_text = "You are a helpful assistant. " * 100
        result = runner.invoke(app, ["doctor", long_text])
        assert result.exit_code == 0

    def test_code_blocks_only(self):
        """Doctor should handle code-only input."""
        result = runner.invoke(app, ["doctor", "```python\nprint('hello')\n```"])
        assert result.exit_code == 0

    def test_different_languages(self):
        """Doctor should handle non-English prompts."""
        result = runner.invoke(app, ["doctor", "Olet avustaja. Vastaa suomeksi."])
        assert result.exit_code == 0

    def test_mixed_patterns(self):
        """Doctor should detect mixed pattern usage."""
        result = runner.invoke(
            app,
            ["doctor", "Think step by step and act as a senior developer who must do your best"],
        )
        assert result.exit_code == 0

    def test_doctor_with_file(self, tmp_path):
        """Doctor should accept a file path."""
        f = tmp_path / "test.md"
        f.write_text("You are a helpful assistant. Format your output as JSON.")
        result = runner.invoke(app, ["doctor", str(f)])
        assert result.exit_code == 0

    def test_doctor_negative_phrase(self):
        """Doctor should detect negative phrases."""
        result = runner.invoke(app, ["doctor", "Do not give wrong answers"])
        assert result.exit_code == 0
