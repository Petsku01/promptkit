---
category: "model-optimized"
title: "GPT-5.6 Sol: Reasoning"
subcategory: "openai"
model: "gpt-5.6-sol"
source: "promptkit-authored"
---
[← Back to Model-Optimized Openai](../index.md)

# GPT-5.6 Sol: Reasoning

## Auditable Policy Rule Resolution
```
Determine the applicable outcome for [case] under [policy corpus].

Case facts: [facts and evidence IDs]
Rules: [numbered rules, exceptions, and effective dates]
Precedence policy: [explicit override rules, if supplied]
Required output fields: [decision, applied rules, exceptions, and uncertainty]

Separate factual predicates from policy interpretation. Check whether each
relevant rule was in force at the time of the case. Apply only the supplied
precedence rules; if two equally authoritative rules conflict, report the
conflict rather than inventing an override.

Return the outcome with a compact rule-application table: rule ID, predicate,
supporting fact, and applicability. Identify the smallest missing fact that
would change the result. Provide an auditable justification, not a private
reasoning transcript or an unsupported legal conclusion.
```

## Value-of-Information Budget Choice
```
Choose which investigation to fund before [business decision].

Options: [investigations and their costs]
Decision alternatives: [actions]
Available estimates: [payoffs, probabilities, or ranges with provenance]
Budget and deadline: [limits]
Available calculator: [execution tool, if supplied]

Identify which uncertainties can actually reverse the preferred action. Compare
an investigation's cost with the improvement it could enable. Use expected
value only when defensible probabilities are supplied; otherwise present
break-even thresholds and bounded scenarios. Keep empirical estimates separate
from assumptions introduced for sensitivity analysis.

Return one recommended investigation or a justified choice to act now, the
calculation or formula supporting it, and conditions that would reverse the
recommendation. State whether numerical results were executed and checked.
Keep the explanation focused on decision value rather than exhaustive analysis.
```
