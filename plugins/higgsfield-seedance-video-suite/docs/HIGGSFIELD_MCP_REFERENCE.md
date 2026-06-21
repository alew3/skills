# Higgsfield MCP Reference

Authoritative, schema-grounded reference for driving the Higgsfield MCP from the suite's skills. Field names are quoted verbatim from the live MCP tool schemas. **When this doc and a blog/web source disagree, trust the schema.** Capability claims about specific 2026 models (Seedance 2.0, Kling 3.0, Veo 3.1, Nano Banana Pro) shift between releases — re-verify live with `models_explore` before relying on a specific enum.

> This file is shared infrastructure. Skills reference it by one line ("Resolve models/params per `docs/HIGGSFIELD_MCP_REFERENCE.md`") instead of re-deriving parameters. See also `docs/DUAL_MODE.md` (when to call MCP vs emit a prompt) and `docs/IMAGE_PROMPT_CONVENTIONS.md` (how to write the prompt text).

---

## 0. The one rule that governs everything

**The generation tool schemas are intentionally thin.** `generate_image.params` and `generate_video.params` are open objects (`additionalProperties: {}`) with only `model` hard-required. Models, allowed `aspect_ratio`/`duration`/`resolution`/`quality`, per-model media `roles`, and special fields (`soul_id`, `style_id`, `mode`, `genre`, `generate_audio`) are **NOT in the schema** — they live in the model catalog and are discovered at runtime:

```
models_explore(action:"recommend", query:"<goal in plain creative terms>", input:"text|image", type:"image|video|audio|3d", limit:5)
   → inspect match_reason, tags, parameters of top candidates
models_explore(action:"get", model_id:"<chosen>")
   → read EXACT params, enums, durations, aspect_ratios, medias[].roles BEFORE generate_*
```

Model-scoped params are passed at the **top level of `params`** (e.g. `params.resolution`, `params.quality`, `params.soul_id`), exactly as the catalog lists them.

`models_explore(action:"recommend")` is a filter, not an oracle: it over-weights intent keywords — a query containing "product"/"ad"/"marketing" forces Marketing Studio models to the top. **Strip those words unless you actually want Marketing Studio**, and always validate the top hit.

---

## 1. Media workflow (references, start frames) — never pass URLs

Any reference image / start frame / motion video is passed inside `medias: [{ value, role }]`. **`value` must be a `media_id` (UUID) or a prior generation's `job_id` — never an `https://` URL** (the sole exception: `reframe` accepts URLs for *image* refs).

| You have… | Do this | Result |
|---|---|---|
| Local file (Apps UI client) | `media_upload_widget` (`type:'image'`/`'video'`) → user picks | confirmed `media_id` |
| Local file (byte upload) | `media_upload` → PUT bytes → `media_confirm` | confirmed `media_id` |
| A web URL | `media_import_url({ url })` | confirmed `media_id` |
| A prior generated asset | reuse its `job_id` directly | use as `value` |

Never ask the user to attach files in Claude chat — remote MCP tools cannot read those.

---

## 2. `generate_image`

Call shape: `generate_image({ params: { ... } })`.

| Field (in `params`) | Req | Notes |
|---|---|---|
| `model` | **Yes** | Catalog ID (§5). The dominant quality lever; gates which other params are legal. |
| `prompt` | no* | Always write one (except pure `soul_id`/element runs). *Schema-optional only because Marketing Studio derives it. |
| `aspect_ratio` | no | **Per-model enum** — verify via `models_explore get`. `soul_2` lacks `21:9`/`4:5`; `soul_cast` is `16:9`-only. |
| `count` | no | 1–4 separate results (default 1). Cost scales with count. |
| `medias` | no | Reference inputs `[{value, role}]`; role is `"image"` for all current image models. Respect per-model max (`soul_2` = 1). |
| `get_cost` | no | `true` → returns credit cost, submits no job. Preflight 4K/high-quality/batch. |
| `resolution` | no | Model-scoped: `1k/2k/4k` (Nano Banana 2/Pro, GPT Image 2, Cinema Studio 2.5, Marketing Studio) or `1k/2k` (Flux 2, Kling O1, Recraft). |
| `quality` | no | Model-scoped: `soul_2`/`soul_cinematic` → `1.5k/2k`; Seedream → `basic/high`; GPT Image → `low/medium/high`. |
| `soul_id` | no | Trained-character id; **`soul_2`/`soul_cinematic` only**; one per gen. |
| `style_id` | **req for `ms_image`** | from `show_marketing_studio(type:'image_style')`. |

**No `seed` field** → don't promise pixel reproducibility; consistency comes from refs/Soul/Elements (§4). `resolution` and `quality` are **different axes** owned by different models (GPT Image 2 has both; `soul_2` uses `quality`, not `resolution`).

Companion tools: `upscale_image` (needs source `width`+`height` px, `resolution:2k/4k`), `outpaint_image` (extend/uncrop, `aspect_ratio`), `remove_background` (`media_id`, `media_type:image/video`). All have no prompt/count.

---

## 3. `generate_video` & `motion_control`

`generate_video({ params: { ... } })`:

| Field (in `params`) | Req | Notes |
|---|---|---|
| `model` | **Yes** | Catalog ID (§5). Gates audio / `end_image` / motion availability. |
| `prompt` | no* | Supply for cinematic control; optional only for Marketing Studio. |
| `medias` | no | i2v/refs. Roles: `start_image` (first frame), `end_image` (last frame), `image` (identity/style ref), `audio` (Seedance audio ref). Exact roles per model from `models_explore get`. |
| `aspect_ratio` | no | Common `16:9/9:16/1:1/4:3/21:9`; per-model. |
| `duration` | no | Integer seconds. **Out-of-range silently clamps to nearest allowed** — verify the model's allowed steps. |
| `count` | no | 1–4. |
| `get_cost` | no | Preflight credits. |
| `preset_id` | no | **Only with `model:"higgsfield_preset"`** (from `presets_show`). |

**No `seed`, no motion-strength field.** Control motion via prompt, model choice, or `motion_control`. Audio is model-specific (e.g. `generate_audio:true` on Seedance/Veo/Cinema; Seedance audio refs via `medias` role `audio`) — surfaced by `models_explore`.

**Image-to-video** = `generate_video` + a video `model` + `medias:[{role:"start_image", value:"<media_id-or-job_id>"}]` + `prompt` (describe only motion/camera/changes — see `docs/IMAGE_PROMPT_CONVENTIONS.md` §i2v).

`motion_control({ params: { ... } })` — Kling 3.0 motion transfer (recast/puppeteer). Strict schema, **no prompt/count**:
| Field | Req | Notes |
|---|---|---|
| `image_id` | **Yes** | Character still (UUID media_id or image job_id). |
| `motion_video_id` | **Yes** | Driving motion video (UUID media_id or video job_id). |
| `resolution` | no | `720p` (default) / `1080p`. |
| `scene_control` | no | `image` (keep character bg, default) / `video` (adopt motion-clip bg). |

Use `motion_control` when you have an approved still **and** a real reference motion clip and want exact, identity-preserving motion. Use `generate_video` i2v when motion is prompt-described or you need t2v/multi-shot/specific duration/audio.

Post-processing: `upscale_video` (bytedance: needs `width`+`height`, `preset:aigc` for AI footage, `fps>30` doubles cost; or topaz: `resolution:1080p/2160p`), `reframe` (change aspect / outpaint video; `aspect_ratio` required; accepts URL image refs).

---

## 4. Character & subject consistency — Soul vs Elements (mutually exclusive)

| | **Soul** (`show_characters`) | **Elements** (`show_reference_elements`) |
|---|---|---|
| What | Trained identity model (digital twin) | Reusable reference (char/env/prop) from image(s) |
| Create | `action:'train'`, `name` + 5–20 ref imgs, ~10 min (non-blocking) → `soul_id` | `action:'create'`, `medias[]` → `element_id` (instant, 1 image OK) |
| Use | `params.soul_id` on **`soul_2`/`soul_cinematic` only**; **one identity per gen** | embed `<<<element_id>>>` in `params.prompt`; **multiple per prompt** → multi-character |
| Models | Soul 2 / Soul Cinematic only | Nano Banana Pro/2, GPT Image 2, Seedream 4.5/5-lite, Cinema Studio Image 2.5; video: Cinema Studio 2/3.0, Seedance 2.0, Kling 3.0 — **not** Soul |
| Best for | One specific person reused across many solo shots | 2+ subjects in a shot, non-person subjects, single-image instant refs |

**Decision rule:** "train / digital twin / 5+ photos of one person / solo output" → Soul. ">1 character in a shot, prop/environment, single image, instant, or a non-Soul model" → Elements. If unspecified, **ask** — they're incompatible at generation time. Elements go in the **prompt**, never in `medias[]`.

---

## 5. Model quick-pick (verify live with `models_explore`)

**Image** — lots of/critical **text, typography, diagrams** → `gpt_image_2` or `nano_banana_pro`; **general creative / illustrative / photoreal + image editing** → `nano_banana_2`; realistic people/UGC/fashion → `soul_2` (+`soul_id`); cinematic still → `soul_cinematic` / `cinematic_studio_2_5`; precise edit/transform → `seedream_v4_5` / `flux_kontext`; logos/vector/icons → `recraft-v4-1` (`model_type:vector`); environment/location → `soul_location`; text-only consistent character → `soul_cast` (16:9); game sprite sheet → `autosprite`. Per-model prompt phrasing: `docs/MODEL_PROMPTING.md`.

**Video** — realistic hero/outdoor → `veo3_1` (`quality:ultra`); multi-shot character story / 4K / cheap → `kling3_0`; reference-driven product + native audio + identity → `seedance_2_0`; fast t2v / single start-frame → `kling3_0_turbo`; Higgsfield-native flagship cinema → `cinematic_studio_3_0`; physics + facial emotion short → `minimax_hailuo`; viral one-image template → `presets_show` → `higgsfield_preset`; product ad → `marketing_studio_video`; YouTube → shorts → `clipify`.

**Audio (TTS only)** — default voiceover/dubbing → `text2speech_v2_elevenlabs`; long narration → `text2speech_v2_seed_speech`; clone from ~3s → `text2speech_v2_vibe_voice`; low-latency multilingual → `text2speech_v2_cozy_voice`. Pick voice via `list_voices` (pass exact `voice_id` + `voice_type`). `generate_audio` is **speech only** — it cannot make music/SFX (those models are game-pipeline-only; decline general music/SFX requests).

**3D** — image→GLB turntable/asset → `image_to_3d` (single) / `multi_image_to_3d` (1–4 views); single object lift → `sam_3_3d`; rig existing GLB → `3d_rigging`. Animated rig: `enable_rigging` + `enable_animation` + `animation_action_id`.

---

## 6. Generation lifecycle & gotchas

1. **Preflight cost** with `get_cost:true` (supported on `generate_image`, `generate_video`, `generate_audio`, `reframe` — NOT `motion_control`/`upscale_video`); confirm with the user before spending credits.
2. **Async jobs:** poll `job_status(jobId)` — non-terminal responses carry `poll_after_seconds`; `job_status(...,sync:true)` blocks ~25s for fewer round-trips. Video ≈ 60–180s, images ≈ 10–20s.
3. **Recovery:** if a `generate_*` call returns a `recovery_tool`, call it immediately (don't explain/ask first). Lost results → `reveal_generation` / `show_generations`.
4. **URLs ≠ media_ids** in `medias[].value` (except `reframe` images).
5. **Model gates features** — audio/`end_image`/motion params exist only if the model declares them; `models_explore get` first.
6. `duration` out-of-range **silently clamps**; aspect ratios are **per-model**; `soul_2` max 1 ref; `ms_image` needs `style_id`; `preset_id` only with `higgsfield_preset`; `upscale_image`/`upscale_video` (bytedance) need source `width`+`height`.
7. **Don't call `generate_*` to "test"** — every real call costs credits. Use `get_cost:true` + read-only `models_explore` for exploration.

---

## 6a. Auxiliary tools — use any when the project needs it

The suite is not limited to `generate_image/video/audio`. Any skill or orchestrator may call additional Higgsfield MCP tools when finishing a project calls for it (preflight cost and confirm credits first, same as any generation):

- **Voice / speech:** `generate_audio` (TTS voiceover/dialogue), `list_voices` (pick a voice), `voice_change` (convert/restyle a voice), `dubbing` (translate/dub existing audio or video).
- **Identity / reference:** `show_characters` (train/reuse a Soul), `show_reference_elements` (reusable character/prop/env Elements), `show_medias`/`show_generations`/`reveal_generation` (find prior assets).
- **Motion:** `motion_control` (recast/puppeteer/motion-transfer onto a still).
- **Post / finishing:** `upscale_image`, `upscale_video` (enhance/resolution), `reframe` (change aspect / outpaint video), `outpaint_image` (extend/uncrop), `remove_background` (cutout/transparency).
- **3D / assets:** `generate_3d` (image→GLB turntable/asset), `autosprite` (game sprite sheets).
- **Account:** `balance` / `show_plans_and_credits` (check credits before a big batch).

Principle: pick the **dedicated tool** over re-generating (e.g. enhance with `upscale_*`, change aspect with `reframe`, cut out with `remove_background`). Discover exact params with `models_explore` / the tool schema before relying on them.

## 7. Skill → MCP tool map

| Skill | Primary MCP tool(s) |
|---|---|
| image-generator | `generate_image` |
| character-designer | `generate_image` (+ `show_characters`/`show_reference_elements` for reuse) |
| character-sheet-builder | `generate_image` (master → derive views) |
| environment-sheet-builder | `generate_image` (`soul_location` / Nano Banana Pro) |
| style-board-builder | `generate_image` |
| storyboard-builder | `generate_image` (frames) |
| video-prompt-architect | `generate_video` (+ `motion_control` when a driving clip exists) |
| audio-generator | `generate_audio` (+ `list_voices`) |
| higgsfield-package-adapter | media upload → `generate_*` → `job_status` |
| all | `models_explore`, `get_cost`, `job_status` |

> Uncertainty: per-model credit costs are not exposed by listing tools (use `get_cost`). Specific 2026 capability claims are web-sourced; live enums are runtime-discovered. Re-confirm at call time.
