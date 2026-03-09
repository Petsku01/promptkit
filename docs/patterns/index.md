# Prompt Patterns

Patterns are proven techniques that improve LLM responses. Each pattern targets a specific problem.

## Available Patterns

| Pattern | Use When You Need To... |
|---------|-------------------------|
| **[chain-of-thought](#chain-of-thought)** | Get step-by-step reasoning |
| **[self-consistency](#self-consistency)** | Verify through multiple approaches |
| **[few-shot](#few-shot)** | Teach by example |
| **[json-output](#json-output)** | Get structured data |
| **[senior-reviewer](#senior-reviewer)** | Critical code review |
| **[tree-of-thought](#tree-of-thought)** | Complex problem solving |
| **[step-back](#step-back)** | Find underlying principles |
| **[decomposition](#decomposition)** | Break down complex problems |
| **[reflection](#reflection)** | Self-correction |
| **[role-play](#role-play)** | Domain-specific perspective |

---

## chain-of-thought

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

## self-consistency

Solves the problem multiple ways and picks the best answer.

```python
builder.pattern("self-consistency")
```

**When to use:** High-stakes decisions, verification needed.

**The prompt:**
```
Solve this problem three different ways, then compare your 
answers and give the most likely correct one.
```

---

## few-shot

Teaches through examples (including what NOT to do).

```python
builder.pattern("few-shot")
builder.example("input", "expected output")
```

**When to use:** Classification, formatting, style transfer.

---

## json-output

Enforces valid JSON output.

```python
builder.pattern("json-output")
builder.output_format("json", schema={"key": "type"})
```

**When to use:** API responses, structured data extraction.

**The prompt:**
```
Return ONLY valid JSON matching this schema:
{schema}

No explanation, no markdown, no code blocks.
```

---

## senior-reviewer

Strict, critical code review persona.

```python
builder.pattern("senior-reviewer")
```

**When to use:** Code review, catching edge cases.

**The prompt:**
```
You are a senior engineer with 15 years of experience. 
You are known for thorough, critical reviews. 
Never say 'looks good' unless it's genuinely excellent.
```

---

## tree-of-thought

Multiple experts deliberate together.

```python
builder.pattern("tree-of-thought")
```

**When to use:** Complex reasoning, exploring solution space.

---

## step-back

Identifies core principles before solving.

```python
builder.pattern("step-back")
```

**When to use:** When direct approach fails, need fresh perspective.

---

## decomposition

Breaks complex problems into sub-problems.

```python
builder.pattern("decomposition")
```

**When to use:** Large tasks, system design.

---

## reflection

Self-reviews and improves the answer.

```python
builder.pattern("reflection")
```

**When to use:** Writing, important outputs.

---

## role-play

Adopts a specific professional perspective.

```python
builder.pattern("role-play")
```

**When to use:** Domain expertise needed.

---

## Combining Patterns

Patterns stack:

```python
prompt = (PromptBuilder()
    .pattern("chain-of-thought")
    .pattern("reflection")
    .pattern("json-output")
    .task("Analyze this data")
    .build())
```

!!! tip "Order matters"
    Patterns are added in order. Put reasoning patterns first,
    output format patterns last.
