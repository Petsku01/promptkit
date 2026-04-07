"""Edge case tests for the doctor command."""

from unittest.mock import patch

from llm_promptkit.cli import doctor_command


class DummyArgs:
    def __init__(self, target=None, file=None):
        self.target = target
        self.file = file


@patch('llm_promptkit.commands.doctor.console')
def test_doctor_empty_prompt(mock_console):
    doctor_command(DummyArgs(target=""))
    assert mock_console.print.called


@patch('llm_promptkit.commands.doctor.console')
def test_doctor_code_only(mock_console):
    doctor_command(DummyArgs(target="```python\nprint('hello')\n```"))
    assert mock_console.print.called


@patch('llm_promptkit.commands.doctor.console')
def test_doctor_long_prompt(mock_console):
    doctor_command(DummyArgs(target="a" * 300))
    assert mock_console.print.called


@patch('llm_promptkit.commands.doctor.console')
def test_doctor_negative_phrase(mock_console):
    doctor_command(DummyArgs(target="do not do this. You are an expert. Format as JSON. Example: 1"))
    assert mock_console.print.called


@patch('llm_promptkit.commands.doctor.console')
def test_doctor_long_prompt_with_repeated_text(mock_console):
    prompt = "a" * 1500
    doctor_command(DummyArgs(target=prompt))
    assert mock_console.print.called


@patch('llm_promptkit.commands.doctor.console')
def test_doctor_multiple_code_blocks(mock_console):
    prompt = "```python\ndef foo():\n    pass\n```\n" * 5
    doctor_command(DummyArgs(target=prompt))
    assert mock_console.print.called


@patch('llm_promptkit.commands.doctor.console')
def test_doctor_non_english_prompt(mock_console):
    prompt = "Eres un asistente de IA. Formatea como JSON. Ejemplo: [1]"
    doctor_command(DummyArgs(target=prompt))
    assert mock_console.print.called


@patch('llm_promptkit.commands.doctor.console')
def test_doctor_mixed_patterns(mock_console):
    prompt = "You are a helpful assistant. Make it good ASAP. Format as JSON. Do not fail. Here is an example: X"
    doctor_command(DummyArgs(target=prompt))
    assert mock_console.print.called
