# Llama 3.2 Prompting Guide

## Model Characteristics

Llama 3.2 is a family, not one interchangeable endpoint: 1B and 3B are text models; 11B and 90B are vision models. Standard cards describe 128K context, but the quantized instruct variants documented by Meta have an **8K** window. Check the exact checkpoint and serving configuration before allocating input and output. These older-family templates are not specifications for Llama 4.

## Vision Models (11B, 90B)

Use [multimodal.md](multimodal.md) for image-grounded tasks. Meta's documented image marker is `<|image|>`, placed immediately before the query; an XML-style image wrapper is not the native format. Attach the actual image through the serving interface rather than inserting a textual claim that an image exists. The client should apply the correct chat template once.

Meta's documented restrictions include unavailable vision access from the EU and no supported tool calling with text and image together. Verify the deployment's availability instead of promising a multimodal tool loop.

## Text Models (1B, 3B)

Use [general.md](general.md) for bounded text tasks with a clear output contract. These variants do not support the builtin Brave Search or Wolfram integrations. Custom tool definitions may appear in the system or user message, but execution still requires a real harness.

## Visual Analysis

Separate visible observations from inferences, quote image text only when legible, and stop when the required attachment is missing. Do not request a fabricated private reasoning transcript.

## Key Tips

Keep one task and one artifact per request. Validate output and report tools or tests actually used. The re-authored prompts remain not model-tested; no accuracy claim is implied.

## Primary Sources

Audit-verified 2026-11-02: [Meta's Llama 3.2 prompt formats](https://www.llama.com/docs/model-cards-and-prompt-formats/llama3_2/).
