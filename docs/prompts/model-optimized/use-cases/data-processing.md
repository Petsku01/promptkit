[← Back to Model-Optimized Use-Cases](../index.md)

# Use Case: Data Processing

## Data Extraction

```
Extract structured data from this text:

Text:
[unstructured text]

Extract into:
{
  "field1": "",
  "field2": "",
  "field3": []
}

Rules:
- Use null for missing fields
- Normalize dates to YYYY-MM-DD
- Normalize phone numbers to +X-XXX-XXX-XXXX
- Extract all mentions if multiple
```

## Data Cleaning

```
Clean this data:

Raw data:
[messy data]

Cleaning tasks:
□ Standardize formatting
□ Fix typos/OCR errors
□ Remove duplicates
□ Fill obvious missing values
□ Flag anomalies

Output cleaned data + list of changes made.
```

## Data Transformation

```
Transform data from format A to format B:

Input format:
[describe or show input format]

Input data:
[data to transform]

Output format:
[describe or show desired format]

Rules:
- [any transformation rules]

Output:
```

## Entity Matching

```
Match entities across datasets:

Dataset A:
[entries from A]

Dataset B:
[entries from B]

Match criteria:
- Primary: [field(s) for exact match]
- Fuzzy: [field(s) for approximate match]
- Threshold: [minimum similarity]

Output:
| A Entry | B Entry | Match Type | Confidence |
|---------|---------|------------|------------|
```

## Data Validation

```
Validate this data:

Data:
[data to validate]

Rules:
- [validation rule 1]
- [validation rule 2]
- [validation rule 3]

Report:
| Row | Field | Issue | Suggested Fix |
|-----|-------|-------|---------------|
```

## Text Normalization

```
Normalize this text data:

Input:
[text entries]

Normalizations:
□ Lowercase
□ Remove extra whitespace
□ Expand abbreviations
□ Standardize formats (dates, numbers)
□ Remove special characters
□ Correct common misspellings

Output:
[normalized entries]

Changes made:
[list of normalizations applied]
```

## Batch Classification

```
Classify these items in batch:

Categories: [list categories]

Items:
1. [item 1]
2. [item 2]
3. [item 3]
...

Output as:
| Item # | Category | Confidence |
|--------|----------|------------|
```

## Data Summarization

```
Summarize this dataset:

Data:
[dataset or description]

Generate:
## Overview
- Total records: [count]
- Date range: [range]
- Key fields: [list]

## Statistics
| Field | Type | Stats |
|-------|------|-------|
| [field] | [type] | [min/max/avg/unique] |

## Data Quality
- Completeness: [X]%
- Issues found: [list]

## Key Insights
- [insight 1]
- [insight 2]
```
