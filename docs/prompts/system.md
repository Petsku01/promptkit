# System Prompts

Base system-level prompts for LLM configuration.

## Available Prompts

| Prompt | Use Case |
|--------|----------|
| [coding-assistant](https://github.com/Petsku01/promptkit/blob/master/prompts/system/coding-assistant.md) | Core coding workflow |
| [error-recovery](https://github.com/Petsku01/promptkit/blob/master/prompts/system/error-recovery.md) | Error handling and resilience |

## Usage

System prompts define the base behavior of your AI:

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
