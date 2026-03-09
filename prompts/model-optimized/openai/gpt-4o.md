# GPT-4o Prompting Guide

## Model Characteristics
- **Context:** 128K tokens
- **Strengths:** Speed, multimodal (vision + audio), cost-effective
- **Best for:** Real-time apps, vision tasks, high-volume

## Chain of Thought

GPT-4o is faster but may skip steps. Be explicit:

```
Solve this step by step. You MUST show each step.

Step 1: [State the problem]
Step 2: [Identify key information]
Step 3: [Plan approach]
Step 4: [Execute]
Step 5: [Verify]
Step 6: [Final answer]

Do not skip any steps.
```

## JSON Output

Supports Structured Outputs (strict schema):

```python
from pydantic import BaseModel

class Result(BaseModel):
    answer: str
    confidence: float
    
response = client.beta.chat.completions.parse(
    model="gpt-4o",
    response_format=Result,
    messages=[...]
)
```

## Vision Tasks

```
Look at this image and describe:
1. What objects are present
2. Their spatial relationships
3. Any text visible

Be specific and detailed.
```

## Key Tips

- Faster than GPT-4 but may be less thorough
- Add "show each step" to prevent skipping
- Great for multimodal (images)
- Use Structured Outputs for guaranteed JSON schema
