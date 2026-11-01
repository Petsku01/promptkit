---
category: "code"
title: "Evidence-Gated PySpark Performance Review"
source: "github/awesome-copilot"
license: "MIT"
---
[← Back to Code Prompts](../index.md)

# Evidence-Gated PySpark Performance Review

**Category:** code
**Source:** Adapted from https://github.com/github/awesome-copilot/blob/1a4c3a7fc2c636ad5111a8b1b86493d5600f038e/agents/spark-performance.agent.md (MIT)

Copyright GitHub, Inc. Full permission and warranty notice: [NOTICE.md](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md#agentic-workflow-adaptations--github-mit).

## When to Use

Review the distributed execution of an existing PySpark job using code, plans, and available runtime evidence, without modifying the job or launching a benchmark.

## The Prompt

```text
Review this existing PySpark job for distributed performance and parallelism.
Job scope: [repository paths and slow transformation]
Workload scale: [data volume, partition counts, key distribution and growth]
Runtime context: [Spark/Python versions, cluster resources and relevant settings]
Available evidence: [formatted plans, Spark UI exports and observed symptoms]
Review constraints: [sensitive data rules and report destination]

1. Inspect the scoped code and identify the input, transformations, actions and
   output contract. Record Spark version, execution mode, executor resources,
   adaptive query execution settings and actual workload size when supplied.
   Do not assume petabyte data or a thousand-node cluster. Missing context is
   unknown, not permission to invent infrastructure or Spark UI statistics.
   Keep this task read-only: do not edit jobs, change cluster configuration,
   collect production records, submit actions or run performance experiments.
2. Trace lazy transformations to the actions that trigger them. Anchor each
   finding to a path and line or exact supplied expression. Inspect collect,
   toPandas, local iterators, serial loops around actions, repeated counts,
   unnecessary DataFrame-to-RDD conversions and Python worker boundaries.
   Explain whether work runs on the driver, executors or both; a Python thread
   pool on the driver does not automatically distribute work across executors.
   Do not condemn every thread pool without examining its purpose and workload.
3. Read supplied logical and physical plans. Identify exchanges, join strategies,
   predicate pushdown, partition pruning, redundant scans and wide aggregations.
   Separate plan observations from runtime bottleneck hypotheses. A shuffle is
   not automatically a defect. Request only the minimum missing evidence that
   distinguishes the leading explanations, such as stage task-duration spread,
   shuffle read/write, memory/disk spill, partition sizes or key-frequency data.
   Never report spill, skew, CPU saturation or timing as measured without evidence.
4. Prioritize Spark SQL and DataFrame-native alternatives before custom Python.
   Evaluate aggregation/window rewrites, earlier selective filters and projection,
   join ordering and partitioning against the actual data contract. Recommend
   broadcast only with bounded relation size and executor-memory justification;
   avoid universal partition-count recipes. Distinguish repartition from coalesce
   and explain the shuffle or parallelism trade-off. Consider cache reuse and
   unpersist lifetime rather than recommending caching every intermediate result.
5. If Python logic is genuinely required, compare scalar/vectorized Pandas UDFs,
   grouped applyInPandas and iterator-based mapInPandas according to output shape,
   grouping and schema requirements. Check the target Spark API rather than
   assuming availability. Explain Arrow conversion costs, null/type behavior and
   memory limits. Batch sizing does not bound an entire oversized group for a
   grouped operation. Mention supported Arrow batch controls where applicable,
   but do not promise vectorization will be faster or fix skew by itself.
6. Provide a small set of prioritized recommendation snippets, not applied edits.
   For every rewrite specify result-equivalence checks: schema, nulls, duplicate
   multiplicities, aggregation precision, ordering when contractual, empty input,
   skewed keys and boundary cases. For nondeterministic results define a valid
   comparison strategy rather than demanding accidental row order. Any later
   benchmark needs separate authorization, representative inputs and comparable
   cache, resource and concurrent-load conditions. Improvement remains unvalidated
   until both semantic tests and repeated before/after measurements support it.

Return five sections: quick verdict; line-anchored findings; prioritized options;
distributed correctness checks; validation and evidence requests. Give severity
and confidence separately for each finding. Include evidence provenance and
missing checks. If runtime evidence is absent, finish with static hypotheses and
a bounded validation plan, never a fabricated speedup or production-ready claim.
```

## How It Works

Code-to-plan tracing separates distributed anti-patterns from observed bottlenecks. This reviews an existing Spark job; it does not construct the end-to-end system covered by Data Pipeline Architecture. Recommendations remain advisory until semantic and runtime checks are authorized and executed.

## Variables

- `[repository paths and slow transformation]`: existing job and review boundary.
- `[data volume, partition counts, key distribution and growth]`: real scale, not a forced large-cluster assumption.
- `[Spark/Python versions, cluster resources and relevant settings]`: compatibility and resource context.
- `[formatted plans, Spark UI exports and observed symptoms]`: available evidence with capture conditions.
- `[sensitive data rules and report destination]`: redaction and permitted report output.

## Tested On

Not model-tested. Curated adaptation; no live model-quality evaluation is claimed.
