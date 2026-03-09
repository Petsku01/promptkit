# PromptBuilder API

The main class for composing prompts.

## Import

```python
from llm_promptkit import PromptBuilder
```

## Methods

### `persona(role: str)`

Set the AI persona/role.

```python
builder.persona("Senior Developer")
# → "You are a Senior Developer."
```

---

### `pattern(pattern_name: str)`

Add a prompt pattern. Can be called multiple times.

```python
builder.pattern("chain-of-thought")
builder.pattern("reflection")
```

**Available patterns:**

- `chain-of-thought` — Step-by-step reasoning
- `self-consistency` — Multiple solution paths
- `few-shot` — Learn from examples
- `json-output` — Structured JSON output
- `senior-reviewer` — Critical review persona
- `tree-of-thought` — Multi-expert deliberation
- `step-back` — Find underlying principles
- `decomposition` — Break into sub-problems
- `reflection` — Self-review and improve
- `role-play` — Professional perspective

---

### `task(task_description: str)`

Set the main task/question.

```python
builder.task("Review this code for bugs")
# → "Task: Review this code for bugs"
```

---

### `context(context_text: str)`

Add context (code, document, data).

```python
builder.context("def hello(): pass")
# → "Context:\n```\ndef hello(): pass\n```"
```

---

### `example(input_text: str, output_text: str)`

Add a few-shot example.

```python
builder.example("2+2", "4")
builder.example("3+3", "6")
```

---

### `examples(examples_list: List[Dict])`

Add multiple examples at once.

```python
builder.examples([
    {"input": "2+2", "output": "4"},
    {"input": "3+3", "output": "6"}
])
```

---

### `output_format(format_type: str, schema: Optional[Dict] = None)`

Specify output format.

```python
# Simple format
builder.output_format("markdown")

# JSON with schema
builder.output_format("json", schema={"name": "string", "age": "number"})
```

---

### `constraint(constraint: str)`

Add a constraint/guardrail. Can be called multiple times.

```python
builder.constraint("Maximum 100 words")
builder.constraint("Use bullet points")
```

---

### `system(system_prompt: str)`

Set a custom system prompt (overrides persona).

```python
builder.system("You are a helpful assistant specialized in Python.")
```

---

### `build() -> str`

Build the final prompt string.

```python
prompt = builder.build()
print(prompt)
```

---

### `estimate_tokens(model: str = "gpt-4") -> int`

Estimate token count.

```python
tokens = builder.estimate_tokens()
print(f"~{tokens} tokens")
```

!!! note
    Requires `tiktoken` for accurate counting. Falls back to rough estimate (chars/4).

---

## Fluent Interface

All methods return `self` for chaining:

```python
prompt = (PromptBuilder()
    .persona("Developer")
    .pattern("chain-of-thought")
    .task("Debug this")
    .context(code)
    .constraint("Be concise")
    .build())
```

---

## Class Attributes

### `PromptBuilder.PATTERNS`

Dict of all available patterns:

```python
print(PromptBuilder.PATTERNS.keys())
# dict_keys(['chain-of-thought', 'few-shot', ...])

print(PromptBuilder.PATTERNS["chain-of-thought"])
# "Think through this step-by-step..."
```
