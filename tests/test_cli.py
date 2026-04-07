"""Tests for CLI module."""

from unittest.mock import patch

from llm_promptkit.cli import build_prompt, doctor_command, list_patterns, main


class MockBuildArgs:
    def __init__(self, persona=None, pattern=None, task=None, context=None,
                 constraint=None, output=None, tokens=False):
        self.persona = persona
        self.pattern = pattern
        self.task = task
        self.context = context
        self.constraint = constraint
        self.output = output
        self.tokens = tokens


class MockDoctorArgs:
    def __init__(self, target=None, file=None):
        self.target = target
        self.file = file


class TestListPatterns:
    @patch("llm_promptkit.cli.console")
    def test_list_patterns_outputs_table(self, mock_console):
        list_patterns()
        assert mock_console.print.called


class TestBuildPrompt:
    @patch("llm_promptkit.cli.console")
    def test_build_basic(self, mock_console):
        args = MockBuildArgs(persona="Dev", task="Review code")
        build_prompt(args)
        assert mock_console.print.called

    @patch("llm_promptkit.cli.console")
    def test_build_with_pattern(self, mock_console):
        args = MockBuildArgs(pattern=["chain-of-thought"], task="Analyze")
        build_prompt(args)
        assert mock_console.print.called

    @patch("llm_promptkit.cli.console")
    def test_build_invalid_pattern(self, mock_console):
        args = MockBuildArgs(pattern=["nonexistent-pattern"])
        build_prompt(args)
        mock_console.print.assert_any_call("[red]Error: Unknown pattern 'nonexistent-pattern'. Available: " + mock_console.print.call_args_list[0][0][0].split("Available: ")[1])

    @patch("llm_promptkit.cli.console")
    def test_build_with_constraints(self, mock_console):
        args = MockBuildArgs(task="Test", constraint=["No recursion", "Use Python"])
        build_prompt(args)
        assert mock_console.print.called

    @patch("llm_promptkit.cli.console")
    def test_build_with_tokens(self, mock_console):
        args = MockBuildArgs(task="Test", tokens=True)
        build_prompt(args)
        calls = [str(c) for c in mock_console.print.call_args_list]
        assert any("token" in c.lower() for c in calls)

    @patch("llm_promptkit.cli.console")
    def test_build_output_to_file(self, mock_console, tmp_path):
        output_file = tmp_path / "out.txt"
        args = MockBuildArgs(task="Test task", output=str(output_file))
        build_prompt(args)
        assert output_file.exists()
        assert "Test task" in output_file.read_text()


class TestDoctorCommand:
    @patch("llm_promptkit.cli.console")
    def test_no_issues(self, mock_console):
        args = MockDoctorArgs(target="You are a helpful assistant. Format as JSON. Example: {}")
        doctor_command(args)
        mock_console.print.assert_any_call("[bold green]No issues found. Prompt looks solid.[/bold green]")

    @patch("llm_promptkit.cli.console")
    def test_with_issues(self, mock_console):
        args = MockDoctorArgs(target="Make it good please")
        doctor_command(args)
        assert mock_console.print.called
        calls = mock_console.print.call_args_list
        table_found = any("Table" in str(type(c[0][0])) for c in calls)
        assert table_found

    @patch("llm_promptkit.cli.console")
    def test_file_input(self, mock_console, tmp_path):
        f = tmp_path / "prompt.md"
        f.write_text("You are an expert. Return JSON. Example: 1")
        args = MockDoctorArgs(file=str(f))
        doctor_command(args)
        mock_console.print.assert_any_call("[bold green]No issues found. Prompt looks solid.[/bold green]")

    @patch("llm_promptkit.cli.console")
    def test_file_not_found(self, mock_console):
        args = MockDoctorArgs(file="/nonexistent/file.md")
        doctor_command(args)
        mock_console.print.assert_any_call("[red]Error: File not found: /nonexistent/file.md[/red]")

    @patch("llm_promptkit.cli.console")
    def test_empty_prompt(self, mock_console):
        args = MockDoctorArgs(target="")
        doctor_command(args)
        assert mock_console.print.called


class TestMain:
    @patch("llm_promptkit.cli.list_patterns")
    def test_list_command(self, mock_list):
        with patch("sys.argv", ["promptkit", "list"]):
            main()
        mock_list.assert_called_once()

    @patch("llm_promptkit.cli.doctor_command")
    def test_doctor_command(self, mock_doctor):
        with patch("sys.argv", ["promptkit", "doctor", "test prompt"]):
            main()
        mock_doctor.assert_called_once()

    @patch("llm_promptkit.cli.build_prompt")
    def test_build_command(self, mock_build):
        with patch("sys.argv", ["promptkit", "build", "-t", "test"]):
            main()
        mock_build.assert_called_once()
