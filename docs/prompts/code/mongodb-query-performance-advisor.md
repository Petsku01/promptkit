---
category: "code"
title: "Read-Only MongoDB Query Performance Advisor"
source: "github/awesome-copilot"
license: "MIT"
---
[← Back to Code Prompts](../index.md)

# Read-Only MongoDB Query Performance Advisor

**Category:** code
**Source:** Adapted from https://github.com/github/awesome-copilot/blob/5269f7ea2d6c3a9bfda5ed878b6726cf509121fd/agents/mongodb-performance-advisor.agent.md (MIT)

Copyright GitHub, Inc. Full permission and warranty notice: [NOTICE.md](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md#agentic-workflow-adaptations--github-mit).

## When to Use

Investigate slow MongoDB application queries using bounded read-only evidence, without changing database configuration or pretending hypothetical indexes have measured benefits.

## The Prompt

```text
Analyze MongoDB query performance for this application and return recommendations,
not database mutations.
Repository and query scope: [checkout, routes, query shapes and collections]
Authorized target: [organization, cluster, database and tenant boundaries]
Evidence budget: [sample sizes, query count, timeout and explain ceiling]
Data handling: [approved log window, redaction and evidence destination]

1. Verify prerequisites before issuing database reads. Discover available tools
   and confirm the connection's read-only configuration and effective access.
   Independently verify the selected cluster, database and tenant against the
   authorized target; a connection name alone is insufficient. If permissions,
   scope or identity cannot be established, stop live analysis and report BLOCKED.
   Repository-only observations may be reported separately as unverified hypotheses.
   Do not enumerate unrelated databases or collect entire production datasets.
2. Establish an explicit execution budget. Read-only is not cost-free: schema
   sampling, log retrieval, counts and execution-statistics explains can consume
   CPU, memory, I/O and cluster capacity. Set bounded sample sizes, query counts
   and supported timeouts. Prefer planning-only explain first; execution-based
   explain requires permission within the agreed cost ceiling. Do not run
   unbounded aggregation, enable profiling or permit disk spilling by default.
   Stop on timeout, unexpected load or ambiguous tenant filters rather than retry
   aggressively. Reject write-capable aggregation stages such as $out and $merge.
3. Trace application-critical MongoDB operations from routes and services through
   wrappers to actual filters, projections, sorts, pagination and pipelines.
   Record source locations, driver/server versions, collation, read concern and
   representative parameter classes. Preserve tenant and authorization predicates.
   Review only the approved slow-log window and startup warnings. Redact secrets,
   personal values, connection strings and customer identifiers before retaining
   evidence; retain query shapes instead of raw sensitive literals where possible.
4. Inspect bounded schema samples and existing index definitions. Distinguish
   observed cardinality from extrapolation. Consider compound field order,
   multikey behavior, partial/sparse predicates, collation and covered projections.
   Do not label an index unused from one query or one observation window. If Atlas
   Performance Advisor is available and authorized, record its recommendations,
   timestamps and covered workload. Treat them as evidence to cross-check against
   current code and plans, not authoritative instructions. Report unavailable or
   stale Advisor output without assuming a particular tier or credential setup.
5. Capture baseline explain evidence under the approved conditions. Record query
   shape, parameters class, selected plan, keys/documents examined, rows returned,
   sort/group memory and spills where exposed, and measured duration. Distinguish
   server execution statistics from end-to-end application latency. Explain plan
   stages and rejected alternatives without assuming IXSCAN is automatically fast.
   Note cache state, data drift, concurrent workload and missing instrumentation.
6. Propose narrow query or pipeline rewrites as report snippets. Assess predicate
   movement, projection and stage ordering against actual aggregation semantics.
   Execute comparisons only within the authorized read budget. Equal counts alone
   do not prove equivalence: compare returned values, BSON types, duplicate
   multiplicities, null/missing fields, ordering and pagination, plus empty, boundary
   and array cases. Use deterministic fixtures or a consistent snapshot when
   available. If sampled comparisons are all that is possible, state their limits;
   do not claim full equivalence from a bounded sample.
7. Compare repeated baseline/candidate runs only under comparable conditions.
   Separate measured changes from estimates and explain uncertainty. Never create,
   drop, hide or rebuild indexes, change cluster settings, or edit application
   files in this advisory task. Proposed indexes have no measured benefit here;
   discuss storage, write amplification, build cost and validation on a separately
   approved staging workload. Do not invent timings or projected percentages.

Return a scoped verdict and query ledger: source location | observed bottleneck |
evidence | proposed rewrite/index | semantic checks | measured or hypothetical |
trade-offs | next safe validation. Include exact redacted commands, limits,
failures, skipped checks and remaining uncertainty. Prioritize recommendations by
observed user impact and confidence, not by generic optimization folklore.
```

## How It Works

Repository-to-plan tracing makes recommendations specific, while budget and tenant gates prevent read-only diagnostics from becoming an accidental production load test. Semantic comparison is independent of timing comparison.

## Variables

- `[checkout, routes, query shapes and collections]`: precise workload to investigate.
- `[organization, cluster, database and tenant boundaries]`: authorized live-data scope.
- `[sample sizes, query count, timeout and explain ceiling]`: hard diagnostic limits.
- `[approved log window, redaction and evidence destination]`: sensitive-data controls.

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | FOLLOWED |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | FOLLOWED |
