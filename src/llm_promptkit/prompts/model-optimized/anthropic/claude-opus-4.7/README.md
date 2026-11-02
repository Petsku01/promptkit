---
category: "model-optimized"
title: "Claude Opus 4.7: Guide"
subcategory: "anthropic"
model: "claude-opus-4.7"
source: "promptkit-authored"
---
# Claude Opus 4.7: Guide

## Verified Model Profile

- Exact Claude API ID: `claude-opus-4-7`. Folder name uses the repo’s dotted Opus convention.
- Status: **active legacy**, released 2026-04-16, retirement not sooner than 2026-04-16 + 1 year. Anthropic recommends considering Opus 5.5. This folder does not describe 4.7 as the newest Opus.
- Context 1M tokens, max output 128K (300K only on Batch API beta). Input: text and images. Output: text. Reliable knowledge cutoff: January 2026.
- Thinking: adaptive. Default effort: `high`. Pricing on the model page at fetch: $5 / $25 per MTok plus cache and batch rates.
- Same ID on Bedrock, Google Cloud, Microsoft Foundry, and Claude Platform on AWS (`anthropic.claude-opus-4-7` on Bedrock).

## API Controls and Prompt Pairing

Set thinking and effort in the request, not as fake fields in the user message. The templates insist on evidence ledgers, allowlists, and real command output because 4.7 follows instructions literally and will otherwise implement the first bullet only. Tools, computer use, and subagents require an actual harness.

## Prompt Files

- [Analysis](analysis.md): source-linked audits and visual inventories.
- [Coding](coding.md): bounded implementation with verification.
- [Reasoning](reasoning.md): living investigation / ADR templates.
- [Long-horizon](long-horizon.md): living multi-step feature and migration protocol.

Four prompt files plus this guide. Original promptkit/Petsku01 text.

## Primary Sources

Verified 2026-11-02:

- [Claude Opus 4.7 overview](https://platform.claude.com/docs/en/models/opus-4-7/overview)
- [Model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)
- [Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)

Specs are vendor claims, not promptkit eval scores.
