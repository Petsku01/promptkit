# Model-Optimized Prompts

Each model family has different strengths and optimal prompting styles. This directory contains model-specific optimizations for common patterns.

## Model Families

| Family | Models | Key Optimizations |
|--------|--------|-------------------|
| **OpenAI** | GPT-4, GPT-4o, o1, o3 | developer/user roles, concise, markdown |
| **Anthropic** | Claude 3/4, Opus, Sonnet, Haiku | XML tags, long context OK, thinking tags |
| **Mistral** | Mistral, Mixtral, Large | clear sections, worded scales, few-shot |
| **Meta** | Llama 3, 3.1, 3.2, 3.3 | simple structure, explicit format, BOS/EOS |
| **Google** | Gemini Pro, Flash, Ultra | structured, bullets, grounding |
| **Open Source** | Qwen, DeepSeek, Yi, Phi | simple prompts, less meta-instructions |

## Usage

```python
from llm_promptkit import PromptBuilder

# Auto-select optimized version
prompt = (PromptBuilder()
    .pattern("chain-of-thought")
    .for_model("claude-3-opus")
    .task("Analyze this code")
    .build())
```

## Directory Structure

```
model-optimized/
├── openai/
│   ├── chain-of-thought.md
│   ├── json-output.md
│   └── ...
├── anthropic/
│   ├── chain-of-thought.md
│   └── ...
├── mistral/
├── meta/
├── google/
└── open-source/
```

## Optimization Sources

- [OpenAI Prompt Engineering Guide](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic Claude Best Practices](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering)
- [Mistral Prompting Guide](https://docs.mistral.ai/guides/prompting_capabilities/)
- [Meta Llama Documentation](https://llama.meta.com/docs/)
- [Google Gemini Prompting Guide](https://ai.google.dev/gemini-api/docs/prompting-intro)
