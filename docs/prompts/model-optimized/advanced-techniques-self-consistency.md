[← Back to Model-Optimized Prompts](../index.md)

# Self-Consistency

Generate multiple responses and select the most common -> more reliable result.

## Basic Self-Consistency

```
Solve this problem 3 times using different approaches:

[problem]

Approach 1: [solve]
Approach 2: [solve using different method]
Approach 3: [solve using yet another method]

Compare answers:
- If all agree: High confidence
- If 2/3 agree: Medium confidence
- If all differ: Need more analysis

Final answer: [most common answer]
```

## Code Self-Consistency

```
Implement [function] in 3 different ways:

Version 1 (iterative):
[code]

Version 2 (recursive):
[code]

Version 3 (functional):
[code]

Test all three with: [test cases]

Compare outputs:
- If all match: Implementation is likely correct
- If mismatch: Investigate the differing version
```

## Verification Self-Consistency

```
Verify this claim using multiple methods:

Claim: [claim]

Method 1 - Logic:
[logical analysis]
Verdict: [true/false]

Method 2 - Evidence:
[evidence analysis]
Verdict: [true/false]

Method 3 - Counterexample search:
[attempt to find counterexamples]
Verdict: [true/false]

Consensus: [final verdict based on majority]
```

## Self-Debate

```
Analyze this question from multiple perspectives:

Question: [question]

Perspective A (supports):
[arguments for]

Perspective B (opposes):
[arguments against]

Perspective C (nuanced):
[balanced view]

Synthesis:
[combined conclusion considering all perspectives]
```

## Confidence Calibration

```
Answer this question and rate your confidence:

[question]

My answer: [answer]

Confidence: [1-10]
Reasoning for confidence level:
- Factors increasing confidence: [list]
- Factors decreasing confidence: [list]

If confidence < 7, provide alternative answers to consider.
```
