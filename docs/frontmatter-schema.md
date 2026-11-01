# Prompt and pattern frontmatter schema

Content files under `src/llm_promptkit/{prompts,patterns}/` start with a single
YAML mapping between `---` delimiters. README files are not content files.
Values are strings; unknown optional fields are omitted, never `null`, `tbd` or
an inferred project-wide license. The Markdown body remains byte-for-byte intact.

| Field | Rule |
| --- | --- |
| `category` | Required: first category directory relative to `prompts/` or `patterns/`, e.g. `code`, `reasoning`, `model-optimized`. |
| `title` | Required: existing first level-one Markdown heading, without its `# ` prefix. |
| `subcategory` | Prompts only, when present: next directory, e.g. `anthropic` or `agentic`. |
| `model` | Only for `model-optimized/<subcategory>/<model>/<file>.md`: exact model directory name. Flat technique/role groups do not imply a model. |
| `source` | Optional: one of the exact attribution strings below, backed by NOTICE.md and the existing Source line. Other Source lines stay in the body but are not promoted to one of these known attributions. |
| `license` | Optional: `MIT` or `CC0`, only when established by NOTICE.md. Unknown licenses are absent. |

The supported, exact source/license pairs are:

- `prompts.chat` → `CC0`
- `Awesome ChatGPT Prompts, CC0` → `CC0`
- `Fabric (danielmiessler/Fabric), MIT` → `MIT`

Patterns currently carry only `category` and `title`; their directory does not
establish copyright provenance. Titles are YAML-quoted, including any punctuation.

```yaml
---
category: "model-optimized"
title: "Claude 3 Haiku - Analysis"
subcategory: "anthropic"
model: "claude-3-haiku"
---
```

The metadata example illustrates the schema, not a license grant. Existing
contributor names and legacy Category/Source lines are retained in the body.

## Registry API

`llm_promptkit.patterns._registry` exposes `get_pattern_metadata(name)`,
`get_pattern_category(name)`, `get_pattern_attribution(name)` (the YAML `source`),
and `get_pattern_license(name)`. Optional getters return `None` when absent;
metadata mappings do not gain fabricated source/license keys. Legacy/custom
files without frontmatter remain readable, with directory category fallback.
The existing `get_pattern_source(name)` API is unchanged: it identifies the
registry origin (`custom` / `built-in`), not copyright attribution.
`read_pattern(name)` strips YAML before extracting the existing template body.

## Documentation mirrors and drift lint

Run `python scripts/generate_docs.py` to regenerate. Run
`python scripts/generate_docs.py --check` for read-only drift lint (exit 1 for
changed, missing or orphaned managed Markdown; exit 0 for an exact mirror).

Each content mirror is exactly **source frontmatter + Unicode-arrow navigation
line + two LF bytes + source body**. Provider/model paths retain their existing
flattened documentation names. Patterns have individual mirrors under
`docs/patterns/<category>/<file>.md`; the hand-written `docs/patterns/*.md`
overviews are preserved. Generated prompt indexes are also checked for drift.

The ERA 3.A inventory at HEAD `135c222` contains **290 prompts + 19 patterns**,
including 155 model-optimized prompts. The supplied 292/157 inventory does not
match that tree; no missing content has been invented to meet those totals.
