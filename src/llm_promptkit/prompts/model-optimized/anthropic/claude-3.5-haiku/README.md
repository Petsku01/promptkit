# Claude 3.5 Haiku Prompting Guide

## Model Characteristics
- **Type:** Fast, cost-efficient Claude model
- **Context:** 200K tokens
- **Strengths:** Speed, low cost, good for simple tasks, follows instructions well
- **Best for:** Classification, extraction, simple Q&A, formatting, bulk processing
- **Not ideal for:** Complex reasoning, long analysis, nuanced creative writing

---

## Prompt Files

| Theme | File | Description |
|-------|------|-------------|
| Simple Tasks | [simple-tasks.md](simple-tasks.md) | Classification, extraction, formatting, quick answers |
| Coding | [coding.md](coding.md) | Quick code gen, simple debugging, boilerplate |

## Prompting Tips

- Haiku is about 10× cheaper and faster than Sonnet — use it for volume
- Keep prompts short and focused — one task per prompt
- Don't ask for long, detailed outputs — it shines on quick, precise work
- For anything requiring real reasoning, use Sonnet or Opus instead
- XML tags help structure input: `<task>`, `<data>`, `<format>`
- Perfect for processing many items cheaply (batch classification, extraction, etc.)