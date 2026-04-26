# Reasoning Prompts

Prompts for step-by-step thinking, analysis, and problem decomposition.

## Browsing Prompts

```bash
promptkit search "reasoning"
promptkit search "analysis"
```

## Available Prompts

| Prompt | Description |
|--------|-------------|
| chain-of-thought | Step-by-step reasoning |
| decomposition | Break down complex problems |
| expert-persona | Domain expert perspective |
| data-analyst | Data analysis tasks |
| financial-analyst | Financial analysis |
| readability-logic-simulator | Logic and readability analysis |
| red-team | Adversarial testing |
| scenario-planner | Scenario planning |
| socratic-questioning | Socratic method |
| thinking-framework | Structured thinking |

## Built-in Patterns

The `chain-of-thought`, `self-consistency`, `tree-of-thought`, `step-back`, `decomposition`, and `reflection` patterns are built into PromptKit:

```python
from llm_promptkit import PromptBuilder

builder = PromptBuilder()
builder.pattern("chain-of-thought")
builder.task("Solve this logic puzzle")
prompt = builder.build()
```

See [Reasoning Patterns](../patterns/reasoning.md) for details.