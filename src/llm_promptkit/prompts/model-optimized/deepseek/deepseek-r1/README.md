---
category: "model-optimized"
title: "DeepSeek-R1: Guide"
subcategory: "deepseek"
model: "deepseek-r1"
source: "promptkit-authored"
---
# DeepSeek-R1: Guide

## Verified Model Profile

- Open weights: `deepseek-ai/DeepSeek-R1` (and R1-Zero / distill siblings). 671B total, 37B active, 128K context, MIT for R1 itself; distill licenses follow Qwen/Llama bases.
- Distinct prompting SKU: empty **system** prompt, all instructions in the user turn, `<think>` traces, temperature 0.5–0.7 (0.6 recommended). Force a `"<think>\n"` prefix if the model skips thinking.
- Not the 2026 hosted chat IDs. Hosted DeepSeek is `deepseek-flash` and `deepseek-v4-pro` with `reasoning_content` and tool-replay rules.

## API and Sampler Pairing

Keep system empty. Put constraints, boxed-answer rules, and stop conditions in the user message. Do not ask the model to hide think tags if the runtime still emits them. Multi-sample averaging is an eval technique, not something these templates perform.

## Prompt Files

- [Coding](coding.md): constraint-first algorithms and debug with think-then-artifact output.
- [Reasoning](reasoning.md): zero-shot math/logic with `\\boxed{}` and an insufficiency path.

Two prompt files plus this guide. Original promptkit/Petsku01 text. Vendor benchmark tables on the card are not copied as promptkit scores.

## Primary Sources

Verified 2026-11-02:

- [DeepSeek-R1 model card](https://huggingface.co/deepseek-ai/DeepSeek-R1) (usage recommendations, architecture)

These are documented characteristics, not live inference results.
