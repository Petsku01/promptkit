# Model-Optimized Prompts

Valitse yhtiö/kategoria → malli → teema → kopioi.

## Yhtiöt

| Yhtiö | Mallit | Linkki |
|-------|--------|--------|
| **OpenAI** | GPT-4, GPT-4o, o1/o3 | [openai/](openai/) |
| **Anthropic** | Claude Opus, Sonnet, Haiku | [anthropic/](anthropic/) |
| **Mistral** | Mistral Large, Mixtral | [mistral/](mistral/) |
| **Meta** | Llama 3.1, 3.2, 3.3 | [meta/](meta/) |
| **Google** | Gemini Pro | [google/](google/) |
| **Qwen** | Qwen 2.5, 3, 3.5 | [qwen/](qwen/) |
| **Pienet mallit** | Phi, Gemma (<10B) | [small-models/](small-models/) |

## Rakenne

```
model-optimized/
├── openai/
│   └── gpt-4o/
│       ├── README.md      ← Yleiskatsaus
│       ├── analysis.md    ← Analyysipromptit
│       ├── coding.md      ← Koodauspromptit
│       └── ...
├── qwen/
│   ├── qwen-2.5/
│   └── qwen-3.5/          ← Pienet versiot
└── small-models/
    ├── phi-3.5/
    └── gemma-2/
```

## Pikaviitteet

| Malli | Muista |
|-------|--------|
| GPT-4o | "Show each step" |
| o1/o3 | ÄLÄ "think step by step" |
| Claude | XML-tagit |
| Haiku | LYHYET promptit |
| Qwen 3.5 | Yksinkertaiset tehtävät |
| Phi/Gemma | Max 200 tokenia |
