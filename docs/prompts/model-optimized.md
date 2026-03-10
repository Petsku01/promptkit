# Model-Optimized Prompts

Provider-specific prompts optimized for each model's strengths.

## Supported Providers

| Provider | Models | Specialty |
|----------|--------|-----------|
| [OpenAI](https://github.com/Petsku01/promptkit/tree/master/prompts/model-optimized/openai) | GPT-4o, o1, o3 | General, reasoning |
| [Anthropic](https://github.com/Petsku01/promptkit/tree/master/prompts/model-optimized/anthropic) | Claude 3.5/4, Opus | Analysis, coding |
| [Google](https://github.com/Petsku01/promptkit/tree/master/prompts/model-optimized/google) | Gemini 2, Flash | Multimodal, long-context |
| [DeepSeek](https://github.com/Petsku01/promptkit/tree/master/prompts/model-optimized/deepseek) | V3, Coder | Math, code |
| [Cohere](https://github.com/Petsku01/promptkit/tree/master/prompts/model-optimized/cohere) | Command R/R+ | RAG, citations |
| [xAI](https://github.com/Petsku01/promptkit/tree/master/prompts/model-optimized/xai) | Grok 2 | Real-time, creative |
| [Qwen](https://github.com/Petsku01/promptkit/tree/master/prompts/model-optimized/qwen) | 2.5, 3, 3.5 | Multilingual |
| [Small Models](https://github.com/Petsku01/promptkit/tree/master/prompts/model-optimized/small-models) | Phi, Gemma | Resource-constrained |

## Why Model-Specific?

Different models respond better to different prompt styles:

- **OpenAI o1/o3**: Minimal prompts, let the model reason
- **Claude**: Detailed XML structure, explicit constraints  
- **Gemini**: Good with multimodal, long context windows
- **Small models**: Simple prompts, one task at a time

## Structure

Each provider folder contains themed prompt files:

```
model-optimized/
├── openai/
│   ├── analysis.md
│   ├── coding.md
│   ├── json-output.md
│   └── writing.md
├── anthropic/
│   ├── analysis.md
│   └── ...
```

[Browse all model-optimized prompts →](https://github.com/Petsku01/promptkit/tree/master/prompts/model-optimized)
