[← Back to Few-Shot](./index.md)

# Few-Shot: Muunnos

## Text to JSON

```
Convert the text to JSON format.

Input: "John Smith, 25 years old, works at Google as a software engineer"
Output: {"name": "John Smith", "age": 25, "company": "Google", "role": "software engineer"}

Input: "Product: iPhone 15, Price: $999, Color: Blue, Storage: 128GB"
Output: {"product": "iPhone 15", "price": 999, "color": "Blue", "storage": "128GB"}

Input: "Meeting on March 15th at 2pm with Sarah about Q2 planning"
Output: {"date": "March 15th", "time": "2pm", "attendee": "Sarah", "topic": "Q2 planning"}

Input: [YOUR TEXT]
Output:
```

## Formal to Casual

```
Rewrite in casual tone.

Input: "We would like to inform you that your request has been processed."
Output: "Hey, just letting you know we've taken care of your request!"

Input: "Please be advised that the meeting has been rescheduled."
Output: "Heads up - we moved the meeting!"

Input: "We regret to inform you that your application was not successful."
Output: "Sorry, but we couldn't move forward with your application this time."

Input: [FORMAL TEXT]
Output:
```

## Casual to Formal

```
Rewrite in formal business tone.

Input: "Hey, can you send me that report thingy?"
Output: "Could you please forward the requested report at your earliest convenience?"

Input: "This idea is super cool, let's do it!"
Output: "This proposal has considerable merit. I recommend we proceed with implementation."

Input: "My bad, I totally forgot about the meeting."
Output: "I apologize for the oversight. The meeting unfortunately slipped my attention."

Input: [CASUAL TEXT]
Output:
```

## Active to Passive

```
Convert to passive voice.

Input: "The team completed the project ahead of schedule."
Output: "The project was completed ahead of schedule by the team."

Input: "The manager approved the budget yesterday."
Output: "The budget was approved yesterday by the manager."

Input: "Scientists discovered a new species in the Amazon."
Output: "A new species was discovered in the Amazon by scientists."

Input: [ACTIVE SENTENCE]
Output:
```

## Bullet Points to Paragraph

```
Convert bullet points to a cohesive paragraph.

Input:
- Company founded in 2010
- Headquarters in San Francisco
- 500 employees worldwide
- Focus on AI technology
Output: Founded in 2010, the company is headquartered in San Francisco and has grown to employ 500 people worldwide. The organization focuses primarily on AI technology.

Input:
- Meeting scheduled for Monday
- Discussing Q3 results
- All department heads required
- Lunch will be provided
Output: A meeting has been scheduled for Monday to discuss Q3 results. All department heads are required to attend, and lunch will be provided.

Input: [BULLET POINTS]
Output:
```

## Code Comment Generator

```
Generate a descriptive comment for this code.

Input: def fibonacci(n): return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
Output: # Recursively calculates the nth Fibonacci number. Returns n for base cases (0,1), otherwise returns sum of two preceding numbers.

Input: users = [u for u in data if u['active'] and u['age'] >= 18]
Output: # Filters data to get only active users who are 18 years or older

Input: cache = {}; def memoize(f): def wrapper(*args): return cache.setdefault(args, f(*args)); return wrapper
Output: # Memoization decorator that caches function results to avoid redundant calculations

Input: [CODE]
Output:
```
