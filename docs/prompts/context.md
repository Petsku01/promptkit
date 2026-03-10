# Context Prompts

Prompts for few-shot learning and RAG patterns.

## Available Prompts

| Prompt | Use Case |
|--------|----------|
| [few-shot-negatives](https://github.com/Petsku01/promptkit/blob/master/prompts/context/few-shot-negatives.md) | Few-shot with negative examples |

## About Few-Shot with Negatives

The most effective few-shot prompts include both positive AND negative examples. This helps the model understand not just what to do, but what to avoid.

```python
from llm_promptkit import PromptBuilder

prompt = (PromptBuilder()
    .pattern("few-shot")
    .example("Good input", "Good output")
    .example("Bad input", "Why this is wrong: ...")
    .task("Classify this input")
    .build())
```
