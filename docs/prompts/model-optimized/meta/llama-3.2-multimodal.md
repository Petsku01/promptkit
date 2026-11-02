---
category: "model-optimized"
title: "Llama 3.2: Multimodal"
subcategory: "meta"
model: "llama-3.2"
source: "promptkit-authored"
---
[← Back to Model-Optimized Meta](../index.md)

# Llama 3.2: Multimodal

## When to Use

Use this template with **Llama 3.2 Vision** instruct weights (**11B / 90B**): image + text in, **text out**, **128k** context, knowledge cutoff December 2023. Meta documents visual recognition, image reasoning, captioning, DocVQA-style document questions, and general questions about an image. For **image+text**, English is the only language the vision card lists as supported. Text-only turns on these weights behave like Llama 3.1 8B/70B; tool calling with **text+image together is not supported**.

The instruct template needs the special token `<|image|>` **immediately before** the text query; the image that precedes the query is the one used. A system prompt is not required when an image is present. Meta notes these vision weights are **not accessible from the EU**; check the serving stack rather than this file. Do not send this prompt to 1B/3B text models.

## The Prompt

```
<|begin_of_text|><|start_header_id|>user<|end_header_id|>

<|image|>[task: caption | VQA | DocVQA | visual reasoning]

Question or instruction (English): [instruction]
Image note: the runtime must attach the actual image bytes to the
<|image|> token. If no image is attached, reply
"insufficient: no image" and stop. Do not describe a missing picture.

Constraints:
- Report only what is visible or a clearly labeled inference.
- If text in the image is unreadable, say unreadable rather than guess.
- Structured extract (optional schema): [schema or "none"]
- Do not call tools. Vision+text tool-calling is out of scope.

Output:
1. Direct answer.
2. Evidence: visible elements you used.
3. Uncertainties: what the image does not show.

<|eot_id|><|start_header_id|>assistant<|end_header_id|>
```

## How It Works

The retired stub was four generic “describe this image” bullets with a JSON wish. The Llama 3.2 vision SKU is a late-fusion adapter on Llama 3.1: the cross-attention mask treats the image immediately before the query as the referent, so putting the question *before* `<|image|>` is a silent failure mode. Forbidding tools matches the card (vision+text tool-calling is out of scope). Splitting answer / evidence / uncertainty stops the 11B from narrating a scene that is not in the pixels. English-only for image+text is a card limit; do not ask for a Hindi caption of a photo and expect the same path as 3.2 text. EU availability is a distribution constraint, not a prompting trick. Text-only turns on 11B/90B may use 3.1-style tools; this file is the image path. Captioning, VQA, and DocVQA share this skeleton; the task tag is only for the user. Llama 4 living files cover later multimodal Meta weights.

## Stop rules

Stop if no image is attached, if `<|image|>` is not immediately before the query, or if the user asked for image+text tool calls (unsupported). Do not answer in a non-English language for image+text jobs; the vision card lists English only. Do not treat EU unavailability as a prompt flag you can override. Unreadable text in a photo is “unreadable,” not a guess. 1B/3B text weights cannot consume this template.

## Variables

- `[task: caption | VQA | DocVQA | visual reasoning]`: job.
- `[instruction]`: English question or caption request.
- `[schema or "none"]`: optional extract shape.

## Related

Text 1B/3B: [general](general.md). Llama 3.3 text: `../llama-3.3/`. Llama 4: `../llama-4/`.

Grounded 2026-11-02 against Meta’s [Llama 3.2 prompt formats](https://www.llama.com/docs/model-cards-and-prompt-formats/llama3_2/) (vision section, `<|image|>` placement, EU note) and [MODEL_CARD_VISION.md](https://github.com/meta-llama/llama-models/blob/main/models/llama3_2/MODEL_CARD_VISION.md).

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
