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

Add a prompt pattern by slug name. Can be called multiple times.
Raises `PatternNotFoundError` if the pattern does not exist.

```python
builder.pattern("chain-of-thought")
builder.pattern("reflection")
```

**Available patterns (18):**

| Category | Pattern | Description |
|----------|---------|-------------|
| Reasoning | `chain-of-thought` | Step-by-step reasoning |
| Reasoning | `self-consistency` | Multiple solution paths |
| Reasoning | `tree-of-thought` | Multi-expert deliberation |
| Reasoning | `step-back` | Find underlying principles |
| Reasoning | `decomposition` | Break into sub-problems |
| Reasoning | `reflection` | Self-review and improve |
| Agentic | `react` | Interleave thought, action, observation |
| Agentic | `prompt-chaining` | Multi-stage task decomposition |
| Agentic | `meta-prompting` | Let model choose approach |
| Context | `few-shot` | Learn from examples |
| Context | `few-shot-negatives` | Learn from positive and negative examples |
| Context | `role-play` | Adopt a specific persona |
| Output | `json-output` | Structured JSON output |
| Output | `json-enforcer` | Strictly enforce valid JSON |
| Code | `tdd-prompting` | Tests first, then implementation |
| Code | `stack-trace-decoder` | Debug stack traces |
| Review | `senior-reviewer` | Critical code review |
| Defensive | `hallucination-reducer` | Reduce confident nonsense |

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

Add multiple examples at once. Each dict must have `"input"` and `"output"` keys.

```python
builder.examples([
    {"input": "2+2", "output": "4"},
    {"input": "3+3", "output": "6"}
])
```

Raises `ValueError` if any example is missing `input` or `output` keys.

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

Raises `PatternLoadError` if a pattern file cannot be read.

---

### `estimate_tokens(model: str = "gpt-4") -> int`

Estimate token count.

```python
tokens = builder.estimate_tokens()
print(f"~{tokens} tokens")
```

Requires `tiktoken` for accurate counting. Falls back to rough estimate (chars/4).

---

### `get_available_patterns() -> tuple`

List all available pattern names.

```python
patterns = PromptBuilder().get_available_patterns()
print(patterns)
# ('chain-of-thought', 'self-consistency', 'few-shot', ...)
```

---

## Exceptions

| Exception | Parent | When |
|-----------|--------|------|
| `PromptKitError` | `Exception` | Base exception for all promptkit errors |
| `PatternNotFoundError` | `PromptKitError`, `LookupError` | Pattern name not found |
| `PatternLoadError` | `PromptKitError`, `OSError` | Pattern file cannot be read |

---

## Fluent Interface

All builder methods return `self` for chaining:

```python
prompt = (PromptBuilder()
    .persona("Developer")
    .pattern("chain-of-thought")
    .task("Debug this")
    .context(code)
    .constraint("Be concise")
    .build())
```