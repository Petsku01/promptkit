[← Back to Model-Optimized Anthropic](../index.md)

# Claude Opus 4.7: Reasoning

## Deep Technical Investigation
```
Investigate this technical problem thoroughly.

Context: [system/technology/domain]
Problem: [what's happening vs. what should happen]

Investigation approach:
1. State all known facts
2. Generate at least 3 hypotheses for the root cause
3. For each hypothesis, identify what evidence would confirm/deny it
4. Rank hypotheses by likelihood
5. Trace through the most likely one step by step
6. Identify the root cause with confidence level
7. Propose verification steps

Be rigorous — distinguish between what you know, what you infer, and what you assume.
```

## Architecture Decision with Trade-Off Analysis
```
I need to make an architecture decision. Think it through carefully.

Decision: [what to decide]
Context: [business/technical context, constraints]
Options: [list 2-4 options]

For each option, analyze:
- Implementation complexity (1-10)
- Operational complexity (1-10)
- Performance characteristics
- Scalability ceiling
- Failure modes
- Migration cost from current state

Then:
1. Eliminate options with fatal flaws
2. Compare remaining options on key criteria
3. Make a recommendation with confidence level
4. State what would change your mind

Use extended thinking. Show your work.
```

## Complex Bug Root Cause Analysis
```
Perform a structured RCA for this bug:

Symptom: [observable behavior]
Reproduction: [how to trigger it, if known]
Environment: [runtime, OS, versions]
Impact: [who/what is affected]

Analysis protocol:
1. Isolate the failure point (where does it first diverge from expected?)
2. Check data flow into and out of the failure point
3. Identify what changed recently (code, config, data, load)
4. Apply 5 Whys from the failure point
5. Validate the root cause against ALL known symptoms
6. Check if the root cause could explain other known issues

Root cause classification: code bug / config error / race condition / data corruption / resource exhaustion / design flaw
```

## Security Threat Assessment
```
Assess the security posture of: [system/service/API]

Scope: [what's in scope]

Threat model:
1. Identify assets (data, services, credentials)
2. Identify trust boundaries
3. Map attack surface (endpoints, inputs, privilege boundaries)
4. For each surface area, list: threat actors, attack vectors, required privileges
5. Assess existing mitigations
6. Identify gaps

Critical threats:
- [highest risk finding]

Recommendations:
- Immediate (fix now)
- Short-term (next sprint)
- Long-term (architectural)

Compliance check: [ GDPR / SOC2 / HIPAA / PCI-DSS ]
```

## Research & Evidence Synthesis
```
Synthesize evidence on: [topic/question]

Sources:
1. [source] — [key finding]
2. [source] — [key finding]
3. [source] — [key finding]

Tasks:
1. Extract core claims from each source
2. Identify areas of consensus
3. Identify contradictions — explain possible reasons
4. Evaluate source quality (methodology, sample size, recency)
5. Assess overall evidence strength
6. Present reconciled understanding with confidence levels
7. State what additional evidence would be most valuable

Flag any motivated reasoning or confirmation bias in the sources.
```

---
**Claude Opus 4.7 Reasoning Tips:**
- Use extended thinking for complex multi-step reasoning — it excels here
- Benefits from structured frameworks (5 Whys, STRIDE, SWOT)
- Takes instructions very literally — be precise about what you want
- Can handle very long reasoning chains without losing context
- Self-verifies before responding — ask it to double-check its work
- Distinguishes carefully between knowledge, inference, and assumption
- Ask for confidence levels explicitly — it will calibrate well