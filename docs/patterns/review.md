# Review Patterns

Patterns for critical analysis and review tasks.

## Senior Reviewer

The core review persona.

```python
from llm_promptkit import PromptBuilder

prompt = (PromptBuilder()
    .pattern("senior-reviewer")
    .task("Review this architecture proposal")
    .context(proposal)
    .build())
```

---

## Multi-Pass Review

Combine patterns for thorough analysis:

```python
prompt = (PromptBuilder()
    .pattern("senior-reviewer")
    .pattern("decomposition")      # Break into aspects
    .pattern("reflection")         # Self-check findings
    .task("Review this system design")
    .context(design_doc)
    .build())
```

---

## Security Review

```python
prompt = (PromptBuilder()
    .pattern("senior-reviewer")
    .pattern("chain-of-thought")
    .task("Security audit this code")
    .context(code)
    .constraint("Check for: injection, auth bypass, data exposure, SSRF")
    .constraint("Rate each finding: Critical/High/Medium/Low")
    .output_format("json", schema={
        "findings": [{
            "severity": "string",
            "location": "string", 
            "description": "string",
            "recommendation": "string"
        }]
    })
    .build())
```

---

## Document Review

```python
prompt = (PromptBuilder()
    .pattern("reflection")
    .task("Review this documentation for accuracy and clarity")
    .context(doc)
    .constraint("Check technical accuracy")
    .constraint("Identify unclear sections")
    .constraint("Suggest improvements")
    .build())
```
