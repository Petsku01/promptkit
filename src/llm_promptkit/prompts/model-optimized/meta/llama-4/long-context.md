# Llama 4: Long Context (10M Tokens)

## Full-Codebase Understanding
```
I'm providing my entire codebase. Analyze it holistically.

[paste all source files — 10M context can hold large codebases]

Questions:
1. [what you need to understand]
2. [question 2]
3. [question 3]

For each answer, cite specific files and line numbers.
```

## Long-Document Deep Dive
```
Read this entire document carefully and answer my questions.

[paste full document]

Questions:
1. [question about specific detail]
2. [question about overall theme]
3. [question about something near the end]

Important: Pay attention to details throughout — don't just focus on the beginning.
```

## Multi-Source Research
```
I'm providing multiple research sources. Synthesize them.

Source 1: [paste document]
Source 2: [paste document]
Source 3: [paste document]
...

Research question: [what I'm investigating]

Tasks:
1. Extract key claims from each source
2. Identify areas of consensus
3. Flag contradictions — explain possible reasons
4. Assess source reliability where possible
5. Synthesize a unified understanding
6. Rate overall evidence strength
```

## Massive Data Extraction
```
Extract structured information from this large dataset.

[paste data — can be very large]

Extraction schema:
{
  "field1": "type",
  "field2": "type",
  ...
}

Rules:
- Process all records, not just the first N
- Normalize values to [format]
- Mark missing fields as null
- Deduplicate

Output as [JSON / CSV / table format].
```

---

**Llama 4 Long Context Tips:**
- 10M token window — can hold entire codebases, book-length documents, or massive datasets
- Llama 4's MoE architecture means only relevant experts activate per token, keeping inference efficient
- Place your instructions at both the beginning AND end of long prompts for best results
- For retrieval tasks, explicitly say "search the entire document" to prevent lazy reading
- Scout variant is cheaper for long-context work that doesn't need top-tier reasoning
- Maverick variant gives best results for complex reasoning over long contexts