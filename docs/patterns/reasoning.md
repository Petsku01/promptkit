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

**When to use:** Math, logic puzzles, debugging, any multi-step problem.

---

## Self-Consistency

Solves the problem multiple ways and picks the best answer.

```python
prompt = (PromptBuilder()
    .pattern("self-consistency")
    .task("What is the capital of Australia?")
    .build())
```

**When to use:** High-stakes decisions, verification needed.

---

## Tree of Thought

Multiple experts deliberate together.

```python
prompt = (PromptBuilder()
    .pattern("tree-of-thought")
    .task("Design a scalable microservices architecture")
    .build())
```

**When to use:** Complex reasoning, exploring solution space.

---

## Step-Back

Identifies core principles before solving.

```python
prompt = (PromptBuilder()
    .pattern("step-back")
    .task("Why does this algorithm fail on edge cases?")
    .build())
```

**When to use:** When direct approach fails, need fresh perspective.

---

## Decomposition

Breaks complex problems into sub-problems.

```python
prompt = (PromptBuilder()
    .pattern("decomposition")
    .task("Build an e-commerce platform")
    .build())
```

**When to use:** Large tasks, system design.

---

## Reflection

Self-reviews and improves the answer.

```python
prompt = (PromptBuilder()
    .pattern("reflection")
    .task("Write a summary of this article")
    .build())
```

**When to use:** Writing, important outputs, quality improvement.