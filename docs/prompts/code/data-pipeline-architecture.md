---
category: "code"
title: "Incremental Data Pipeline with Replay and Quality Gates"
source: "wshobson/agents"
license: "MIT"
---
[← Back to Code Prompts](../index.md)

# Incremental Data Pipeline with Replay and Quality Gates

**Category:** code
**Source:** Adapted from https://github.com/wshobson/agents/blob/7e2fb559cf4b824b27f1fec49fe88f7511066d26/plugins/data-engineering/commands/data-pipeline.md (MIT)

Copyright (c) 2024 Seth Hobson. Full permission and warranty notice: [NOTICE.md](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md#agentic-workflow-adaptations--wshobsonagents-mit).

## When to Use

Design and implement one incremental batch or streaming pipeline, including concrete ingestion, transformation, orchestration, quality, and recovery artifacts with replay tests.

## The Prompt

```text
Build one bounded incremental pipeline from source to serving sink.
Data contract: [one source, sink, record schema and consumer requirements]
Workload: [volume, arrival pattern, latency budget and retention]
Existing stack: [repository paths, orchestrator, processing and storage tools]
Correctness policy: [identity, updates, deletes, lateness and quality thresholds]
Execution scope: [local fixtures, sandbox permissions and spending ceiling]

1. Inspect existing ingestion, transformation, scheduling and quality conventions.
   Choose either incremental batch or streaming for this use case, not a platform
   containing both by default. Trace source → ingestion → transformation → sink
   and the serving consumer. Record schema, ownership, sensitive fields, throughput,
   freshness expectations and available transactional features. If stable identity,
   deletion semantics or source consistency cannot be established, block the
   affected correctness claim rather than inventing a business rule.
2. Define the incremental cursor precisely. For batch, specify watermark column,
   stable tie-breaker, inclusive/exclusive boundaries, extraction snapshot and
   overlap window for late updates. Explain equal timestamps and updates arriving
   behind the watermark. For streaming, specify partition offsets, event time,
   ordering assumptions and lateness policy. Persist progress only after the
   corresponding sink work is durably accepted; describe restart behavior from
   the last valid checkpoint and the limits imposed by source retention.
3. Specify idempotency and deduplication before selecting append or merge. Define
   event identity separately from entity identity, key scope, duplicate retention
   horizon, update ordering and conflict resolution. State whether repeated events
   are ignored, replace prior values or represent distinct facts. Handle tombstones
   and concurrent runs explicitly. A plain append followed by offset commits can
   duplicate data after a crash. Kafka offset commits alone do not provide
   end-to-end exactly-once delivery, especially to an external sink. Identify the
   actual transaction boundary or implement at-least-once with tested idempotent
   writes and state the remaining failure windows.
4. Implement schema validation at ingestion and record source metadata, batch/event
   identifiers and extraction time without leaking sensitive payloads into logs.
   Quarantine invalid records with a reason and replayable reference. Define whether
   quarantine permits progress, blocks the batch or requires an approved threshold.
   Plan schema evolution: additive nullable fields, missing fields, renamed fields,
   type widening and incompatible changes. Version transformations and validate
   old/new records against their supported schemas. Do not silently coerce unknown
   types or drop columns to make quality tests pass.
5. Implement the smallest complete ingestion, transformation and orchestration path
   using real installed libraries. If choosing dbt, supply actual model SQL and
   schema tests; if using a processing job, supply its runnable entry point and
   schema definitions. Provide bounded retries with backoff, non-retryable failure
   classification, concurrency controls and timeouts. Avoid imaginary helper imports.
   Choose storage layout from observed access patterns and representative measurements,
   not universal partition/file-size thresholds. No vacuum, destructive retention
   change, paid deployment or production cleanup without separate authorization.
6. Test the real path on deterministic synthetic fixtures. Include initial load,
   empty increment, repeated replay, duplicate delivery, equal cursor values,
   late updates, deletes and schema changes. Inject failure before sink write,
   after sink commit but before checkpoint, and during retry. Restart and compare
   final records and progress with the expected oracle: keys, values, duplicate
   multiplicities and aggregates, not row count alone. Exercise concurrent-run
   exclusion and quarantine recovery. Verify retry exhaustion preserves recoverable
   evidence and does not advance progress past unprocessed data.
7. Instrument accepted/rejected/duplicate counts, lag, freshness, retries and checkpoint
   age with batch or correlation identifiers. Set alert thresholds from the agreed
   workload and quality contract. Report measured resource use only for the tested
   environment; do not guarantee cost savings, throughput or universal quality scores.
   Distinguish local fixture evidence from any unverified cloud or production path.

Deliver concrete repository-relative files: a pipeline design note with data flow
and transaction boundaries; ingestion entry point; transformation model/job;
orchestration definition; schema and quality configuration; replay/failure tests
and fixtures; environment example without secrets; and an operations runbook with
checkpoint inspection, bounded replay and quarantine recovery. Map each role to an
actual path, list executed commands/results, and mark remaining blockers explicitly.
```

## How It Works

One source-to-sink slice keeps architecture decisions tied to executable files. Replay and crash-window tests establish delivery semantics rather than relying on an orchestrator's retry setting. This constructs an incremental pipeline; PySpark Performance Review instead examines an existing job's distributed execution.

## Variables

- `[one source, sink, record schema and consumer requirements]`: data and serving contract.
- `[volume, arrival pattern, latency budget and retention]`: sizing and recovery bounds.
- `[repository paths, orchestrator, processing and storage tools]`: existing implementation context.
- `[identity, updates, deletes, lateness and quality thresholds]`: explicit correctness semantics.
- `[local fixtures, sandbox permissions and spending ceiling]`: execution authorization.

## Tested On

Not model-tested. Curated adaptation; no live model-quality evaluation is claimed.
