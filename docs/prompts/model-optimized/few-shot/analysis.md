[← Back to Few-Shot](./index.md)

# Few-Shot: Analysis

## Entity Extraction

```
Extract named entities from the text.

Input: "Apple CEO Tim Cook announced the new iPhone 15 at the Cupertino headquarters on September 12th."
Output:
- Organizations: Apple
- People: Tim Cook
- Products: iPhone 15
- Locations: Cupertino
- Dates: September 12th

Input: "Dr. Sarah Johnson from MIT published a groundbreaking paper on quantum computing in Nature magazine."
Output:
- People: Dr. Sarah Johnson
- Organizations: MIT, Nature
- Topics: quantum computing

Input: [YOUR TEXT]
Output:
```

## Key Points Extraction

```
Extract the key points from this text.

Input: "The quarterly report shows revenue increased 15% YoY, primarily driven by cloud services growth. Customer acquisition costs decreased by 8%, while retention improved to 94%. The company plans to invest $50M in R&D next quarter."
Output:
- Revenue up 15% YoY (driven by cloud)
- Customer acquisition costs down 8%
- Retention at 94%
- $50M planned R&D investment

Input: "The experiment showed that participants who exercised daily had 30% better memory recall. The control group showed no improvement. Side effects were minimal, with only 2% reporting mild headaches."
Output:
- Daily exercise: 30% better memory recall
- Control group: no improvement
- Side effects: 2% mild headaches

Input: [TEXT]
Output:
```

## Pros and Cons

```
Analyze the pros and cons.

Topic: Remote work
Pros:
- Flexibility and work-life balance
- No commute, time and cost savings
- Access to global talent pool
Cons:
- Communication challenges
- Harder to maintain culture
- Potential isolation
Verdict: Best as hybrid model for most companies

Topic: Electric vehicles
Pros:
- Lower operating costs
- Environmental benefits
- Less maintenance needed
Cons:
- Higher upfront cost
- Range anxiety
- Charging infrastructure gaps
Verdict: Increasingly viable, especially for urban use

Topic: [YOUR TOPIC]
Pros:
Cons:
Verdict:
```

## Error Analysis

```
Analyze this error message.

Error: "TypeError: Cannot read property 'map' of undefined"
Analysis:
- Cause: Trying to call .map() on a variable that is undefined
- Likely issues: 
  1. Data not loaded yet (async issue)
  2. Wrong variable name
  3. API returned unexpected structure
- Fix: Add null check: data?.map() or initialize as empty array

Error: "ECONNREFUSED 127.0.0.1:5432"
Analysis:
- Cause: Cannot connect to PostgreSQL database
- Likely issues:
  1. PostgreSQL service not running
  2. Wrong port configuration
  3. Database not accepting connections
- Fix: Start PostgreSQL service, verify port in config

Error: "429 Too Many Requests"
Analysis:
- Cause: Rate limit exceeded on API
- Likely issues:
  1. Too many requests in short time
  2. No rate limiting in client code
- Fix: Implement exponential backoff, add request throttling

Error: [YOUR ERROR]
Analysis:
```

## Summarization

```
Summarize in one sentence.

Text: "The research team spent five years developing a new battery technology that uses solid-state electrolytes instead of liquid ones. This allows for higher energy density, faster charging, and eliminates the risk of thermal runaway that can cause fires in traditional lithium-ion batteries. Initial tests show the batteries can be charged to 80% in just 10 minutes."
Summary: A 5-year research project produced solid-state batteries that charge to 80% in 10 minutes while being safer and more energy-dense than traditional lithium-ion.

Text: "The city council voted 7-2 to approve the new public transit expansion plan, which includes three new subway lines and 15 additional bus routes. The $2.3 billion project is expected to be completed by 2028 and will serve an estimated 500,000 daily commuters."
Summary: City council approved a $2.3B transit expansion with new subway lines and bus routes, serving 500K daily commuters by 2028.

Text: [YOUR TEXT]
Summary:
```
