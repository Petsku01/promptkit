---
category: "debug"
title: "Evidence-Driven Frontend Runtime Performance Investigation"
source: "github/awesome-copilot"
license: "MIT"
---
# Evidence-Driven Frontend Runtime Performance Investigation

**Category:** debug
**Source:** Adapted from https://github.com/github/awesome-copilot/blob/5269f7ea2d6c3a9bfda5ed878b6726cf509121fd/agents/frontend-performance-investigator.agent.md (MIT)

Copyright GitHub, Inc. Full permission and warranty notice: [NOTICE.md](https://github.com/Petsku01/promptkit/blob/main/NOTICE.md#agentic-workflow-adaptations--github-mit).

## When to Use

Investigate slow loading, sluggish interactions or layout instability by connecting reproducible browser observations to concrete application code. This is an investigation, not a general regression-test or implementation workflow.

## The Prompt

```text
Investigate this frontend performance complaint and produce an evidence-backed
remediation plan. Do not implement application changes unless separately asked.
Application: [checkout, revision, approved URL and route]
User-visible complaint: [load, interaction or layout issue and reproduction path]
Measurement conditions: [browser, device/viewport, cache and throttling policy]
Authorization: [allowed browser actions, accounts, startup commands and budget]

1. Establish the exact route, build/revision and user journey. Determine whether
   the symptom concerns initial load, route transition, input responsiveness,
   scrolling, animation or visual stability, and whether it is local, deployed,
   device-specific or reported after a change. Identify authorized navigation and
   interaction boundaries. Do not submit forms, change account data, purchase,
   send messages or access unrelated authenticated content without permission.
   Use an approved disposable account or read-only flow where available.
2. Discover the actual browser/DevTools capabilities before designing collection.
   Inspect exposed tools and supported parameters for network, console, screenshots,
   traces and audits. Do not promise Lighthouse or trace APIs that the integration
   does not provide. Record missing capabilities and use approved manual exports
   or existing telemetry if available; otherwise mark the affected diagnosis
   limited. Playwright is only a fallback for deterministic reproduction or path
   setup, not a substitute for unavailable performance instrumentation or a reason
   to create a separate regression automation track.
3. Prepare a repeatable baseline. Record browser/version, OS/device assumptions,
   viewport, device scale, build mode, route/query parameters, authentication state
   without credentials, service-worker state, cache policy and CPU/network throttle.
   Distinguish cold navigation, warm reload and client-side transitions. Specify
   baseline and repeat counts within the budget and keep conditions comparable.
   Note extensions, background load and instrumentation overhead. Do not compare
   development-mode timings with production builds as if conditions were equal.
4. Collect the supported evidence: navigation/interaction timings, request waterfall,
   transferred and decoded sizes, cache headers, main-thread activity, screenshots
   and layout-shift attribution, plus relevant console warnings. Capture trace or
   Lighthouse evidence only if available and authorized. Link each artifact to its
   run conditions and timestamps. Redact cookies, authorization headers, tokens,
   personal information and sensitive URL/query values before saving or sharing
   artifacts. Do not upload raw traces to an external service without permission.
5. Separate laboratory observations from field Core Web Vitals. Identify whether
   LCP, CLS or responsiveness data came from this synthetic run or authorized real-
   user telemetry, with its population, observation window and aggregation method.
   Synthetic interaction latency is not field INP, and TBT is not interchangeable
   with INP. Do not infer population percentiles from a few local runs. Report
   unavailable field data plainly and avoid optimizing a score while ignoring the
   reported user journey. Repeat noisy measurements and show spread, not just the
   fastest result; preserve outliers with explanations rather than hiding them.
6. Diagnose by observed bottleneck. For slow load, distinguish server response,
   resource discovery, font/image delivery, render-blocking CSS, script execution
   and hydration delay. For interactions, examine input delay, handler work,
   synchronous state updates, layout/reflow and presentation delay. For instability,
   identify the shifted element and triggering resource or injected content.
   Inspect critical-request dependencies, duplicate fetches, compression and cache
   misses rather than calling every large asset causal. Console warnings alone
   do not establish performance impact.
7. Connect findings to observed code paths. Follow source maps when available,
   inspect the responsible route/component/handler or asset declaration, and cite
   file locations. Cross-check framework rerenders, third-party execution and
   network dependencies against the actual trace/waterfall. Label unsupported
   explanations as hypotheses and propose the smallest experiment that could
   falsify each. Reuse established optimization patterns; do not recommend broad
   rewrites or new dependencies for problems fixable with narrow changes.
8. Rank recommendations by user-visible impact, evidence confidence, effort and
   risk. For every action, state the bottleneck, artifact/run reference, responsible
   code area, mechanism, trade-off and comparable before/after validation method.
   Expected benefit is a hypothesis until measured. Do not fabricate improved
   numbers or claim a recent change caused the issue without a comparable baseline.
   Preserve application code and remote state; close only browser/server resources
   created for this investigation and report cleanup limitations.

Return problem summary, capability/conditions ledger, per-run observations, lab
versus field distinction, findings tied to code and evidence, ranked actions and
validation steps. Include exact reproduction steps, unavailable tools, failed
collection, remaining uncertainty and authorized follow-up needed. No generic
optimization checklist should be presented as a measured root-cause finding.
```

## How It Works

Controlled run conditions make comparisons meaningful. Capability discovery avoids imaginary tooling, and artifact-to-code links separate observed bottlenecks from generic performance advice.

## Variables

- `[checkout, revision, approved URL and route]`: exact application under investigation.
- `[load, interaction or layout issue and reproduction path]`: concrete symptom.
- `[browser, device/viewport, cache and throttling policy]`: comparable run conditions.
- `[allowed browser actions, accounts, startup commands and budget]`: safe interaction scope.

## Tested On

Not model-tested. Curated adaptation; no live model-quality evaluation is claimed.
