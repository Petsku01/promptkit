# Self-Evaluation Loop

**Use case:** Quality assurance for generated content

**Pattern:** Self-Evaluation Loop

---

## Quick Version (~100 tokens)

```
SELF-EVALUATION:

After writing, score your output 1-5 on:
- Clarity: Easy to understand?
- Accuracy: Factually correct?
- Completeness: Covers requirements?

Average < 3.0: Rewrite once, re-score
Average >= 3.0: Finalize
```

---

## Extended Version (~450 tokens)

```
SELF-EVALUATION PROTOCOL:

Quality matters. Evaluate your output before finalizing.

EVALUATION RUBRIC:

Rate each criterion 1-5. Be honest — inflated scores hurt quality.

CLARITY (1-5):
1 = Confusing, unclear structure
3 = Understandable but requires effort
5 = Crystal clear, immediate comprehension

ACCURACY (1-5):
1 = Contains factual errors or unsupported claims
3 = Mostly correct, minor inaccuracies
5 = Every claim verifiable and correct

COMPLETENESS (1-5):
1 = Missing major requirements
3 = Covers basics, misses nuances
5 = Thorough, addresses all requirements plus edge cases

RELEVANCE (1-5):
1 = Off-topic or tangential
3 = Related but not focused
5 = Precisely addresses the prompt

TONE (1-5):
1 = Inappropriate for audience
3 = Acceptable but inconsistent
5 = Perfect match for intended audience

ACTIONABILITY (1-5, where applicable):
1 = No practical value
3 = Somewhat useful
5 = Immediately actionable

SCORING RULES:

Calculate average across all applicable criteria.

Average 4.0+: Publish as-is
Average 3.0-3.9: Rewrite weakest criterion, re-evaluate once
Average below 3.0: Discard, log "quality_fail", try different approach

MAXIMUM REWRITES: 2
If still below 3.0 after 2 attempts, the content is not salvageable.

EVALUATION OUTPUT FORMAT:

```
[Your generated content here]

---
EVALUATION:
Clarity: 4/5
Accuracy: 5/5
Completeness: 4/5
Relevance: 5/5
Tone: 3/5
Average: 4.2/5
Decision: PUBLISH_AS_IS
```

WHY SPECIFIC CRITERIA:

Without specific criteria, LLMs rate their own output 5/5 by default. This is not arrogance — it's the "sounds plausible" effect. Specific criteria break this bias by forcing attention to concrete quality dimensions.

HONESTY ENFORCEMENT:

If tempted to inflate scores:
- Remember: Low score now prevents embarrassment later
- Real users will see the actual quality
- Better to skip than publish mediocre content
```

---

## Metadata

- **Author:** Based on Paxrel AI Agent Patterns (2026)
- **Tags:** quality, evaluation, self-review, assurance
- **Models:** All
- **Version:** 1.0
