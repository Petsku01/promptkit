# Gemini 2.5 Pro: Multimodal

## Image Analysis
```
Analyze this image:

[image]

Provide:
1. Overall description
2. Key objects and their positions
3. Text content (transcribe if present)
4. Spatial relationships
5. Notable details and context
6. Interpretation and significance
```

## Video Understanding
```
Analyze this video:

[video]

Provide:
1. Content summary
2. Key moments (with timestamps if possible)
3. Visual elements and style
4. Audio content summary
5. Narrative structure or flow
6. Overall assessment
```

## Audio Analysis
```
Analyze this audio:

[audio]

Identify:
1. Type (speech/music/ambient/mixed)
2. Content summary
3. Speakers or instruments (if applicable)
4. Key points or themes
5. Notable moments
```

## Cross-Modal Reasoning
```
Analyze the relationship between these inputs:

Text: [text content]
Image: [image]
[optional: Audio: [audio]]

Answer:
1. How do the inputs relate?
2. Are there contradictions?
3. What additional context do they provide together?
4. Combined interpretation
```

## Document Processing
```
Process this document:

[PDF/image of document]

Extract:
1. Title and metadata
2. Main text content (preserving structure)
3. Tables (as markdown)
4. Key data points
5. Document structure/outline
6. Forms or fields
```

## Multi-Image Comparison
```
Compare these images:

[image 1]
[image 2]

Analyze:
1. Similarities
2. Differences
3. Context comparison
4. Which is better for [purpose]
5. Recommendations
```

## Diagram to Code
```
Convert this diagram to code:

[image of diagram/architecture/flowchart]

Language: [language]
Framework: [framework if applicable]

Provide:
1. Code implementation
2. Component descriptions
3. Data flow explanation
4. Any assumptions made
```

---

**Gemini 2.5 Pro Multimodal Tips:**
- Pro can reason across multiple modalities in a single request
- Be explicit about what to focus on in images/videos
- For documents, specify extraction format (markdown tables, structured data)
- Cross-modal reasoning is a Pro strength — combine text + images for richer analysis
- Reference specific parts of images: "the chart on the left", "the footnote at the bottom"