# Prompt Patterns

Patterns are proven techniques that improve LLM responses. Each pattern targets a specific problem.

## Available Patterns (18)

| Category | Pattern | Use When You Need To... |
|----------|---------|-------------------------|
| **Reasoning** | `chain-of-thought` | Get step-by-step reasoning |
| **Reasoning** | `self-consistency` | Verify through multiple approaches |
| **Reasoning** | `tree-of-thought` | Complex problem solving with multiple perspectives |
| **Reasoning** | `step-back` | Find underlying principles first |
| **Reasoning** | `decomposition` | Break down complex problems |
| **Reasoning** | `reflection` | Self-correction and improvement |
| **Agentic** | `react` | Interleave thought, action, observation |
| **Agentic** | `prompt-chaining` | Multi-stage task decomposition |
| **Agentic** | `meta-prompting` | Let model choose optimal approach |
| **Context** | `few-shot` | Teach by example |
| **Context** | `few-shot-negatives` | Teach by example (including what NOT to do) |
| **Context** | `role-play` | Domain-specific perspective |
| **Output** | `json-output` | Get structured JSON data |
| **Output** | `json-enforcer` | Strictly enforce valid JSON |
| **Code** | `tdd-prompting` | Generate tests first, then implementation |
| **Code** | `stack-trace-decoder` | Debug errors from stack traces |
| **Review** | `senior-reviewer` | Critical code review |
| **Defensive** | `hallucination-reducer` | Reduce confident nonsense |

---

## Reasoning Patterns

### chain-of-thought

Forces explicit step-by-step reasoning.

```python
builder.pattern("chain-of-thought")
```

**When to use:** Math, logic puzzles, debugging, any multi-step problem.

**The prompt:**
```
Think through this step-by-step:
1. First, analyze the problem
2. Then, consider possible approaches
3. Finally, provide your solution

Show your reasoning at each step.
```

---

### self-consistency

Solves the problem multiple ways and picks the best answer.

```python
builder.pattern("self-consistency")
```

**When to use:** High-stakes decisions, verification needed.

---

### tree-of-thought

Multiple experts deliberate together.

```python
builder.pattern("tree-of-thought")
```

**When to use:** Complex reasoning, exploring solution space.

---

### step-back

Identifies core principles before solving.

```python
builder.pattern("step-back")
```

**When to use:** When direct approach fails, need fresh perspective.

---

### decomposition

Breaks complex problems into sub-problems.

```python
builder.pattern("decomposition")
```

**When to use:** Large tasks, system design.

---

### reflection

Self-reviews and improves the answer.

```python
builder.pattern("reflection")
```

**When to use:** Writing, important outputs.

---

## Agentic Patterns

### react

Interleave thinking, acting, and observing.

```python
builder.pattern("react")
```

**When to use:** Tool use, multi-step actions, iterative problem solving.

---

### prompt-chaining

Break a task into sequential stages.

```python
builder.pattern("prompt-chaining")
```

**When to use:** Complex workflows, multi-step pipelines.

---

### meta-prompting

Let the model choose the best approach.

```python
builder.pattern("meta-prompting")
```

**When to use:** Uncertain which technique to apply.

---

## Context Patterns

### few-shot

Teaches through examples.

```python
builder.pattern("few-shot")
builder.example("input", "expected output")
```

**When to use:** Classification, formatting, style transfer.

---

### few-shot-negatives

Teaches through both positive and negative examples.

```python
builder.pattern("few-shot-negatives")
```

**When to use:** When boundary cases matter, need to show what NOT to do.

---

### role-play

Adopts a specific professional perspective.

```python
builder.pattern("role-play")
```

**When to use:** Domain expertise needed, perspective-specific tasks.

---

## Output Patterns

### json-output

Enforces structured JSON output.

```python
builder.pattern("json-output")
builder.output_format("json", schema={"key": "type"})
```

**When to use:** API responses, structured data extraction.

---

### json-enforcer

Strictly enforces valid JSON, no markdown.

```python
builder.pattern("json-enforcer")
```

**When to use:** Strict JSON parsing needed, no tolerance for formatting errors.

---

## Code Patterns

### tdd-prompting

Generate tests first, then implementation.

```python
builder.pattern("tdd-prompting")
```

**When to use:** Writing new features, ensuring testability.

---

### stack-trace-decoder

Analyze and explain stack traces.

```python
builder.pattern("stack-trace-decoder")
```

**When to use:** Debugging errors, understanding crashes.

---

## Review Patterns

### senior-reviewer

Strict, critical code review persona.

```python
builder.pattern("senior-reviewer")
```

**When to use:** Code review, catching edge cases.

---

## Defensive Patterns

### hallucination-reducer

Reduces confident but incorrect responses.

```python
builder.pattern("hallucination-reducer")
```

**When to use:** Fact-checking, knowledge extraction, reducing made-up facts.

---

## Combining Patterns

Patterns stack. Put reasoning patterns first, output format patterns last:

```python
prompt = (PromptBuilder()
    .pattern("chain-of-thought")
    .pattern("reflection")
    .pattern("json-output")
    .task("Analyze this data")
    .build())
```