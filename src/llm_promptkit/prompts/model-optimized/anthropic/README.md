# Anthropic (Claude) Models

## Models

| Model | Best For | Prompts |
|-------|----------|---------|
| [Claude 3 Opus](claude-3-opus/) | Highest capability, research | 5 |
| [Claude 3 Sonnet](claude-3-sonnet/) | Balanced, production, code | 8 |
| [Claude 3 Haiku](claude-3-haiku/) | Speed, simple tasks, volume | 10 |
| [Claude 3.5 Haiku](claude-3.5-haiku/) | Fast, cheap, simple tasks | 2 |
| [Claude 3.7 Sonnet](claude-3.7-sonnet/) | Advanced coding, reasoning | 2 |
| [Claude Opus 4](claude-opus-4/) | High capability, analysis | 1 |
| [Claude Opus 4.5](claude-opus-4.5/) | Top capability, agentic | 2 |
| [Claude Sonnet 4](claude-sonnet-4/) | Best price/performance | 2 |
| [Claude Opus 4.7](claude-opus-4.7/) | Autonomous coding, high-res vision | 4 |

## Key Differences

- **Opus 4.7**: Best for autonomous coding, literal instruction following, 3.75MP vision
- **Opus 4.5**: Top capability, extended thinking
- **Sonnet 4**: Best price/performance, great for production
- **3.7 Sonnet**: Strong coding and reasoning
- **3.5 Haiku**: Fast, cheap, simple tasks
- **Haiku (v3)**: Fastest, cheapest, volume tasks

## General Tips

- XML tags work well: `<task>`, `<thinking>`, `<answer>`
- 200K context — long documents OK
- Extended thinking for complex problems
- Very precise at following formatting instructions
- Opus 4.7 takes instructions literally — be precise, not vague
- Opus 4.7 self-verifies before responding — ask it to double-check
- Price: Opus 4.7 same as Opus 4.6 ($5/M input, $25/M output)
