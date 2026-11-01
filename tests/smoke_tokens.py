"""Exercise the real optional tiktoken branch (run after pip install '.[tokens]')."""

import tiktoken

from llm_promptkit import PromptBuilder

builder = PromptBuilder().task("Hello, token counter! " * 10)
text = builder.build()
expected = len(tiktoken.encoding_for_model("gpt-4").encode(text))
assert expected > 0
assert expected != len(text) // 4, "Choose text distinguishing tiktoken from the fallback"
assert builder.estimate_tokens("gpt-4") == expected
print(f"tiktoken smoke: exact count {expected} PASS")
