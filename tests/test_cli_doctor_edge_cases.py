import pytest
from unittest.mock import patch
from llm_promptkit.cli import doctor_command

class DummyArgs:
    def __init__(self, target=None, file=None):
        self.target = target
        self.file = file

@patch('llm_promptkit.cli.console')
def test_empty_prompt(mock_console):
    args = DummyArgs(target="")
    doctor_command(args)
    # Print the calls to see what issues are raised
    for call in mock_console.print.call_args_list:
        print("EMPTY PROMPT:", call)

@patch('llm_promptkit.cli.console')
def test_long_prompt(mock_console):
    prompt = "a" * 1500
    args = DummyArgs(target=prompt)
    doctor_command(args)
    for call in mock_console.print.call_args_list:
        print("LONG PROMPT:", call)

@patch('llm_promptkit.cli.console')
def test_code_blocks_only(mock_console):
    prompt = "```python\ndef foo():\n    pass\n```\n" * 5
    args = DummyArgs(target=prompt)
    doctor_command(args)
    for call in mock_console.print.call_args_list:
        print("CODE BLOCKS ONLY:", call)

@patch('llm_promptkit.cli.console')
def test_different_languages(mock_console):
    prompt = "Eres un asistente de IA. Formatea como JSON. Ejemplo: [1]"
    args = DummyArgs(target=prompt)
    doctor_command(args)
    for call in mock_console.print.call_args_list:
        print("DIFFERENT LANGUAGE:", call)

@patch('llm_promptkit.cli.console')
def test_mixed_patterns(mock_console):
    prompt = "You are a helpful assistant. Make it good ASAP. Format as JSON. Do not fail. Here is an example: X"
    args = DummyArgs(target=prompt)
    doctor_command(args)
    for call in mock_console.print.call_args_list:
        print("MIXED PATTERNS:", call)
