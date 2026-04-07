from unittest.mock import patch

from llm_promptkit.commands import doctor_command


class DummyArgs:
    def __init__(self, target=None, file=None, ml=False, model="qwen2.5:3b"):
        self.target = target
        self.file = file
        self.ml = ml
        self.model = model

@patch('llm_promptkit.commands.doctor.console')
def test_doctor_command_no_issues(mock_console, tmp_path):
    good_prompt = "You are a helpful assistant. Format your output as JSON. Here is an example: {}"
    f = tmp_path / "good.md"
    f.write_text(good_prompt)

    args = DummyArgs(file=str(f))
    doctor_command(args)

    mock_console.print.assert_any_call("[bold green]No issues found. Prompt looks solid.[/bold green]")

@patch('llm_promptkit.commands.doctor.console')
def test_doctor_command_with_issues(mock_console):
    bad_prompt = "Make it good. I would like you to do it."
    args = DummyArgs(target=bad_prompt)
    doctor_command(args)

    # Check that console.print was called with a Table object
    assert mock_console.print.called
    args_list = mock_console.print.call_args_list
    table_found = any('Table' in str(type(call_args[0][0])) for call_args in args_list)
    assert table_found

@patch('llm_promptkit.commands.doctor.console')
def test_doctor_command_text_input(mock_console):
    prompt_text = "System: analyze this. Return JSON. Example: X."
    args = DummyArgs(target=prompt_text)
    doctor_command(args)

    mock_console.print.assert_any_call("[bold green]No issues found. Prompt looks solid.[/bold green]")
