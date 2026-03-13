import pytest
from unittest.mock import patch, MagicMock
from llm_promptkit.cli import doctor_command

class DummyArgs:
    def __init__(self, target=None, file=None):
        self.target = target
        self.file = file

@patch('llm_promptkit.cli.console')
def test_doctor_empty_prompt(mock_console):
    doctor_command(DummyArgs(target=""))
    # The last call to print should contain the Table
    assert mock_console.print.called

@patch('llm_promptkit.cli.console')
def test_doctor_code_only(mock_console):
    doctor_command(DummyArgs(target="```python\nprint('hello')\n```"))
    assert mock_console.print.called

@patch('llm_promptkit.cli.console')
def test_doctor_long_prompt(mock_console):
    doctor_command(DummyArgs(target="a" * 300))
    assert mock_console.print.called

@patch('llm_promptkit.cli.console')
def test_doctor_negative_phrase(mock_console):
    doctor_command(DummyArgs(target="do not do this. You are an expert. Format as JSON. Example: 1"))
    assert mock_console.print.called
