# Installation

## From GitHub

```bash
pip install git+https://github.com/Petsku01/promptkit.git
```

## With Token Counting

To enable accurate token estimation:

```bash
pip install "llm-promptkit[tokens] @ git+https://github.com/Petsku01/promptkit.git"
```

## For Development

```bash
git clone https://github.com/Petsku01/promptkit.git
cd promptkit
pip install -e ".[dev]"
```

## Requirements

- Python 3.9+
- No required dependencies (just stdlib)
- Optional: `tiktoken` for accurate token counting
- Optional: `rich` for CLI formatting

## Verify Installation

```python
from llm_promptkit import PromptBuilder

print(PromptBuilder.PATTERNS.keys())
# dict_keys(['chain-of-thought', 'few-shot', 'json-output', ...])
```

Or from CLI:

```bash
llm-promptkit list
# Shows all available patterns
```
