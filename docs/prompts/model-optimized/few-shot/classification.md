[← Back to Few-Shot](./index.md)

# Few-Shot: Luokittelu

## Sentiment Analysis

```
Classify the sentiment as positive, negative, or neutral.

Input: "This product exceeded my expectations! Highly recommend."
Output: positive

Input: "Worst purchase ever. Complete waste of money."
Output: negative

Input: "The package arrived on Tuesday."
Output: neutral

Input: "It's okay I guess, nothing special but not bad either."
Output: neutral

Input: [YOUR TEXT]
Output:
```

## Intent Classification

```
Classify the user intent.
Categories: question, complaint, request, feedback, greeting

Input: "How do I reset my password?"
Output: question

Input: "Your service is terrible and I want a refund!"
Output: complaint

Input: "Can you please send me the invoice?"
Output: request

Input: "The new feature is really helpful, thanks!"
Output: feedback

Input: "Hey, hope you're doing well!"
Output: greeting

Input: [USER MESSAGE]
Output:
```

## Topic Classification

```
Classify the topic of this text.
Categories: technology, sports, politics, entertainment, science, business

Input: "The new iPhone features a faster processor and improved camera."
Output: technology

Input: "The team won 3-2 in overtime after a dramatic comeback."
Output: sports

Input: "The senator proposed a new bill on healthcare reform."
Output: politics

Input: "Researchers discovered a new exoplanet that could support life."
Output: science

Input: [TEXT]
Output:
```

## Priority Classification

```
Classify the support ticket priority.
Levels: critical, high, medium, low

Input: "System is completely down, no one can work"
Output: critical

Input: "Payment processing failing for some customers"
Output: high

Input: "Report generation is slower than usual"
Output: medium

Input: "Can you change the color of the button?"
Output: low

Input: "Login page shows error but users can still log in through app"
Output: medium

Input: [TICKET]
Output:
```

## Language Detection

```
Detect the language of the text.

Input: "Hello, how are you today?"
Output: English

Input: "Bonjour, comment allez-vous?"
Output: French

Input: "Hola, ¿cómo estás?"
Output: Spanish

Input: "Hallo, wie geht es dir?"
Output: German

Input: "Hello, how are you?"
Output: Finnish

Input: [TEXT]
Output:
```

## Spam Detection

```
Classify as spam or not_spam.

Input: "CONGRATULATIONS! You've won $1,000,000! Click here NOW!!!"
Output: spam

Input: "Your meeting has been rescheduled to 3pm tomorrow."
Output: not_spam

Input: "FREE VIAGRA!!! Best prices guaranteed!!!"
Output: spam

Input: "Hi, just following up on our conversation from last week."
Output: not_spam

Input: "Make $5000 daily from home! No experience needed!"
Output: spam

Input: [MESSAGE]
Output:
```
