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

## Deep research and RAG adaptations — LangChain MIT

The following prompts are adaptations, not verbatim source copies or
model-tested vendor prompts. Their pinned upstream file URLs are recorded
in each prompt. The generated `docs/prompts/` mirrors carry the same
attribution.

From `langchain-ai/open_deep_research` at `1b7d2e80db9faa586165c60e09096dbbfd483a64`
(repository archived; snapshot only):

- `src/llm_promptkit/prompts/reasoning/deep-research-supervisor.md`

From `langchain-ai/langgraph` at `23961cff61a42b52525f3b20b4094d8d2fba1744`
(adaptive RAG tutorial cells; generation text authored, Hub templates not copied):

- `src/llm_promptkit/prompts/reasoning/adaptive-rag-gates.md`

License sources:

- https://github.com/langchain-ai/open_deep_research/blob/1b7d2e80db9faa586165c60e09096dbbfd483a64/LICENSE
- https://github.com/langchain-ai/langgraph/blob/23961cff61a42b52525f3b20b4094d8d2fba1744/LICENSE

```text
MIT License

Copyright (c) 2025 LangChain

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

```text
MIT License

Copyright (c) 2024 LangChain, Inc.

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

## Bull-bear research debate — TradingAgents Apache-2.0

Adapted from `TauricResearch/TradingAgents` researcher, manager, and
`graph/conditional_logic.py` files. The exact upstream URLs appear in the
prompt. Applies equally to the generated `docs/prompts/` mirror:

- `src/llm_promptkit/prompts/reasoning/bull-bear-research-debate.md`

Identified modifications relative to the captured researcher prompts: an
explicit round cap (`count >= 2 * max_debate_rounds`), human decision
boundary, no-order rule, required per-turn evidence citations, and optional
downside checks without inventing missing risk-debate speakers. No upstream
NOTICE file was present at authoring time.

License source: https://github.com/TauricResearch/TradingAgents/blob/main/LICENSE

```text
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

## STORM persona pipeline — Stanford OVAL MIT

Adapted from `stanford-oval/storm` knowledge_curation, outline_generation,
and article_polish modules. The exact upstream URLs appear in the prompt.
Applies equally to the generated `docs/prompts/` mirror:

- `src/llm_promptkit/prompts/reasoning/storm-persona-outline-polish.md`

License source: https://github.com/stanford-oval/storm/blob/main/LICENSE

```text
MIT License

Copyright (c) 2024 Stanford Open Virtual Assistant Lab

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

## Self-Discover plan — Fareed Khan MIT

Adapted from `FareedKhan-dev/all-agentic-architectures` `self_discover.py`.
The exact upstream URL appears in the prompt. Method origin is Zhou et al.,
Self-Discover (Google DeepMind, 2024); this is not an official paper
implementation. LangSmith Hub templates are not copied. Applies equally to
the generated `docs/prompts/` mirror:

- `src/llm_promptkit/prompts/reasoning/self-discover-plan.md`

License source: https://github.com/FareedKhan-dev/all-agentic-architectures/blob/main/LICENSE

```text
MIT License

Copyright (c) 2025 Fareed Khan

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

## SEO bet and support-triage loops — Superdesign / Loopany MIT

Adapted from Loopany public template Copy-prompt bodies (seo-try-keywords,
seo-scale-keywords, support-triage) under the loopany-platform MIT license
© 2026 Superdesign. Exact website-to-git identity is not claimed. Applies
equally to the generated `docs/prompts/` mirrors:

- `src/llm_promptkit/prompts/system/seo-bet-scale-lifecycle.md`
- `src/llm_promptkit/prompts/system/support-triage-investigate-hold.md`

License source: https://github.com/superdesigndev/loopany-platform/blob/main/LICENSE

```text
MIT License

Copyright (c) 2026 Superdesign

Loopany is a pnpm monorepo. Every package in this repository - including
packages/daemon (@crewlet/loopany) and packages/server (@loopany/server) - and
everything else (root configuration, scripts, docs) is licensed under the MIT
License. See packages/daemon/LICENSE and packages/server/LICENSE for the
per-package copies; their terms are identical to the ones below.

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
