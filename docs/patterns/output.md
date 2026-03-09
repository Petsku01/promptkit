# Output Control Patterns

Patterns that control response format.

## JSON Output

Forces valid JSON output.

```python
from llm_promptkit import PromptBuilder

prompt = (PromptBuilder()
    .pattern("json-output")
    .output_format("json", schema={
        "sentiment": "positive|negative|neutral",
        "confidence": "0.0-1.0",
        "keywords": ["string"]
    })
    .task("Analyze this review")
    .context("Amazing product, exceeded expectations!")
    .build())
```

**Output:**
```json
{
  "sentiment": "positive",
  "confidence": 0.95,
  "keywords": ["amazing", "exceeded", "expectations"]
}
```

---

## Output Format (General)

Specify any format without a pattern:

```python
# Markdown
prompt = (PromptBuilder()
    .output_format("markdown")
    .task("Document this function")
    .build())

# Bullet list
prompt = (PromptBuilder()
    .output_format("bullet list")
    .task("List the pros and cons")
    .build())

# Table
prompt = (PromptBuilder()
    .output_format("markdown table with columns: Feature, Description, Status")
    .task("Summarize the project status")
    .build())
```

---

## Constraints

Add specific requirements:

```python
prompt = (PromptBuilder()
    .task("Write a summary")
    .constraint("Maximum 100 words")
    .constraint("Use simple language")
    .constraint("Include exactly 3 bullet points")
    .build())
```

**Output:**
```
Constraints:
- Maximum 100 words
- Use simple language
- Include exactly 3 bullet points

Task: Write a summary
```

---

## Combining with Reasoning

```python
prompt = (PromptBuilder()
    .pattern("chain-of-thought")
    .pattern("json-output")
    .output_format("json", schema={"steps": ["string"], "answer": "string"})
    .task("Solve 15% of 80")
    .build())
```

!!! tip "Order matters"
    Put reasoning patterns first, output patterns last.
