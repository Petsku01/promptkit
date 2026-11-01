---
category: "debug"
title: "Backend Performance Profiling Loop"
source: "promptkit-authored"
---
# Backend Performance Profiling Loop

**Category:** debug
**Source:** Original promptkit-authored workflow.

## When to Use

Investigate backend CPU, allocation, contention, or I/O bottlenecks through controlled measurement and repeatable A/B validation. Unlike frontend runtime investigation or a database-specific advisor, this workflow selects runtime-appropriate profilers and accepts an honest no-gain outcome rather than requiring an optimization patch.

## The Prompt

```text
Act as a backend performance engineer. Investigate [perf metric] for [workload]
running on [runtime]. Measure before optimizing. Your deliverable is a reproducible
performance conclusion with supporting artifacts; a code change is optional and
must survive correctness checks and a fair comparison against the baseline.

1. Define the question and permissions. Read repository instructions, service
   architecture, runtime version, deployment shape, and existing benchmarks. Specify
   the target metric, units, direction of improvement, workload boundaries, and
   acceptable regression limits for correctness, error rate, memory, and resource
   cost. Distinguish throughput from latency and service time from queueing time.
   Obtain a time or experiment budget and a minimum practically useful improvement
   before comparing candidates; if unspecified, report this decision as unresolved
   rather than inventing a business threshold. Production profiling, new tooling,
   load generation, and configuration changes require explicit authorization.

2. Make the workload repeatable. Record dataset identity or safe fixture seed,
   request mix, payload sizes, concurrency or arrival rate, dependency behavior,
   duration, warm-up, cache state, and success checks. Use representative sanitized
   traffic, never private payloads copied into public artifacts. Ensure the load
   generator is not the bottleneck and record offered versus completed work. Account
   for coordinated omission when interpreting latency from a closed-loop generator.
   Do not compare a cold candidate to a warmed baseline or change concurrency to
   obtain a favorable result. Treat synthetic microbenchmarks as limited evidence,
   not an automatic prediction of whole-service gains.

3. Capture an unmodified baseline before edits. Record revision, build flags,
   runtime and dependency versions, machine or container limits, relevant settings,
   and competing load. Run repeated trials with the same workload and keep raw
   measurements. Summarize dispersion as well as central tendency and relevant
   latency percentiles. Include errors and completed operations; a faster run that
   drops requests is not an improvement. If variance overwhelms the target effect,
   improve the experiment or return INCONCLUSIVE instead of selecting the best run.

4. Choose a profiler that matches the runtime and suspected resource. Examples:
   Go pprof CPU, heap, mutex, or block profiles; JVM JFR or an approved sampling
   profiler; Python cProfile for controlled function-level investigation or a
   version-compatible sampling profiler; Node CPU profiles and event-loop metrics;
   .NET EventPipe tooling; native CPU sampling with symbols where permitted. Verify
   the installed tool and supported flags rather than issuing guessed commands.
   Low CPU with slow requests suggests waiting: inspect traces, dependency latency,
   pool saturation, or locks instead of declaring a CPU flamegraph conclusive.
   Keep diagnostic endpoints private and bound capture duration and artifact size.

5. Capture one diagnostic view at a time under the same workload, accounting for
   profiler overhead. Keep artifact paths, sampling settings, time window, and
   symbol/build identity. Distinguish self cost from inclusive cost, allocation
   rate from retained memory, and on-CPU time from blocked wall time. Follow hot
   paths to actual source locations and callers. Check whether the hotspot repeats
   across captures and affects the requested metric. A wide frame, a tiny sample,
   or one unusual request is a hypothesis, not sufficient justification for a
   rewrite. Do not add inclusive percentages from overlapping stack frames.

6. Form one falsifiable optimization hypothesis: observed hotspot, proposed
   mechanism, smallest intervention, predicted metric change, and likely tradeoff.
   Change one independent variable at a time. Preserve public behavior, concurrency
   safety, resource cleanup, and security controls. Do not combine caching, query
   rewrites, thread-count changes, and data-structure changes in a single experiment.
   For caches, specify key correctness, invalidation, memory bounds, and cold-cache
   behavior. Run functional regression tests before benchmarking the candidate.
   Reject speedups caused by skipped validation, reduced durability, or lost work.

7. Validate A versus B using the identical workload and measurement settings.
   Alternate or randomize trial order where useful to limit drift, keep warm-up
   consistent, and preserve all valid runs. Measure final outcomes without the
   profiler as well as diagnostic captures when overhead matters. Report absolute
   values, units, variability, and computed relative change using tools. Check
   secondary metrics and profile again to test the proposed mechanism. Do not
   cherry-pick one run, silently discard outliers, or call correlation proof.

8. Stop when the agreed goal is reached, the experiment budget is exhausted,
   evidence is too noisy, the next change crosses a permission boundary, or no
   candidate demonstrates a useful gain. Revert only your rejected local changes
   and retain the evidence. Report NO MEASURABLE GAIN when supported; do not keep
   an unjustified optimization because it looks clever. An unavailable profiler
   or unrepresentative workload is a verification limitation, not a performance
   finding. Deployment and production validation are separate authorized steps.

Return the question, reproducible workload recipe, baseline table, profiler choice
and artifacts, hotspot evidence, one-variable experiment ledger, correctness checks,
A/B results, and limitations. Conclude IMPROVED, REGRESSED, NO MEASURABLE GAIN,
INCONCLUSIVE, or BLOCKED, with a retain/revert recommendation and next evidence
needed. Never invent timings, percentiles, benchmark gains, or test results.
```

## How It Works

The experiment loop separates locating a bottleneck from proving an end-to-end improvement. CPU/heap selection, self versus cumulative cost, source attribution, and re-profiling are grounded in the Go team's [Profiling Go Programs](https://go.dev/blog/pprof); its historical command examples and benchmark numbers are not treated as current universal results. Runtime alternatives and controlled A/B rules are established engineering practice. Tool-grounded inspection and verification also follow the [OpenAI GPT-4.1 prompting guide](https://cookbook.openai.com/examples/gpt4-1_prompting_guide). This workflow makes no effectiveness claim for any model.

## Variables

- `[runtime]`: language runtime, exact version, service topology, and tooling constraints.
- `[workload]`: representative dataset/request recipe, load model, and environment.
- `[perf metric]`: metric, units, target, and secondary regression constraints.

## Tested On

Not model-tested. Curated original workflow; no live model-quality evaluation is claimed.
