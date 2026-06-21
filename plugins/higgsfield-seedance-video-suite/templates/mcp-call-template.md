# Higgsfield MCP Call Template

The standard MCP-mode sequence shared by all generation skills. See `docs/HIGGSFIELD_MCP_REFERENCE.md` and `docs/DUAL_MODE.md`.

1. RESOLVE MODEL + PARAMS
   models_explore(action:"recommend", query:"<goal in plain terms>", input:"text|image", type:"image|video|audio|3d", limit:5)
   models_explore(action:"get", model_id:"<chosen>")   // confirm enums: aspect_ratio, duration, quality/resolution, medias[].roles

2. PREP REFERENCES (never pass URLs)
   local file → media_upload_widget (Apps UI) → media_id
   web URL    → media_import_url({url}) → media_id
   prior asset→ reuse its job_id

3. PREFLIGHT COST + CONFIRM
   generate_*({ params: { …, get_cost: true } })   // show credits, get user OK

4. GENERATE
   generate_image / generate_video / generate_audio / motion_control({ params: { … } })

5. POLL
   job_status(jobId)   // respect poll_after_seconds; or job_status(jobId, sync:true)

6. APPROVE
   route the returned media through asset-approval-gate; if a recovery_tool is returned, call it immediately.

EXAMPLES

# generate_image with a reference
{ "params": { "model": "soul_2", "prompt": "<prompt>", "aspect_ratio": "2:3", "quality": "2k",
  "medias": [{ "value": "<media_id>", "role": "image" }], "count": 1 } }

# generate_video image-to-video from an approved still
{ "params": { "model": "kling3_0_turbo", "prompt": "<motion/camera only>", "aspect_ratio": "9:16",
  "duration": 5, "medias": [{ "role": "start_image", "value": "<media_id-or-job_id>" }] } }

# motion_control (motion transfer)
{ "params": { "image_id": "<uuid>", "motion_video_id": "<uuid>", "resolution": "1080p", "scene_control": "image" } }
