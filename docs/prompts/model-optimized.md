# Model-Optimized Prompts

Prompts tuned for specific LLM providers and models.

## How It Works

Model-optimized prompts are located in the `model-optimized/` subdirectory, organized by provider. Each prompt is tuned for a specific model's strengths and conventions.

## Supported Providers

| Provider | Models | Best For |
|----------|--------|----------|
| OpenAI | GPT-4o, o1, o3 | General, reasoning |
| Anthropic | Claude 3.5/4, Opus | Analysis, coding |
| Google | Gemini 2, Flash | Multimodal |
| DeepSeek | V3, Coder | Math, code |
| Cohere | Command R/R+ | RAG, citations |
| xAI | Grok 2 | Real-time, creative |
| Qwen | 2.5, 3, 3.5 | Multilingual |
| Small Models | Phi, Gemma | Lightweight tasks |

## Browsing

```bash
# List all models
promptkit prompts --model model-optimized

# Search for a provider
promptkit search "openai"
```

## Why Model-Specific?

Different models interpret instructions differently. A prompt optimized for Claude's XML structure may not work well with GPT's markdown preferences. Model-optimized prompts account for:

- Token efficiency per model
- Instruction following conventions
- Output format preferences
- Known strengths and weaknesses

## Example Usage

```python
from llm_promptkit import PromptBuilder

builder = PromptBuilder()
builder.persona("Expert Python developer")
builder.pattern("chain-of-thought")
builder.task("Refactor this code")
prompt = builder.build()
```