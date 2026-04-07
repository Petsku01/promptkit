# Prompts Library

29 curated, ready-to-use prompts for common tasks. Copy-paste and customize.

## Categories

| Category | Count | Description |
|----------|-------|-------------|
| [Code](code.md) | 7 | Code review, development, TDD |
| [Debug](debug.md) | 4 | Error analysis, troubleshooting |
| [Reasoning](reasoning.md) | 5 | Logic, analysis, problem-solving |
| [Defensive](defensive.md) | 4 | Hallucination reduction, review |
| [Output](output.md) | 3 | JSON, formatting, diagrams |
| [System](system.md) | 2 | Base system prompts |
| [Professional](professional.md) | 2 | Product/project management |
| [Education](education.md) | 1 | Socratic teaching |
| [Creative](creative.md) | 2 | Tech writing, essays |

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
promptkit build --task "Review this code" --pattern senior-reviewer
```
