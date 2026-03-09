# Chain of Thought — Google (Gemini Pro, Flash, Ultra)

## Optimizations

- **Structured format** — Gemini excels with clear structure
- **Bullet points** — Use bullets for multi-part instructions
- **Grounding** — Reference source material explicitly
- **Multimodal aware** — Gemini can reason about images/video

## The Prompt

```
Analyze this problem using structured reasoning:

• First, identify the key question
• List the relevant information
• Break down into logical steps
• Work through each step systematically
• Verify your reasoning
• State your conclusion

Format your response with clear headers for each phase.
```

## With Section Headers

```
## Instructions
Solve this problem step-by-step, showing your reasoning.

## Required Sections

### Understanding
What is being asked?

### Analysis
What are the key components?

### Solution Steps
Work through each step.

### Verification
Check your work.

### Final Answer
State your conclusion.
```

## For Gemini Flash (Speed-Optimized)

```
Quick analysis:
1. Problem: [restate]
2. Key info: [list]
3. Steps: [numbered]
4. Answer: [final]

Keep responses concise.
```

## Notes

- Gemini Pro: best for complex reasoning
- Gemini Flash: faster, keep prompts shorter
- Gemini Ultra: most capable, can handle nuanced instructions
- For multimodal: explicitly reference "the image shows..." in prompts
