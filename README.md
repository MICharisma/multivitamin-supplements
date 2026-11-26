# Multivitamin Supplements

Recipes for using two or more multivitamin libraries together.

Each multivitamin is a catalog of thirteen realistic scenarios per feature
for one library. A **supplement** is a recipe that combines two or more of
those libraries. It links back to the exact feature folders and scenarios it
draws on, then shows the seam between them: the contract each side relies
on, a worked scenario, short code excerpts in each language, and the
pitfalls that only show up when the libraries meet.

| Multivitamin | Library | Repo |
| --- | --- | --- |
| RubyLLM | `ruby_llm` 2.1.1 | [MICharisma/rubyllm-multivitamin](https://github.com/MICharisma/rubyllm-multivitamin) |
| Phoenix | Phoenix 1.8, LiveView 1.2, SQLite | [MICharisma/phoenix-multivitamin](https://github.com/MICharisma/phoenix-multivitamin) |
| Stimulus | Stimulus 3.2.2 | [MICharisma/stimulus-multivitamin](https://github.com/MICharisma/stimulus-multivitamin) |
| SwiftData | SwiftData (macOS 14 API) | [MICharisma/swiftdata-multivitamin](https://github.com/MICharisma/swiftdata-multivitamin) |
| Terminal | macOS Terminal, zsh and the command line | [MICharisma/terminal-multivitamin](https://github.com/MICharisma/terminal-multivitamin) |
| Web client | React 19, Vite, TypeScript | [MICharisma/multivitamin-web](https://github.com/MICharisma/multivitamin-web) |

## Supplement Facts

| Supplement Facts | |
| --- | --- |
| Serving size | 1 guide |
| Libraries per guide | 2 to 6 |
| Guides | 10 |
| Source scenarios cited | every link checked by `scripts/check_sources.py` |
| Index | [`supplements.json`](supplements.json), schema in [`schema/`](schema/supplements.schema.json) |

## Guides

| # | Guide | Combines | Worked scenario |
| --- | --- | --- | --- |
| 01 | [A streamed answer in a Stimulus transcript](guides/01-stimulus-rubyllm-streaming-transcript/) | Stimulus + RubyLLM | Warsaw tram depot night handover |
| 02 | [A LiveView that asks a RubyLLM service](guides/02-phoenix-asks-a-rubyllm-service/) | Phoenix + RubyLLM | Puerto Natales crosswind brief |
| 03 | [A RubyLLM tool that reads a Phoenix JSON endpoint](guides/03-rubyllm-tool-reads-phoenix-json/) | RubyLLM + Phoenix (+ Terminal) | Chinggis Khaan winter morning, Ulaanbaatar |
| 04 | [An Apple client for an LLM-backed Rails API](guides/04-swiftdata-client-for-a-rubyllm-api/) | SwiftData + RubyLLM | Sala del Tule pour for Madrid |
| 05 | [LiveView and Stimulus, side by side](guides/05-liveview-and-stimulus-side-by-side/) | Phoenix vs Stimulus | Kiruna de-icing holdover board |
| 06 | [Authoring a catalog multivitamin-web can render](guides/06-stimulus-catalog-in-multivitamin-web/) | Stimulus + multivitamin-web + build | Fog signal board in the client |
| 07 | [One shell session across the family](guides/07-terminal-drives-every-multivitamin/) | Terminal + every repo | A Saturday release check in Porto |
| 08 | [Publishing a catalog from the shell](guides/08-publishing-catalogs-from-the-terminal/) | Build package + Terminal + multivitamin-web | Publishing Phoenix's routing-and-plugs trial |
| 09 | [A durable-agent worker under launchd](guides/09-durable-agent-worker-under-launchd/) | RubyLLM + Terminal | Fløibanen closure desk, Bergen |
| 10 | [A Mac app that mirrors a Phoenix JSON API](guides/10-swiftdata-mirrors-phoenix-json/) | SwiftData + Phoenix | Punta Arenas Antarctic loads |

## What a guide contains

Every guide has the same sections:

1. **When to combine:** the job that needs both libraries, and when not to bother.
2. **Source scenarios:** a table of the exact feature folders and scenarios it draws on, with what each contributes.
3. **Architecture:** a Mermaid sketch.
4. **The seams:** the contracts between the libraries. This is the reason the guide exists.
5. **Worked scenario:** a realistic job with real places and names, and short code excerpts in each language.
6. **Pitfalls:** what goes wrong only when the libraries meet.

## Honesty rules

- Code copied from a multivitamin is quoted as-is and linked.
- Code written for a guide is labeled **supplement glue**. It uses the API
  names the source scenarios use, and it hasn't been run as a whole.
- Anything outside the repos (turbo-rails broadcasts, Req calls, Solid
  Queue's `bin/jobs`, launchd plists) is called out where it appears.
- Anything that doesn't exist yet is marked: the Terminal multivitamin's
  feature folders, the build package's public source and CLI, GitHub Pages
  sites for every catalog except RubyLLM, and file tabs in multivitamin-web.

## Check the links

```sh
GITHUB_TOKEN=$(gh auth token) python3 scripts/check_sources.py   # every source exists
python3 scripts/index_sources.py                                  # refresh sources in supplements.json from the guides
```
