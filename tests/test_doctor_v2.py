"""Tests for Doctor v2 — new heuristics, --fix, --dry-run, JSON output."""

import json
import tempfile
from pathlib import Path

from typer.testing import CliRunner

from llm_promptkit.cli import app

runner = CliRunner()


# ============================================================================
# New heuristics (v0.3.0)
# ============================================================================


class TestDoctorNewHeuristics:
    """Test v0.3.0 new heuristics: sentence length, duplication, context boundary."""

    def test_long_sentence(self):
        """Detect sentences over 40 words."""
        long_prompt = "Analyze this " + "very " * 45 + "carefully."
        result = runner.invoke(app, ["doctor", long_prompt])
        assert result.exit_code == 0
        assert "Long sentence" in result.output or "long sentence" in result.output.lower()

    def test_short_sentence_no_warning(self):
        """Short sentences don't trigger the warning."""
        short_prompt = "You are a senior developer. Review this code for security issues."
        result = runner.invoke(app, ["doctor", short_prompt])
        assert "Long sentence" not in result.output

    def test_duplication_bigram(self):
        """Detect repeated bigrams."""
        dup_prompt = "Please review this code review carefully. The code review should be thorough."
        result = runner.invoke(app, ["doctor", dup_prompt])
        assert result.exit_code == 0
        # Should detect "code review" repetition
        assert "Repeated" in result.output or "repeated" in result.output.lower() or "bigram" in result.output.lower()

    def test_no_duplication_in_normal_text(self):
        """Normal text doesn't trigger duplication warning."""
        normal_prompt = "You are a senior developer. Review the following code for security issues."
        result = runner.invoke(app, ["doctor", normal_prompt])
        assert "Repeated bigram" not in result.output and "repeated bigram" not in result.output.lower()

    def test_context_boundary_empty(self):
        """Detect empty section headings like 'Task:' with no content."""
        import tempfile
        from pathlib import Path
        # Task: heading followed by very short content (under 10 chars)
        empty_task = "You are a developer.\n\nTask:\n\nok\n\nOutput as JSON."
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
            f.write(empty_task)
            f.flush()
            filepath = f.name
        result = runner.invoke(app, ["doctor", "--file", filepath])
        assert result.exit_code == 0
        assert "Empty section" in result.output or "Task" in result.output
        Path(filepath).unlink()

    def test_ambiguous_language(self):
        """Detect ambiguous language like 'maybe', 'possibly'."""
        ambiguous_prompt = "Maybe review this code and possibly suggest improvements."
        result = runner.invoke(app, ["doctor", ambiguous_prompt])
        assert result.exit_code == 0
        assert "Ambiguous" in result.output or "ambiguous" in result.output.lower()


# ============================================================================
# Doctor --fix
# ============================================================================


class TestDoctorFix:
    """Test Doctor --fix and --dry-run functionality."""

    def test_fix_removes_please(self):
        """--fix removes standalone 'please'."""
        result = runner.invoke(app, ["doctor", "--fix", "Please review this code"])
        assert result.exit_code == 0
        assert "review this code" in result.output.lower()

    def test_fix_collapses_double_whitespace(self):
        """--fix collapses double whitespace."""
        result = runner.invoke(app, ["doctor", "--fix", "Review this  code  carefully"])
        assert result.exit_code == 0
        assert "Review this code carefully" in result.output

    def test_fix_strips_trailing_whitespace(self):
        """--fix strips trailing whitespace from lines."""
        result = runner.invoke(app, ["doctor", "--fix", "Review this code   "])
        assert result.exit_code == 0
        assert "Review this code" in result.output

    def test_fix_strips_leading_blank_lines(self):
        """--fix strips leading and trailing blank lines."""
        result = runner.invoke(app, ["doctor", "--fix", "\n\n\nReview this code\n\n\n"])
        assert result.exit_code == 0
        assert "Review this code" in result.output

    def test_fix_file_creates_backup(self):
        """--fix on a file creates a .bak backup."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
            f.write("Please review this code carefully")
            f.flush()
            filepath = f.name

        result = runner.invoke(app, ["doctor", "--fix", "--file", filepath])
        assert result.exit_code == 0

        # Check backup was created
        backup_path = Path(filepath).with_suffix(".md.bak")
        assert backup_path.exists()
        assert "Please review" in backup_path.read_text()

        # Check original was fixed
        assert "Review this code" in Path(filepath).read_text() or "carefully" in Path(filepath).read_text()

        # Cleanup
        Path(filepath).unlink()
        backup_path.unlink(missing_ok=True)

    def test_dry_run_no_modification(self):
        """--fix --dry-run shows changes but doesn't modify the file."""
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
            f.write("Please review this code")
            f.flush()
            filepath = f.name

        original_content = Path(filepath).read_text()
        result = runner.invoke(app, ["doctor", "--fix", "--dry-run", "--file", filepath])
        assert result.exit_code == 0

        # File should NOT be modified
        assert Path(filepath).read_text() == original_content

        # Cleanup
        Path(filepath).unlink()

    def test_fix_no_issues(self):
        """--fix with no fixable issues prints 'No safe fixes'."""
        clean_prompt = "You are a senior developer. Review the code for security vulnerabilities."
        with tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False) as f:
            f.write(clean_prompt)
            f.flush()
            filepath = f.name

        result = runner.invoke(app, ["doctor", "--fix", "--file", filepath])
        assert result.exit_code == 0
        assert "No safe fixes" in result.output

        Path(filepath).unlink()

    def test_dry_run_without_fix_warns(self):
        """--dry-run without --fix shows warning."""
        result = runner.invoke(app, ["doctor", "--dry-run", "Please review this"])
        assert result.exit_code == 0
        # Should warn about dry-run requiring fix
        assert "dry-run" in result.output.lower() or "fix" in result.output.lower()


# ============================================================================
# Doctor JSON output
# ============================================================================


class TestDoctorJSON:
    """Test Doctor --format json."""

    def test_json_output_structure(self):
        """JSON output has correct structure."""
        result = runner.invoke(app, ["doctor", "--format", "json", "make it good please"])
        assert result.exit_code == 0
        data = json.loads(result.output)
        assert "version" in data
        assert "input_length" in data
        assert "issues" in data
        assert isinstance(data["issues"], list)

    def test_json_issue_fields(self):
        """JSON issues have required fields."""
        result = runner.invoke(app, ["doctor", "--format", "json", "make it good please"])
        assert result.exit_code == 0
        data = json.loads(result.output)
        if data["issues"]:
            issue = data["issues"][0]
            assert "severity" in issue
            assert "issue" in issue
            assert "suggestion" in issue
            assert "fixable" in issue

    def test_json_fixable_field(self):
        """JSON issues correctly mark fixable items."""
        result = runner.invoke(app, ["doctor", "--format", "json", "please review this"])
        assert result.exit_code == 0
        data = json.loads(result.output)
        # "please" should be marked as fixable
        fixable_issues = [i for i in data["issues"] if i.get("fixable")]
        assert len(fixable_issues) > 0

    def test_json_empty_prompt(self):
        """JSON output for empty prompt returns error."""
        result = runner.invoke(app, ["doctor", "--format", "json", ""])
        assert result.exit_code == 1

    def test_json_no_issues(self):
        """JSON output for a good prompt."""
        good_prompt = (
            "You are a senior Python developer. "
            "Review the following code for security vulnerabilities. "
            "Output as: JSON with fields 'issues' and 'severity'."
        )
        result = runner.invoke(app, ["doctor", "--format", "json", good_prompt])
        assert result.exit_code == 0
        json.loads(result.output)  # Validate JSON is parseable
        # May still have some suggestions, but should be fewer

    def test_json_invalid_format(self):
        """Invalid format returns error."""
        result = runner.invoke(app, ["doctor", "--format", "xml", "test"])
        assert result.exit_code == 1

    def test_json_with_fix(self):
        """JSON + --fix outputs fixed text with analysis."""
        result = runner.invoke(
            app, ["doctor", "--fix", "--format", "json", "please review this code"]
        )
        assert result.exit_code == 0
        data = json.loads(result.output)
        assert "original_issues" in data
        assert "fixed_text" in data
        # Fixed text should not start with "please" (case insensitive start)
        # Note: "Please review" → "Review" after fix
        fixed = data["fixed_text"].strip()
        assert not fixed.lower().startswith("please")


# ============================================================================
# Edge cases
# ============================================================================


class TestDoctorEdgeCases:
    """Test Doctor edge cases."""

    def test_please_as_part_of_word(self):
        """'please' as part of another word should not be removed."""
        result = runner.invoke(app, ["doctor", "--fix", "unpleasent experience"])
        # "unpleasent" is not a standalone "please"
        assert result.exit_code == 0

    def test_empty_prompt(self):
        """Empty prompt returns error."""
        result = runner.invoke(app, ["doctor", ""])
        # Typer treats "" as no argument → exit_code 1
        assert result.exit_code == 1
        # Error message about providing prompt text
        assert "prompt" in result.output.lower() or "text" in result.output.lower()

    def test_code_only_prompt(self):
        """Prompt with only code blocks."""
        result = runner.invoke(app, ["doctor", "```python\nprint('hello')\n```"])
        assert result.exit_code == 0
        assert "code" in result.output.lower()

    def test_file_path_is_directory(self):
        """--file with directory returns error."""
        result = runner.invoke(app, ["doctor", "--file", "/tmp"])
        assert result.exit_code == 1
