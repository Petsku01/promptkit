# Context Prompts

Prompts for managing context, examples, and information retrieval.

## Browsing Prompts

```bash
promptkit prompts --model context
promptkit search "few-shot"
```

## Available Prompts

| Prompt | Description |
|--------|-------------|
| few-shot-negatives | Few-shot with positive and negative examples |

## About Few-Shot with Negatives

The `few-shot-negatives` pattern teaches the model by showing both what to do and what NOT to do, which improves boundary understanding.

```python
from llm_promptkit import PromptBuilder

builder = PromptBuilder()
builder.pattern("few-shot-negatives")
builder.example("correct input", "correct output")
builder.example("wrong input", "wrong output")
builder.task("Classify this text")
prompt = builder.build()
```