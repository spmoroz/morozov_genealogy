"""Scan a public repo checkout for data about living persons before pushing.

Builds a list of identifying strings for every ID in LIVING/MINORS from the
full (private) index.html: full names, first name + patronymic, surnames that
belong only to living people, maiden names. Then searches every text file in
the public directory except index.html (the masked page is generated and
already checked by mask_living.py) and exits 1 on any hit.

Usage: python3 tools/check_public.py PRIVATE_INDEX PUBLIC_DIR
"""
import json
import os
import sys

from mask_living import LIVING, MARK, MINORS

TEXT = (".md", ".json", ".txt", ".py", ".html", ".csv", ".ged")


def needles(d):
    hidden = LIVING | MINORS
    by_id = {p["id"]: p for p in d["persons"]}
    surnames_dead = {s for p in d["persons"]
                     if p["id"] not in hidden and len(p["name"].split()) > 1
                     for s in p["name"].split()[-1].split("/")}
    out = {}
    for pid in hidden:
        p = by_id[pid]
        if p["name"] == "Живой родственник":  # placeholder, real name lives only in private data
            continue
        parts = p["name"].split()
        cands = {p["name"]} if len(parts) > 1 else set()
        if len(parts) > 2:
            cands.add(" ".join(parts[:2]))
        if len(parts) > 1:
            cands |= {f"{parts[0]} {parts[-1]}", f"{parts[0]} ({parts[-1]})"}
        for s in [parts[-1] if len(parts) > 1 else "", p.get("maiden_name", "")]:
            if s and s not in surnames_dead:
                cands.add(s)
        out[pid] = {c for c in cands if len(c) > 3}
    return out


def main(src, pub):
    s = open(src, encoding="utf-8").read()
    i = s.index(MARK) + len(MARK)
    d, _ = json.JSONDecoder().raw_decode(s[i:])
    nd = needles(d)
    hits = []
    for root, dirs, files in os.walk(pub):
        dirs[:] = [x for x in dirs if x != ".git"]
        for f in files:
            path = os.path.join(root, f)
            if not f.endswith(TEXT) or os.path.relpath(path, pub) == "index.html":
                continue
            text = open(path, encoding="utf-8", errors="ignore").read()
            for pid, cands in nd.items():
                hits += [(os.path.relpath(path, pub), pid, c) for c in cands if c in text]
    for h in hits:
        print("LEAK %s: %s (%s)" % h)
    print("OK, no living-person strings found" if not hits else f"{len(hits)} hit(s); fix before pushing")
    sys.exit(1 if hits else 0)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
