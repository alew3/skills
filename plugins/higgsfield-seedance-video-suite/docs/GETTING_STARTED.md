# Getting Started

This plugin turns an idea into AI **images** and **video** using the Higgsfield MCP — or, if you don't have the MCP, into clean prompts you can paste into Seedance / Kling / Veo / GPT Image / Nano Banana yourself. Every skill works **both ways** and **asks for any missing parameter** (format, aspect ratio, duration, model, references…) before it generates.

## The two modes (applies to every skill)

- **PROMPT MODE** — the skill hands you a `SEND VERBATIM:` block containing only the final prompt (plus, often, ready-to-run MCP arguments). Copy it anywhere. No MCP needed.
- **MCP MODE** — the skill drives the Higgsfield MCP: picks a model, previews the credit cost and asks you to confirm, generates, and shows the result for approval.

If you don't say which you want, the skill asks once. See `docs/DUAL_MODE.md`.

## The two orchestrators + the specialists

- `image-workflow-orchestrator` — idea → a coherent **image set** (style board, characters, character sheets, environment sheets, hero images).
- `video-workflow-orchestrator` — idea → a finished/specified **video** (brief → style *(optional)* → character / prop / environment design sheets *(always built — reusable Soul/Element assets for future videos)* → storyboard sheet → per-shot video prompts → audio → handoff). It can pull the image workflow in to build assets first.

You can also call any specialist on its own: `image-generator`, `character-designer`, `character-sheet-builder`, `environment-sheet-builder`, `style-board-builder`, `storyboard-builder`, `video-prompt-architect`, `audio-generator`, `creative-brief-grill`, `asset-approval-gate`, `passthrough-guardian`, `higgsfield-package-adapter`.

A project can have **multiple characters and multiple environments** — design each once, then reuse them across shots.

---

## Example A — Video workflow (from scratch)

> "I want a 15s vertical TikTok teaser: detective Maya finds a clue in a neon alley at night, then on a rainy rooftop."

1. **Brief** — `video-workflow-orchestrator` starts `creative-brief-grill`, asking one question at a time, and captures: format **9:16, ~15s, 3 shots**, look **neo-noir**, **cast = [maya]**, **environments = [alley, rooftop]**, and **execution mode**. → you approve the brief. ★
2. **Character** — `character-designer` locks Maya's master + identity block + reuse strategy (one person across solo shots → **Soul**). → approve. ★ Then `character-sheet-builder` derives a turnaround. → approve. ★
3. **Prop sheets** — `prop-sheet-builder`, once per hero prop (e.g. the clue/photo Maya finds) → approve. ★ Each prop sheet becomes a reusable **Element** you can drop into future videos.
4. **Environments** — `environment-sheet-builder` builds `alley`, then `rooftop` (each: empty master + location bible + angles). → approve each. ★
5. **Style** *(optional)* — `style-board-builder` locks palette/grade/lighting. → approve. ★
6. **Storyboard sheet** — `storyboard-builder` produces the per-shot rows + one keyframe per shot (each shot binds maya + any prop(s) + its location). → approve. ★
7. **Per-shot video prompts** — `video-prompt-architect` writes one prompt per shot, using each approved keyframe as the **image-to-video start frame**, and chains shot N's last frame into shot N+1 for continuity. `passthrough-guardian` checks each prompt.
8. **Audio** (optional) — `audio-generator` for Maya's VO line, or native model audio.
9. **Handoff / render** — `higgsfield-package-adapter` gives you the full package (PROMPT MODE) or renders the shots (MCP MODE, with a P1 look-test before the rest).

**Just want the prompts?** Say "prompt mode" and step 7 hands you three `SEND VERBATIM` blocks (one per shot) you can paste into Seedance.

## Example B — Image workflow (from scratch)

> "Design two characters and a lab for a comic, plus a cover image."

1. **Brief** — `image-workflow-orchestrator` → `creative-brief-grill`: style, **cast = [maya, theo]**, **environments = [lab]**, aspect ratios, execution mode. ★
2. **Style board** first — `style-board-builder` locks the look every later image inherits. ★
3. **Characters** — `character-designer` for `maya`, then `theo` (two in one panel later → **Element** strategy). Each → `character-sheet-builder`. → approve each. ★
4. **Environment** — `environment-sheet-builder` for `lab`. → approve. ★
5. **Cover** — `image-generator`, reusing maya + theo + lab + style board as references. → approve. ★
6. **Package** — `higgsfield-package-adapter` returns the approved image set / asset map.

---

## Using individual skills (no orchestrator)

- **One image:** call `image-generator` → "a photoreal flat-lay of vintage cameras on linen, top-down, soft window light, 1:1". It asks for any missing format/style, then gives a `SEND VERBATIM` prompt (and MCP args), or generates it.
- **A character:** `character-designer` → produces the master + reusable identity block + Soul/Element plan.
- **A turnaround sheet:** `character-sheet-builder` (give it the approved master) → per-view prompts derived from the master.
- **An environment board:** `environment-sheet-builder` → master + angles + location bible.
- **A prop/object sheet:** `prop-sheet-builder` → hero render + multi-angle views + callouts + scale + variants, reusable as an Element.
- **A single video shot:** `video-prompt-architect` → "slow push-in on Maya as she reads a note, rainy office, 6s, 16:9". It confirms duration/aspect/start-frame, then emits the video prompt or generates it.
- **Voiceover:** `audio-generator` → script + voice, via `generate_audio`.

## Install

See the repo root **README → "Install in Claude Code"**: `/plugin marketplace add alew3/skills` then `/plugin install higgsfield-seedance-video-suite@alew3-skills`.

## Where things live

- `docs/DUAL_MODE.md` — clarify + MCP-vs-prompt contract
- `docs/IMAGE_PROMPT_CONVENTIONS.md` / `docs/VIDEO_PROMPT_CONVENTIONS.md` — how prompts are written
- `docs/MODEL_PROMPTING.md` — per-model strategy + which model to pick (text → GPT Image 2; creative → Nano Banana 2; video → Seedance 2)
- `docs/HIGGSFIELD_MCP_REFERENCE.md` — models, params, media workflow, and the full auxiliary-tool catalog
- `templates/` — fill-in templates (brief, shot list, sheets, workflow-state, MCP call)
- `examples/` — worked end-to-end examples
