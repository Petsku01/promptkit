# OpenAI Models

## Models

| Model | Best For | Prompts |
|-------|----------|---------|
| [GPT-4](gpt-4/) | Complex reasoning, reliability | 8 |
| [GPT-4o](gpt-4o/) | Speed, vision, multimodal | 8 |
| [o1/o3](o1/) | Hard problems, math, code | 8 |

## Key Differences

- **GPT-4**: Most reliable, detailed instructions OK
- **GPT-4o**: Faster, may skip steps → say "show each step"
- **o1/o3**: Reasoning models → DON'T say "think step by step"

## General Tips

- Use `developer` role for system instructions
- Markdown formatting works well
- JSON mode: `response_format: {"type": "json_object"}`
- Structured Outputs (GPT-4o+): guaranteed schema
