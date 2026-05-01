[← Back to Model-Optimized Anthropic](../index.md)

# Claude Sonnet: Analysis

## Chain of Thought (XML)

```xml
<task>
Solve this problem systematically.
</task>

<process>
1. Understand what is being asked
2. Identify key information
3. Plan your approach
4. Execute step by step
5. Verify your solution
</process>

<output_format>
<thinking>
[Your step-by-step reasoning]
</thinking>

<answer>
[Your final answer]
</answer>
</output_format>
```

## Document Analysis

```xml
<task>
Analyze the following document thoroughly.
</task>

<analysis_sections>
1. **Summary**: 3-5 sentence overview
2. **Key Points**: Bullet list of main ideas
3. **Entities**: People, organizations, dates mentioned
4. **Sentiment**: Overall tone and attitude
5. **Action Items**: Any tasks or next steps implied
6. **Questions**: Unclear points needing clarification
</analysis_sections>

<document>
[paste document here]
</document>
```

## Decision Analysis

```xml
<task>
Help me decide between these options.
</task>

<options>
1. [Option A]
2. [Option B]
</options>

<context>
[Relevant background information]
</context>

<analysis_format>
For each option:
- Pros (at least 3)
- Cons (at least 3)
- Risks
- Long-term implications

Then:
- Comparison matrix
- Clear recommendation
- Reasoning
</analysis_format>
```

## Research Summary

```xml
<task>
Summarize and synthesize these sources on [topic].
</task>

<sources>
[paste sources]
</sources>

<output>
1. Key findings across sources
2. Points of agreement
3. Points of disagreement
4. Gaps in the research
5. Recommendations
</output>
```
