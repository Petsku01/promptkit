# Hallucination Reducer Pattern

## Description
This pattern reduces the likelihood of the model hallucinating facts by explicitly instructing it to only use provided information or admit when it does not know the answer.

## Usage
Add this to your prompt when accuracy is critical.

```text
Answer the question using ONLY the provided context. If the answer is not contained in the context, reply exactly with: "I cannot answer this based on the provided context." Do not guess or extrapolate.
```
