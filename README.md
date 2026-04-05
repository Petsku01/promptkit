# LLM Promptkit

[![CI](https://github.com/Petsku01/promptkit/actions/workflows/ci.yml/badge.svg)](https://github.com/Petsku01/promptkit/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/llm-promptkit.svg)](https://badge.fury.io/py/llm-promptkit)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

A toolkit for building effective LLM prompts. Includes:
- **Prompt Doctor** - Analyze prompts for common issues
- **275+ model-specific prompts** - Curated by provider (OpenAI, Anthropic, Google, etc.)
- **9 reusable prompt patterns** - Documented templates for common techniques
- Python library for composing prompts
- CLI tool for quick prompt generation and prompt browsing

## What's Included

### Prompts Directory (`prompts/`)
**275+ curated prompts** organized by category:
- `code/` — Code generation, refactoring, review
- `debug/` — Debugging, error analysis
- `reasoning/` — Chain-of-thought, step-by-step
- `output/` — Structured outputs, JSON
- `defensive/` — Safety, hallucination reduction
- `system/` — System prompts, personas
- `professional/`, `education/`, `creative/` — Domain-specific

Each prompt has **Quick** (~100 tokens) and **Extended** (~300-500 tokens) versions.

### Patterns Directory (`patterns/`)
**9 documented prompt engineering patterns** (reusable templates):
- Reasoning: Chain-of-Thought, Self-Consistency
- Code: TDD Prompting, Stack Trace Decoder
- Output: JSON Enforcer
- Context: Few-Shot with Negatives
- Defensive: Hallucination Reducer
- Review: Senior Reviewer

Copy-paste ready with examples.

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
promptkit doctor --file my-prompt.md

# Browse included prompts
promptkit prompts                              # List all providers
promptkit prompts --model openai/gpt-4o        # List prompts for a model
promptkit prompts --show openai/gpt-4o/coding  # View prompt content

# Search prompts
promptkit search "code review"
```

## Prompt Doctor

Analyze prompts for common issues without API calls:

```bash
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

**Checks:**
- Vague/ambiguous instructions
- Missing role/persona
- Token inefficiency (verbose phrasing)
- Missing output format
- Lack of examples (few-shot)
- Negative constraints ("don't" → use positive)
- Structural formatting (long prompts need headers/lists)
- Code block handling (skips NLP checks inside code)

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

## Pattern Directory

| Category | Pattern | Use When You Need To... |
|----------|---------|-------------------------|
| **Reasoning** | [Chain-of-Thought](patterns/reasoning/chain-of-thought.md) | Get step-by-step logical reasoning |
| **Reasoning** | [Self-Consistency](patterns/reasoning/self-consistency.md) | Verify answers through multiple paths |
| **Output** | [JSON Enforcer](patterns/output/json-enforcer.md) | Get clean, valid JSON output |
| **Code** | [TDD Prompting](patterns/code/tdd-prompting.md) | Generate tests first, then implementation |
| **Code** | [Stack Trace Decoder](patterns/code/stack-trace-decoder.md) | Debug errors from stack traces |
| **Review** | [Senior Reviewer](patterns/review/senior-reviewer.md) | Get strict code review feedback |
| **Context** | [Few-Shot with Negatives](patterns/context/few-shot-negatives.md) | Teach by example (including what NOT to do) |
| **Defensive** | [Hallucination Reducer](patterns/defensive/hallucination-reducer.md) | Reduce confident nonsense |

## Available Patterns (Builder API)

```python
from llm_promptkit import PromptBuilder

# Chain of Thought - step-by-step reasoning
builder.pattern("chain-of-thought")

# Few-Shot - learning from examples
builder.pattern("few-shot")
builder.example("input", "expected output")

# JSON Output - structured responses
builder.pattern("json-output")
builder.output_format("json", schema={"key": "type"})

# Senior Reviewer - critical code review
builder.pattern("senior-reviewer")

# Self-Consistency - verify through multiple paths
builder.pattern("self-consistency")
```

## CLI Reference

Full command reference for the `promptkit` CLI:

```bash
$ promptkit --help

Usage: promptkit [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  build       Build a prompt from pattern
  doctor      Analyze a prompt for issues
  list        List available patterns
  prompts     Browse included prompts
  search      Search prompts by keyword
```

### promptkit build

```bash
$ promptkit build --help

Usage: promptkit build [OPTIONS]

  Build a prompt from pattern

Options:
  --persona TEXT       Set AI persona/role
  --pattern TEXT       Select prompt pattern (chain-of-thought, json-output, etc.)
  --task TEXT          Main task description
  --context TEXT       Context text (code, document, data)
  --output TEXT        Output format (json, markdown, list)
  --interactive        Interactive mode (prompts for values)
  --tokens             Show estimated token count
  --help               Show this message and exit.
```

### promptkit doctor

```bash
$ promptkit doctor --help

Usage: promptkit doctor [OPTIONS] [TEXT]

  Analyze a prompt for common issues

Options:
  --file PATH  Analyze prompt from file
  --help       Show this message and exit.
```

### promptkit prompts

```bash
$ promptkit prompts                              # List all providers
$ promptkit prompts --model openai/gpt-4o        # List prompts for a model
$ promptkit prompts --show openai/gpt-4o/coding  # View prompt content
```

### promptkit search

```bash
$ promptkit search "code review"                 # Search prompts by keyword
```

## Builder API Reference

```python
builder = PromptBuilder()

# Set persona/role
builder.persona("Senior Developer")

# Add patterns
builder.pattern("chain-of-thought")

# Set task
builder.task("Analyze this code")

# Add context
builder.context("def hello(): ...")

# Add examples (for few-shot)
builder.example("input", "output")
builder.examples([{"input": "x", "output": "y"}])

# Set output format
builder.output_format("json", schema={"key": "type"})

# Add constraints
builder.constraint("Max 100 words")

# Build the prompt
prompt = builder.build()

# Estimate tokens (requires tiktoken)
tokens = builder.estimate_tokens()
```

## Anatomy of a Pattern

Each documented pattern follows this format:

```markdown
# Pattern Name

## When to Use
The specific scenario where this pattern excels.

## How It Works
The underlying mechanics of WHY the LLM responds well to this.

## The Prompt
[The actual prompt template]

## Example
**Input:** [What you provide]
**Output:** [What you get back]

## Tested On
- GPT-4: Yes
- Claude: Yes
- Llama 3: Partial
```

## Categories

- **reasoning/** - Logic, step-by-step, self-correction
- **output/** - JSON, structured lists, schema extraction
- **code/** - Generation, refactoring, debugging
- **review/** - Code review, security, performance
- **context/** - RAG, few-shot, long-context management
- **defensive/** - Hallucination reduction, constraint enforcement

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT

---

*Built by [Petsku](https://github.com/Petsku01) & Kuu*
