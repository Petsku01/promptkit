# Model-Optimized Prompts

Jokaiselle mallille omat optimoidut promptit. Valitse mallisi → avaa tiedosto → kopioi.

## Mallit

| Malli | Tiedosto | Prompteja |
|-------|----------|-----------|
| GPT-4 | [openai/gpt-4.md](openai/gpt-4.md) | 8 |
| GPT-4o | [openai/gpt-4o.md](openai/gpt-4o.md) | 8 |
| o1/o3 | [openai/o1.md](openai/o1.md) | 8 |
| Claude Opus | [anthropic/claude-3-opus.md](anthropic/claude-3-opus.md) | 5 |
| Claude Sonnet | [anthropic/claude-3-sonnet.md](anthropic/claude-3-sonnet.md) | 8 |
| Claude Haiku | [anthropic/claude-3-haiku.md](anthropic/claude-3-haiku.md) | 10 |
| Mistral Large | [mistral/mistral-large.md](mistral/mistral-large.md) | 8 |
| Mixtral | [mistral/mixtral.md](mistral/mixtral.md) | 5 |
| Llama 3.1 | [meta/llama-3.1.md](meta/llama-3.1.md) | 5 |
| Llama 3.2 | [meta/llama-3.2.md](meta/llama-3.2.md) | 5 |
| Llama 3.3 | [meta/llama-3.3.md](meta/llama-3.3.md) | 9 |

## Esimerkki per malli

**GPT-4o:**
```
Analyze step by step. Show EVERY step. Do not skip.
```

**Claude Sonnet:**
```xml
<task>Solve this</task>
<thinking>[reasoning]</thinking>
<answer>[answer]</answer>
```

**o1/o3:**
```
Solve: [problem]
```
⚠️ ÄLÄ sano "think step by step" - o1 ajattelee automaattisesti.

**Llama 3.3:**
```
Step 1: Understand
Step 2: Plan
Step 3: Execute
Final Answer:
```

**Mistral Large:**
```markdown
## Task
[description]

## Process
### 1. Analysis
### 2. Solution
```

## Lähteet

- [OpenAI Docs](https://platform.openai.com/docs/guides/prompt-engineering)
- [Anthropic Docs](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering)
- [Mistral Docs](https://docs.mistral.ai/guides/prompting_capabilities/)
