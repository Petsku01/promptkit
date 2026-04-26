# System Prompts

Core system prompts for setting AI behavior and identity.

## Browsing Prompts

```bash
promptkit search "system"
promptkit prompts --model system
```

## Available Prompts

| Prompt | Description |
|--------|-------------|
| coding-assistant | General coding assistant |
| claude-soul-principles | Claude ethical principles |
| prompt-improver | Improve and optimize any LLM prompt |

## Example Usage

```python
from llm_promptkit import PromptBuilder

builder = PromptBuilder()
builder.system("You are an expert Python developer.")
builder.pattern("chain-of-thought")
builder.task("Debug this function")
prompt = builder.build()
```