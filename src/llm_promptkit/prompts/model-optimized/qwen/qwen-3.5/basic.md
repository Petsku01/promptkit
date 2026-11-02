---
category: "model-optimized"
title: "Qwen 3.5: Basic Tasks"
subcategory: "qwen"
model: "qwen-3.5"
source: "promptkit-authored"
---
# Qwen 3.5: Basic Tasks

## When to Use

Use this template on official Qwen3.5 post-trained cards such as `Qwen/Qwen3.5-4B` and `Qwen/Qwen3.5-9B` for short classify, extract, yes/no, and summary jobs. Those cards are **causal language models with a vision encoder** (image-text-to-text), not the 0.6B–32B “tiny edge SLM” list in the retired folder README. Documented native context is **262,144** tokens, extensible toward **1,010,000** with YaRN; the card still advises keeping at least **128K** available so thinking does not collapse. Thinking is **on by default** (`<think>...</think>` before the answer); disable it in the client (`enable_thinking` / instruct mode) for these short tasks so you do not pay a reasoning trace for a label.

Do not dump vendor MMLU tables into the prompt. Do not treat 3.5 as Qwen3.8. Prefer [json-output](json-output.md) when the artifact must be schema-valid JSON, and [coding](coding.md) when the artifact is code.

## The Prompt

```
Task: [classify | extract | yes-no | summarize | language-id]
Input:
[text, or a caption plus attached image]

Allowed labels (classify only): [closed list, or "n/a"]
Fields to extract (extract only): [name: type, ...]
Summary limit: [e.g. 2 sentences, or n/a]
Image: [attached | none]. If none, do not invent pixels.

Thinking: disable thinking / use instruct mode in the client for this
short job. Do not paste a fake enable_thinking field here.

Rules:
- One task only. Do not also translate, rewrite, or advise.
- If the input is empty, off-language in a way that blocks the task,
  or the image is required and missing, reply with
  {"status":"insufficient","reason":"..."} and stop.
- For classify, pick one label from the list or "none".
- For yes-no, answer yes or no; if the question is not polar, say
  "not-yes-no".
- For language-id, return the language name only.
- Do not add a preamble or markdown fence unless asked.

Output: the artifact only, in the format implied by the task.
```

## How It Works

The retired stub was a Finnish/English pile of seven toy jobs with no insufficiency path. Qwen3.5’s real SKU is a small multimodal thinker with a large native window; this file keeps the *job* small (one classify/extract/summary) while correcting the model profile. The old folder README’s 0.6B–32B “edge SLM” list does not match `Qwen/Qwen3.5-4B` / `Qwen3.5-9B`. Instruct/non-thinking mode belongs in the server, matching the card’s “Instruct (or Non-Thinking) Mode” section; leave thinking on only when the label depends on a multi-step rule. Presence of a vision encoder does not mean every basic task has an image—the prompt makes attachment explicit so the model cannot caption a missing file. Sampling for instruct general tasks on the card is temperature 0.7 / top_p 0.8 / top_k 20; set that in the client. History should store the final answer without `<think>` blocks (card best practice 4). Stop at one artifact. Do not cite the card’s IFEval row as a classify accuracy for this prompt.

## Variables

- `[classify | extract | yes-no | summarize | language-id]`: exactly one.
- `[text, or a caption plus attached image]`: input.
- `[closed list, or "n/a"]`: labels.
- `[name: type, ...]`: extract schema.
- `[e.g. 2 sentences, or n/a]`: summary cap.
- `[attached | none]`: media honesty.

## Related

[coding](coding.md), [json-output](json-output.md). Earlier Qwen3: `../qwen-3/`. Champion: `../qwen3.8-2.4t-a95b/`.

Grounded 2026-11-02 against [Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B) and [Qwen3.5-9B](https://huggingface.co/Qwen/Qwen3.5-9B) (thinking default, 262,144 context, vision encoder). Vendor blog URL on the card: https://qwen.ai/blog?id=qwen3.5

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
