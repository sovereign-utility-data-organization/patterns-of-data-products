# Update log

## 2026-11-07

Licensed the catalog content under Creative Commons
Attribution-ShareAlike 4.0 International (CC BY-SA 4.0): added a
`LICENSE` file with the full legal code (recognized by GitHub, so the
repo now displays a CC BY-SA 4.0 license chip) and a "License" section
in `README.md` pointing to it. Derivative works must carry the same
license; the audit is clean.

## 2026-11-07

Restored the missing "Data Product" label on the 49 original cell
diagrams under `assets/cells/` (the `NNN.svg` files), whose center box
was blank while all 176 H-cell SVGs kept the label. Each label is
placed at the same position inside the center box and uses the same
text style and sizing (relative to the box) as the H-cell labels, so
the two families of diagrams now look uniform. Nothing else in the
SVGs was changed — names and file references are untouched, the
`NNN.svg` mapping was not renumbered, and the site build was run
against the updated assets; the audit is clean.

Added a collapsible sidebar page tree to the static site build
(`scripts/build_site.py`, derived build only — the bundle itself is
unchanged). The tree is generated from each section's `index.md`
(Home, Knowledge Concepts, Data Product Types grouped by In-state row,
Playbooks, plus Log and README), so it can never drift from the catalog.
The current page is highlighted and its section and row start expanded;
the other sections start collapsed, and on narrow screens the whole tree
slides in behind a "Pages" toggle in the header. Rebuilt with
`python3 scripts/build_site.py` (self-validation passes); the OKF audit
is clean.

Removed the opaque full-canvas black background `<rect fill="#000000"/>`
that the 49 original cell diagrams under `assets/cells/` (the `NNN.svg`
files) carried in front of their content, so every diagram in the catalog
now renders on a transparent background and adapts to light or dark page
themes. The 176 H-cell SVGs and the two interface figures already had no
background. Only the SVG assets were touched — no content, naming, or
linking changed.

## 2026-11-07

Corrected two recurring claims in the human-pattern cells. **(1) Synthetic
stream is defined by event provenance, not by pattern letter.** The rule
*S in OUT, not in IN ⇒ synthetic* is now a red flag, not the definition: a
stream is synthetic only when the product *manufactures* the events it emits,
off a state-only source (event time = observation time). A human action
delivered through the product's own surface — a submission, an approval, an
entry — is itself a discrete, real event, and relaying such actions as a feed
is a **trigger-based** stream, not a synthetic one, even though the IN side
carries no `S`. [synthetic stream](/knowledge-concepts/synthetic-stream) is
redefined around that distinction, cross-cutting observation #1 softened to
match, and the classify playbook's pseudo-stream note now asks "how are the
events made?" before asserting synthesis. All **32 H-in → S-out cells**
(rows `BHR`, `RH`, `BH`, `H`) now present both shapes — the five contract
items apply only to the observed-state shape — and 27 "typical next step" feed
annotations on those rows no longer assert "synthetic, since S is absent
from IN"; the 9 annotations citing the machine-side family (rows `BR`/`R`/`B`)
are unchanged, since a state-only source by definition manufactures its feed.
**(2) Cell 15.15 is named for what it is.** H in → H out is the
**pre-automation pattern**: a shared record between people, no machine
mediation on either side — analog in that sense, not in the sense of paper
(the Word document, the spreadsheet, the wiki page are this cell too). The
cell's title, intro, and verdict rationale are rewritten to own that framing
(verdict stays *plausible*), and the cross-cutting observation #5 and the
type-matrix index entry are updated to match.

## 2026-11-07

Added a **Publishing** pipeline so the catalog is browsable with working links
on GitHub. The problem: OKF internal links are bundle-root-absolute and
extension-less by design, which an OKF renderer resolves but GitHub (repo view
*and* a project Pages site) does not, so every cross-page link 404s. The fix
keeps the bundle strictly conformant and does the translation in a derived
build. `scripts/build_site.py` (Python; only dependency is `python-markdown`)
reads the bundle and writes a **finished** static site to `site/`: it rewrites
each internal link to a path a static host resolves (relative, `.html`/section
`index.html`/asset), renders every page to HTML, wraps each in a shared layout
with a global search bar, and emits a dependency-free JSON search index; it
self-validates that every link and search URL resolves (exit non-zero otherwise).
`.github/workflows/pages.yml` builds it in GitHub Actions on a plain
`ubuntu-latest` runner (checkout, `setup-python`, `pip install markdown`, run the
script) and deploys to GitHub Pages. No Docker, no framework, no native
extensions. `site/` is a gitignored build artifact; the canonical `*.md` and
`assets/` are never rewritten. `scripts/okf_audit.py` skips the generated site so
the conformance gate stays clean regardless. `AGENTS.md` and `README.md` document
the pipeline.

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
