# Video Prompt Conventions

Shared rules for writing video prompts (`video-prompt-architect`, `storyboard-builder` motion notes, `video-workflow-orchestrator`). Tuned for Seedance 2.0 / Kling 3.0 / Veo 3.1 / Cinema Studio as exposed via the Higgsfield MCP, but the structure is model-agnostic. Pair with `docs/HIGGSFIELD_MCP_REFERENCE.md` (params/models) and `docs/DUAL_MODE.md` (clarify + execution).

> Capability specifics below (durations, native audio, lip-sync) are current-as-of-2026 vendor/community claims and post-date the training cutoff — re-verify each model's allowed `duration`/`aspect_ratio` via `models_explore(action:"get")` before generating.

---

## 0. Model — Seedance 2 by default

The suite standardizes on **Seedance 2** (`seedance_2_0`) for all video — identity-consistent text/image-to-video with native synchronized audio. Override only for a need it doesn't cover: multi-shot narrative → Kling 3; photoreal hero shot → Veo. Confirm allowed `duration`/`aspect_ratio` via `models_explore`.

---

## 1. Prompt structure (the order the models reward)

Seedance's 6-part formula: **[Subject + appearance] + [Action/behavior] + [Environment + lighting] + [Camera movement + shot type] + [Style] + [Constraints]**, target **60–100 words**. Equivalent compressed stack: **Subject → Action → Camera → Style → Constraints.**

- **Scene first, camera last.** Put the camera instruction at the end. Name the **shot type** up front to anchor framing.
- **Lighting has the biggest single quality impact** — if a prompt is weak, add concrete lighting (direction + quality) first.
- For multi-shot in one prompt, declare **shots + total duration + aspect ratio at the very top**, then number `Shot 1 / Shot 2…`.

## 2. Motion: subject vs camera

- **Separate subject motion from camera motion explicitly.** "The dancer spins; the camera holds a fixed frame" — never "spinning camera around a person." One subject verb + one camera verb.
- Use **rhythm words, not specs**: `slow, gentle, gradual, smooth, controlled, steady`. Do **not** put `f/2.8, ISO 800, 24fps, 85mm` inside motion description.
- **`fast` is the most quality-degrading keyword** — unqualified speed + busy scene = jitter/artifacts. Qualify it ("a quick but smooth whip pan").
- Sequences: choreograph beats (`calm → threat → reaction`) or timed keyframes (`0–3s …, 3–6s …`). Inline VFX in brackets: `[VFX: …]`.

## 3. Camera vocabulary (one primary move per shot)

Never chain push-in→pan→orbit in one shot — pick **one** move and state direction + speed + what it reveals/tracks. Add `gimbal`/`stabilized` for fluid, `handheld, slight natural shake` for energy. Be explicit about what the camera is **not** doing (`no cuts, locked framing`) or models default to cutting.

- Approach: `slow push in / dolly in` (not "zoom"). Retreat: `pull back / dolly out`.
- Lateral: `truck left/right`, `pan left/right following the subject`. Vertical: `tilt up` (pivot) vs `pedestal up` (travel).
- Follow: `tracking shot`. Rotate: `orbit clockwise / arc`. Epic: `crane up, sweeping`. Aerial: `drone descent / FPV sweep`.
- Shot sizes: `extreme close-up → close-up → medium → full → wide → establishing`. Angles: `low / high / eye-level / OTS / POV / dutch`.

## 4. Image-to-video (i2v)

When starting from an approved still (the production path for character work):
- **Identity lives in the start frame; the prompt describes only what *changes*** — action, camera, mood, timing. Don't re-describe the whole scene.
- **Restate identity anchors** that must persist (hair color, specific garment, position) so they don't drift, and **replicate the established framing/composition** rather than reimagining it.
- Helpful negatives: `avoid identity drift, avoid temporal flicker`.
- Pass the still via `medias:[{role:"start_image", value:"<media_id-or-job_id>"}]` (see MCP reference).

## 5. Format, duration, audio (always confirm — DUAL_MODE clarify)

- **Aspect:** `16:9` cinematic, `9:16` social, `21:9` widescreen, `1:1` — per model (Veo is 16:9/9:16 only).
- **Duration:** discrete steps only and **per model** (e.g. Seedance 4/5/6/8/10/12/15s; Kling 3–15s; Veo 4/6/8s) — an unsupported value silently clamps. Keep clips short (≈5–8s) for stability; drift rises past ~6–10s.
- **Audio:** model-specific (`generate_audio:true` on Seedance/Veo/Cinema; Seedance audio refs via `medias` role `audio`). Decide native audio vs silent + separate `audio-generator` track.

## 6. Shot Spec template (fill, then assemble in prompt order — camera last)

```text
SHOT SPEC
shot_size:     e.g. medium close-up (chest-up)
angle:         e.g. low angle / eye level / OTS / dutch
subject:       reuse the EXACT identity noun phrase across all shots
action:        ONE subject verb (what changes this shot)
environment:   setting + time of day
lighting:      direction + quality (e.g. low-key, single practical key from left, cool fill)
lens_optics:   e.g. 85mm, shallow depth of field, creamy bokeh
composition:   e.g. rule of thirds, framed through doorway, slight headroom
color_mood:    e.g. teal-orange grade, subtle 35mm grain
camera_move:   ONE move; direction + speed; LAST in the assembled prompt
duration:      allowed step for the chosen model
aspect_ratio:  per model
start_frame:   media_id of the approved still (i2v) or none (t2v)
audio:         native (model) / separate track / none
continuity:    screen positions, eyeline, "match Shot N lighting/lens"
constraints:   negatives (no extra people, no jitter, no identity drift)
```

Assembled example (Seedance order): *Medium close-up, low angle. Maya, mid-30s in a rain-soaked coat, her smile fading as she reads a note, in a dim apartment with rain on the windows at night. Low-key lighting, single practical lamp keying from the left, cool blue fill. 85mm, shallow depth of field. Teal-orange grade, subtle 35mm grain. Slow push-in, gimbal-stabilized. 6 seconds, 16:9. Avoid jitter and identity drift.*

## 7. Continuity across shots

Models have **no persistent 3D world memory** — enforce it in the prompt + references:
- **Keep the identity in the start frame** and chain shots (best last frame of shot N → start frame of shot N+1) to prevent cumulative drift.
- **180° rule / screen direction:** restate placement every shot ("Leo on left, Maya on right").
- **Eyeline match:** state gaze direction ("gaze ~10° off-camera toward the other character"); flip in reverse shots so glances meet.
- **Carry the same** lighting descriptor, lens, palette, grade, and aspect ratio across a sequence; switching breaks the one-scene illusion.
- One outfit-anchor per wardrobe; never introduce clothing words in a motion prompt.

## 8. Top mistakes

1. Chaining multiple camera moves → jitter. 2. Vague `fast` / `epic` / `amazing`. 3. `cinematic` with no concrete lighting/lens. 4. Omitting lighting. 5. Conflating subject and camera motion. 6. Camera specs (f-stop/ISO/fps) instead of rhythm words. 7. Not declaring shots/duration/aspect for multi-shot → unwanted cuts. 8. Re-describing the whole scene in i2v instead of just motion/changes. 9. Dropping identity anchors in i2v → drift. 10. Requesting an unsupported duration (silently clamps) or pushing 15s + busy + fast → artifacts.
