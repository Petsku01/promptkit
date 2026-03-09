# Llama 3.2 Prompting Guide

## Model Characteristics
- **Context:** 128K tokens
- **Sizes:** 1B, 3B (text), 11B, 90B (vision)
- **Strengths:** Multimodal, edge deployment, efficient
- **Best for:** Vision tasks, mobile/edge, lightweight apps

## Vision Models (11B, 90B)

```
<image>
[Image is provided]
</image>

Describe what you see in this image:
1. Main subjects
2. Setting/background
3. Any text visible
4. Notable details
```

## Text Models (1B, 3B)

Keep prompts simple for small models:

```
Answer this question:
[question]

Answer:
```

## Chain of Thought (Vision)

```
Look at this image and analyze:

Step 1: What objects do you see?
Step 2: What is happening?
Step 3: What can you infer?

Conclusion:
```

## Key Tips

- 1B/3B: Very simple prompts, basic tasks only
- 11B/90B: Multimodal, can see images
- Edge-optimized for mobile deployment
- Vision models need explicit image references
- Smaller context needs for edge models
