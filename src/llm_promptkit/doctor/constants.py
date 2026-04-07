"""Constants for prompt doctor analysis."""

VAGUE_PHRASES = [
    "make it good",
    "do it well",
    "as best as you can",
    "stuff",
    "things",
    "as soon as possible",
    "asap",
    "etc",
    "and so on",
    "whatever you think",
]

ROLE_PHRASES = [
    "you are a",
    "you are an",
    "role:",
    "persona:",
    "act as",
    "system:",
    "<role>",
    "<system_prompt>",
    "<persona>",
]

VERBOSE_PHRASES = [
    "please could you",
    "i would like you to",
    "if you don't mind",
    "can you please",
    "please",
    "thank you",
    "thanks",
    "kindly",
]

FORMAT_PHRASES = ["format", "json", "markdown", "output:", "structure", "return as"]
EXAMPLE_PHRASES = ["example:", "example", "e.g.", "for instance", "few-shot", "here is an example"]
NEGATIVE_PHRASES = ["don't", "do not", "never", "avoid", "must not", "stop"]
