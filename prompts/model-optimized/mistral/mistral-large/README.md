# Mistral Large

## Characteristics
- **Context**: 128K tokens
- **Strengths**: Reasoning, multilingual, function calling
- **Best for**: Complex tasks, enterprise, code

## Prompt Themes

| Theme | File |
|-------|------|
| Analysis | [analysis.md](analysis.md) |
| Coding | [coding.md](coding.md) |
| JSON | [json-output.md](json-output.md) |

## Key Features

- Native function calling
- Strong reasoning
- Good at following complex instructions
- Excellent multilingual support (especially French)

## System Prompt Format

```
<s>[INST] You are a helpful assistant specialized in [domain].

Your guidelines:
- [guideline 1]
- [guideline 2]
[/INST]

Understood. I will follow these guidelines.</s>

[INST] [user message] [/INST]
```

## Tips

✅ **Best practices:**
- Use `[INST]...[/INST]` tags for clarity
- System prompt first, then instructions
- Mistral handles complex reasoning well

❌ **Avoid:**
- Overly simple prompts (it can handle more)
- Ignoring its multilingual strengths
