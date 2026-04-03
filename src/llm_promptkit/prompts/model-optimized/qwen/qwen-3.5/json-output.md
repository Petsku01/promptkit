# Qwen 3.5: JSON (simplified)

## Perus JSON

```
Return JSON only:
{"key": "value"}

Input: [text]
JSON:
```

## Lista

```
Extract as JSON array:
["item1", "item2"]

Input: [text]
JSON:
```

## Avain-arvo

```
Parse to JSON:
{"name": "", "value": ""}

Input: [text]
JSON:
```

## Luokittelu JSON

```
Classify and return:
{"category": "", "confidence": "high/low"}

Text: [input]
JSON:
```

## Yksinkertainen schema

```
Extract:
{
  "title": "",
  "date": "",
  "author": ""
}

From: [text]
JSON:
```

##  Small mallit

- Max 3-5 fields
- Simple types (string, number)
- No deep nested structures
- Always provide example output
```
