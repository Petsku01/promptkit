# Prompt Doctor

Rule-based prompt analysis -- catches common anti-patterns without API calls.

## Python API

```python
from llm_promptkit import analyze_prompt

issues = analyze_prompt("Make it good please")
for issue in issues:
    print(f"[{issue.severity.value}] {issue.issue} -- {issue.suggestion}")
```

## Issue Model

```python
from llm_promptkit.doctor import Issue, Severity

# Severity levels
Severity.CRITICAL    # Prompt is broken (e.g., empty)
Severity.WARNING     # Likely problem (vague language, missing format)
Severity.SUGGESTION  # Could be improved (missing role, structure)
Severity.INFO        # Optimization opportunity (verbose phrasing)
```

## What It Checks

| Check | Severity | Example Trigger |
|-------|----------|-----------------|
| Empty prompt | Critical | `""` |
| Very short prompt | Warning | `"do it"` |
| Vague instructions | Warning | `"make it good"`, `"stuff"`, `"asap"` |
| Missing role/persona | Suggestion | No `"You are a..."` or `"role:"` |
| Token inefficiency | Info | `"please"`, `"thank you"`, `"kindly"` |
| Missing output format | Warning | No `"json"`, `"markdown"`, `"format"` |
| Missing examples | Info | No `"example:"`, `"e.g."`, `"for instance"` |
| Negative constraints | Warning | `"don't"`, `"never"`, `"avoid"` |
| Lacks structure | Suggestion | Long prompt without headers/lists/XML |
| Code-only prompt | Info | Only code blocks, no instructions |

## CLI Usage

```bash
# Analyze inline
promptkit doctor "Write something good"

# Analyze from file
promptkit doctor --file my-prompt.md
```
