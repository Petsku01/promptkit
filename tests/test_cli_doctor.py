"""Tests for the doctor command using CliRunner."""

from typer.testing import CliRunner

from llm_promptkit.cli import app

runner = CliRunner()


class TestDoctorCommand:
    def test_doctor_command_no_issues(self):
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
        result = runner.invoke(app, ["doctor", "Write something nice about whatever you want"])
        assert result.exit_code == 0

    def test_doctor_command_text_input(self):
        result = runner.invoke(app, ["doctor", "You are an assistant"])
        assert result.exit_code == 0


class TestDoctorEdgeCases:
    def test_empty_prompt(self):
        result = runner.invoke(app, ["doctor", "   "])
        assert result.exit_code == 0 or result.exit_code == 1

    def test_long_prompt(self):
        result = runner.invoke(app, ["doctor", "You are a helpful assistant. " * 100])
        assert result.exit_code == 0

    def test_code_blocks_only(self):
        result = runner.invoke(app, ["doctor", "```python\nprint('hello')\n```"])
        assert result.exit_code == 0

    def test_different_languages(self):
        result = runner.invoke(app, ["doctor", "Olet avustaja. Vastaa suomeksi."])
        assert result.exit_code == 0

    def test_mixed_patterns(self):
        result = runner.invoke(
            app,
            ["doctor", "Think step by step and act as a senior developer who must do your best"],
        )
        assert result.exit_code == 0

    def test_doctor_with_file(self, tmp_path):
        f = tmp_path / "test.md"
        f.write_text("You are a helpful assistant. Format your output as JSON.")
        result = runner.invoke(app, ["doctor", str(f)])
        assert result.exit_code == 0

    def test_doctor_negative_phrase(self):
        result = runner.invoke(app, ["doctor", "Do not give wrong answers"])
        assert result.exit_code == 0
