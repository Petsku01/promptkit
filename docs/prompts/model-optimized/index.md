# Model-Optimized Prompts

Prompts optimized for specific LLM models.

## Browsing Prompts

```bash
# List all providers and models
promptkit prompts

# List model-optimized prompts
promptkit prompts --model model-optimized

# Search for a specific prompt
promptkit search "code review"
```

## Available Prompts

### advanced-techniques

| Prompt | Description |
|--------|-------------|
| [chain-of-thought](advanced-techniques-chain-of-thought.md) | Chain-of-Thought (CoT) |
| [meta-prompting](advanced-techniques-meta-prompting.md) | Meta-Prompting |
| [prompt-chaining](advanced-techniques-prompt-chaining.md) | Prompt Chaining |
| [react](advanced-techniques-react.md) | ReAct (Reasoning + Acting) |
| [self-consistency](advanced-techniques-self-consistency.md) | Self-Consistency |
| [tree-of-thoughts](advanced-techniques-tree-of-thoughts.md) | Tree-of-Thoughts (ToT) |

### agentic

| Prompt | Description |
|--------|-------------|
| [orchestration](agentic-orchestration.md) | Agentic: Orchestration |
| [planning](agentic-planning.md) | Agentic: Planning |
| [reflection](agentic-reflection.md) | Agentic: Reflection |
| [tool-use](agentic-tool-use.md) | Agentic: Tool Use |

### anthropic / claude-3-haiku

| Prompt | Description |
|--------|-------------|
| [analysis](anthropic-claude-3-haiku-analysis.md) | Claude Haiku: Quick Analysis |
| [coding](anthropic-claude-3-haiku-coding.md) | Claude Haiku: Quick Coding |

### anthropic / claude-3-opus

| Prompt | Description |
|--------|-------------|
| [analysis](anthropic-claude-3-opus-analysis.md) | Claude Opus: Deep Analysis |
| [reasoning](anthropic-claude-3-opus-reasoning.md) | Claude Opus: Complex Reasoning |

### anthropic / claude-3-sonnet

| Prompt | Description |
|--------|-------------|
| [analysis](anthropic-claude-3-sonnet-analysis.md) | Claude Sonnet: Analysis |
| [coding](anthropic-claude-3-sonnet-coding.md) | Claude Sonnet: Coding |
| [json-output](anthropic-claude-3-sonnet-json-output.md) | Claude Sonnet: JSON Output |
| [writing](anthropic-claude-3-sonnet-writing.md) | Claude Sonnet: Writing |

### anthropic / claude-3.7-sonnet

| Prompt | Description |
|--------|-------------|
| [coding](anthropic-claude-3.7-sonnet-coding.md) | Claude 3.7 Sonnet: Coding |
| [reasoning](anthropic-claude-3.7-sonnet-reasoning.md) | Claude 3.7 Sonnet: Hybrid Reasoning |

### anthropic / claude-opus-4

| Prompt | Description |
|--------|-------------|
| [analysis](anthropic-claude-opus-4-analysis.md) | Claude Opus 4: Deep Analysis |

### anthropic / claude-opus-4.5

| Prompt | Description |
|--------|-------------|
| [coding](anthropic-claude-opus-4.5-coding.md) | Claude Opus 4.5: Coding |
| [reasoning](anthropic-claude-opus-4.5-reasoning.md) | Claude Opus 4.5: Extended Thinking |

### anthropic / claude-sonnet-4

| Prompt | Description |
|--------|-------------|
| [coding](anthropic-claude-sonnet-4-coding.md) | Claude Sonnet 4: Coding |
| [reasoning](anthropic-claude-sonnet-4-reasoning.md) | Claude Sonnet 4: Reasoning |

### benchmarks

| Prompt | Description |
|--------|-------------|
| [coding](benchmarks-coding.md) | Benchmark: Coding |
| [instruction-following](benchmarks-instruction-following.md) | Benchmark: Instruction Following |
| [reasoning](benchmarks-reasoning.md) | Benchmark: Reasoning |
| [safety](benchmarks-safety.md) | Benchmark: Safety |

### cohere / command-r

| Prompt | Description |
|--------|-------------|
| [analysis](cohere-command-r-analysis.md) | Command R: Analysis |
| [grounding](cohere-command-r-grounding.md) | Command R: Grounded Generation |
| [rag](cohere-command-r-rag.md) | Command R: RAG (Retrieval Augmented Generation) |

### cohere / command-r-plus

| Prompt | Description |
|--------|-------------|
| [analysis](cohere-command-r-plus-analysis.md) | Command R+: Analysis |
| [grounding](cohere-command-r-plus-grounding.md) | Command R+: Grounded Generation |
| [rag](cohere-command-r-plus-rag.md) | Command R+: RAG (Retrieval Augmented Generation) |

### deepseek / deepseek-coder

| Prompt | Description |
|--------|-------------|
| [debugging](deepseek-deepseek-coder-debugging.md) | DeepSeek Coder: Debugging |
| [generation](deepseek-deepseek-coder-generation.md) | DeepSeek Coder: Generointi |
| [refactoring](deepseek-deepseek-coder-refactoring.md) | DeepSeek Coder: Refactoring |
| [review](deepseek-deepseek-coder-review.md) | DeepSeek Coder: Code Review |

### deepseek / deepseek-r1

| Prompt | Description |
|--------|-------------|
| [coding](deepseek-deepseek-r1-coding.md) | DeepSeek-R1: Coding |
| [reasoning](deepseek-deepseek-r1-reasoning.md) | DeepSeek-R1: Zero-Shot Reasoning |

### deepseek / deepseek-v3

| Prompt | Description |
|--------|-------------|
| [analysis](deepseek-deepseek-v3-analysis.md) | DeepSeek V3: Analysis |
| [coding](deepseek-deepseek-v3-coding.md) | DeepSeek V3: Coding |
| [json-output](deepseek-deepseek-v3-json-output.md) | DeepSeek V3: JSON Output |
| [math](deepseek-deepseek-v3-math.md) | DeepSeek V3: Matematiikka |

### evaluation

| Prompt | Description |
|--------|-------------|
| [ab-testing](evaluation-ab-testing.md) | Evaluation: A/B Testing |
| [llm-judge](evaluation-llm-judge.md) | Evaluation: LLM as Judge |
| [quality-metrics](evaluation-quality-metrics.md) | Evaluation: Quality Metrics |

### few-shot

| Prompt | Description |
|--------|-------------|
| [analysis](few-shot-analysis.md) | Few-Shot: Analysis |
| [classification](few-shot-classification.md) | Few-Shot: Luokittelu |
| [generation](few-shot-generation.md) | Few-Shot: Generointi |
| [transformation](few-shot-transformation.md) | Few-Shot: Muunnos |

### google / gemini-2

| Prompt | Description |
|--------|-------------|
| [analysis](google-gemini-2-analysis.md) | Gemini 2: Analysis |
| [coding](google-gemini-2-coding.md) | Gemini 2: Coding |
| [multimodal](google-gemini-2-multimodal.md) | Gemini 2: Multimodal |

### google / gemini-2.5

| Prompt | Description |
|--------|-------------|
| [multimodal](google-gemini-2.5-multimodal.md) | Gemini 2.5: Multimodal |
| [reasoning](google-gemini-2.5-reasoning.md) | Gemini 2.5: Reasoning |

### google / gemini-flash

| Prompt | Description |
|--------|-------------|
| [basic](google-gemini-flash-basic.md) | Gemini Flash: Basic Tasks |
| [long-context](google-gemini-flash-long-context.md) | Gemini Flash: Long context |

### google / gemini-pro

| Prompt | Description |
|--------|-------------|
| [analysis](google-gemini-pro-analysis.md) | Gemini Pro: Analysis |
| [coding](google-gemini-pro-coding.md) | Gemini Pro: Coding |

### meta / llama-3.1

| Prompt | Description |
|--------|-------------|
| [analysis](meta-llama-3.1-analysis.md) | Llama 3.1: Analysis |
| [coding](meta-llama-3.1-coding.md) | Llama 3.1: Coding |

### meta / llama-3.2

| Prompt | Description |
|--------|-------------|
| [general](meta-llama-3.2-general.md) | Llama 3.2: General Tasks |
| [multimodal](meta-llama-3.2-multimodal.md) | Llama 3.2: Multimodal |

### meta / llama-3.3

| Prompt | Description |
|--------|-------------|
| [analysis](meta-llama-3.3-analysis.md) | Llama 3.3: Analysis |
| [coding](meta-llama-3.3-coding.md) | Llama 3.3: Coding |

### mistral / codestral

| Prompt | Description |
|--------|-------------|
| [coding](mistral-codestral-coding.md) | Codestral: Specialized Coding |

### mistral / mistral-large

| Prompt | Description |
|--------|-------------|
| [coding](mistral-mistral-large-coding.md) | Mistral Large: Coding |

### mistral / mistral-nemo

| Prompt | Description |
|--------|-------------|
| [general](mistral-mistral-nemo-general.md) | Mistral Nemo: Efficient General Tasks |

### mistral / mixtral

| Prompt | Description |
|--------|-------------|
| [analysis](mistral-mixtral-analysis.md) | Mixtral: Analysis (MoE) |
| [coding](mistral-mixtral-coding.md) | Mixtral: Coding (MoE) |

### openai / codex-5.3

| Prompt | Description |
|--------|-------------|
| [coding](openai-codex-5.3-coding.md) | Codex 5.3: Agentic Coding |

### openai / gpt-3.5-turbo

| Prompt | Description |
|--------|-------------|
| [quick-tasks](openai-gpt-3.5-turbo-quick-tasks.md) | GPT-3.5 Turbo: Quick Tasks |

### openai / gpt-4

| Prompt | Description |
|--------|-------------|
| [analysis](openai-gpt-4-analysis.md) | GPT-4: Analysis |
| [coding](openai-gpt-4-coding.md) | GPT-4: Coding |

### openai / gpt-4-turbo

| Prompt | Description |
|--------|-------------|
| [analysis](openai-gpt-4-turbo-analysis.md) | GPT-4 Turbo: Analysis (Long Context) |
| [coding](openai-gpt-4-turbo-coding.md) | GPT-4 Turbo: Coding (Long Context) |

### openai / gpt-4o

| Prompt | Description |
|--------|-------------|
| [analysis](openai-gpt-4o-analysis.md) | GPT-4o: Analysis Analysis & Reasoning Reasoning |
| [coding](openai-gpt-4o-coding.md) | GPT-4o: Coding |
| [json-output](openai-gpt-4o-json-output.md) | GPT-4o: JSON Output |
| [vision](openai-gpt-4o-vision.md) | GPT-4o: Visionn (Image Analysis) |
| [writing](openai-gpt-4o-writing.md) | GPT-4o: Writing |

### openai / gpt-5

| Prompt | Description |
|--------|-------------|
| [coding](openai-gpt-5-coding.md) | GPT-5: Coding |
| [reasoning](openai-gpt-5-reasoning.md) | GPT-5: Advanced Reasoning |

### openai / o1

| Prompt | Description |
|--------|-------------|
| [reasoning](openai-o1-reasoning.md) | O1: Deep Reasoning |

### openai / o3-mini

| Prompt | Description |
|--------|-------------|
| [reasoning](openai-o3-mini-reasoning.md) | O3-mini: Efficient Reasoning |

### qwen / qwen-2.5

| Prompt | Description |
|--------|-------------|
| [analysis](qwen-qwen-2.5-analysis.md) | Qwen 2.5: Analysis |
| [coding](qwen-qwen-2.5-coding.md) | Qwen 2.5: Coding |
| [json-output](qwen-qwen-2.5-json-output.md) | Qwen 2.5: JSON Output |
| [multilingual](qwen-qwen-2.5-multilingual.md) | Qwen 2.5: Multilingual |

### qwen / qwen-3

| Prompt | Description |
|--------|-------------|
| [coding](qwen-qwen-3-coding.md) | Qwen 3: Coding |
| [multilingual](qwen-qwen-3-multilingual.md) | Qwen 3: Multilingual |

### qwen / qwen-3.5

| Prompt | Description |
|--------|-------------|
| [basic](qwen-qwen-3.5-basic.md) | Qwen 3.5: Basic Tasks |
| [coding](qwen-qwen-3.5-coding.md) | Qwen 3.5: Coding (simplified) |
| [json-output](qwen-qwen-3.5-json-output.md) | Qwen 3.5: JSON (simplified) |

### roles

| Prompt | Description |
|--------|-------------|
| [business](roles-business.md) | Bisnesroolit |
| [creative](roles-creative.md) | Luovat roolit |
| [education](roles-education.md) | Opetusroolit |
| [simulators](roles-simulators.md) | Simulaattorit |
| [technical](roles-technical.md) | Technical Roles |

### safety

| Prompt | Description |
|--------|-------------|
| [injection-defense](safety-injection-defense.md) | Safety: Prompt Injection Defense |
| [moderation](safety-moderation.md) | Safety: Content Moderation |

### small-models / gemma-2

| Prompt | Description |
|--------|-------------|
| [simple-tasks](small-models-gemma-2-simple-tasks.md) | Gemma 2: Simple Tasks |

### small-models / phi-3

| Prompt | Description |
|--------|-------------|
| [basic](small-models-phi-3-basic.md) | Phi 3.5: Basic Tasks |
| [coding](small-models-phi-3-coding.md) | Phi 3.5: Coding |

### small-models / phi-3.5

| Prompt | Description |
|--------|-------------|
| [basic](small-models-phi-3.5-basic.md) | Phi 3.5: Basic Tasks |
| [coding](small-models-phi-3.5-coding.md) | Phi 3.5: Coding |

### system-prompts

| Prompt | Description |
|--------|-------------|
| [coding](system-prompts-coding.md) | System Prompts: Coding |
| [creative](system-prompts-creative.md) | System Prompts: Luova |
| [education](system-prompts-education.md) | System Prompts: Opetus |
| [expert](system-prompts-expert.md) | System Prompts: Asiantuntija |
| [productivity](system-prompts-productivity.md) | System Prompts: Tuottavuus |

### use-cases

| Prompt | Description |
|--------|-------------|
| [customer-support](use-cases-customer-support.md) | Use Case: Customer Support |
| [data-processing](use-cases-data-processing.md) | Use Case: Data Processing |
| [hr-recruiting](use-cases-hr-recruiting.md) | Use Case: HR & Recruiting |
| [sales-marketing](use-cases-sales-marketing.md) | Use Case: Sales & Marketing |

### xai / grok-2

| Prompt | Description |
|--------|-------------|
| [analysis](xai-grok-2-analysis.md) | Grok 2: Analysis |
| [coding](xai-grok-2-coding.md) | Grok 2: Coding |
| [creative](xai-grok-2-creative.md) | Grok 2: Luova |
| [realtime](xai-grok-2-realtime.md) | Grok 2: Real-time information |

### xai / grok-3

| Prompt | Description |
|--------|-------------|
| [coding](xai-grok-3-coding.md) | Grok 3: Coding |
| [reasoning](xai-grok-3-reasoning.md) | Grok 3: Reasoning |
