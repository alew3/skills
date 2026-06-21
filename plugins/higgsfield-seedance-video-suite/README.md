# Higgsfield + Seedance Video Suite

A modular skill pack for building AI **images and video** — from a rough idea to a finished render or a clean, paste-ready prompt package. Built around the **Higgsfield MCP** (Seedance 2, Kling 3, Veo, Cinema Studio, Soul, Nano Banana, GPT Image 2…), but every skill also works **without** the MCP by emitting prompts you run anywhere.

New in 0.2.0: **dual-mode** (MCP **or** prompt) in every skill, a **clarify-before-generate** gate, **two orchestrators** (image + video), per-deliverable skills (character / character-sheet / environment / style / storyboard / audio), and first-class support for **multiple characters and multiple environments**.

→ **Start here:** [`docs/GETTING_STARTED.md`](docs/GETTING_STARTED.md) — worked examples for both workflows and for individual skills.

## Two modes (every skill)

- **PROMPT MODE** — get a `SEND VERBATIM:` block with only the final prompt (often plus ready-to-run MCP args). Paste it into Seedance/Kling/Veo/GPT Image/Nano Banana yourself.
- **MCP MODE** — the skill drives the Higgsfield MCP: resolves a model, previews credit cost and asks you to confirm, generates, polls, and routes the result to approval.

Skills **ask for any missing parameter** (format, aspect ratio, duration, model, references…) and resolve ambiguity before generating. See [`docs/DUAL_MODE.md`](docs/DUAL_MODE.md).

## Skills (14)

| Skill | Responsibility |
|---|---|
| `video-workflow-orchestrator` | Guided idea → finished video; routes specialists, gates, MCP/prompt mode; multi-character/environment |
| `image-workflow-orchestrator` | Guided idea → coherent image set (style, characters, sheets, environments, hero images) |
| `creative-brief-grill` | One-question-at-a-time interview → approved image or video brief (cast, locations, format, mode) |
| `image-generator` | Generic single/freeform image |
| `character-designer` | One character's canonical look + identity block + reuse strategy (Soul vs Element) |
| `character-sheet-builder` | Turnaround / expression / pose sheet via master→derive |
| `environment-sheet-builder` | Location board: empty master + location bible + angles + time-of-day |
| `style-board-builder` | Style/mood/palette board = continuity constraints |
| `storyboard-builder` | Shot list + storyboard frames binding cast/locations per shot |
| `video-prompt-architect` | Final video prompt (Seedance/Kling/Veo/Cinema); t2v / i2v / multi-shot |
| `audio-generator` | Speech/voiceover via generate_audio (TTS only) |
| `asset-approval-gate` | Approve/revise/reject for prompts and media; owns the named multi-asset map |
| `passthrough-guardian` | Validates SEND VERBATIM cleanliness / asset-map consistency |
| `higgsfield-package-adapter` | Final handoff package; in MCP mode drives upload + generation |

All skills are independently callable; the orchestrators coordinate them.

## Reference docs

- [`docs/GETTING_STARTED.md`](docs/GETTING_STARTED.md) — the guide + examples
- [`docs/DUAL_MODE.md`](docs/DUAL_MODE.md) — clarify + MCP-vs-prompt contract
- [`docs/IMAGE_PROMPT_CONVENTIONS.md`](docs/IMAGE_PROMPT_CONVENTIONS.md) / [`docs/VIDEO_PROMPT_CONVENTIONS.md`](docs/VIDEO_PROMPT_CONVENTIONS.md) — how prompts are written
- [`docs/HIGGSFIELD_MCP_REFERENCE.md`](docs/HIGGSFIELD_MCP_REFERENCE.md) — models, params, media workflow (schema-grounded)
- `templates/` — brief, video prompt, sheets, storyboard/shot-list, audio, MCP call, workflow-state
- `examples/` — end-to-end MCP, prompt-only, and individual-skill walkthroughs

## Core rules

1. Clarify missing parameters before generating; resolve ambiguous intent first.
2. One question at a time during briefing; always give a recommended answer.
3. Never default to "cinematic" — state concrete lighting, lens, composition.
4. Approval gates after any asset that affects downstream generation (both modes).
5. `SEND VERBATIM` holds only the final downstream prompt — nothing else.
6. In MCP mode, preview credit cost and confirm before spending; never pass URLs in `medias[].value` (convert to media_ids first).
7. Lock approved assets in a named asset map; thread references (character/Soul, environment, style board, aspect ratio) through every later stage.
8. Preserve the user's intent over creative improvisation.

## License

MIT.
