import pytest
from unittest.mock import patch, MagicMock
from promptkit.cli import build_prompt

class MockArgs:
    def __init__(self):
        self.persona = "Senior Developer"
        self.pattern = ["chain-of-thought"]
        self.task = "Review code"
        self.context = None
        self.constraint = None
        self.tokens = False
        self.output = None

@patch("promptkit.cli.console.print")
def test_build_prompt_cli(mock_print):
    args = MockArgs()
    build_prompt(args)
    assert mock_print.called
