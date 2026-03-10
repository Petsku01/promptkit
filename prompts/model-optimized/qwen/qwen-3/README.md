# Qwen 3

## Ominaisuudet
- **Sizes:** 0.6B, 1.7B, 4B, 8B, 14B, 32B, 30B-A3B (MoE), 235B-A22B (MoE)
- **Konteksti:** 32K - 128K
- **Strengths:** MoE-arkkitehtuuri, reasoning, tool use

## Prompts

Use the same prompts as Qwen 2.5:
- [../qwen-2.5/analysis.md](../qwen-2.5/analysis.md)
- [../qwen-2.5/coding.md](../qwen-2.5/coding.md)
- [../qwen-2.5/json-output.md](../qwen-2.5/json-output.md)

## MoE-mallit (30B-A3B, 235B-A22B)

- Aktivoi vain osa parametreista -> nopea
- Behaves like larger model, but more efficient
- Samat promptit toimivat

## Qwen3-Coder

For coding tasks use Qwen3-Coder variant:
- Parempi koodin generointi
- Parempi debuggaus
- Samat promptit toimivat
