[← Back to Model-Optimized Evaluation](../index.md)

# Evaluation: A/B Testing

## Prompt Comparison

```
Compare two prompts on the same task:

Task: [task description]

Prompt A:
[prompt A]

Prompt B:
[prompt B]

Test with inputs:
1. [input 1]
2. [input 2]
3. [input 3]

For each input, which prompt produces better output?

Results:
| Input | Winner | Margin | Reason |
|-------|--------|--------|--------|
| 1 | A/B/Tie | | |
| 2 | A/B/Tie | | |
| 3 | A/B/Tie | | |

Overall winner: [A/B]
Recommendation: [which prompt to use and why]
```

## System Prompt Comparison

```
Compare two system prompts:

System A:
[system prompt A]

System B:
[system prompt B]

Test conversation:
User: [test message 1]
User: [test message 2]
User: [edge case message]

Evaluate on:
| Criterion | System A | System B |
|-----------|----------|----------|
| Relevance | [1-10] | [1-10] |
| Helpfulness | [1-10] | [1-10] |
| Tone | [1-10] | [1-10] |
| Safety | [1-10] | [1-10] |

Better system: [A/B]
Key differences: [observations]
```

## Model Comparison

```
Compare models on same prompt:

Prompt: [prompt]

Model A ([name]):
[response A]

Model B ([name]):
[response B]

Comparison:
| Aspect | Model A | Model B |
|--------|---------|---------|
| Accuracy | | |
| Speed | | |
| Verbosity | | |
| Creativity | | |
| Following instructions | | |

Preferred: [A/B] for [use case]
```

## Temperature Comparison

```
Compare same prompt at different temperatures:

Prompt: [prompt]

Temperature 0.0 (deterministic):
[response]

Temperature 0.5 (balanced):
[response]

Temperature 1.0 (creative):
[response]

Analysis:
- Most accurate: temp [X]
- Most creative: temp [X]
- Best for this task: temp [X]

Recommendation for production: [temperature and why]
```

## Few-shot vs Zero-shot

```
Compare with and without examples:

Task: [task]

Zero-shot prompt:
[prompt without examples]

Zero-shot result:
[output]

Few-shot prompt:
[prompt with examples]

Few-shot result:
[output]

Comparison:
| Metric | Zero-shot | Few-shot |
|--------|-----------|----------|
| Accuracy | | |
| Format compliance | | |
| Consistency | | |

Improvement from few-shot: [none/minor/significant]
Worth the extra tokens? [yes/no]
```

## Iterative Improvement Test

```
Track prompt improvement across versions:

V1 prompt: [original]
V1 score: [X/10]
V1 issues: [problems found]

V2 prompt: [improved]
V2 score: [X/10]
V2 fixes: [what improved]
V2 remaining issues: [what's still wrong]

V3 prompt: [further improved]
V3 score: [X/10]

Improvement trajectory: [improving/stagnant/degrading]
Best version: [V#]
```
