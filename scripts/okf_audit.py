#!/usr/bin/env python3
"""OKF v0.1 conformance audit for this bundle."""
import os, re, sys, datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
os.chdir(ROOT)
errors, warns = [], []

all_md = []
for dp, dns, fns in os.walk("."):
    # Skip VCS, caches, and the *generated* build outputs (site-src/, site/) --
    # those are derived artifacts, not part of the canonical OKF bundle.
    dns[:] = [d for d in dns if d not in (".git", "__pycache__", "site-src", "site")]
    for fn in fns:
        if fn.endswith(".md"):
            all_md.append(os.path.normpath(os.path.join(dp, fn)))
all_md = sorted(set(m for m in all_md if not m.startswith(".git")))

def fm_of(text, fname):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    # closing fence is the 4 chars "\n---" starting at `end`; body begins at end+4
    body = text[end + 4:]
    # closing fence must be on its own line: the next char after --- must be a newline
    if body and not body.startswith("\n"):
        errors.append(f"{fname}: frontmatter closing fence is not on its own line (missing newline after ---)")
    return text[4:end], text[end + 4:]

try:
    import yaml as _yaml
except ImportError:
    _yaml = None

# 1. Frontmatter checks
for m in all_md:
    text = open(m).read()
    if m in ("index.md", "log.md", "README.md", "AGENTS.md") or os.path.basename(m) == "index.md":
        if text.startswith("---"):
            errors.append(f"{m}: index/log/README must not have frontmatter")
        continue
    fm_str, body = fm_of(text, m)
    if fm_str is None:
        errors.append(f"{m}: missing valid YAML frontmatter block")
        continue
    if _yaml is not None:
        try:
            fm = _yaml.safe_load(fm_str)
            if not isinstance(fm, dict):
                errors.append(f"{m}: frontmatter is not a mapping")
                fm = {}
        except Exception as e:
            errors.append(f"{m}: frontmatter is not valid YAML: {e}")
            fm = {}
        # description is NOT an OKF requirement (only `type` is) and this
        # bundle's one-line summary is the SKOS `definition` key.
        for req in ("type", "okf_version", "timestamp", "definition"):
            if not str(fm.get(req, "")).strip():
                errors.append(f"{m}: missing required frontmatter field '{req}'")
        if str(fm.get("okf_version", "")).strip() != "0.1":
            errors.append(f"{m}: okf_version must be \"0.1\", got {fm.get('okf_version')!r}")
        # SKOS metadata (house convention, see AGENTS.md): skos:example may be
        # a scalar or a list; skos:altLabel must be a non-empty list.
        ex = fm.get("example")
        if not (isinstance(ex, list) and ex and all(str(x).strip() for x in ex)
                or isinstance(ex, str) and ex.strip()):
            errors.append(f"{m}: missing or invalid SKOS 'example' frontmatter field")
        al = fm.get("altLabel")
        if not (isinstance(al, list) and al and all(str(x).strip() for x in al)):
            errors.append(f"{m}: missing or invalid SKOS 'altLabel' frontmatter field (non-empty list)")
    else:
        fm = {}
        for line in fm_str.splitlines():
            km = re.match(r'^([a-zA-Z_]+):\s*(.*)$', line)
            if km and not line.startswith(" "):
                fm[km.group(1)] = km.group(2)
        # `definition` (SKOS) is this bundle's one-line summary; `description`
        # is not an OKF requirement and is intentionally absent.
        for req in ("type", "okf_version", "timestamp", "definition"):
            if not fm.get(req, "").strip():
                errors.append(f"{m}: missing required frontmatter field '{req}'")
        if not re.search(r"^example:\s*\S", fm_str, re.M):
            errors.append(f"{m}: missing required SKOS 'example' frontmatter field")
        if not re.search(r"^altLabel:\s*\n((?:-[^\n]*\n?)+)", fm_str, re.M):
            errors.append(f"{m}: missing required SKOS 'altLabel' frontmatter field (non-empty list)")
    ts = fm.get("timestamp", "").strip().strip('"')
    if ts:
        ok = False
        for fmt in ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%d"):
            try:
                datetime.datetime.strptime(ts, fmt); ok = True; break
            except ValueError:
                pass
        if not ok:
            try:
                datetime.datetime.fromisoformat(ts.replace("Z", "+00:00")); ok = True
            except ValueError:
                pass
        if not ok:
            errors.append(f"{m}: timestamp {ts!r} is not ISO 8601")

# 2. Cross-link checks: every (/...) link is bundle-ROOT-relative; resolve from cwd (= bundle root).
#    Includes both markdown links `](/…)` and the `related:` frontmatter list.
link_re = re.compile(r'\]\((/[^)#\s]+)\)')
related_targets = []   # (file, target)
for m in all_md:
    text = open(m).read()
    for link in link_re.findall(text):
        related_targets.append((m, link))
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        fm_str = text[4:end] if end != -1 else None
        if fm_str and re.search(r"^related:\s*$", fm_str, re.M):
            block = re.search(r"^related:\s*\n((?:-[^\n]*\n?)+)", fm_str, re.M)
            if block:
                for line in block.group(1).splitlines():
                    pm = re.match(r"^-\s*(/\S+)", line)
                    if pm:
                        related_targets.append((m, pm.group(1)))

for m, target in related_targets:
    raw = target.lstrip("/").rstrip("/")
    if raw.endswith((".svg", ".png", ".jpg", ".toml", ".yaml")):
        if not os.path.exists(raw):
            errors.append(f"{m}: broken asset link {target}")
        continue
    cand = raw if raw.endswith(".md") else raw + ".md"
    if not os.path.exists(cand):
        cand = raw + "/index.md"
        if not os.path.exists(cand):
            errors.append(f"{m}: broken internal link {target}")

# 3. index entry format: bullets, headings, blank lines only (section listings)
#    The ROOT index.md is the site home page (prose, figures, the full matrix),
#    not a section listing, so it is exempt from this bullet-only check.
for m in all_md:
    if os.path.basename(m) == "index.md" and m != "index.md":
        for i, line in enumerate(open(m), 1):
            if line.strip() and not line.lstrip().startswith(("#", "*", "-")):
                warns.append(f"{m}:{i}: non-bullet/non-heading line: {line.strip()[:60]}")

print(f"checked {len(all_md)} markdown files")
for w in warns:
    print("WARN ", w)
for e in errors:
    print("ERROR", e)
sys.exit(1 if errors else 0)
