# LLM Promptkit

A lean toolkit for building effective LLM prompts from proven patterns.

## Why Promptkit?

- **Proven patterns** -- battle-tested prompt techniques from research and practice
- **Composable** -- mix and match patterns with a fluent Python API
- **Prompt doctor** -- catch anti-patterns before you ship
- **Framework agnostic** -- works with any LLM (GPT, Claude, Llama, etc.)
- **Minimal** -- 7 source files, 1 dependency (`rich`)

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
| **48 Patterns** | Chain-of-Thought, Self-Consistency, Few-Shot, and more |
| **29 Curated Prompts** | Best prompts for code, debug, reasoning, review |
| **Python API** | Fluent builder for composing prompts |
| **Prompt Doctor** | Rule-based linter for prompt quality |
| **CLI Tool** | 3 commands: `list`, `build`, `doctor` |
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
