# Model-Optimized Prompts

Valitse yhtiö → malli → kopioi promptit.

## Yhtiöt

| Yhtiö | Mallit | Linkki |
|-------|--------|--------|
| **OpenAI** | GPT-4, GPT-4o, o1/o3 | [openai/](openai/) |
| **Anthropic** | Claude Opus, Sonnet, Haiku | [anthropic/](anthropic/) |
| **Mistral** | Mistral Large, Mixtral | [mistral/](mistral/) |
| **Meta** | Llama 3.1, 3.2, 3.3 | [meta/](meta/) |
| **Google** | Gemini Pro | [google/](google/) |
| **Open Source** | Qwen, DeepSeek, Yi | [open-source/](open-source/) |

## Rakenne

```
model-optimized/
├── openai/
│   ├── README.md       ← Yleiskatsaus
│   ├── gpt-4/
│   │   └── README.md   ← GPT-4 promptit
│   ├── gpt-4o/
│   │   └── README.md
│   └── o1/
│       └── README.md
├── anthropic/
│   ├── README.md
│   ├── claude-3-opus/
│   ├── claude-3-sonnet/
│   └── claude-3-haiku/
...
```

## Pikaviitteet

| Malli | Tärkeintä muistaa |
|-------|-------------------|
| GPT-4o | "Show each step" (voi skipata) |
| o1/o3 | ÄLÄ sano "think step by step" |
| Claude | XML-tagit toimii hyvin |
| Haiku | LYHYET promptit |
| Llama | Yksinkertainen > monimutkainen |
