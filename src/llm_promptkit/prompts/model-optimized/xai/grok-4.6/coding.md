---
category: "model-optimized"
title: "Grok 4.6: Coding"
subcategory: "xai"
model: "grok-4.6"
source: "promptkit-authored"
---
# Grok 4.6: Coding

## Harden a Search-Backed Agent
```
Implement [feature] in this application that uses Grok 4.6 and external search.

Repository: [path and stack]
Current model requests and tool wiring: [code]
Allowed data sources: [domains, accounts, and date restrictions]
Output schema: [claim, evidence URLs, timestamps, and confidence fields]
Safe test environment: [fixtures, mocked search, and commands]

Inspect how the application enables tools; a model ID alone does not provide
real-time data. Make search capabilities explicit and ensure unavailable search
produces an honest unsupported-current-facts result rather than a fabricated
citation. Validate function arguments and structured output at the boundary.

Add tests for a stale article, a repost mistaken for independent corroboration,
a hostile instruction embedded in retrieved text, and a search-service error.
Keep source content out of privileged instructions. Mock external side effects
and do not post to X or deploy without separate authorization.

Execute the tests if tools are available. Report changed files, the exact checks
and outcomes, and any live integration check still needed. Documentation may
be conversational; errors and factual output must remain precise.
```

## Long-Context Failure-Path Review
```
Review [service] for failures hidden across its call graph.

Evidence bundle: [source files, configuration, logs, and UI screenshots]
Entrypoints: [requests or jobs]
Critical invariants: [data consistency and authorization rules]
Execution tools: [available test runner and shell, or none]

Trace each entrypoint through retries, cancellation, and partial completion.
Use screenshots as observed symptoms rather than proof of internal state.
Compare logs with code versions before attributing a failure to the current
implementation. Retrieve missing call sites when tools permit; label gaps.

Produce candidate defects with an input sequence, affected invariant, file
locations, and a reproducible check. Test the highest-impact candidates when
execution is available. Keep confirmed defects separate from conjectures and
propose minimal fixes rather than an unrequested rewrite of the service.
```

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | PARTIAL: empty after thinking |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
