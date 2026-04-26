# Debug Prompts

Prompts for error analysis, troubleshooting, and security.

## Browsing Prompts

```bash
promptkit search "debug"
promptkit search "security"
```

## Available Prompts

| Prompt | Description |
|--------|-------------|
| rubber-duck | Rubber duck debugging |
| debugger-extended | Comprehensive debugging |
| bug-risk-analysis | Bug risk assessment |
| security-fixes-cves | Security vulnerability fixes |
| comprehensive-repository-analysis | Full repo bug analysis |
| security-fixes | General security fixes |
| sentry-bug-fixer | Sentry error resolution |
| stack-trace-analyzer | Stack trace analysis |
| stackoverflow-post | Stack Overflow question formatting |
| tech-troubleshooter | General troubleshooting |
| test-first-bug-fixing-approach | Test-driven bug fixing |
| want-to-analyze-security-issues | Security analysis |

## Example Usage

```python
from llm_promptkit import PromptBuilder

builder = PromptBuilder()
builder.pattern("stack-trace-decoder")
builder.task("Debug this error")
builder.context(traceback_text)
prompt = builder.build()
```