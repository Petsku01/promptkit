# Llama 3.3 (70B) Prompting Guide

## Model Characteristics
- **Context:** 128K tokens
- **Size:** 70B parameters
- **Strengths:** Instruction following, reasoning, matches 405B quality
- **Best for:** Production open-source, complex tasks

---

## Prompt 1: Structured Reasoning

```
Solve this problem step by step:

**Step 1 - Understand:**
What is the question asking?

**Step 2 - Information:**
What key facts do I have?

**Step 3 - Approach:**
How will I solve this?

**Step 4 - Execute:**
[Work through the solution]

**Step 5 - Verify:**
Is my answer correct?

**Final Answer:**
[Clear, concise answer]
```

---

## Prompt 2: Code Generation

```
Write a function that [description].

Requirements:
- Language: [Python/JavaScript/etc]
- Include docstring
- Handle errors
- Add comments

Output format:
1. The code
2. Example usage
3. What edge cases it handles

Code:
```

---

## Prompt 3: Text Summarization

```
Summarize this text:

Guidelines:
- Length: [X sentences/words]
- Include: key points, main argument
- Exclude: minor details, examples
- Tone: [formal/casual/technical]

Text to summarize:
[paste text]

Summary:
```

---

## Prompt 4: JSON Output

```
Extract information from this text as JSON.

Schema:
{
  "title": "string",
  "date": "YYYY-MM-DD",
  "entities": ["string"],
  "summary": "string"
}

Rules:
- Valid JSON only
- No explanation
- null for missing fields

Text:
[input]

JSON:
```

---

## Prompt 5: Question Answering

```
Answer this question based on the context provided.

Context:
[paste context/document]

Question:
[question]

Instructions:
- Answer only from the context
- Quote relevant parts
- Say "not found in context" if answer isn't there
- Be concise but complete

Answer:
```

---

## Prompt 6: Translation

```
Translate this text:

Source language: [language]
Target language: [language]

Requirements:
- Maintain original meaning
- Keep same tone/formality
- Preserve formatting
- Handle idioms appropriately

Text:
[input text]

Translation:
```

---

## Prompt 7: Classification

```
Classify this text into one of these categories:

Categories:
1. [Category A] - [brief description]
2. [Category B] - [brief description]
3. [Category C] - [brief description]

Text:
[input text]

Output format:
Category: [chosen category]
Confidence: [high/medium/low]
Reasoning: [1-2 sentences why]
```

---

## Prompt 8: Creative Writing

```
Write a [type of content] about [topic].

Requirements:
- Length: [X words/paragraphs]
- Tone: [serious/humorous/inspiring]
- Audience: [who is this for]
- Include: [specific elements]

Additional guidance:
[any other requirements]

Output:
```

---

## Prompt 9: Data Analysis

```
Analyze this data and provide insights:

Data:
[paste data/table]

Analysis required:
1. Summary statistics
2. Key trends
3. Anomalies or outliers
4. Actionable insights
5. Recommendations

Format your response with clear sections.
```

---

## Key Tips

- 70B matches 405B quality at lower cost
- Better instruction following than 3.1
- Improved reasoning capabilities
- Good for complex multi-step tasks
- Strong code generation
- Works well with explicit format examples
