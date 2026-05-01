# OpenAI Models

## Models

| Model | Best For | Prompts |
|-------|----------|---------|
| [GPT-3.5 Turbo](gpt-3.5-turbo/) | Quick, cheap tasks | 1 |
| [GPT-4](gpt-4/) | Complex reasoning, reliability | 8 |
| [GPT-4 Turbo](gpt-4-turbo/) | Fast reasoning | 8 |
| [GPT-4o](gpt-4o/) | Speed, vision, multimodal | 8 |
| [GPT-4.1](gpt-4.1/) | Instruction following, coding | 5 |
| [GPT-5](gpt-5/) | Advanced coding & reasoning | 2 |
| [GPT-5.4](gpt-5.4/) | Agentic coding, deep analysis | 4 |
| [o1](o1/) | Hard problems, math, code | 8 |
| [o3-mini](o3-mini/) | Efficient reasoning | 8 |
| [o3](o3/) | Advanced reasoning | 2 |
| [Codex 5.3](codex-5.3/) | Code generation | 1 |

## Key Differences

- **GPT-3.5 Turbo**: Cheapest, fastest, simplest tasks only
- **GPT-4 / GPT-4 Turbo**: Reliable, detailed instructions OK
- **GPT-4o**: Faster, may skip steps → say "show each step"
- **GPT-4.1**: Improved instruction following, coding
- **GPT-5**: State-of-the-art coding and multimodal
- **GPT-5.4**: Agentic workflows, deep analysis, Thinking mode
- **o1/o3**: Reasoning models → DON'T say "think step by step"
- **o3-mini**: Cheaper reasoning, good for standard tasks
- **Codex 5.3**: Specialized for code generation

## General Tips

- Use `developer` role for system instructions
- Markdown formatting works well
- JSON mode: `response_format: {"type": "json_object"}`
- Structured Outputs (GPT-4o+): guaranteed schema
- GPT-5.4 supports extended Thinking mode for deep reasoning
