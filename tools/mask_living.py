"""Mask living persons in index.html before publishing.

Living adults keep first name + surname initial and their relationships;
dates, places, maiden names and notes are removed. Minors stay fully hidden.
Family notes that touch a living person are cleared (they used to leak
minors' first names). Idempotent: safe to run again after data edits.

Before writing, it refuses to publish if anyone looks living but is not
listed in LIVING/MINORS (no death record and an estimated birth year after
CUTOFF, estimated from relatives when the person has no date). Fix by adding
the ID to LIVING, or to DECEASED if you know the person has died.

Usage: python3 tools/mask_living.py SRC [DST]
  SRC: full (unmasked) page from the private repo; DST defaults to SRC.
"""
import json
import re
import sys
from datetime import date

# Kept unmasked: the site owner.
OWNER = {"P001"}
MINORS = {"P005", "P007", "P008", "P014"}
# Persons presumed living (no death record, born after ~1926 or recent generation).
LIVING = {
    "P002", "P003", "P004", "P006", "P009", "P010", "P011", "P012", "P013",
    "P015", "P016", "P017", "P018", "P019", "P109", "P110", "P210", "P220",
    "P221", "P222", "P231", "P232", "P233", "P148", "P094", "P095",
}
# Known deceased although the data has no death date (checked by the owner).
# P052, P124: deep ancestors; P053: wife of P052; P088: reserve NCO in 1890s records;
# P106: son of P103 (generation born c. 1900); P238: Mikhailov line, born c. 1900.
DECEASED = {"P052", "P053", "P088", "P106", "P124", "P238"}
CUTOFF = date.today().year - 100
MARK = "const DATA = "
NOTE = "Живущий человек: личные данные скрыты"


def short_name(name):
    parts = name.split()
    if len(parts) < 2 or parts[-1].endswith("."):
        return name
    return f"{parts[0]} {parts[-1][0]}."


def year(v):
    m = re.search(r"\d{4}", v or "")
    return int(m[0]) if m else None


def estimate_births(d):
    """Own birth year, else inferred from parents (+20), children (-25), spouses."""
    est = {p["id"]: year(p["birth_date"]) for p in d["persons"]}
    links = []
    for f in d["families"]:
        par = [x for x in (f["husband_id"], f["wife_id"]) if x in est]
        kids = [c.strip() for c in f["children_ids"].split(";") if c.strip() in est]
        links += [(c, x, 20) for c in kids for x in par]
        links += [(x, c, -25) for c in kids for x in par]
        if len(par) == 2:
            links += [(par[0], par[1], 0), (par[1], par[0], 0)]
    for _ in range(6):
        for who, src, delta in links:
            if est[who] is None and est[src] is not None:
                est[who] = est[src] + delta
    return est


def suspects(d):
    est = estimate_births(d)
    known = MINORS | LIVING | OWNER | DECEASED
    out = []
    for p in d["persons"]:
        if p["id"] in known or p["death_date"] or p["death_place"]:
            continue
        e = est[p["id"]]
        if e is None or e >= CUTOFF:
            out.append((p["id"], p["name"], e))
    return out


def mask(d):
    for p in d["persons"]:
        if p["id"] in MINORS:
            p.update(name="Живой родственник", maiden_name="", birth_date="",
                     birth_place="", notes="Данные о несовершеннолетнем скрыты")
        elif p["id"] in LIVING:
            p.update(name=short_name(p["name"]), maiden_name="", birth_date="",
                     birth_place="", notes=NOTE)
        else:
            continue
        p.update(death_date="", death_place="", source="", living=True)
    hidden = MINORS | LIVING | OWNER
    for f in d["families"]:
        kids = {c.strip() for c in f["children_ids"].split(";")}
        if f["husband_id"] in hidden or f["wife_id"] in hidden or kids & hidden:
            f.update(notes="", marriage_date="", marriage_place="")
    return d


def main(src, dst):
    s = open(src, encoding="utf-8").read()
    i = s.index(MARK) + len(MARK)
    d, end = json.JSONDecoder().raw_decode(s[i:])
    bad = suspects(d)
    if bad:
        print(f"Not published: {len(bad)} person(s) may be living and are not in LIVING/MINORS.")
        for pid, name, e in bad:
            print(f"  {pid} {name}: estimated birth {e or 'unknown'}")
        print("Add each ID to LIVING (or MINORS), or to DECEASED if known dead.")
        sys.exit(1)
    out = json.dumps(mask(d), ensure_ascii=False, indent=1)
    open(dst, "w", encoding="utf-8").write(s[:i] + out + s[i + end:])


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "index.html"
    main(src, sys.argv[2] if len(sys.argv) > 2 else src)
