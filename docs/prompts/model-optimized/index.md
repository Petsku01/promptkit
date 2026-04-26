# Model-Optimized

Prompts optimized for specific LLM models and providers. 123 prompts across 19 groups.

## Provider-Specific

| Group | Description | Count |
|-------|-------------|-------|
| [Anthropic](anthropic/index.md) | Optimized for Claude models (3 Haiku, 3 Opus, 3 Sonnet, 3.7 Sonnet, Opus 4, Opus 4.5, Sonnet 4) | 15 |
| [OpenAI](openai/index.md) | Optimized for GPT and o-series models | 15 |
| [Google](google/index.md) | Optimized for Gemini models (2, 2.5, Flash, Pro) | 9 |
| [DeepSeek](deepseek/index.md) | Optimized for DeepSeek Coder, R1, and V3 | 10 |
| [Meta](meta/index.md) | Optimized for LLaMA models (3.1, 3.2, 3.3) | 6 |
| [Mistral](mistral/index.md) | Optimized for Codestral, Mistral Large, Nemo, and Mixtral | 5 |
| [Qwen](qwen/index.md) | Optimized for Qwen models (2.5, 3, 3.5) | 9 |
| [Cohere](cohere/index.md) | Optimized for Cohere Command R and R+ | 6 |
| [xAI](xai/index.md) | Optimized for Grok 2 and Grok 3 | 6 |
| [Small Models](small-models/index.md) | Optimized for small models (Phi-3, Phi-3.5, Gemma 2) | 5 |

## Techniques & Patterns

| Group | Description | Count |
|-------|-------------|-------|
| [Advanced Techniques](advanced-techniques/index.md) | Chain-of-thought, tree-of-thoughts, self-consistency, and more | 6 |
| [Agentic](agentic/index.md) | Orchestration, planning, reflection, and tool use | 4 |
| [Few-Shot](few-shot/index.md) | Analysis, classification, generation, and transformation examples | 4 |
| [Roles](roles/index.md) | Business, creative, education, simulators, and technical | 5 |
| [System Prompts](system-prompts/index.md) | Coding, creative, education, expert, and productivity | 5 |
| [Safety](safety/index.md) | Injection defense and moderation | 2 |
| [Benchmarks](benchmarks/index.md) | Instruction following, reasoning, coding, and safety benchmarks | 4 |
| [Evaluation](evaluation/index.md) | A/B testing, LLM judges, and quality metrics | 3 |
| [Use Cases](use-cases/index.md) | Customer support, data processing, HR, and sales/marketing | 4 |

## Browsing

```bash
# List all model-optimized prompts
promptkit prompts --model model-optimized

# Search for a specific provider
promptkit search "claude"
```
