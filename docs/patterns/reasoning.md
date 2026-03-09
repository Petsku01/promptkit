# Reasoning Patterns

Patterns that improve logical thinking and problem-solving.

## Chain of Thought

Forces step-by-step reasoning.

```python
from llm_promptkit import PromptBuilder

prompt = (PromptBuilder()
    .pattern("chain-of-thought")
    .task("What is 23 × 17?")
    .build())
```

**Best for:** Math, logic, debugging, any multi-step problem.

**Research:** [Wei et al., 2022](https://arxiv.org/abs/2201.11903)

---

## Self-Consistency

Solves the problem multiple ways, compares answers.

```python
prompt = (PromptBuilder()
    .pattern("self-consistency")
    .task("Is this code thread-safe?")
    .context(code)
    .build())
```

**Best for:** High-stakes decisions, verification.

---

## Tree of Thought

Multiple experts deliberate step-by-step.

```python
prompt = (PromptBuilder()
    .pattern("tree-of-thought")
    .task("Design a caching strategy")
    .build())
```

**Best for:** Complex problems with many possible approaches.

**Research:** [Yao et al., 2023](https://arxiv.org/abs/2305.10601)

---

## Step-Back

Identifies core principles before solving.

```python
prompt = (PromptBuilder()
    .pattern("step-back")
    .task("Why is my Docker container crashing?")
    .context(error_logs)
    .build())
```

**Best for:** When direct approach fails.

**Research:** [Zheng et al., 2024](https://arxiv.org/abs/2310.06117)

---

## Decomposition

Breaks complex problems into sub-problems.

```python
prompt = (PromptBuilder()
    .pattern("decomposition")
    .task("Design a URL shortener service")
    .build())
```

**Best for:** System design, large tasks.

---

## Reflection

Self-reviews and improves the answer.

```python
prompt = (PromptBuilder()
    .pattern("reflection")
    .task("Write a product description")
    .build())
```

**Best for:** Writing, important outputs that need polish.
