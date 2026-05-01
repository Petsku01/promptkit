[← Back to Model-Optimized Anthropic](../index.md)

# Claude 3.5 Haiku: Coding

## Quick Function Generation
```xml
<task>Write a [language] function.</task>

<description>
[what it does]
</description>

<requirements>
- Type hints on all parameters and return
- Handle [specific edge case]
- Keep it simple
</requirements>
```

## Simple Debugging
```xml
<task>Fix this bug.</task>

<error>
[paste error message]
</error>

<code>
[paste code]
</code>

<output_format>
Root cause: [1 sentence]
Fix: [corrected code]
</output_format>
```

## Boilerplate Generation
```
Generate boilerplate for: [component type]

Framework: [framework]
Language: [language]

Include:
- [standard elements]

Keep it minimal — I'll fill in the details.
```

## Test Generation
```xml
<task>Write basic tests.</task>

<code>
[paste function/module]
</code>

<framework>[pytest / jest / etc.]</framework>

Cover:
- Happy path
- Empty/none inputs
- Obvious edge cases
```

## Code Formatting / Refactoring (Simple)
```xml
<task>Clean up this code.</task>

<code>
[paste code]
</code>

<goals>
- Consistent formatting
- Better variable names
- Remove dead code
</goals>

Don't change functionality. Just make it cleaner.
```

---

**Claude 3.5 Haiku Coding Tips:**
- Great for quick boilerplate, simple functions, and basic tests
- Fast and cheap enough for generating many files in one session
- Don't ask for complex architecture or multi-file refactoring — use Sonnet/Opus for that
- XML tags help it stay focused on the specific task
- Keep instructions direct: "Write X, include Y, skip Z"
- Perfect for generating repetitive code patterns (CRUD endpoints, DTOs, migrations)