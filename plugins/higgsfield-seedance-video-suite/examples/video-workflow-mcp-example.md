# Example: Video workflow, MCP mode (generate now)

User: *"Make a 6s 9:16 clip — detective Maya lowers a photo in a rainy neon alley, slow push-in. Generate it for me."*

`video-workflow-orchestrator` runs in MCP mode. Abbreviated trace:

**1. Clarify (grouped, with defaults)** — confirms: aspect 9:16 ✓, duration 6s (allowed Seedance step) ✓, one character (maya), one environment (alley), camera = slow push-in, image-to-video from a storyboard keyframe, native audio = none. Execution = MCP.

**2. Character (`character-designer` → MCP)**
```json
// models_explore(action:"recommend", query:"realistic detective portrait", input:"text", type:"image") → soul_2
// get_cost first, confirm credits, then:
{ "params": { "model": "soul_2", "prompt": "Detective Maya, 34, sharp jaw, shoulder-length dark hair, tired green eyes, charcoal trench coat. Front-facing, neutral expression, flat even light, plain grey background.", "aspect_ratio": "2:3", "quality": "2k", "count": 1 } }
```
→ poll `job_status` → master approved via `asset-approval-gate` → trained to a Soul: `show_characters(action:'train', name:"maya", images:[<media_ids>])` → `soul_id`.

**3. Environment (`environment-sheet-builder` → MCP)** — master establishing of the alley (Nano Banana Pro, 16:9), approved; location bible records "neon signs left, wet pavement, fire escape right; cool key from left".

**4. Storyboard keyframe (`storyboard-builder` → MCP)** — one still for the shot, generated from maya's Soul + alley master + style board, 9:16. Approved → this is the i2v start frame.

**5. Video shot (`video-prompt-architect` → MCP)**
```json
// media_import_url / reuse keyframe job_id → media_id, then:
{ "params": { "model": "kling3_0_turbo",
  "prompt": "Medium close-up of the detective, she lowers a photo and her eyes narrow, slow camera push-in, rain-soaked neon alley at night with wet reflective pavement, soft streetlight from frame left, moody neo-noir grade, shallow depth of field, no extra characters, avoid identity drift",
  "aspect_ratio": "9:16", "duration": 6,
  "medias": [{ "role": "start_image", "value": "<keyframe media_id>" }] } }
```
→ `get_cost` confirmed → generate → `job_status` until ready → result routed to `asset-approval-gate`.

**6. Handoff** — `higgsfield-package-adapter` returns the rendered clip + the named asset map (`character:maya`, `environment:alley`, `shot:S01-01`) and echoes the exact params used so the user can reproduce or tweak.
