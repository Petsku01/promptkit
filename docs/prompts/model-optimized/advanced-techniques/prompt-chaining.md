[← Back to Model-Optimized Advanced-Techniques](../index.md)

# Prompt Chaining

Split complex task into chained prompts.

## Basic Chain

```
# Prompt 1: Research
Research [topic]. List 5 key facts.

# Prompt 2: Organize
Take these facts and organize them into an outline.

# Prompt 3: Write
Using this outline, write a [document type].

# Prompt 4: Review
Review and improve the draft.
```

## Analysis -> Synthesis Chain

```
# Step 1: Extract
Extract all key data points from: [document]
Format as bullet points.

# Step 2: Categorize  
Categorize these data points into themes:
[paste step 1 output]

# Step 3: Analyze
Identify patterns and insights from these categories:
[paste step 2 output]

# Step 4: Conclude
Write conclusions and recommendations based on:
[paste step 3 output]
```

## Code Development Chain

```
# Prompt 1: Design
Design the architecture for [feature]:
- Components needed
- Interfaces
- Data flow

# Prompt 2: Implement
Implement [component] based on this design:
[paste design]

# Prompt 3: Test
Write tests for this implementation:
[paste code]

# Prompt 4: Document
Document this code:
[paste code and tests]
```

## Content Creation Chain

```
# Prompt 1: Brainstorm
Generate 10 ideas for [content type] about [topic].

# Prompt 2: Select
From these ideas, select the best 3 and explain why:
[paste ideas]

# Prompt 3: Outline
Create detailed outline for idea #[X]:
[paste selected idea]

# Prompt 4: Draft
Write first draft based on this outline:
[paste outline]

# Prompt 5: Edit
Edit for clarity, tone, and engagement:
[paste draft]
```

## Refactoring Chain

```
# Prompt 1: Analyze
Identify code smells in:
[paste code]

# Prompt 2: Plan
Create refactoring plan for these issues:
[paste analysis]
Prioritize by impact.

# Prompt 3: Execute
Apply the highest priority refactoring:
[paste plan + code]

# Prompt 4: Verify
Compare before/after. Verify behavior is unchanged:
[paste both versions]
```

## Translation Chain

```
# Prompt 1: Understand
Analyze the source text for:
- Tone and style
- Cultural references
- Idiomatic expressions
Source: [text]

# Prompt 2: Draft Translation
Translate preserving the elements identified:
[paste analysis + source]

# Prompt 3: Localize
Adapt cultural references for target audience:
[paste translation]

# Prompt 4: Polish
Final polish for fluency:
[paste localized version]
```
