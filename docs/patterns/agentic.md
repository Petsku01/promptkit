# Agentic Patterns

Patterns for multi-step, tool-using, and autonomous agent workflows.

## ReAct

Interleave thinking, acting, and observing.

```python
from llm_promptkit import PromptBuilder

prompt = (PromptBuilder()
    .pattern("react")
    .task("Find the weather in Helsinki and plan an outfit")
    .build())
```

**When to use:** Tool use, multi-step actions, iterative problem solving.

---

## Prompt Chaining

Break a task into sequential stages.

```python
prompt = (PromptBuilder()
    .pattern("prompt-chaining")
    .task("Research, outline, then write an article about AI safety")
    .build())
```

**When to use:** Complex workflows, multi-step pipelines.

---

## Meta-Prompting

Let the model choose the best approach.

```python
prompt = (PromptBuilder()
    .pattern("meta-prompting")
    .task("Solve this problem using the best technique")
    .build())
```

**When to use:** Uncertain which technique to apply, let model decide.