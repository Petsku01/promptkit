# LLM Promptkit

[![CI](https://github.com/Petsku01/promptkit/actions/workflows/ci.yml/badge.svg)](https://github.com/Petsku01/promptkit/actions/workflows/ci.yml)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

A lean toolkit for building effective LLM prompts from proven patterns.

- **PromptBuilder** — fluent Python API for composing prompts
- **Prompt Doctor** — rule-based prompt linter (no API calls, no dependencies)
- **48 prompt patterns** — documented, tested templates (chain-of-thought, few-shot, etc.)
- **29 curated prompts** — the best prompts for code, debug, reasoning, and more
- **Simple CLI** — 3 commands: `list`, `build`, `doctor`

## Installation

```bash
pip install llm-promptkit

# With token counting support
pip install llm-promptkit[tokens]
```

## Quick Start

### Python API

```python
from llm_promptkit import PromptBuilder

prompt = (PromptBuilder()
    .persona("Senior Developer")
    .pattern("chain-of-thought")
    .task("Review this code for security issues")
    .context(code_snippet)
    .output_format("json", schema={"issues": [], "severity": "string"})
    .build())
```

### Prompt Doctor

Analyze prompts for common issues — no API calls needed:

```python
from llm_promptkit import analyze_prompt

issues = analyze_prompt("Make it good please")
for issue in issues:
    print(f"[{issue.severity.value}] {issue.issue} — {issue.suggestion}")
```

### CLI

```bash
# List available patterns
promptkit list

# Build a prompt
promptkit build \
    --persona "Senior Developer" \
    --pattern chain-of-thought \
    --task "Review this code" \
    --tokens

# Analyze a prompt
promptkit doctor "Write something good"
promptkit doctor --file my-prompt.md
```

## Prompt Doctor

Catches common prompt anti-patterns:

```
$ promptkit doctor "Make it good please"

┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Severity ┃ Issue                      ┃ Suggestion                   ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Warning  │ Vague or ambiguous         │ Found 'make it good'. Be     │
│          │ instructions.              │ more specific.               │
│ Info     │ Token inefficiency.        │ Found 'please'. Use direct   │
│          │                            │ commands.                    │
│ Sugges.  │ Missing context or role.   │ Add a persona.               │
│ Warning  │ Missing output format.     │ Specify format (JSON, etc).  │
└──────────┴────────────────────────────┴──────────────────────────────┘
```

**What it checks:**
- Vague/ambiguous instructions
- Missing role/persona
- Token inefficiency (verbose phrasing)
- Missing output format
- Lack of examples
- Negative constraints ("don't" -> use positive)
- Structural formatting for long prompts
- Code block awareness (skips NLP checks inside code)

## Patterns

48 documented prompt engineering patterns in `patterns/`:

| Category | Patterns |
|----------|----------|
| **reasoning/** | chain-of-thought, self-consistency, step-by-step-analysis, react |
| **code/** | tdd-prompting, stack-trace-decoder, comprehensive-code-review, test-generation, api-design, ... |
| **output/** | json-enforcer, structured-output-enforcement, markdown-table-format, bullet-list |
| **context/** | few-shot-negatives, rag-retrieval, template-based, zero-shot |
| **defensive/** | hallucination-reducer, chain-of-verification, fact-check, negative-constraints |
| **planning/** | task-decomposition, system-design-document, architecture-decision-record, ... |
| **review/** | senior-reviewer, code-review-checklist |
| **system/** | agent-role-definition, error-recovery, circuit-breaker, tool-use, ... |

Each pattern includes: when to use, how it works, the template, examples, and model compatibility.

## Curated Prompts

29 best prompts in `prompts/`, organized by domain:

| Category | Prompts |
|----------|---------|
| **code/** | senior-engineer, brutal-reviewer, tdd-generator, code-reviewer, fullstack-developer, ... |
| **debug/** | rubber-duck, stack-trace-analyzer, bug-risk-analysis, root-cause-analyst |
| **reasoning/** | chain-of-thought, tree-of-thoughts, decomposition, self-consistency, expert-persona |
| **output/** | structured-json-enforcer, json-enforcer, diagram-generator |
| **defensive/** | pull-request-review-assistant, hallucination-reducer, refactoring-expert, contrarian |
| **system/** | coding-assistant, error-recovery |
| **professional/** | product-manager, project-manager |
| **education/** | socratic-teacher |
| **creative/** | tech-writer, essay-writer |

## Builder API Reference

```python
builder = PromptBuilder()

builder.persona("Senior Developer")       # Set persona/role
builder.pattern("chain-of-thought")       # Add a pattern
builder.task("Analyze this code")         # Set the task
builder.context("def hello(): ...")       # Add context
builder.example("input", "output")       # Add few-shot example
builder.output_format("json", schema={}) # Set output format
builder.constraint("Max 100 words")      # Add constraint

prompt = builder.build()                  # Build the prompt string
tokens = builder.estimate_tokens()        # Estimate token count
```

All methods return `self` for chaining.

## Project Structure

```
src/llm_promptkit/
    __init__.py          # Exports: PromptBuilder, analyze_prompt
    builder.py           # Fluent prompt builder API
    doctor.py            # Rule-based prompt analysis
    cli.py               # CLI: list, build, doctor
    pattern_loader.py    # Load patterns from markdown files
    console.py           # Rich console instance
    utils.py             # Clipboard helper
patterns/                # 48 documented prompt engineering patterns
prompts/                 # 29 curated best prompts
```

## License

MIT

---

*Built by [Petsku](https://github.com/Petsku01) & Kuu*
