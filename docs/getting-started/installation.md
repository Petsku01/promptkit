# Installation

## From PyPI

```bash
pip install llm-promptkit
```

## With Token Counting

To enable accurate token estimation:

```bash
pip install "llm-promptkit[tokens]"
```

## From Source

```bash
git clone https://github.com/Petsku01/promptkit.git
cd promptkit
pip install -e .
```

## For Development

```bash
git clone https://github.com/Petsku01/promptkit.git
cd promptkit
pip install -e ".[dev]"
```

## Requirements

- Python 3.9+
- Required: `rich`, `typer` (installed automatically)
- Optional: `tiktoken` for accurate token counting

## Verify Installation

```python
from llm_promptkit import PromptBuilder

builder = PromptBuilder()
print(builder.get_available_patterns())
# ('chain-of-thought', 'self-consistency', 'few-shot', ...)
```

Or from CLI:

```bash
promptkit list
# Shows all 18 available patterns
```