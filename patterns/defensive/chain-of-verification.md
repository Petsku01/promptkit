# Chain of Verification Pattern

## Description

Force the model to explicitly check its own work against specific criteria before finalizing output.

## When to use

Any output that will be used without human review, especially in pipelines where errors compound.

## When to avoid

When speed is critical and verification overhead is prohibitive.

## Template

```
[Generate your output]

VERIFICATION CHECKLIST:
1. [Criterion 1]: [Pass/Fail + evidence]
2. [Criterion 2]: [Pass/Fail + evidence]
3. [Criterion 3]: [Pass/Fail + evidence]

If any check fails: rewrite the failing section and re-run the checklist.
Only proceed when all checks pass.
```

## Example

```
Write a newsletter article about the new AI regulation.

VERIFICATION CHECKLIST:
1. Is every factual claim traceable to a source URL? (Y/N)
2. Is the article length between 150-300 words? (Current: ___)
3. Is the tone consistent with previous articles? (Y/N)
4. Does the headline contain the main keyword? (Y/N)

If any check fails: rewrite the failing section and re-run the checklist.
Only proceed when all checks pass.
```

## Tags

verification, quality-check, self-review, accuracy
