# DeepSeek Models

## Models

| Model | Best For | Prompts |
|-------|----------|---------|
| [DeepSeek-Coder](deepseek-coder/) | Code generation & review | 4 |
| [DeepSeek-R1](deepseek-r1/) | Reasoning, math, analysis | 2 |
| [DeepSeek-V3](deepseek-v3/) | General purpose, coding, analysis | 5 |
| [DeepSeek-V3.1](deepseek-v3.1/) | Improved coding & analysis | 2 |
| [DeepSeek-V4 Pro](deepseek-v4-pro/) | Agentic coding, long-context, cost-efficient | 2 |
| [DeepSeek-V4 Flash](deepseek-v4-flash/) | High-throughput, batch processing | 2 |

## Key Differences

- **V4 Pro**: Newest, 1.6T params (49B active), 1M context, best coding
- **V4 Flash**: 284B params (13B active), 1M context, fast/cheap, high-throughput
- **V3.1**: Improved V3, good general-purpose coding
- **V3**: Solid coding and analysis, cost-efficient
- **R1**: Reasoning-focused (use V4 thinking mode instead when available)
- **Coder**: Specialized code generation

## General Tips

- V4 Pro is ~1/7th the cost of Claude Opus for similar coding quality
- V4 Flash is ~35× cheaper on input than Claude Opus
- Use `deepseek-chat` for standard, `deepseek-reasoner` for thinking mode
- MIT license — can self-host
- 1M context window (V4) can hold entire codebases
- V4 Pro replaces R1 for most use cases
