# LLM Promptkit

A toolkit for building effective LLM prompts from proven patterns.

## Why Promptkit?

- **Proven patterns** — 18 battle-tested prompt techniques from research and practice
- **Composable** — Mix and match patterns with a fluent Python API
- **Copy-paste ready** — Each pattern documented with examples
- **Framework agnostic** — Works with any LLM (GPT, Claude, Llama, etc.)

## Quick Example

```python
from llm_promptkit import PromptBuilder

prompt = (PromptBuilder()
    .persona("Senior Developer")
    .pattern("chain-of-thought")
    .task("Review this code for security issues")
    .context(code_snippet)
    .build())
```

## Features

| Feature | Description |
|---------|-------------|
| **18 Patterns** | Chain-of-Thought, Self-Consistency, ReAct, and more |
| **Prompt Doctor** | Analyze prompts for common issues |
| **275+ Curated Prompts** | Model-optimized, role-based, and technique prompts |
| **Python API** | Fluent builder for composing prompts |
| **CLI Tool** | Quick prompt generation from terminal |
| **Token Estimation** | Know your token count before sending |

## Getting Started

<div class="grid cards" markdown>

- :material-download: **[Installation](getting-started/installation.md)**
  
    Install via pip or from source

- :material-rocket-launch: **[Quick Start](getting-started/quickstart.md)**
  
    Build your first prompt in 5 minutes

- :material-book-open-variant: **[Patterns](patterns/index.md)**
  
    Browse all available patterns

- :material-api: **[API Reference](api/builder.md)**
  
    Full API documentation

</div>

---

*Built by [Petsku](https://github.com/Petsku01) & Kuu*