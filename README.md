# LLM Promptkit

[![CI](https://github.com/Petsku01/promptkit/actions/workflows/ci.yml/badge.svg)](https://github.com/Petsku01/promptkit/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/llm-promptkit.svg)](https://badge.fury.io/py/llm-promptkit)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

A toolkit for building effective LLM prompts. Includes:
- **Prompt Doctor** — Analyze prompts for common issues
- **18 prompt patterns** across 7 categories (reasoning, agentic, context, output, code, review, defensive)
- **257+ curated prompts** — Model-optimized, role-based, and technique prompts
- **Python API** — Fluent builder for composing prompts
- **CLI** — Quick prompt generation and browsing from the terminal

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

print(prompt)
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

# Interactive mode
promptkit build --interactive

# Analyze a prompt for issues
promptkit doctor "Write something good"

# Analyze from file
promptkit doctor my-prompt.md
promptkit doctor --file my-prompt.md

# Browse included prompts
promptkit prompts                              # List all providers
promptkit prompts --model openai/gpt-4o        # List prompts for a model
promptkit prompts --show openai/gpt-4o/coding  # View prompt content

# Search prompts
promptkit search "code review"
promptkit search "json" --category output
```

## Prompt Doctor

Analyze prompts for common issues without API calls:

```bash
$ promptkit doctor "Make it good please"

┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Severity ┃ Issue                      ┃ Suggestion                   ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ Warning  │ Vague or ambiguous         │ Found 'make it good'. Be    │
│          │ instructions.              │ more specific.              │
│ Info     │ Token inefficiency.        │ Found 'please'. Use direct  │
│          │                            │ commands.                   │
│ Sugges.  │ Missing context or role.   │ Add a persona.              │
│ Warning  │ Missing output format.     │ Specify format (JSON, etc). │
└──────────┴────────────────────────────┴──────────────────────────────┘
```

**Checks:**
- Vague/ambiguous instructions
- Missing role/persona
- Token inefficiency (verbose phrasing)
- Missing output format
- Lack of examples (few-shot)
- Negative constraints ("don't" → use positive)
- Structural formatting (long prompts need headers/lists)
- Code block handling (skips NLP checks inside code)

## Prompt Patterns

| Category | Pattern | Use When You Need To... |
|----------|---------|-------------------------|
| **Reasoning** | `chain-of-thought` | Get step-by-step logical reasoning |
| **Reasoning** | `self-consistency` | Verify answers through multiple paths |
| **Reasoning** | `tree-of-thought` | Explore multiple expert perspectives |
| **Reasoning** | `step-back` | Identify core principles first |
| **Reasoning** | `decomposition` | Break complex problems into sub-problems |
| **Reasoning** | `reflection` | Self-critique and improve initial response |
| **Agentic** | `react` | Interleave thought, action, observation |
| **Agentic** | `prompt-chaining` | Multi-stage task decomposition |
| **Agentic** | `meta-prompting` | Let model choose optimal approach |
| **Context** | `few-shot` | Learn from examples |
| **Context** | `few-shot-negatives` | Learn from both positive and negative examples |
| **Context** | `role-play` | Adopt a specific persona |
| **Output** | `json-output` | Get structured JSON responses |
| **Output** | `json-enforcer` | Strictly enforce valid JSON |
| **Code** | `tdd-prompting` | Generate tests first, then implementation |
| **Code** | `stack-trace-decoder` | Debug errors from stack traces |
| **Review** | `senior-reviewer` | Get strict code review feedback |
| **Defensive** | `hallucination-reducer` | Reduce confident nonsense |

## Builder API Reference

```python
from llm_promptkit import PromptBuilder

builder = PromptBuilder()

# Set persona/role
builder.persona("Senior Developer")

# Add patterns (by slug name)
builder.pattern("chain-of-thought")

# Set task
builder.task("Analyze this code")

# Add context
builder.context("def hello(): pass")

# Add examples (for few-shot)
builder.example("input", "output")
builder.examples([{"input": "x", "output": "y"}])

# Set output format
builder.output_format("json", schema={"key": "type"})

# Add constraints
builder.constraint("Max 100 words")

# Override system prompt (overrides persona)
builder.system("You are a helpful assistant specialized in Python.")

# Build the prompt
prompt = builder.build()

# Estimate tokens (requires tiktoken, falls back to chars/4)
tokens = builder.estimate_tokens()

# List available patterns
patterns = builder.get_available_patterns()
```

## Available Patterns

```python
from llm_promptkit.patterns import list_pattern_names

names = list_pattern_names()
# ('meta-prompting', 'prompt-chaining', 'react', 'stack-trace-decoder',
#  'tdd-prompting', 'few-shot-negatives', 'few-shot', 'role-play',
#  'hallucination-reducer', 'json-enforcer', 'json-output',
#  'chain-of-thought', 'decomposition', 'reflection', 'self-consistency',
#  'step-back', 'tree-of-thought', 'senior-reviewer')
```

## Quick vs Extended Prompts

Prompts come in two types:

| Type | Size | Use Case | Example |
|------|------|----------|---------|
| **Quick** | ~100 tokens | Single questions, fast iteration | `code-reviewer.md` |
| **Extended** | 300-500 tokens | System prompts, agents, critical tasks | `code-reviewer-extended.md` |

Extended prompts include:
- Structured multi-pass processes
- Specific output formats
- Explicit rules and constraints
- Failure modes to avoid

**Rule of thumb:** Use extended for anything a sub-agent will run autonomously.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT

---

*Built by [Petsku](https://github.com/Petsku01) & Kuu*