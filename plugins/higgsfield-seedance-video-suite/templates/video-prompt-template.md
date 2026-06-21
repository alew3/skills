# Video Prompt Template (Seedance / Kling / Veo / Higgsfield)

Model-agnostic. One block = one shot = one model. See `docs/VIDEO_PROMPT_CONVENTIONS.md`.

FORMAT:
[aspect ratio / duration (allowed step for the model) / text-to-video or image-to-video / native audio?]

MODEL TARGET:
[seedance_2_0 (default) — override to kling3_0 / veo3_1 only if needed]

REFERENCES:
[start_image = <approved storyboard frame / character master>; other refs by role]

SHOT SPEC (assemble in order; camera move LAST):
- shot_size: [ECU / CU / MCU / MS / WS / EWS]
- angle: [eye-level / low / high / OTS / dutch]
- subject: [exact identity noun phrase — reuse verbatim across shots]
- action: [ONE present-tense subject beat]
- environment: [setting + time of day]
- lighting: [direction + quality]
- lens_optics: [e.g. 85mm, shallow depth of field]
- color_mood: [grade + grain]
- camera_move: [ONE move; direction + speed]
- continuity: [screen positions, eyeline, "match Shot N lighting/lens"]
- constraints: [negatives — no extra people, no jitter, no identity drift]

SEND VERBATIM:
[The final assembled video prompt only — nothing else. In i2v, describe only motion/camera/changes; do not re-describe what the start frame already fixes.]

MCP CALL (optional, same prompt string):
{ "params": { "model": "seedance_2_0", "prompt": "<same as SEND VERBATIM>", "aspect_ratio": "", "duration": 0, "medias": [{ "role": "start_image", "value": "<media_id>" }] } }
