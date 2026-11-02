---
category: "model-optimized"
title: "Grok 4.6: Reasoning"
subcategory: "xai"
model: "grok-4.6"
source: "promptkit-authored"
---
# Grok 4.6: Reasoning

## Adversarial Claim Testing
```
Evaluate the strongest defensible version of [controversial or uncertain claim].

Claim and scope: [precise proposition and applicable population]
Evidence: [sources and dates]
Enabled retrieval: [search tools, if any]
Decision threshold: [what would count as sufficient support]

Translate vague wording into a testable proposition without changing its
meaning. Identify the strongest supporting evidence and the strongest credible
counterevidence. For time-sensitive premises, use enabled search or explicitly
mark them unverified. Do not manufacture symmetry when the evidence is uneven.

Ask which observation would most clearly distinguish competing explanations.
Check base rates, selection effects, and alternative causes where relevant.
Return a calibrated verdict, decisive evidence links, the most important
remaining uncertainty, and a falsification test. Provide a compact rationale
rather than a hidden reasoning trace. Wit is optional; accuracy is not.
```

## Quantitative Counterexample Search
```
Test the conjecture [mathematical or algorithmic claim].

Definitions and domain: [precise definitions and bounds]
Known examples: [examples with provenance]
Available computation: [code execution tool, if supplied]
Desired deliverable: [proof, counterexample, or bounded empirical result]

Check the domain boundaries and degenerate cases before generalizing. If a
computation tool is available, search a well-defined finite region and record
the algorithm, bounds, and actual result. A finite search without a counterexample
is not a proof over an unbounded domain. If execution is unavailable, supply
reproducible search code and label it unexecuted.

Return a verified counterexample or a concise proof with explicit assumptions.
If neither is established, report the exact bounded result and remaining gap.
Independently check any proposed counterexample against the original definition,
not a simplified substitute. Keep the final mathematical exposition direct.
```

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
