---
category: "model-optimized"
title: "Codestral: Specialized Coding"
subcategory: "mistral"
model: "codestral"
source: "promptkit-authored"
---
# Codestral: Specialized Coding

## When to Use

Use this template with Mistral’s current Codestral SKU for fill-in-the-middle, prefix completion, and short code generation. The live model page lists **Codestral v25.08** (`codestral-2508`), Premier, released end of July 2025, specialized for low-latency, high-frequency FIM and code generation, **128k** context, chat completions plus **`/v1/fim/completions`**, structured outputs, function calling, predicted outputs, prefix, and batching. Older `codestral-2501` / `codestral-2405` IDs are deprecated; the documented alternative is `codestral-25-08`. This is not Mistral Large and not Vibe Code (the agent product with a filesystem).

Use FIM when you have prefix and suffix (cursor in the middle of a file). Use chat generation when you need a whole function plus tests. Do not send long product conversations, RAG essays, or vision. Do not treat the existing folder README’s 32K figure as current—the 2025-08 card is 128k.

## The Prompt

Chat / generate mode:

```
Language: [language]
Task: [function or fix]
Prefix (already in the file): [code before the hole]
Suffix (must still compile): [code after the hole]
Requirements:
- [req]
- Match surrounding style and imports
- No new dependencies unless named

If you are on the FIM endpoint, the client sends `prompt` + `suffix` and you
should emit only the missing middle. If you are on chat completions, emit
only the middle between the markers below, no fences unless asked.

[code before]
<FILL>
[code after]

Stop at the first complete, compilable middle. Do not repeat the prefix or
suffix. Do not write a tutorial. If the hole cannot be filled without
breaking the suffix, say so in one line instead of emitting invalid code.
```

FIM API note (client, not model text): POST `/v1/fim/completions` with the 25.08 model id, prefix as prompt, optional suffix. Predicted outputs / prefix features are separate Studio endpoints; enable them in the client if you use them.

## How It Works

Codestral’s catalog value is FIM, which general instruct models fake poorly. The prompt therefore dual-specifies: chat users wrap `<FILL>`; API users set prompt/suffix and must not also ask for a markdown essay. “Do not repeat prefix/suffix” is the main stop rule—FIM models otherwise echo context. 128k allows a large current file plus neighbors, not a whole monorepo dump. Function calling and structured outputs exist on the card but do not turn Codestral into an autonomous engineer; keep jobs to a hole, a function, or a unit-test file. Pricing on the model page ($0.3 / $0.9 per M tokens at fetch time) is vendor pricing, not a quality claim.

## Variables

- `[language]`: language of the surrounding file.
- `[function or fix]`: intent, in case the hole is ambiguous.
- `[code before the hole]` / `[code after the hole]`: FIM context.
- `[req]`: behavioral musts the suffix cannot express.

## Related

Living generalist coding: `../mistral-large/coding.md`. This folder’s README already lists FIM examples; this file is the long-form prompt.

Grounded 2026-11-02 against [Codestral 25.08](https://docs.mistral.ai/models/codestral-25-08) and the [models overview](https://docs.mistral.ai/models) (code-model row, deprecated 2501→25-08).

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED: structural smoke passed |
