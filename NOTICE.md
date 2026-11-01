# Kolmansien osapuolten attribuutiot

Tämä täydentää projektin LICENSE-tiedostoa; projektin MIT-lisenssi ei korvaa
kolmansien osapuolten ehtoja eikä ratkaise tuntemattoman alkuperän oikeuksia.
Polut ovat suhteessa repon juureen.

## Fabric — MIT

Lähde: https://github.com/danielmiessler/Fabric
Lisenssiteksti: https://raw.githubusercontent.com/danielmiessler/Fabric/main/LICENSE

Alla on koko raw-lisenssiteksti muuttamatta. Myös upstreamin copyright-rivi
(Scott Chacon and others) on säilytetty sellaisenaan.

```text
MIT License

Copyright (c) 2012-2024 Scott Chacon and others

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
```

### Fabric-kohdetiedostot (18)

Vertailukohde: `https://raw.githubusercontent.com/danielmiessler/Fabric/main/`
sekä taulukon upstream-polku. Paikallisesta `The Prompt` -osiosta erotettiin
ulomman koodiaidan sisältö viimeisine rivinvaihtoineen. Molemmista normalisoitiin
vain CRLF → LF; muuta whitespacea tai sisältöä ei normalisoitu.
VERIFIOITU tarkoittaa byte-täsmäosumaa, ei pelkkää lähdemerkintää.
Muut rivit ovat olemassa olevan Source-merkinnän Fabric-derivaatteja, eivät
tämän tarkistuksen täsmäosumia; niiden frontmatteria ei muutettu.
Lisenssi-ilmoitus säilytetään kaikille 18 johdannaiselle.

| Paikallinen tiedosto | Upstream-polku | Byte-vertailu |
| --- | --- | --- |
| `src/llm_promptkit/prompts/code/create-git-diff-commit.md` | `data/patterns/create_git_diff_commit/system.md` | VERIFIOITU |
| `src/llm_promptkit/prompts/code/explain-code.md` | `data/patterns/explain_code/system.md` | EI TÄSMÄOSUMAA |
| `src/llm_promptkit/prompts/code/generate-code-rules.md` | `data/patterns/generate_code_rules/system.md` | EI TÄSMÄOSUMAA |
| `src/llm_promptkit/prompts/code/review-code.md` | `data/patterns/review_code/system.md` | EI TÄSMÄOSUMAA |
| `src/llm_promptkit/prompts/creative/create-art-prompt.md` | `data/patterns/create_art_prompt/system.md` | EI TÄSMÄOSUMAA |
| `src/llm_promptkit/prompts/defensive/analyze-malware.md` | `data/patterns/analyze_malware/system.md` | VERIFIOITU |
| `src/llm_promptkit/prompts/defensive/analyze-threat-report.md` | `data/patterns/analyze_threat_report/system.md` | VERIFIOITU |
| `src/llm_promptkit/prompts/defensive/create-stride-threat-model.md` | `data/patterns/create_stride_threat_model/system.md` | VERIFIOITU |
| `src/llm_promptkit/prompts/defensive/greybeard-secure-prompt-engineer.md` | `data/patterns/greybeard_secure_prompt_engineer/system.md` | VERIFIOITU |
| `src/llm_promptkit/prompts/defensive/write-hackerone-report.md` | `data/patterns/write_hackerone_report/system.md` | VERIFIOITU |
| `src/llm_promptkit/prompts/output/create-mermaid-visualization.md` | `data/patterns/create_mermaid_visualization/system.md` | VERIFIOITU |
| `src/llm_promptkit/prompts/output/to-flashcards.md` | `data/patterns/to_flashcards/system.md` | EI TÄSMÄOSUMAA |
| `src/llm_promptkit/prompts/output/transcribe-minutes.md` | `data/patterns/transcribe_minutes/system.md` | VERIFIOITU |
| `src/llm_promptkit/prompts/professional/analyze-candidates.md` | `data/patterns/analyze_candidates/system.md` | EI TÄSMÄOSUMAA |
| `src/llm_promptkit/prompts/professional/create-prd.md` | `data/patterns/create_prd/system.md` | EI TÄSMÄOSUMAA |
| `src/llm_promptkit/prompts/reasoning/check-falsifiability.md` | `data/patterns/check_falsifiability/system.md` | EI TÄSMÄOSUMAA |
| `src/llm_promptkit/prompts/reasoning/find-logical-fallacies.md` | `data/patterns/find_logical_fallacies/system.md` | EI TÄSMÄOSUMAA |
| `src/llm_promptkit/prompts/system/improve-prompt.md` | `data/patterns/improve_prompt/system.md` | EI TÄSMÄOSUMAA |

## Awesome ChatGPT Prompts — CC0 1.0 Universal

Paikallisen `**Source:** Awesome ChatGPT Prompts` -merkinnän sisältävät 14
promptitiedostoa on attribuoitu projektille f/awesome-chatgpt-prompts.
Upstreamin LICENSE erottaa prompttisisällön ja -datan (CC0 1.0 Universal)
lähdekoodista ja sivuston omasta sisällöstä (MIT). Prompttien perusteella ei
synny MIT-copyright- tai permission-ilmoituksen säilyttämisvaatimusta.
Nykyiset tekijämerkinnät säilytetään. Tämä tarkistus ei ollut CC0-prompttien
sisältövertailu eikä osoita paikallisten johdannaisten byte-identtisyyttä.

- https://github.com/f/awesome-chatgpt-prompts
- https://raw.githubusercontent.com/f/awesome-chatgpt-prompts/main/LICENSE
- https://raw.githubusercontent.com/f/awesome-chatgpt-prompts/main/LICENSE-CC0

## prompts.chat — CC0 1.0 Universal

Paikallisen `**Source:** prompts.chat` -merkinnän sisältävät 79 promptitiedostoa
on attribuoitu prompts.chat-projektille. Sen LICENSE määrittelee prompttisisällön
ja -datan CC0 1.0 Universal -aineistoksi; sivuston lähdekoodin MIT-lisenssiä ei
sovelleta promptteihin tämän perusteella. Nykyiset contributor-merkinnät säilytetään.
Tämä tarkistus ei sisältänyt näiden prompttien byte-vertailua.

- https://github.com/f/prompts.chat
- https://raw.githubusercontent.com/f/prompts.chat/main/LICENSE
- https://raw.githubusercontent.com/f/prompts.chat/main/LICENSE-CC0

## Tunnettu alkuperä, lisenssi epäselvä

Seuraavat ovat paikallisia Source-merkintöjä, eivät käyttöoikeuden todistuksia:

- `src/llm_promptkit/prompts/code/debugger-interactive.md` — TheBigPromptLibrary
  (ChatGPT GPT): alkuperä tunnettu, lisenssi epäselvä — käyttäjän päätettävä.
- `src/llm_promptkit/prompts/system/claude-soul-principles.md` — Anthropic
  (Claude Soul Document): alkuperä tunnettu, lisenssi epäselvä — käyttäjän päätettävä.

## Selvitettävät alkuperät

README-tiedostot pois lukien inventaario sisältää 292 promptitiedostoa.
Näistä 160 tiedostossa ei ole Source-kenttää. Niiden alkuperää tai lisenssiä ei
päätellä kategoriasta eikä niihin lisätä keksittyjä lähteitä. Niitä ei muutettu.
Suurimmat kategoriat (mallikohtaisten alla valmistajaryhmän mukaan):

- `model-optimized/openai`: 26 tiedostoa.
- `model-optimized/anthropic`: 21 tiedostoa.
- `model-optimized/deepseek`: 16 tiedostoa.
- `model-optimized/google`: 15 tiedostoa.
- `model-optimized/meta`: 9 tiedostoa.
- `model-optimized/qwen`: 9 tiedostoa.

## Agentic workflow adaptations — GitHub MIT

The following prompts are adaptations, not verbatim source copies or model-tested
vendor prompts. Their pinned upstream file URLs are recorded in each prompt.
The generated `docs/prompts/` mirrors carry the same attribution.

From `github/awesome-copilot` at `5269f7ea2d6c3a9bfda5ed878b6726cf509121fd`:

- `src/llm_promptkit/prompts/debug/mcp-server-release-qa.md`
- `src/llm_promptkit/prompts/context/codebase-memory-mcp-discovery.md`
- `src/llm_promptkit/prompts/code/browser-exploration-to-verified-playwright-tests.md`
  (combines `playwright-explore-website` and `playwright-generate-test`).
- `src/llm_promptkit/prompts/code/launchdarkly-flag-removal.md`
- `src/llm_promptkit/prompts/code/mongodb-query-performance-advisor.md`
- `src/llm_promptkit/prompts/code/windows-arm64-python-wheel-ci.md`
- `src/llm_promptkit/prompts/code/embedded-c-misra-deviations.md`
- `src/llm_promptkit/prompts/debug/frontend-performance-investigation.md`
- `src/llm_promptkit/prompts/code/clojure-repl-pair-programming.md`
- `src/llm_promptkit/prompts/code/gha-node-runtime-upgrade.md`

From `github/spec-kit` at `7370e592f3cd9c06e5b698983957e227c75b30e2`:

- `src/llm_promptkit/prompts/defensive/spec-plan-task-consistency-audit.md`

License sources (both carry the notice below):

- https://github.com/github/awesome-copilot/blob/5269f7ea2d6c3a9bfda5ed878b6726cf509121fd/LICENSE
- https://github.com/github/spec-kit/blob/7370e592f3cd9c06e5b698983957e227c75b30e2/LICENSE

```text
MIT License

Copyright GitHub, Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Agentic workflow adaptations — wshobson/agents MIT

Source: https://github.com/wshobson/agents
Pinned upstream: `7e2fb559cf4b824b27f1fec49fe88f7511066d26`.
The exact upstream file URLs appear in the prompts. This notice also covers
all generated `docs/prompts/` mirrors of these adaptations:

- `src/llm_promptkit/prompts/code/logical-git-revert-confirmation.md`
- `src/llm_promptkit/prompts/code/executable-implementation-plans.md`
  (bounded feature/bug intake and separate specification approval only;
  the primary Superpowers source retains its separate notice above).

License source: https://github.com/wshobson/agents/blob/7e2fb559cf4b824b27f1fec49fe88f7511066d26/LICENSE

```text
MIT License

Copyright (c) 2024 Seth Hobson

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## Agentic workflow adaptations — Superpowers MIT

Adapted from `obra/superpowers` at `2ce8aa15d05bd57213e6f746f953aafb7ded7a8b`;
the exact upstream skill URL is recorded in each prompt. Applies equally to
the generated `docs/prompts/` mirrors:

- `src/llm_promptkit/prompts/code/git-worktree-isolation-baseline.md`
- `src/llm_promptkit/prompts/system/test-driven-agent-skill-authoring.md`
- `src/llm_promptkit/prompts/defensive/evidence-gated-completion-claims.md`
- `src/llm_promptkit/prompts/code/code-review-reception-pushback.md`
- `src/llm_promptkit/prompts/debug/four-phase-root-cause-debugging.md`
- `src/llm_promptkit/prompts/code/executable-implementation-plans.md`
  (also uses bounded intake and separate specification approval from
  `wshobson/agents`; both MIT notices apply).
- `src/llm_promptkit/prompts/defensive/task-reviewer-compliance-quality.md`

License source: https://github.com/obra/superpowers/blob/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/LICENSE

```text
MIT License

Copyright (c) 2025 Jesse Vincent

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
