---
category: "model-optimized"
title: "Qwen 3.5: JSON Output"
subcategory: "qwen"
model: "qwen-3.5"
source: "promptkit-authored"
---
# Qwen 3.5: JSON Output

## When to Use

Use this template when a Qwen3.5-4B or Qwen3.5-9B server must return **only** JSON that matches a schema you supply. The model card’s own benchmarking note for multiple-choice is to standardize with a JSON `answer` field—this file generalizes that idea to extraction and classification, without copying vendor scores. Thinking is on by default and will wrap the reply in `<think>` unless you switch to instruct/non-thinking mode in the client; for JSON jobs, disable thinking so the first bytes of the assistant message can be `{` or `[`.

Keep the schema shallow. 4B/9B can follow a short object; they are not a guarantee of nested JSON Schema Draft 2020-12 compliance. If the runtime exposes structured-output / grammar sampling, enable it in the client and still keep this prompt as the semantic contract. Prefer [basic](basic.md) for a one-word label and [coding](coding.md) for code.

## The Prompt

```
Return JSON only. No markdown fence, no commentary, no <think> block
in the visible answer (disable thinking in the client).

Schema (authoritative):
[object or array shape with types and required keys]

Closed enums (optional):
[field: allowed values]

Input:
[text, and/or attached image]

Rules:
- Emit one JSON value that validates against the schema.
- Use null for missing optional fields. Do not omit required keys.
- Do not invent keys. Do not add trailing commentary.
- Numbers must be JSON numbers, not strings, unless the schema says
  string.
- If the input cannot fill a required field without guessing, emit
  {"status":"insufficient","missing":["field",...],"reason":"..."}
  instead of a fake object.
- If an image is required by the schema and none is attached, use the
  insufficient object. Do not describe imaginary pixels.

Stop after the JSON value.
```

## How It Works

The retired stub showed five tiny examples and a “max 3–5 fields” footnote aimed at a fictional SLM lineup. Official Qwen3.5 cards are multimodal thinkers; the failure mode that still matters is **thinking traces and fences breaking parsers**. The prompt therefore (1) demands thinking off in the client, (2) forbids fences, (3) gives an insufficiency object so the model has a legal alternative to fabrication. Enums belong in the prompt because 4B/9B will otherwise free-type synonyms. Required keys versus optional-null is the other parser break: models like to drop empty fields. Numbers as JSON numbers matches the card’s “standardize output format” advice for benchmarks, applied here to extraction. Structured decoding, if present, is a server feature; this text cannot enable it. If thinking cannot be disabled, strip through `</think>` before `json.loads`. Do not cite IFEval numbers from the card as a JSON success rate.

## Stop rules

Stop at the first JSON value. If thinking leaked into the stream, strip it before parse; do not ask the caller to accept a fence. Do not widen the schema with extra keys “for convenience.” Do not treat vision as a license to invent pixels. Instruct/non-thinking mode is the pairing for this file; leave thinking on only when the card’s math-boxed format is the job, which it is not here. 262K context does not mean dump a whole corpus into one extract.

## Variables

- `[object or array shape with types and required keys]`: schema.
- `[field: allowed values]`: enums, or omit.
- `[text, and/or attached image]`: source.

## Related

[basic](basic.md), [coding](coding.md). Qwen3 multilingual: `../qwen-3/multilingual.md`. Champion: `../qwen3.8-2.4t-a95b/`.

Grounded 2026-11-02 against [Qwen3.5-4B](https://huggingface.co/Qwen/Qwen3.5-4B) best-practice item 3 (standardize output; JSON `answer` field for MCQ) and the thinking-default note. Not a live parser eval.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
