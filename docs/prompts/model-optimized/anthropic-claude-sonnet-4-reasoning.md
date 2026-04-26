[← Back to Model-Optimized Prompts](../index.md)

# Claude Sonnet 4: Reasoning

## Analysis Task
```xml
<task>
Analyze [topic/data/situation].
</task>

<context>
[relevant background]
</context>

<output>
Provide:
1. Key observations
2. Insights
3. Recommendations
</output>
```

## Problem Solving
```xml
<problem>
[describe the problem]
</problem>

<constraints>
[list constraints]
</constraints>

Think through this step by step:
1. Understand the core issue
2. Identify possible solutions
3. Evaluate tradeoffs
4. Recommend best approach
```

## Comparison
```xml
<items_to_compare>
A: [description]
B: [description]
</items_to_compare>

<criteria>
- [criterion 1]
- [criterion 2]
- [criterion 3]
</criteria>

Compare and recommend which is better for [use case].
```

## Summarization
```xml
<content>
[paste content to summarize]
</content>

<requirements>
- Length: [word count]
- Focus: [specific aspects]
- Audience: [who will read this]
</requirements>
```

---
**Claude Sonnet 4 Reasoning Tips:**
- Good for structured analysis tasks
- Fast enough for interactive use
- Use XML for complex multi-part requests
- Balances depth with speed
