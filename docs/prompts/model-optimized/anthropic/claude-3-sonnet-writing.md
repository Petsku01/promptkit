[← Back to Anthropic](./index.md)

# Claude Sonnet: Writing

## Text Improvement

```xml
<task>
Improve this text while maintaining original meaning.
</task>

<improvements>
- Fix grammar and spelling
- Improve clarity and flow
- Make it more concise
- Strengthen weak phrases
- Maintain original tone
</improvements>

<output_format>
<improved_text>
[Your improved version]
</improved_text>

<changes_made>
- [List of specific changes]
</changes_made>
</output_format>

<original_text>
[paste text]
</original_text>
```

## Professional Email

```xml
<task>
Write a professional email.
</task>

<context>
- Purpose: [request/follow-up/etc]
- Recipient: [role/relationship]
- Tone: [formal/friendly]
- Key points: [what to include]
</context>

<constraints>
- Keep under 200 words
- Clear call to action
- Professional but warm
</constraints>
```

## Technical Documentation

```xml
<task>
Write documentation for this [code/feature/API].
</task>

<sections_required>
1. Overview - what it does
2. Installation/Setup
3. Usage with examples
4. API reference
5. Troubleshooting
</sections_required>

<audience>
[Developers / End users / Both]
</audience>

<subject>
[paste code or describe feature]
</subject>
```

## Meeting Summary

```xml
<task>
Summarize this meeting transcript.
</task>

<output_format>
## Meeting Summary

**Date:** 
**Attendees:**

### Key Decisions
- 

### Action Items
| Task | Owner | Deadline |
|------|-------|----------|

### Discussion Points
-

### Next Steps
-
</output_format>

<transcript>
[paste transcript]
</transcript>
```

## Content Rewrite

```xml
<task>
Rewrite this content for a different audience.
</task>

<original_audience>
[Technical experts / General public / etc]
</original_audience>

<target_audience>
[Executive / Beginner / etc]
</target_audience>

<guidelines>
- Adjust complexity level
- Change examples if needed
- Keep core message
- Match expected tone
</guidelines>

<content>
[paste content]
</content>
```
