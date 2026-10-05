"""Mask living persons in index.html before publishing.

Living adults keep first name + surname initial and their relationships;
dates, places, maiden names and notes are removed. Minors stay fully hidden.
Family notes that touch a living person are cleared (they used to leak
minors' first names). Idempotent: safe to run again after data edits.

Usage: python3 tools/mask_living.py SRC [DST]
  SRC: full (unmasked) page from the private repo; DST defaults to SRC.
"""
import json
import sys

# Kept unmasked: the site owner.
OWNER = {"P001"}
MINORS = {"P005", "P007", "P008", "P014"}
# Persons presumed living (no death record, born after ~1926 or recent generation).
LIVING = {
    "P002", "P003", "P004", "P006", "P009", "P010", "P011", "P012", "P013",
    "P015", "P016", "P017", "P018", "P019", "P109", "P110", "P210", "P220",
    "P221", "P222", "P231", "P232", "P233", "P148", "P094", "P095",
}
MARK = "const DATA = "
NOTE = "Живущий человек: личные данные скрыты"


def short_name(name):
    parts = name.split()
    if len(parts) < 2 or parts[-1].endswith("."):
        return name
    return f"{parts[0]} {parts[-1][0]}."


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
    out = json.dumps(mask(d), ensure_ascii=False, indent=1)
    open(dst, "w", encoding="utf-8").write(s[:i] + out + s[i + end:])


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else "index.html"
    main(src, sys.argv[2] if len(sys.argv) > 2 else src)
