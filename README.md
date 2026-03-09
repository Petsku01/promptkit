# LLM Promptkit

[![CI](https://github.com/Petsku01/promptkit/actions/workflows/ci.yml/badge.svg)](https://github.com/Petsku01/promptkit/actions/workflows/ci.yml)
[![PyPI version](https://badge.fury.io/py/llm-promptkit.svg)](https://badge.fury.io/py/llm-promptkit)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

A toolkit for building effective LLM prompts. Includes:
- Documented prompt patterns (copy-paste ready)
- Python library for composing prompts
- CLI tool for quick prompt generation

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
from promptkit import PromptBuilder

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
