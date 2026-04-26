# Defensive Prompts

Prompts for reducing hallucinations, enforcing safety, and improving accuracy.

## Browsing Prompts

```bash
promptkit search "defensive"
promptkit search "security"
```

## Available Prompts

| Prompt | Description |
|--------|-------------|
| contrarian | Challenge assumptions |
| accessibility-auditor | Accessibility review |
| resume-reviewer | Resume review |
| content-review-plan | Content review planning |
| secure-web-development | Secure development |
| hallucination-reducer | Reduce confident nonsense |
| journal-reviewer | Journal/paper review |
| plagiarism-checker | Plagiarism detection |
| pull-request-review-assistant | PR review |
| refactoring-expert | Code refactoring |
| tech-reviewer | Technical review |
| update-checker | Check for outdated info |
| website-security-vulnerability-checker | Web security audit |
| llm-security-specialist | LLM application security auditing |

## Built-in Pattern

The `hallucination-reducer` pattern is also available as a built-in pattern:

```python
from llm_promptkit import PromptBuilder

builder = PromptBuilder()
builder.pattern("hallucination-reducer")
builder.task("Answer this question based on the provided context")
builder.context(source_text)
prompt = builder.build()
```