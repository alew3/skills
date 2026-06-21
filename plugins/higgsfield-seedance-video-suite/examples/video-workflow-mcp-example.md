# Example: Video workflow, MCP mode (generate now)

User: *"Make a 6s 9:16 clip — detective Maya lowers a photo in a rainy neon alley, slow push-in. Generate it for me."*

`video-workflow-orchestrator` runs in MCP mode. Abbreviated trace:

**1. Clarify (grouped, with defaults)** — confirms: aspect 9:16 ✓, duration 6s (allowed Seedance step) ✓, one character (maya), one environment (alley), camera = slow push-in, image-to-video from a storyboard keyframe, native audio = none. Execution = MCP.

**2. Character (`character-designer` → MCP)**
```json
// models_explore(action:"recommend", query:"realistic detective portrait", input:"text", type:"image") → gpt_image_2 (project default)
// get_cost first, confirm credits, then:
{ "params": { "model": "gpt_image_2", "prompt": "Detective Maya, 34, sharp jaw, shoulder-length dark hair, tired green eyes, charcoal trench coat. Front-facing, neutral expression, flat even light, plain grey background.", "aspect_ratio": "2:3", "resolution": "2k", "quality": "high", "count": 1 } }
```
→ poll `job_status` quietly → `job_display` once → master approved via `asset-approval-gate` → reused on later gens via reference image (`medias`) or an Element (train a Soul with `soul_2` only if a trained double is wanted).

**3. Environment (`environment-sheet-builder` → MCP)** — master establishing of the alley (GPT Image 2, 16:9), approved; location bible records "neon signs left, wet pavement, fire escape right; cool key from left".

**4. Storyboard (`storyboard-builder` → MCP) — REQUIRED before any video** — a scene-by-scene visual storyboard sheet (numbered, titled panels + captions + bottom info bar) plus a keyframe per shot, generated from maya's master + alley master + style board, 9:16. Approved ★ → each keyframe is its shot's i2v start frame.

**5. Video shot (`video-prompt-architect` → MCP)**
```json
// media_import_url / reuse keyframe job_id → media_id, then:
{ "params": { "model": "seedance_2_0",
  "prompt": "Medium close-up of the detective, she lowers a photo and her eyes narrow, slow camera push-in, rain-soaked neon alley at night with wet reflective pavement, soft streetlight from frame left, moody neo-noir grade, shallow depth of field, no extra characters, avoid identity drift",
  "aspect_ratio": "9:16", "duration": 6,
  "medias": [{ "role": "start_image", "value": "<keyframe media_id>" }] } }
```
→ `get_cost` confirmed → generate → poll `job_status` quietly → `job_display` once when ready → result routed to `asset-approval-gate`.

**6. Handoff** — `higgsfield-package-adapter` returns the rendered clip + the named asset map (`character:maya`, `environment:alley`, `shot:S01-01`) and echoes the exact params used so the user can reproduce or tweak.
