from unittest.mock import patch

from llm_promptkit.cli import doctor_command


class DummyArgs:
    def __init__(self, target=None, file=None):
        self.target = target
        self.file = file


def print_issues(args):
    with patch("llm_promptkit.cli.console.print") as mock_print:
        doctor_command(args)
        for call in mock_print.call_args_list:
            arg = call[0][0]
            if "Table" in str(type(arg)):
                print("Table columns:", [c.header for c in arg.columns])
                for col in arg.columns:
                    print(f"Col {col.header}:", list(col.cells))
            else:
                print(arg)


print("=== EMPTY PROMPT ===")
print_issues(DummyArgs(target=""))

print("=== LONG PROMPT ===")
print_issues(DummyArgs(target="a" * 1500))

print("=== CODE BLOCKS ONLY ===")
print_issues(DummyArgs(target="```python\ndef foo():\n    pass\n```\n" * 5))

print("=== DIFFERENT LANGUAGE ===")
print_issues(DummyArgs(target="Eres un asistente de IA. Formatea como JSON. Ejemplo: [1]"))

print("=== MIXED PATTERNS ===")
print_issues(
    DummyArgs(
        target="You are a helpful assistant. Make it good ASAP. Format as JSON. Do not fail. Here is an example: X"
    )
)
