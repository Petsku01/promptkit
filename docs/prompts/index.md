# Prompts Library

Ready-to-use prompts for common tasks. Copy-paste and customize for your needs.

## Categories

| Category | Count | Description |
|----------|-------|-------------|
| [Code](code.md) | 18 | Code review, development, debugging |
| [Reasoning](reasoning.md) | 15 | Logic, analysis, problem-solving |
| [Debug](debug.md) | 12 | Error analysis, troubleshooting |
| [Defensive](defensive.md) | 13 | Hallucination reduction, safety |
| [Education](education.md) | 11 | Teaching, explaining, tutoring |
| [Professional](professional.md) | 11 | Business, consulting, writing |
| [Creative](creative.md) | 10 | Writing, storytelling, ideation |
| [Output](output.md) | 9 | JSON, formatting, structure |
| [System](system.md) | 2 | Base system prompts |
| [Context](context.md) | 1 | Few-shot, RAG |
| [Model-Optimized](model-optimized.md) | 20+ | Provider-specific prompts |

## Quick vs Extended

Each prompt comes in two variants:

- **Quick** (~100 tokens): Single questions, fast iteration
- **Extended** (300-500 tokens): System prompts, agents, critical tasks

## Usage

### Direct Copy-Paste

Browse the categories and copy the prompts you need.

### With PromptBuilder API

```python
from llm_promptkit import PromptBuilder

# Combine prompts with patterns
prompt = (PromptBuilder()
    .system(open("prompts/code/senior-engineer.md").read())
    .pattern("chain-of-thought")
    .task("Review this PR")
    .build())
```

### With CLI

```bash
# Build with a base prompt file
promptkit build --task "Review this code" --pattern senior-reviewer
```
