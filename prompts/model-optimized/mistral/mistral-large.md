# Mistral Large Prompting Guide

## Model Characteristics
- **Context:** 128K tokens
- **Strengths:** Multilingual, reasoning, code, function calling
- **Best for:** Complex tasks, enterprise, European languages

---

## Prompt 1: Structured Analysis

```markdown
## Task
Analyze the following problem thoroughly.

## Process

### 1. Understanding
What is being asked?

### 2. Key Information
What facts are relevant?

### 3. Analysis
Work through the problem step by step.

### 4. Conclusion
State your answer clearly.

## Problem
[Insert problem here]
```

---

## Prompt 2: Multilingual Translation

```markdown
## Task
Translate and localize this content.

## Source
- Language: [source language]
- Text: [paste text]

## Target
- Language: [target language]
- Tone: [formal/informal]
- Context: [business/casual/technical]

## Requirements
- Preserve meaning and intent
- Adapt idioms appropriately
- Maintain formatting
- Flag any culturally sensitive content

## Output
Translation:
Notes on localization choices:
```

---

## Prompt 3: Code Generation with Tests

```markdown
## Task
Write a function that [description].

## Requirements
- Language: Python 3.10+
- Include type hints
- Add docstring with examples
- Handle edge cases

## Output Format

### Code
```python
[function code]
```

### Unit Tests
```python
[pytest tests]
```

### Edge Cases Handled
- [List of edge cases]
```

---

## Prompt 4: Document Summarization

```markdown
## Task
Summarize this document.

## Parameters
- Length: [X sentences/bullet points]
- Focus: [key themes to emphasize]
- Audience: [who will read this]

## Document
[paste document]

## Output

### Executive Summary
[2-3 sentences]

### Key Points
- Point 1
- Point 2
- Point 3

### Action Items
- [Any tasks mentioned]
```

---

## Prompt 5: Data Extraction to JSON

```markdown
## Task
Extract structured data from this text.

## Schema
```json
{
  "entities": [{"name": "string", "type": "string"}],
  "dates": ["YYYY-MM-DD"],
  "amounts": [{"value": "number", "currency": "string"}],
  "locations": ["string"]
}
```

## Rules
- Return valid JSON only
- No markdown formatting
- Use null for missing values

## Text
[input text]
```

---

## Prompt 6: Comparative Analysis

```markdown
## Task
Compare these options objectively.

## Options
1. [Option A]
2. [Option B]

## Criteria to Evaluate
- Cost
- Performance
- Ease of use
- Scalability
- Risk factors

## Output Format

| Criterion | Option A | Option B |
|-----------|----------|----------|
| ... | ... | ... |

### Summary
[Overall comparison]

### Recommendation
[Which to choose and why]
```

---

## Prompt 7: Technical Documentation

```markdown
## Task
Generate technical documentation for this code.

## Code
[paste code]

## Documentation Required

### Overview
What does this code do?

### Installation
How to set up?

### Usage
How to use with examples.

### API Reference
Document each function/method.

### Error Handling
What errors can occur?
```

---

## Prompt 8: Function Calling Setup

```json
{
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "search_database",
        "description": "Search the product database",
        "parameters": {
          "type": "object",
          "properties": {
            "query": {"type": "string", "description": "Search query"},
            "limit": {"type": "integer", "description": "Max results"}
          },
          "required": ["query"]
        }
      }
    }
  ]
}
```

When to call functions:
```
You have access to a database search function.
Use it when the user asks about products.
For general questions, answer directly.
```

---

## Key Tips

- Use markdown headers for clear structure
- Excellent for European languages
- Strong function/tool calling support
- Worded scales work better than numbers ("excellent" > "5")
- Few-shot examples improve consistency
- Good at following complex multi-section prompts
