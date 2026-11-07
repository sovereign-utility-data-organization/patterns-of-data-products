# AGENTS.md

This repo is not code. It is a knowledge catalog conforming to
[Open Knowledge Format (OKF) v0.1](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md):
a directory of markdown concept docs with YAML frontmatter, section indexes,
and an update log. There is no test suite; the local gate is the audit script.
A **derived** build (see "Publishing") renders this bundle into a GitHub Pages
site but treats the bundle as read-only source of truth and never rewrites it.

## Verification

- After **every** edit: `python3 scripts/okf_audit.py` — must finish with zero
  ERRORs (WARNs are index-style advisories).
- The audit checks frontmatter fields and format, ISO-8601 `timestamp`, and
  that every internal `/…` link resolves to an existing concept doc or section
  index. It ignores the generated build outputs (`site-src/`, `site/`).

## Publishing (GitHub Pages)

The canonical bundle stays the source of truth and strictly conformant; a
derived build publishes it to GitHub Pages without ever modifying it. No Docker,
no framework, no native extensions — just Python (stdlib + `python-markdown`):

- `scripts/build_site.py` — reads the bundle and writes a **finished** static
  site to `site/`: rewrites each OKF internal link to a path a static host
  resolves (relative, `.html`/section `index.html`/asset), renders every page to
  HTML, wraps each in a shared layout with a global search bar, and emits a
  dependency-free JSON search index. Self-validates that every link + search URL
  resolves; exits non-zero if any do not.
- `.github/workflows/pages.yml` — GitHub Actions on a plain `ubuntu-latest`
  runner: checkout, `setup-python`, `pip install markdown`, run the script
  (→ `site/`), upload the artifact, deploy to GitHub Pages. Triggers on push to
  `main`. Requires the repo's Pages **Source** to be set to **GitHub Actions**.

`site/` is a build artifact — gitignored, never committed.

## Layout (what lives where)

- `index.md` — root listing; `log.md` — update log, **newest entry first**
- `knowledge-concepts/` — core vocabulary (data product, B/R/S/H patterns,
  synthetic stream, cross-cutting observations, verdict)
- `data-product-types/` — 225 docs, one per interface cell (15 IN × 15 OUT),
  named `in-{IN}-out-{OUT}.md`, plus the matrix index
- `playbooks/` — how-to docs
- `assets/` — the 4-pattern interface figure
  (`all-possible-interaction-patern-data-product.svg`), the 49-cell (3-pattern)
  grid SVG, and per-cell SVGs under `assets/cells/`: the 49 original cells as
  `NNN.svg`, the 176 H-cells as `in-{IN}-out-{OUT}.svg`
- `AGENTS.md` and `README.md` are meta files exempted from the OKF rules in
  `scripts/okf_audit.py` — keep that exemption in sync if the audit changes.

Stale references: `README.md` still points at `docs/*` paths; that content was
absorbed into the bundle and removed (see `log.md`).

## Format rules (enforced by the audit)

- Every concept doc has YAML frontmatter: `type`, `okf_version: '0.1'`,
  `timestamp` (ISO 8601; bump it when editing), `description`.
- `index.md`, `log.md`, `README.md`, `AGENTS.md` must **not** have frontmatter.
- All internal links are **bundle-root absolute, extensionless**:
  `/knowledge-concepts/data-product`, or `/data-product-types/` (a directory
  link resolves to that section's `index.md`). Don't use relative links between
  sections.
- `index.md` files contain only headings and bullet entries (a linked label to
  an extensionless root path, plus a short description); every concept doc in
  the section is listed there.
- Cell numbering: row = IN, column = OUT; both sides enumerated 1–15 as
  BRS, BR, BS, RS, S, R, B (the 7 machine-only states), then BRSH, BHR, BHS,
  RSH, SH, RH, BH, H (the 8 human states). E.g. `in-rs-out-r` is
  **Cell 4.6**; `in-h-out-r` is **Cell 15.6**.
- Cell diagrams: each cell page embeds one figure — an
  `![Interface diagram: IN {IN} to OUT {OUT}](assets/cells/CELL.svg)` line —
  placed between the intro and `## When to use`, with a leading `/` in the real
  link. The 49 originals point at an **arbitrary** `NNN.svg` (not derivable
  from the name); the 176 H-cells point at `in-{IN}-out-{OUT}.svg` (derivable
  name, distinct from the `NNN.svg`). Never renumber or regenerate the 49
  `NNN.svg`; the H-cell SVGs are generated from the interaction figure by
  keeping the Data Product box plus the IN-state icons (left) and OUT-state
  icons (right) per pattern band. Asset `.svg` links are audit-checked, so the
  real ones must resolve.

## Change workflow

1. Edit the concept doc (frontmatter + body).
2. Keep the section `index.md` entry and any `related:` fields / cross-links
   consistent with the doc — broken links fail the audit.
3. Add a dated entry at the **top** of `log.md` (newest first, prose, no
   frontmatter).
4. `python3 scripts/okf_audit.py` clean → commit / push.

## Repo conventions

- Anything named in the catalog (standards, specs, sources) must be real and
  verifiable. If a reference can't be resolved to an actual source, remove it
  — never create placeholder entries.
- GitHub remote `origin` (org `sovereign-utility-data-organization`, repo
  `patterns-of-data-products`); single branch `main`.
