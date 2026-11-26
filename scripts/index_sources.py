#!/usr/bin/env python3
"""Refresh the `sources` list of each supplement in supplements.json from the
MICharisma links in its guide README. Titles, summaries, and `combines` are
edited by hand; sources are always derived, so they can't drift from the
guide text."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFS = r"(?:main|highlighting-trial|gh-pages|cursor/multivitamin-web-v1-b7f7|cursor/terminal-multivitamin-v1-43fa)"
LINK = re.compile(
    r"\(https://github\.com/MICharisma/([\w-]+)(?:/(?:tree|blob)/(" + REFS + r")(?:/([^)\s#]*))?)?(?:#[^)]*)?\)"
)
LIBRARY = {
    "rubyllm-multivitamin": "rubyllm",
    "phoenix-multivitamin": "phoenix",
    "stimulus-multivitamin": "stimulus",
    "swiftdata-multivitamin": "swiftdata",
    "terminal-multivitamin": "terminal",
    "multivitamin-web": "multivitamin-web",
}


def sources_for(guide: Path):
    seen, found = set(), []
    for repo, ref, path in LINK.findall(guide.read_text()):
        if repo not in LIBRARY:
            continue
        key = (repo, ref or "main", path or "")
        if key in seen:
            continue
        seen.add(key)
        found.append({"multivitamin": LIBRARY[repo], "repo": f"MICharisma/{repo}",
                      "ref": key[1], "path": key[2]})
    return found


def main():
    index_path = ROOT / "supplements.json"
    index = json.loads(index_path.read_text())
    for supplement in index["supplements"]:
        supplement["sources"] = sources_for(ROOT / supplement["folder"] / "README.md")
    index_path.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n")
    for supplement in index["supplements"]:
        print(f'{supplement["id"]}: {len(supplement["sources"])} sources')


if __name__ == "__main__":
    main()
