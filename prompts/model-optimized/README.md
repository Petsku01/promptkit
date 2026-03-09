# Model-Optimized Prompts

Version-specific prompting guides for each model family.

## Directory Structure

```
model-optimized/
├── openai/
│   ├── gpt-4.md          # GPT-4 (8K/32K)
│   ├── gpt-4o.md         # GPT-4o (128K, multimodal)
│   └── o1.md             # o1/o3 reasoning models
├── anthropic/
│   ├── claude-3-opus.md  # Highest capability
│   ├── claude-3-sonnet.md # Balanced
│   └── claude-3-haiku.md # Fast & cheap
├── mistral/
│   ├── mistral-large.md  # Top tier
│   └── mixtral.md        # MoE models
├── meta/
│   ├── llama-3.1.md      # 128K, tool use
│   ├── llama-3.2.md      # Multimodal, edge
│   └── llama-3.3.md      # Best 70B
├── google/
│   └── _base-cot.md      # Gemini
└── open-source/
    └── chain-of-thought.md  # Qwen, DeepSeek, etc.
```

## Quick Reference

| Model | Key Optimization |
|-------|-----------------|
| **GPT-4** | Concise, markdown, developer role |
| **GPT-4o** | "Show each step" (may skip), Structured Outputs |
| **o1/o3** | DON'T say "think step by step" - it's automatic |
| **Claude Opus** | XML tags, extended thinking, detailed |
| **Claude Sonnet** | XML tags, balanced, great for code |
| **Claude Haiku** | SHORT prompts, simple tasks only |
| **Mistral Large** | Markdown sections, worded scales |
| **Mixtral** | Few-shot examples, efficient |
| **Llama 3.1** | 128K context, tool calling |
| **Llama 3.2** | Vision support (11B/90B) |
| **Llama 3.3** | Best instruction following |

## Usage

Find your model → Open the guide → Copy optimized patterns.

```python
# Future API support planned:
prompt = PromptBuilder().pattern("cot").for_model("claude-3-sonnet").build()
```

## Sources

- [OpenAI Prompt Engineering](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic Claude Docs](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering)
- [Mistral Documentation](https://docs.mistral.ai/guides/prompting_capabilities/)
- [Meta Llama Docs](https://llama.meta.com/docs/)
