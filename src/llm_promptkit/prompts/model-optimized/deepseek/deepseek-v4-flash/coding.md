# DeepSeek V4 Flash: Coding

## Fast Code Generation
```
Write code for: [description]

Language: [Python/JavaScript/TypeScript/etc.]
Style: [follow project conventions]

Requirements:
- [requirement 1]
- [requirement 2]

Output clean, working code with minimal explanation.
Include type hints and basic error handling.
```

## Quick Debugging
```
Fix this bug:

Error: [paste error message]
Code: [paste relevant code]

Find the root cause and provide a minimal fix.
Explain the fix in 1-2 sentences.
```

## Batch Code Generation
```
Generate the following code files:

1. [filename1]: [description]
2. [filename2]: [description]
3. [filename3]: [description]

Language: [lang]
Framework: [framework if any]

For each file: output filename as heading, then complete code.
Keep implementations focused and minimal.
```

## Code Transformation
```
Transform this code:

Original: [paste code]
Source language: [lang]
Target: [different language / framework / pattern]

Requirements:
- Preserve functionality
- Follow target conventions
- Include equivalent type annotations
- Handle language-specific idioms

Output the transformed code only.
```

---
**DeepSeek V4 Flash Coding Tips:**
- Optimized for speed and throughput — best for high-volume generation
- 284B total params, 13B active (MoE) — fast inference
- 1M context window available when needed
- Great for batch operations: bulk transformations, test generation, scaffolding
- API: `deepseek-chat` (non-thinking) for speed, `deepseek-reasoner` for accuracy
- ~35× cheaper on input than Claude Opus — use for tasks that don't need Pro
- Perfect for CI/CD integration and automated code generation pipelines