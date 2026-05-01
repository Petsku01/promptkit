[← Back to Model-Optimized Google](../index.md)

# Gemini 2.5 Flash: Long Context

## Document Q&A
```
Answer based on the documents below.

[documents]

---

Question: [question]
Answer with source references:
```

## Multi-Document Summary
```
Summarize key points from all documents:

Document 1:
[content]

Document 2:
[content]

Document 3:
[content]

Summary:
1. Key themes
2. Important findings
3. Contradictions (if any)
```

## Batch Document Processing
```
Process each document and extract:

1. Summary (one sentence)
2. Key entities
3. Sentiment

[b Documents pasted inline — Flash can handle many in 1M context]

Results:
```

## Meeting Transcript
```
Analyze this meeting transcript:

[transcript]

Extract:
1. Decisions made
2. Action items (with owners)
3. Key discussion points
4. Unresolved issues
```

## Code Repository Scan
```
Analyze this codebase:

[paste multiple files]

Questions:
1. What does this project do?
2. Key components?
3. Potential issues?
```

## Long Document Search
```
In the document below, find all mentions of [topic/term].

[long document]

List each occurrence with:
- Location (section/page)
- Context (surrounding sentence)
- Type (reference/definition/usage)
```

---

**Gemini 2.5 Flash Long Context Tips:**
- 1M token context — pack multiple documents into a single call
- Great for batch processing: classify/extract from many items at once
- Separate documents with clear delimiters (---, Document N:)
- For Q&A, ask Flash to reference where it found the answer
- Flash retrieves well from long context, but keep reasoning instructions simple