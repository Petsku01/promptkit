[← Back to Evaluation](./index.md)

# Evaluation: Quality Metrics

## BLEU-style Evaluation

```
Compare generated text to reference:

Reference (ground truth):
[reference text]

Generated:
[generated text]

Evaluate:
- Key phrases present: [X/Y]
- Meaning preserved: [yes/partial/no]
- Fluency: [natural/awkward/broken]
- Extra info: [none/helpful/irrelevant]

Quality score: [0-100]
```

## Task-Specific Metrics

### Code Quality

```
Evaluate this code:

[code]

Metrics:
- Correctness: Does it work? [yes/no/partially]
- Efficiency: Time/space complexity [good/acceptable/poor]
- Readability: Easy to understand? [1-5]
- Best practices: Follows conventions? [1-5]
- Documentation: Well documented? [1-5]

Overall code quality: [1-10]
```

### Summarization Quality

```
Evaluate this summary:

Original (length: X words):
[original]

Summary (length: Y words):
[summary]

Metrics:
- Compression: [Y/X ratio]
- Key points retained: [X/Y points]
- Accuracy: No false information? [yes/no]
- Coherence: Flows well? [1-5]
- Standalone: Understandable without original? [1-5]

Summary quality: [1-10]
```

### Translation Quality

```
Evaluate this translation:

Source ([language]):
[source text]

Translation ([language]):
[translation]

Metrics:
- Meaning preserved: [fully/mostly/partially/no]
- Grammar: [correct/minor errors/major errors]
- Fluency: [native-like/acceptable/awkward]
- Terminology: [accurate/close/wrong]
- Style: [matches/close/different]

Translation quality: [1-10]
```

### QA Quality

```
Evaluate this Q&A:

Question: [question]
Expected answer: [ground truth if available]
Actual answer: [generated answer]

Metrics:
- Correct answer: [yes/partial/no]
- Complete answer: [yes/partial/no]
- Concise: [appropriate length/too long/too short]
- Well-structured: [yes/no]

QA quality: [1-10]
```

## Consistency Check

```
Check response consistency across variations:

Original prompt: [prompt]
Response 1: [response]

Rephrased prompt: [rephrased]
Response 2: [response]

Consistency analysis:
- Core answer same? [yes/no]
- Facts consistent? [yes/no]
- Contradictions? [none/minor/major]

Consistency score: [1-10]
```

## Coherence Evaluation

```
Evaluate text coherence:

[text]

Check:
- Logical flow: [smooth/choppy/confused]
- Transitions: [present/weak/missing]
- Topic consistency: [focused/wandering]
- No contradictions: [yes/no]

Coherence score: [1-10]
Problem areas: [list if any]
```
