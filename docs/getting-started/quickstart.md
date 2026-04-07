# Quick Start

Build effective prompts in 5 minutes.

## Basic Usage

```python
from llm_promptkit import PromptBuilder

# Simple prompt
prompt = PromptBuilder().task("Explain quantum computing").build()
print(prompt)
# Output: "Task: Explain quantum computing"
```

## Adding a Persona

```python
prompt = (PromptBuilder()
    .persona("Physics professor")
    .task("Explain quantum computing to a 10-year-old")
    .build())
```

Output:
```
You are a Physics professor.

Task: Explain quantum computing to a 10-year-old
```

## Using Patterns

Patterns are proven prompt techniques that improve LLM responses:

```python
prompt = (PromptBuilder()
    .persona("Senior Developer")
    .pattern("chain-of-thought")  # Step-by-step reasoning
    .task("Find the bug in this code")
    .context(buggy_code)
    .build())
```

## Combining Multiple Patterns

```python
prompt = (PromptBuilder()
    .pattern("chain-of-thought")
    .pattern("reflection")  # Review and improve answer
    .task("Solve this math problem")
    .build())
```

## Adding Constraints

```python
prompt = (PromptBuilder()
    .task("Write a poem about AI")
    .constraint("Maximum 4 lines")
    .constraint("Must rhyme")
    .build())
```

## Structured Output

Force JSON output:

```python
prompt = (PromptBuilder()
    .pattern("json-output")
    .output_format("json", schema={"sentiment": "string", "confidence": "number"})
    .task("Analyze the sentiment of this text")
    .context("I love this product!")
    .build())
```

## Prompt Doctor

Check your prompts for common issues:

```python
from llm_promptkit import analyze_prompt

issues = analyze_prompt("Make it good please")
for issue in issues:
    print(f"[{issue.severity.value}] {issue.issue}")
```

Or from the CLI:

```bash
promptkit doctor "Make it good please"
```

## CLI Usage

```bash
# List patterns
promptkit list

# Build a prompt
promptkit build \
    -p "Data Scientist" \
    -P chain-of-thought \
    -t "Analyze this dataset" \
    --tokens

# Analyze a prompt
promptkit doctor "Write something good"
promptkit doctor --file my-prompt.md
```

## Next Steps

- Browse all [available patterns](../patterns/index.md)
- See the full [API reference](../api/builder.md)
- Check out [code patterns](../patterns/code.md) for development tasks
