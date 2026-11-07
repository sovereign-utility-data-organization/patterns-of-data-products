# Update log

## 2026-11-07

Migrated the bundle from the self-hosted Gitea instance to GitHub. It now lives
at
<https://github.com/sovereign-utility-data-organization/patterns-of-data-products>
(public; GitHub repo name `patterns-of-data-products`, local working directory
still `data-product-classification`). The whole `main` branch and its commit
history were pushed unchanged — no rewrites, no cherry-picks, no tags introduced.
`origin` now points at the GitHub repo and the Gitea remote was retired; the
single-branch-`main` convention is unchanged. `AGENTS.md` "repo conventions"
updated to name the GitHub home instead of Gitea. Audit clean.

## 2026-11-07

Added an **interface diagram** to each of the 176 new human-pattern cells.
Each page now embeds a
`![Interface diagram: IN {IN} to OUT {OUT}](assets/cells/in-…).svg` line
(real links use a leading `/`, e.g. the cell 9.1 figure is
`/assets/cells/in-bhr-out-brs.svg`) between the intro and `## When to use` —
the same format and position as the 49 originals. The 176 SVGs are generated
from the 4-pattern interaction figure by keeping the Data Product box plus the
**IN-state icons on the left** and the **OUT-state icons on the right** (a
per-pattern band selection), so each figure shows exactly the patterns present
on each side of that cell (and only those). They are written to `assets/cells/`
under the derivable `in-….svg` name, distinct from — and never touching — the
49 original `NNN.svg`. (The interaction-figure filename this bundle references
is `all-possible-interaction-patern-data-product.svg`.) The audit now verifies
these asset links resolve; it still passes clean with 0 errors/warnings.

## 2026-11-06

Added **human (H)** as the fourth integration pattern, orthogonal to
batch/request-response/streaming, on **both** sides. Each side state is now any
non-empty subset of `{B, R, S, H}` → 15 states → a **15 × 15 = 225** type space
(was 7 × 7 = 49). Created all **176 new human-pattern cells** (every IN × OUT
pair with H on at least one side), each a full reference page: When to use,
What's inside, State & cost, Watch out, Typical next step (cross-referenced by
cell number), and a verdict. The original 49 cells keep their historical
numbering (1–7); the 8 human states are 8–15 (BRSH, BHR, BHS, RSH, SH, RH, BH,
H). Added a [human pattern](/knowledge-concepts/pattern-human) concept doc and
re-based the model: [data-product](/knowledge-concepts/data-product) now lists
4 patterns and the 15 × 15 quick map, [cross-cutting
observations](/knowledge-concepts/cross-cutting-observations) gains a fifth
observation (the human layer), and the [synthetic-stream
family](/knowledge-concepts/synthetic-stream) is re-counted at **56 cells**
(S in OUT, not IN). The `data-product-types/` index now lists all 225 cells.
The human-pattern interface figure lives at
`/assets/all-possible-interaction-patern-data-product.svg`; the 49-cell
(3-pattern) grid SVG and the 49 original cell pages are unchanged. The
OKF audit still passes clean.

## 2026-11-06

Elaborated all 49 data-product-type pages from "sparse" to full reference
pages. Each cell now carries, in addition to its original description,
when-to-use, and verdict: a **What's inside** note (the durable state and
serving stacks the cell implies), a **State & cost** note (what the cell stores
and where its cost lives), and a **Typical next step** (the integration pattern
most likely added next and the cell that results). The 12 synthetic-stream cells
(S in OUT, not IN) additionally carry a **Synthetic stream** section fixing the
five contract items. All new content is grounded in the catalog's own rules and
references the [cross-cutting observations](/knowledge-concepts/cross-cutting-observations),
[synthetic stream](/knowledge-concepts/synthetic-stream), and [verdict](/knowledge-concepts/verdict)
concepts; every existing description, verdict,
diagram, and Related entry is preserved verbatim. Frontmatter timestamps were
bumped; the OKF conformance audit still passes clean.

## 2026-11-06

Restructured the working documents into an OKF v0.1 conformant knowledge
catalog: added `knowledge-concepts/` (6 concept docs: data product, three
integration patterns, synthetic stream, cross-cutting observations),
`data-product-types/` (49 concept docs, one per interface combination, plus
matrix index), and `playbooks/` (classify-a-data-product procedure). Moved the
grid figure to `assets/`. `docs/classification.md` and `docs/options.md`
were absorbed into the bundle and removed (previous versions remain in git
history).

## 2026-11-06

Initial working document: decided the interface model — 3 integration
patterns (batch, request/response, streaming) × input/output sides → 7
side states → 7×7 = 49 data product types. Added the full-combination grid
figure and per-combination descriptions with usage conditions and verdicts.
