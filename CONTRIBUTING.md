# Contributing a supplement

1. Pick two or more multivitamins whose libraries a real project would use
   together. If one of them only appears in passing, it's not a supplement.
2. Read the source scenarios before writing. Every API name in a guide must
   appear in a linked scenario, or be labeled as coming from outside the
   repos.
3. Copy the section order from any existing guide.
4. Use the family's house rules: realistic names, no placeholder names,
   places mostly outside the USA, varied institutions. Places that already
   recur in the catalogs (Kiruna, Warsaw, Bergen, Oaxaca, Punta Arenas) are
   welcome.
5. Add the guide to `supplements.json` with a hand-written title, summary,
   `combines`, and `scenario`. Then run `python3 scripts/index_sources.py`
   to fill in `sources`, and `python3 scripts/check_sources.py` to check them.
