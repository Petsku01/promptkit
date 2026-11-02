---
category: "model-optimized"
title: "GPT-5.6 Sol: Analysis"
subcategory: "openai"
model: "gpt-5.6-sol"
source: "promptkit-authored"
---
[← Back to Model-Optimized Openai](../index.md)

# GPT-5.6 Sol: Analysis

## Structured Professional Evidence Extraction
```
Extract decision-relevant obligations from [business document collection].

Documents: [attach contracts, policy text, and scanned pages]
Extraction schema: [field names, types, and nullable fields]
Scope: [entities, jurisdictions, and effective dates]
Evidence locator format: [document ID plus section or page]

For each obligation identify the responsible party, triggering event, deadline,
exception, and consequence. Preserve exact amounts and date expressions before
normalizing them. Treat scanned-page readings as uncertain if text is unclear.
Do not infer a missing obligation from industry custom or fill missing fields
with plausible values. Use null and a short explanation where the schema allows.

Return records matching the caller's configured output schema. Every populated
substantive field must have an evidence locator in [evidence field]. List
conflicting clauses separately instead of merging them into a synthetic rule.
Conclude with only the unresolved issues permitted by the schema.
```

## Spreadsheet-to-Report Reconciliation
```
Reconcile [management report] with [underlying data exports].

Report and tables: [attach files or paste named tables]
Metric dictionary: [metric definitions, currencies, and time periods]
Tolerances: [rounding and materiality thresholds]
Available computation tool: [code interpreter or equivalent, if supplied]

Trace each headline metric to its source rows. Check duplicate records, excluded
categories, period boundaries, and currency conversions before comparing totals.
Run reproducible calculations with an available tool and retain the formulas or
code. If execution is unavailable, provide the reconciliation procedure and
mark totals unverified. Never imply that reading a chart is a recalculation.

Output a reconciliation table containing reported value, recomputed value,
variance, tolerance, and source. Explain only material variances and recommend
the smallest data correction or definition clarification for each one.
```

## Tested On

| Model | Status | Notes |
|-------|--------|-------|
| glm-5.3-flash | Smoke 2026-11-02 | PARTIAL: incomplete or off-spec |
| deepseek-v4.1-flash:1017 | Smoke 2026-11-02 | PARTIAL: refusal |
