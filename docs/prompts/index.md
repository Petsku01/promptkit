# Prompts Library

Ready-to-use prompts organized by category. Over 200 prompts across 9 categories.

## Categories

| Category | Description | Count |
|----------|-------------|-------|
| [Code](code.md) | Software development prompts | 18 |
| [Context](context.md) | Context and example management | 1 |
| [Creative](creative.md) | Writing and storytelling | 10 |
| [Debug](debug.md) | Error analysis and troubleshooting | 12 |
| [Defensive](defensive.md) | Safety, accuracy, hallucination reduction | 13 |
| [Education](education.md) | Teaching and tutoring | 10 |
| [Output](output.md) | Format control and presentation | 11 |
| [Professional](professional.md) | Business and consulting | 10 |
| [Reasoning](reasoning.md) | Analysis and problem-solving | 10 |
| [System](system.md) | Core system prompts | 2 |
| [Model-Optimized](model-optimized.md) | Provider-specific tuning | 8 providers |

## Quick vs Extended

Most categories include both quick prompts (200-500 tokens) and extended prompts (1000+ tokens). Quick prompts for simple tasks, extended for complex reasoning.

## Usage

### Direct Copy-Paste

```bash
# Browse all prompts interactively
promptkit prompts

# Search by keyword
promptkit search "code review"
```

### With PromptBuilder API

```python
from llm_promptkit import PromptBuilder

# Combine prompts with patterns
builder = PromptBuilder()
builder.pattern("chain-of-thought")
builder.persona("Senior developer")
builder.task("Review this code")
prompt = builder.build()
```

### With CLI

```bash
# Build with a base prompt file
promptkit build --pattern chain-of-thought --persona "Expert analyst"
```