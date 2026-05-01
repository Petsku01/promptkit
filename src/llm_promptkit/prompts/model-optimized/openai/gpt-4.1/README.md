# GPT-4.1

## Features
- **Context:** 1M tokens
- **Strengths:** Coding, instruction following, agentic workflows
- **Best for:** Software development, complex multi-step tasks, structured output

## Prompts by theme

| Theme | File | Description |
|-------|------|-------------|
| Coding | [coding.md](coding.md) | Implementation, review, debug |
| Analysis | [analysis.md](analysis.md) | Problem solving, reasoning |
| Writing | [writing.md](writing.md) | Documentation, content |
| JSON | [json-output.md](json-output.md) | Structured data extraction |
| Instruction | [instruction-following.md](instruction-following.md) | Complex multi-step tasks |

## Important to remember

- GPT-4.1 follows instructions more precisely than GPT-4o — be explicit about what you want
- Use `developer` role for system-level instructions (preferred over `system`)
- Specify output format upfront for best results
- Handles long, detailed prompts without degrading quality