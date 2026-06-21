# Image Prompt Conventions

Shared rules for writing image prompts across all image skills (`image-generator`, `character-designer`, `character-sheet-builder`, `environment-sheet-builder`, `style-board-builder`, `storyboard-builder`). Skills reference this file rather than restating it. Tuned for GPT Image 2 / Nano Banana 2 / Nano Banana Pro / Soul / Seedream as exposed via the Higgsfield MCP, but the structure is model-agnostic. Pair with `docs/HIGGSFIELD_MCP_REFERENCE.md` (params/models), `docs/MODEL_PROMPTING.md` (per-model strategy), and `docs/DUAL_MODE.md` (clarify + execution).

---

## 0. Pick the model first

Default split: **lots of / critical text, typography, UI, infographics, precise edits → GPT Image 2** (or **Nano Banana Pro** for 4K/multilingual typography); **general creative / illustrative / photoreal, fast iteration, image editing, multi-reference compositing → Nano Banana 2**; realistic people/portraits via Soul → **Soul 2**. Each model wants slightly different phrasing — see `docs/MODEL_PROMPTING.md` before writing the prompt (e.g. GPT Image 2 honors "no X" negatives; Nano Banana 2 wants positive framing like "empty street", not "no cars").

---

## 1. Prompt structure

Recommended order: **intended use → scene/setting → subject → key details → lighting → lens/optics → composition → style → explicit constraints.** Stating the *intended use* ("e-commerce product shot", "event flyer", "character reference sheet") sets the model's mode and polish level.

- **Natural language wins.** Modern models (GPT Image 2, Nano Banana Pro) are not tag-soup dependent — clear sentences or short labeled segments beat keyword piles. **Clarity over cleverness.**
- For complex scenes, use **short labeled lines or segments**, not one long run-on paragraph. 1–3 clear sentences is often enough.
- **Lighting is the single biggest quality lever** after subject. Always state light **direction** and quality ("soft daylight from camera-left, gentle catchlights"), never just "good lighting".
- **Don't default to "cinematic."** It's a no-op. Specify the concrete look (lens, lighting, grade) you actually mean.

## 2. Photorealism, style & text

- Photoreal: put "photorealistic" / "professional photography" in the prompt. You may cite a lens *feel* ("85mm portrait look", "shallow depth of field") for high-level intent, but **don't trust exact camera/lens specs as literal simulation** — they're interpreted loosely.
- Add **subtle film grain** to break plastic AI smoothness on photoreal stills.
- **In-image text:** put literal copy in quotes or ALL CAPS, specify font style/placement, spell tricky words, and use a higher quality/resolution tier for small/dense text. Nano Banana Pro / GPT Image 2 render text best.
- Vector/logo work → Recraft (`model_type:vector`).

## 3. Negative guidance

These models **honor explicit exclusions** stated as positive constraints — `"no text, no watermark, no extra people, no logos"` — far better than vague "avoid …". List the few things that actually ruin the shot.

## 4. Aspect ratio / format (always confirm — see DUAL_MODE clarify)

Portrait/character → `2:3` or `4:5`; social story → `9:16`; standard → `1:1` or `4:3`; widescreen/establishing → `16:9` or `21:9`; reference sheets → `16:9` (room for panels). **Aspect ratios are per-model** (e.g. `soul_2` lacks `21:9`/`4:5`) — verify via `models_explore get`.

## 5. Character & object consistency

There is usually **no seed**; consistency comes from anchors, not luck. Stack these (multiplicative):

1. **Master reference image** — generate one clean, front-facing, neutral-lit, neutral-background hero image first; it is your strongest lever (editor models weight an uploaded ref heavily). Then pass it as a reference (or as a Soul/Element) on every later generation.
2. **Verbatim identity block** — a fixed 30–50 word descriptor reused **word-for-word, same order**, placed **before** scene/style text. Synonym drift ("emerald" → "green") = identity drift. Repeat the words "consistent / identical" per element (face, hair, outfit, palette).
3. **Reuse strategy** (ask the user — see `HIGGSFIELD_MCP_REFERENCE.md` §4): **Soul** (train one person, `soul_2`/`soul_cinematic`, one identity per gen) vs **Element** (`<<<element_id>>>` in prompt, multi-subject, non-Soul models). Generic fallback: pass the master image via `medias`.
4. **Lock everything but the variable** — when changing one thing (angle, expression), explicitly say "keep face, hair, wardrobe, lighting, framing identical; change only X", and repeat the preserve-list every iteration.

### Identity block template (paste verbatim, ≤50 words, before scene text)
```
[NAME], a [age]-year-old [ethnicity] [gender] with a [face shape] face, [cheekbone/jaw detail],
[eye color] [eye shape] eyes, [hair length/texture/color] hair parted [side], [skin tone] skin,
[distinctive mark], [build]. Wearing [base outfit]. // SCENE: [setting, pose, expression, camera] only.
```
Lock in priority order — **bone structure first** (face shape drifts most), then eyes, hair, skin tone (state explicitly or lighting bleeds it), exact age ("34, smooth skin"), build, distinctive marks, base wardrobe, 3–5 color palette, and a do-not-drift negative list.

## 6. Reference sheets (full templates live in `templates/`)

A sheet is a **conditioning artifact**, not art for humans. Core discipline:

- **A single text-to-image gen WILL drift** across panels → use **master → derive each view** (regenerate each angle/expression from the approved master, referencing it), not one mega-prompt. Grid-prompting is the bootstrap to pick a master; per-view regeneration is the lock.
- **Turnaround:** front / 45° / side / back, A-pose or T-pose, identical staging (plain light-grey seamless bg, flat even lighting, eye-level, same scale), negative guards against pose/expression/color change.
- **Expression sheet:** same character + same framing + **vary only the expression**; named emotions in a grid.
- **Environment:** establish the **empty location authoritatively first** (wide master), record an architectural-anchor + lighting "location bible", then derive reverse/medium/detail angles and time-of-day variants holding geometry and light **direction** fixed (use depth/edge structure, don't re-feed the master raw or it remixes). Boards (palette/material/mood) last.

## 7. Cinematography for stills

Light **direction** + lens feel + composition is what separates an intentional frame from a flat snapshot. Vocabulary: shot size (ECU→EWS), angle (low/high/eye-level/OTS/dutch), lens feel (24mm wide / 50mm natural / 85mm portrait / telephoto compression), DoF/bokeh/anamorphic, composition (rule of thirds, leading lines, symmetry, foreground layering, negative space, headroom), lighting (key/fill/rim, golden/blue hour, low-key/high-key, practical, volumetric), and grade/stock (teal-orange, desaturated, Kodak Portra, bleach bypass). See `docs/VIDEO_PROMPT_CONVENTIONS.md` for the full shot-spec vocabulary shared with video.

## 8. Top mistakes

1. Overloading one prompt instead of iterating with single-change follow-ups. 2. Omitting light direction. 3. Defaulting to "cinematic" / vague style. 4. Vague "avoid X" instead of explicit "no X". 5. Relying on text alone for character consistency instead of a reference/Soul/Element. 6. Synonym drift in the identity block. 7. One mega-prompt for a sheet instead of master→derive. 8. Generating a background behind the character every shot instead of establishing the location once. 9. Letting light direction flip between continuity shots. 10. Low quality tier for small text or close-up portraits.
