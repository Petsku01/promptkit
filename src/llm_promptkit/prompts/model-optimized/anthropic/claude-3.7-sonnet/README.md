---
category: "model-optimized"
title: "Claude 3.7 Sonnet: Guide"
subcategory: "anthropic"
model: "claude-3.7-sonnet"
source: "promptkit-authored"
---
# Claude 3.7 Sonnet: Guide

## Verified Model Profile

- Historical API snapshot: `claude-3-7-sonnet-20250219`. The dotted folder name follows this repository’s Claude convention.
- Anthropic-operated platforms: **retired** 2026-02-19 (deprecated 2025-10-28). Documented replacement: `claude-sonnet-5-5`. Do not treat this folder as a live flagship.
- Distinct prompting SKU: hybrid reasoning / extended thinking with XML-structured tasks. Later Claude models use adaptive thinking and effort APIs instead of a 3.7-style “please think” user instruction.
- Inputs historically: text and images → text. Exact remaining partner/self-host limits are runtime-specific; check the serving stack rather than this guide.

## Prompt Files

- [Coding](coding.md): living XML generation, review, and debug templates (not part of this re-author pass).
- [Reasoning](reasoning.md): hybrid-reasoning plan → check → answer contract for residual 3.7 runtimes.

Replace bracketed placeholders. Prompts are original promptkit/Petsku01 templates, not vendor excerpts. This folder is two prompt files plus this guide.

## API Controls and Prompt Pairing

If a remaining 3.7 endpoint still exposes extended thinking, enable it in the request rather than only in prose. XML tags (`task`, `context`, `constraints`, `output`) remain the documented Anthropic way to keep regions distinct. Do not copy 5.x `output_config.effort` fields onto 3.7 unless the runtime documents them.

## Primary Sources

Verified 2026-11-02:

- [Model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)
- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)

Lifecycle and prompting notes are vendor documentation, not promptkit live inference.
