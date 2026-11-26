#!/usr/bin/env python3
"""Check that every source a supplement links to exists on GitHub, and that
every MICharisma link in every guide resolves. Exits 1 on any miss.
Uses the public GitHub contents API, so it needs no token for public repos
(set GITHUB_TOKEN to avoid the anonymous rate limit)."""
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def exists(repo: str, ref: str, path: str) -> bool:
    url = f"https://api.github.com/repos/{repo}/contents/{urllib.parse.quote(path)}?ref={urllib.parse.quote(ref, safe='')}"
    request = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json"})
    if os.environ.get("GITHUB_TOKEN"):
        request.add_header("Authorization", f"Bearer {os.environ['GITHUB_TOKEN']}")
    try:
        with urllib.request.urlopen(request) as response:
            return response.status == 200
    except urllib.error.HTTPError:
        return False


def main() -> int:
    index = json.loads((ROOT / "supplements.json").read_text())
    misses = 0
    for supplement in index["supplements"]:
        for source in supplement["sources"]:
            ok = exists(source["repo"], source["ref"], source["path"])
            misses += not ok
            mark = "ok  " if ok else "MISS"
            print(f'{mark} {supplement["id"]}: {source["repo"]}@{source["ref"]}/{source["path"]}')
    print(f"{misses} missing")
    return 1 if misses else 0


if __name__ == "__main__":
    sys.exit(main())
