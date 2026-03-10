# System Prompts

Base system prompts for AI assistants.

## Available Prompts

| Prompt | Use Case |
|--------|----------|
| [coding-assistant](https://github.com/Petsku01/promptkit/blob/master/prompts/system/coding-assistant.md) | General coding assistant |
| [claude-soul-principles](https://github.com/Petsku01/promptkit/blob/master/prompts/system/claude-soul-principles.md) | Claude-style principles |

## Usage

System prompts define the base behavior of your AI. Use them as the foundation:

```python
from llm_promptkit import PromptBuilder

with open("prompts/system/coding-assistant.md") as f:
    system = f.read()

prompt = (PromptBuilder()
    .system(system)
    .task("Help me refactor this function")
    .context(code)
    .build())
```
