---
category: "model-optimized"
title: "Gemini 3.8 Flash: Guide"
subcategory: "google"
model: "gemini-3.8-flash"
source: "promptkit-authored"
---
# Gemini 3.8 Flash: Guide

## Verified Model Profile

- Exact stable model code: `gemini-3.8-flash`, selected as the current general-purpose Flash entry within the requested Gemini 3.x family. Google's catalog already lists Gemini 4 Argon; this folder does not imply 3.8 is the newest Gemini generation.
- Input token limit: 1,048,576. Output token limit: 65,536. Google describes this as a 1M context and 64K output model; count actual inputs and reserve the applicable output budget.
- Inputs: text, images, video, audio, and PDF. Output: text. Audio generation, image generation, and the Live API are not supported by this model.
- Vendor positioning: long-horizon software engineering, autonomous agents, and complex enterprise workflows with Flash speed and cost efficiency.
- Documented capabilities include caching, code execution, computer use, file search, function calling, Google Search grounding, Google Maps grounding, structured outputs, thinking, and URL context. The application must enable the relevant tools and supply files.

## API Controls and Prompt Pairing

Thinking levels are `low`, `medium` (default), and `high`; `minimal` returns an error. The current Interactions API example uses `generation_config.thinking_level`. Google recommends `medium` for complex code and agentic tasks and `high` for difficult reasoning. Set the value in API configuration, not by placing an apparent parameter in the prompt.

The migration guide replaces `thinking_budget` with `thinking_level`, removes deprecated sampling parameters (`temperature`, `top_p`, `top_k`), rejects prefilled model turns, and standardizes Interactions conversations on `previous_interaction_id`. For retained generateContent integrations, follow the documented function-response requirements and preserve thought signatures unchanged. Verify SDK/version compatibility before translating these controls into another API surface.

Attach original media, not only a prose description, for the incident and visual-regression prompts. Large context does not establish complete evidence coverage: ask for source locations and missing-media disclosures. Repeated work can use caller-configured caching; the prompt itself does not create a cache or managed agent.

## Prompt Files

- [Analysis](analysis.md): synchronized multimodal incident evidence and large-corpus answers.
- [Coding](coding.md): media-derived regression tests and stateful API migration.
- [Reasoning](reasoning.md): visual constraint checks and bounded tool orchestration.

The three prompt files are original promptkit/Petsku01-authored templates with bracketed placeholders. This guide is the only extra file; separate audio-generation or Live prompts would target different models and are intentionally excluded.

## Primary Sources

Verified against vendor documentation on 2026-11-01:

- [Gemini model catalog](https://ai.google.dev/gemini-api/docs/models)
- [Gemini 3.8 Flash model reference](https://ai.google.dev/gemini-api/docs/models/gemini-3.8-flash)
- [What's new and migration guidance](https://ai.google.dev/gemini-api/docs/whats-new-gemini-3.8)

These are documented capabilities, not measured promptkit inference results.
