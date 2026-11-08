# Update log

## 2026-11-08

Re-based the **definition of a data product** on the data-mesh sources it
claims to follow — Z. Dehghani, *Data Mesh Principles and Logical
Architecture* ([martinfowler.com](https://martinfowler.com/articles/data-mesh-principles.html))
and *Data Mesh Architecture*
([datamesh-architecture.com](https://www.datamesh-architecture.com/)) — and
**removed the "contract" element from the definition of a product**. The
catalog had defined a product as "data + contract + interface(s)", but the
sources treat a contract as precisely the *interface* specification
("While a data contract represents the interface specification, the actual
implementation that provides the data is the output port of a data product"),
so it does not belong in the product's identity. The definition now follows
the sources: a data product is the fundamental unit of data architecture —
an **architectural quantum** — holding a domain's data plus what makes it
usable (semantics, schema, quality metrics, provenance, documentation), the
code that processes and serves it, and the infrastructure to run it; it is
**owned by the domain team closest to the data**, which is accountable for
quality, availability, and cost; and it is served through **one or more
output ports** (interfaces) — "served as events, batch files, relational
tables, graphs, etc., while maintaining the same semantic". Identity is the
data a team offers; different shapes are different ports of the same
product. Updated: the canonical definition in
[data product](/knowledge-concepts/data-product) (new frontmatter
description, "Identity vs. interface" section rewritten on the sources,
"no contract" boundary case rephrased), the home page (`index.md`),
`README.md`, the section-index bullet, "interface contract" →
"domain-owned offering" in [architectural paradigms](/knowledge-concepts/architectural-paradigms),
and step 1 of the [classify playbook](/playbooks/classify-a-data-product)
("what distinguishes a data product from a raw table" is now team ownership
plus usable semantics/quality, not *the contract*). The word *contract*
survives only where it legitimately belongs — as the interface-level
specification in cell and pattern docs (e.g. the synthetic stream's "five
contract items"). Audit and build are clean.

## 2026-11-08

Fixed the definition of "data product" in the three pages that stated it:
the home page (root `index.md`), `README.md`, and
[data product](/knowledge-concepts/data-product) all claimed that how data
is exposed is what makes products different — "a file drop, a query API, and
an event stream of the same records are three different data products" —
which was the exact opposite of the data-mesh idea of a data product and
contradicted the rest of the catalog (its multi-interface side states, e.g.
omni-channel `BRS`-out = one product, three legs). The definition now states
what a data product is *in the sense of data mesh* (a self-contained,
domain-owned offering of data + contract + one or more interfaces), that a
product's **identity** is the data it offers and the contract it serves
under, and that the interface is only how it is exposed: the same records
served as a file, an API, and a stream are **one** data product through
several interfaces (the flour, not the pack size); adding an interface moves
its **type** (the catalog's cell), not its identity. What this catalog
classifies is the product's **type**, not the product itself.
`knowledge-concepts/data-product.md` gains an "Identity vs. interface"
section that makes the distinction explicit and ties it to data mesh;
`SITE_DESC` in `scripts/build_site.py` and the two stale "7×7 grid"
references (playbook description and its index entry) were aligned with the
15×15/225-type space — the playbook's B/R/S bullet lists now carry the
`H` human pattern too. Audit and build are clean.

## 2026-11-08

Added the missing interface labels to the 49 hand-authored original cell
diagrams (`assets/cells/NNN.svg`, the 3-pattern B/R/S matrix, cells 1.1–7.7).
Those tiles had been cropped out of the master
`assets/all-possible-data-product-patterns.svg` canvas without their
`Streaming`/`Request/Response`/`Batch` captions, so their interface icons were
unlabeled while the equivalent generated `in-*` cells kept theirs — an
inconsistency. Each missing caption was copied verbatim from the master canvas
(the already-labeled source of truth) into the coordinates that already sit
within each cell's own `viewBox`, so every icon now carries the same label the
generated diagrams use. The icon art, the `NNN` numbering, and the
master/generated figures were left untouched — 168 captions added across the 49
files. With this, every interface icon across all 225 cell diagrams and both
top-level figures has its label, and the audit is clean.

## 2026-11-08

Reworked the per-cell **verdict** assessment for the 176 human-pattern cells. The
verdict body had been four shared boilerplate sentences — "source is human",
"people are the source and people read the data back", "reports/dashboards are
among the most common ways people consume data", and a variant — repeated
verbatim across whole rows and columns (measured: four distinct bodies covered
172 of the 225 cells). Each H-cell verdict now states that cell's specific
purpose from its own leg composition ("a product that ingests X and serves Y")
and **states the value premise in place**: human input is the softest and
costliest channel (so it is "not a default pipe"), and where the human act is
the irreplaceable value it is the value-driver that the machine legs *enrich*.
That promotes the `role-of-human-input` value-driver framing from a post-hoc
side doc to a first-class premise of the cell's own verdict, and removes the
shared boilerplate — the verdict field is now unique to every cell (all 225
distinct). Tiers (common / plausible / niche) and every other section are
preserved; the `State & cost` sharing that remains is leg-composition-driven and
cell-neutral by construction, not boilerplate.

## 2026-11-08

Fixed two framework gaps found on review. (1) `verdict.md`'s "Reading the
distribution" claimed the `niche` verdicts cluster in a "fully synthetic
consolidation" family that does **not** exist in the data — the wide
omni-channel cells [1.1](/data-product-types/in-brs-out-brs),
[1.8](/data-product-types/in-brs-out-brsh), and
[8.8](/data-product-types/in-brsh-out-brsh) are all rated *common*. In fact all
thirteen niche cells serve a stream (an `S` on the output side): nine are
synthetic-stream bridges (stream out over a state-only machine source), and four
([1.5](/data-product-types/in-brs-out-s),
[3.4](/data-product-types/in-bs-out-rs),
[4.5](/data-product-types/in-rs-out-s),
[5.4](/data-product-types/in-s-out-rs)) are deliberately narrow / fileless
surfaces kept out of *common* by a scope decision, not an economic hazard. The
section now states that. (2) `pattern-human.md`'s H-out section no longer
demotes the human pattern to a "consumption audience": `H`-out is now defined
affirmatively as a **presentation-and-consolidation** transform (not a 1:1
projection), with the note that human-shaped output — a report — is often itself
the *input* to a downstream machine. Timestamps bumped. The H-in **value-driver**
premise (the `role-of-human-input` framing) is already stated first-class in the
framework pages; making it the per-cell verdict's premise is a separate change.

## 2026-11-08

Corrected three factual errors found on review. `verdict.md` and
`architectural-paradigms.md` still described the pre-expansion **49**-cell
space; both now say **225** (the 49 original machine-only cells and the 49-cell
grid figure are unchanged, still named where they genuinely are the subject).
`verdict.md` also claimed the verdict is stored in a `verdict` frontmatter
field; in practice it is a **tag** in `tags:` plus a `## Verdict` body section
— "Where the verdicts are stored" now matches that and no longer asserts a
nonexistent field. `README.md`'s Contributing line pointed at the long-removed
`docs/classification.md`; it now points at the
[classify playbook](/playbooks/classify-a-data-product) and the knowledge
concepts.

## 2026-11-08

Gave human input the role the catalogue kept reserving for it but never naming.
Human-input cells described `H` almost exclusively through its cost side —
"the softest input" appeared in all 120 human-input watch-outs, and "a
curation product, not a default pipe" in most verdicts — which read as
*undervalued*. The fix separates three facts the catalogue had conflated into
one adjective: **softness** is a quality-and-cost property (irregular,
subjective, error-prone, expensive to re-issue — kept as the
validation/provenance/correction caveat); **automate-where-possible** is the
default, which is exactly why `H`-in is the costlier, *reserved* channel and
why the `plausible`/"not a default pipe" tiers **stay**; and
**irreplaceability** is what makes human input central — where the human act
*is* the value (a judgement, a design intent, content, an accountable
decision), it is the product's **value-driver** and the machine legs exist to
*enrich*. New concept doc
[role of human input](/knowledge-concepts/role-of-human-input) carries the
full argument (including the H×B/R/S interactions and what the verdict
asymmetry means); `pattern-human`, cross-cutting observation #5, and the
verdict page are aligned and linked. All 120 human-input cells now carry the
reframed watch-out (softness-as-cost + value-driver reading, linked to the new
doc); the 118 generic verdict rationales are reframed as *cost and scarcity,
not value* — the tiers themselves are unchanged (15.15 and the
consolidated-BI cell keep their own).

## 2026-11-07

Gave the catalog a proper home page. The root `index.md` was a bare
three-bullet listing; it is now the entry page of the published site:
a description of what a data product is and of the interface model (the four
patterns B/R/S/H, the 15 side states, and why 15 × 15 = 225 types), the
all-interface figure (`assets/all-possible-interaction-patern-data-product.svg`),
the full 225-type matrix table (every cell links to its type page), and the
section listing. The state table and the matrix on the home page are a
verbatim copy of those in `knowledge-concepts/data-product.md` — keep the
two in sync when the matrix changes. Because the root `index.md` is a home
page rather than a section listing, `scripts/okf_audit.py` now exempts it
from the bullet-only "index entry" rule (section indexes stay checked;
no-frontmatter and link checks still apply to it). `AGENTS.md` and
`README.md` document the new role of the home page. Audit and build are
clean.

## 2026-11-07

Fixed the Pages build that the new license section broke: the README's
`## License` section links to the repo's `LICENSE` file, but the static
build only ever copied `assets/` and rendered pages, so the self-validation
("every href in the site must resolve to a real file") failed on
`README.html -> LICENSE`. `scripts/build_site.py` now also copies root
static files (`LICENSE`) to the site root, so the published site carries
the license text and the link resolves; `AGENTS.md`'s builder description
was updated to match. Build and audit are clean.

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
