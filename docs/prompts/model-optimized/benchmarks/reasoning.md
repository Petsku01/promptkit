[← Back to Benchmarks](./index.md)

# Benchmark: Reasoning

## Model Comparison (Reasoning Tasks)

> Sources: LMSYS Arena, MMLU, GSM8K (as of early 2026)

| Model | MMLU | GSM8K | Arena ELO | CoT Benefit |
|-------|------|-------|-----------|-------------|
| **GPT-4o** | 88.7% | 95.2% | ~1280 | +5-10% |
| **Claude 3.5 Sonnet** | 88.3% | 95.0% | ~1270 | +5-10% |
| **Claude 3 Opus** | 86.8% | 95.8% | ~1250 | +5-10% |
| **Gemini 1.5 Pro** | 85.9% | 92.3% | ~1240 | +5-8% |
| **Mistral Large** | 84.0% | 91.2% | ~1200 | +5-8% |
| **Llama 3.1 405B** | 85.2% | 96.8% | ~1210 | +5-10% |
| **Llama 3.1 70B** | 82.0% | 93.0% | ~1150 | +8-12% |
| **o1-preview** | 90.8% | 94.8% | ~1300 | Built-in |
| **DeepSeek V3** | 87.1% | 91.6% | ~1220 | +5-8% |

## Prompt Impact on Reasoning

### Zero-shot vs Few-shot vs CoT

```
Task: Math word problems (GSM8K subset, n=100)

| Prompt Style | GPT-4o | Claude 3.5 | Llama 70B |
|--------------|--------|------------|-----------|
| Zero-shot | 82% | 80% | 71% |
| Few-shot (3) | 89% | 87% | 82% |
| CoT Zero-shot | 91% | 90% | 84% |
| CoT Few-shot | 95% | 94% | 91% |
```

### Best Reasoning Prompts

**For math/logic:**
```
Let's solve this step by step:
1. [force explicit steps]
2. [show work]
3. [verify answer]
```

**For complex reasoning:**
```
Think through this carefully:
- What do we know?
- What are we trying to find?
- What approach should we use?
- Execute and verify.
```

## When NOT to Use CoT

| Model Type | CoT Recommendation |
|------------|-------------------|
| o1/o3 (reasoning models) |  Built-in, don't add |
| GPT-4/Claude |  Significant benefit |
| Small models (<7B) |  Limited benefit |

## Key Findings

1. **CoT helps most on multi-step problems**
   - +10-20% on math
   - +5-10% on logic
   - ~0% on simple factual questions

2. **Few-shot > Zero-shot for consistency**
   - Format compliance improves
   - Edge case handling better

3. **Explicit verification helps**
   - "Verify your answer" catches ~5% more errors
   - "Work backwards to check" even better
