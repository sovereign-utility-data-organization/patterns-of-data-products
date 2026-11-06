#!/usr/bin/env python3
"""OKF v0.1 conformance audit for this bundle."""
import os, re, sys, datetime

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
os.chdir(ROOT)
errors, warns = [], []

all_md = []
for dp, dns, fns in os.walk("."):
    dns[:] = [d for d in dns if d not in (".git", "__pycache__")]
    for fn in fns:
        if fn.endswith(".md"):
            all_md.append(os.path.normpath(os.path.join(dp, fn)))
all_md = sorted(set(m for m in all_md if not m.startswith(".git")))

def fm_of(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    return text[4:end], text[end+5:]

# 1. Frontmatter checks
for m in all_md:
    text = open(m).read()
    if m in ("index.md", "log.md", "README.md") or os.path.basename(m) == "index.md":
        if text.startswith("---"):
            errors.append(f"{m}: index/log/README must not have frontmatter")
        continue
    fm_str, body = fm_of(text)
    if fm_str is None:
        errors.append(f"{m}: missing valid YAML frontmatter block")
        continue
    fm = {}
    for line in fm_str.splitlines():
        km = re.match(r'^([a-zA-Z_]+):\s*(.*)$', line)
        if km and not line.startswith(" "):
            fm[km.group(1)] = km.group(2)
    for req in ("type", "okf_version", "timestamp", "description"):
        if not fm.get(req, "").strip():
            errors.append(f"{m}: missing required frontmatter field '{req}'")
    if fm.get("okf_version", "").strip().strip('"') != "0.1":
        errors.append(f"{m}: okf_version must be \"0.1\", got {fm.get('okf_version')!r}")
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

# 2. Cross-link checks: every (/...) link is bundle-ROOT-relative; resolve from cwd (= bundle root)
link_re = re.compile(r'\]\((/[^)#\s]+)\)')
for m in all_md:
    for link in link_re.findall(open(m).read()):
        raw = link.lstrip("/").rstrip("/")
        if raw.endswith((".svg", ".png", ".jpg", ".toml", ".yaml")):
            if not os.path.exists(raw):
                errors.append(f"{m}: broken asset link {link}")
            continue
        cand = raw if raw.endswith(".md") else raw + ".md"
        if not os.path.exists(cand):
            cand = raw + "/index.md"
            if not os.path.exists(cand):
                errors.append(f"{m}: broken internal link {link}")

# 3. index entry format: bullets, headings, blank lines only
for m in all_md:
    if os.path.basename(m) == "index.md":
        for i, line in enumerate(open(m), 1):
            if line.strip() and not line.lstrip().startswith(("#", "*", "-")):
                warns.append(f"{m}:{i}: non-bullet/non-heading line: {line.strip()[:60]}")

print(f"checked {len(all_md)} markdown files")
for w in warns:
    print("WARN ", w)
for e in errors:
    print("ERROR", e)
sys.exit(1 if errors else 0)
