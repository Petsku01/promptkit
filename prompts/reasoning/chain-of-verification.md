# Chain of Verification Pattern

**Use case:** Self-checking output quality before finalizing

**Pattern:** Chain of Verification

---

## Quick Version (~100 tokens)

```
After generating output, verify before finalizing:

CHECK:
1. Is every claim supported by provided context?
2. Does output match required format?
3. Are there factual contradictions?

If any check fails, revise. Only finalize when all pass.
```

---

## Extended Version (~400 tokens)

```
VERIFICATION PROTOCOL:

After generating output, you MUST perform a self-check before finalizing. Do not skip this step.

VERIFICATION CHECKLIST:

Factual Claims:
□ Is every specific claim traceable to provided context?
□ Are there claims that appear invented or unsupported?
□ Are dates, numbers, and names exactly as in source material?

Format Compliance:
□ Does output match the required schema/format exactly?
□ Are all required fields present?
□ Are field types correct (string/number/boolean/array)?
□ Is there any extra preamble or markdown fencing?

Internal Consistency:
□ Are there contradictions within the output?
□ Does the conclusion logically follow from premises?
□ Are units and measurements consistent?

Quality Standards:
□ Is the tone appropriate for the audience?
□ Is length within specified bounds?
□ Is output actionable (where applicable)?

VERIFICATION RULES:

- If ANY check fails: identify the failing section, revise, and re-run checklist
- Maximum 2 revision cycles per output
- If still failing after 2 cycles: halt and report "verification_failed" in logs
- Only mark complete when ALL checks pass

EXAMPLE OUTPUT FORMAT:

```
[Final output here]

---
VERIFICATION: PASSED
All 8 checks passed on first review.
```
```

---

## Metadata

- **Author:** Based on Paxrel AI Agent Patterns (2026)
- **Tags:** verification, quality, self-check, safety
- **Models:** All
- **Version:** 1.0
