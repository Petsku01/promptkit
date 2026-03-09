# Model-Optimized Prompts

Valitse yhtiö → malli → teema → kopioi.

## Yhtiöt

| Yhtiö | Mallit | Linkki |
|-------|--------|--------|
| **OpenAI** | GPT-4, GPT-4o, o1/o3 | [openai/](openai/) |
| **Anthropic** | Claude Opus, Sonnet, Haiku | [anthropic/](anthropic/) |
| **Google** | Gemini Pro, Flash, 2.0 | [google/](google/) |
| **Meta** | Llama 3.1, 3.2, 3.3 | [meta/](meta/) |
| **Mistral** | Large, Mixtral, Nemo, Codestral | [mistral/](mistral/) |
| **DeepSeek** | V3, Coder | [deepseek/](deepseek/) |
| **Cohere** | Command R, Command R+ | [cohere/](cohere/) |
| **xAI** | Grok 2 | [xai/](xai/) |
| **Qwen** | 2.5, 3, 3.5 | [qwen/](qwen/) |
| **Pienet** | Phi, Gemma (<10B) | [small-models/](small-models/) |

## Pikaviitteet

| Malli | Muista |
|-------|--------|
| GPT-4o | "Show each step" |
| o1/o3 | ÄLÄ "think step by step" |
| Claude | XML-tagit |
| Haiku | LYHYET promptit |
| Gemini Flash | Pitkä konteksti OK |
| DeepSeek V3 | Halpa + hyvä |
| Command R | RAG-erikoinen |
| Grok | Reaaliaikainen tieto |
| Qwen 3.5 | Pienille koneille |
| Phi/Gemma | Max 200 tokenia |

## Rakenne

```
model-optimized/
├── [yhtiö]/
│   ├── README.md           ← Yhtiön yleiskatsaus
│   └── [malli]/
│       ├── README.md       ← Mallin yleiskatsaus
│       ├── analysis.md     ← Analyysipromptit
│       ├── coding.md       ← Koodauspromptit
│       └── ...             ← Teemakohtaiset
```
