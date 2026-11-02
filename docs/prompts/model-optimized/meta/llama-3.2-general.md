---
category: "model-optimized"
title: "Llama 3.2: General Tasks"
subcategory: "meta"
model: "llama-3.2"
source: "promptkit-authored"
---
[← Back to Model-Optimized Meta](../index.md)

# Llama 3.2: General Tasks

## When to Use

Use this template with **Llama 3.2 text** instruct weights (1B / 3B, BF16 or quantized) for short assistant, summarization, and custom-tool jobs on-device or at the edge. Meta’s text card: multilingual text in / text and code out, **128k** context on BF16, **8k** on the quantized instruct variants, knowledge cutoff **December 2023**, officially supported languages English, German, French, Italian, Portuguese, Hindi, Spanish, and Thai. Intended uses include assistant-like chat, agentic retrieval, summarization, and mobile writing. Quantized 1B/3B are aimed at phones, tablets, and other constrained runtimes (ExecuTorch).

Lightweight 3.2 models support **custom function definitions** in the system or user prompt only. They do **not** support Llama 3.1’s built-in Brave Search or Wolfram tools. For images, use [multimodal](multimodal.md) (11B/90B vision). For 70B text, use Llama 3.3. For current Meta open weights, use Llama 4.

## The Prompt

```
<|begin_of_text|><|start_header_id|>system<|end_header_id|>

You complete one user task. Stay inside the constraints. If a required
fact is missing, say so. Do not call built-in web/math tools; this 1B/3B
SKU has no Brave Search or Wolfram builtins.

Optional custom tools (JSON). If none, ignore this block:
[function definitions or "none"]

<|eot_id|><|start_header_id|>user<|end_header_id|>

Task: [task]
Language: [one of the 8 supported, or another with the caveat that it
is off-card]
Constraints:
- [hard constraint]
- Output format: [format]
Context (optional):
[paste]

If you invoke a custom tool, reply with only
[func_name(param=value, ...)] and no other text. Otherwise reply with
the artifact only.

<|eot_id|><|start_header_id|>assistant<|end_header_id|>
```

## How It Works

The retired stub said “just talk naturally.” Llama 3.2 1B/3B follow the Llama 3.1 special-token chat template; dropping headers is how small instruct models drift. The prompt keeps `system` / `user` / `assistant` headers and an explicit no-builtin-tools line because copying a 3.1 70B tool prompt onto 3.2-1B is a documented mismatch. Custom tools, when used, must be the only text in the assistant turn and end at `<|eot_id|>`. Function JSON may live in system or user; 3.2 lightweight does not use Brave Search or Wolfram even if you paste those names. Quantized weights are a drop-in for prompts but not for context length (8k vs 128k)—set max tokens from the card you loaded. ExecuTorch is the documented on-device runtime; this text does not configure it. Official languages are eight; other languages are off-card fine-tunes, not a silent default. This file never claims a benchmark win over 3.1 8B.

## Stop rules

Stop if a custom tool is missing a required argument, if the user asked for Brave Search / Wolfram (unsupported on 1B/3B), or if the quantized 8k window is already full. Do not drop `<|eot_id|>` semantics when your server expects the Llama 3 header template. Do not send this prompt to 11B/90B vision as a substitute for the multimodal file. Edge deployment via ExecuTorch is out of band. Knowledge cutoff is December 2023 unless the user supplied later text.

## Variables

- `[function definitions or "none"]`: custom tools or none.
- `[task]`: the user job.
- `[one of the 8 supported, or another with the caveat that it is off-card]`: language.
- `[hard constraint]`: falsifiable limit.
- `[format]`: output contract.
- `[paste]`: optional context.

## Related

[multimodal](multimodal.md). Llama 3.3 70B: `../llama-3.3/`. Living Llama 4: `../llama-4/`.

Grounded 2026-11-02 against Meta’s [Llama 3.2 prompt formats](https://www.llama.com/docs/model-cards-and-prompt-formats/llama3_2/) and the [Llama 3.2 text model card](https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/MODEL_CARD.md).

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
