# Model Prompting Playbooks

Per-model prompt strategy for the three workhorse models, plus when to pick which. Skills reference this for model-specific phrasing; for general structure see `IMAGE_PROMPT_CONVENTIONS.md` / `VIDEO_PROMPT_CONVENTIONS.md`, and for params/IDs see `HIGGSFIELD_MCP_REFERENCE.md`.

> Model capability specifics below are 2026 and partly post-cutoff (web-sourced) — confirm exact params/enums via `models_explore(action:"get")` before generating.

---

## Model selection

**If the user specifies an image or video model, use that model — an explicit choice always overrides the defaults below.** Otherwise apply the project standards:

**Project standard: use GPT Image 2 (`gpt_image_2`) for ALL image generation.** It handles text-heavy layouts, photoreal, illustration, multi-element design sheets, and reference-based edits well, so the suite standardizes on it for consistency. Override only for a capability it lacks:
- a **trained reusable Soul identity** → requires `soul_2` / `soul_cinematic` (GPT Image 2 has no Soul; use reference-image + Element instead — see below);
- **transparency** → generate on a solid background, then `remove_background`;
- niche: 4K multilingual typography → `nano_banana_pro`; vector logos/icons → `recraft-v4-1`.

For **video**, the project standard is **Seedance 2** (`seedance_2_0`) for all generation — identity-consistent text/image-to-video with native synchronized audio. Override only when needed: multi-shot narrative → Kling 3; photoreal hero shot → Veo. The per-model playbooks below are reference for explicit overrides.

---

## GPT Image 2 — image (preferred for text-heavy)

`gpt_image_2`. Runs a brief reasoning pass before drawing, so multi-element layouts, UI, and text-heavy scenes usually land first try.

- **Structure:** background/scene → subject → key details → constraints, plus the **intended use** ("ad", "UI mock", "infographic") to set polish. Natural language; paragraph / instruction / tags all work — clarity over cleverness; 1–3 sentences, line breaks for complex scenes.
- **Standout strength — TEXT/typography/diagrams** (why it's preferred for text-heavy): put literal copy in **quotes or ALL CAPS**, **spell hard words letter-by-letter**, specify font style/size/color/placement, and use **`quality: medium`/`high`** for small or dense text.
- **Editing & multi-reference:** up to **16 reference images**; address inputs **by index + role** ("Image 1: product; Image 2: style reference") and state the interaction. Edit pattern: "Change ONLY X" + "keep everything else the same", and **repeat the preserve-list every iteration**.
- **Consistency (NO seed):** reuse a **character bible** (6–10 fixed traits, verbatim) + pass an approved **baseline image as a reference**; combine both.
- **Anti-"AI look" (this model over-polishes by default):** frame photoreal shots as *"a real photo captured in the moment, unposed"*; add imperfection/texture (`visible skin pores, subtle oiliness, faint blemishes, asymmetrical features, film grain, sensor noise, slight chromatic aberration`), a **single motivated key light with direction + real contact shadows**, real lens/film-stock language (`35mm lens`, `Kodak Portra 400`, `Cinestill 800T`), `slightly underexposed, muted grade`, and **off-center/rule-of-thirds, imperfect framing**. **DROP** `8K/ultra-detailed/masterpiece` (no realism gain) and don't lean on `photorealistic` alone. See `IMAGE_PROMPT_CONVENTIONS.md` §2.
- **Negatives:** honors explicit exclusions ("no watermark, no text, no logos", plus anti-slop guards: `no plastic/waxy skin, no studio polish, no perfectly symmetrical face, no oversaturated HDR, not centered`) — not vague "avoid".
- **Params:** sizes with max edge ≤3840, both edges ÷16, ratio ≤3:1 (`1024x1024`, `1536x1024`, `1024x1536`, `3840x2160`, `auto`); `quality: low|medium|high|auto`; **no transparency**. (Higgsfield exposes `resolution` 1k/2k/4k + `quality` low/med/high for this model.)

## Nano Banana 2 — image (preferred for creative)

`nano_banana_2` (Google Gemini-family Flash image; sibling of `nano_banana_pro`).

- **Structure:** write **narrative scene descriptions, not keyword tags** — "direct the scene." Conversational and literal. Google's five pillars: **Subject · Composition · Action · Location/Setting · Style**; practical order `[Subject] + [Action] + [Location] + [Composition] + [Style]`. More detail = closer fidelity.
- **Best at:** creative/illustrative **and** photoreal; **fast iteration**; **image-to-image editing & semantic masking**; **multi-image fusion** (blends up to ~14 refs; tracks up to ~5 characters / 14 objects); native 4K; web-grounded world knowledge.
- **Text:** legible and multilingual (can translate text in-image), but small/critical text can fail → **route heavy text to GPT Image 2 / Nano Banana Pro.**
- **Direct like a creative director:** name camera body, lens (f/1.8 shallow DoF, macro), lighting ("three-point softbox", "chiaroscuro", "golden-hour backlight"), film stock/grain, and **specific materials** ("navy blue tweed", not "suit").
- **Negatives:** use **positive framing** — "empty street", NOT "no cars" (exclusion phrasing is unreliable here).
- **Editing:** image + describe the change; for region edits be explicit about **what to keep identical** ("replace the sky…, keep the subject, pose, clothing exactly the same"). Multi-ref formula: `[reference images] + [relationship instruction] + [new scenario]`.
- **Consistency (no seed):** establish the character with specifics in prompt #1 and **reuse identical descriptors**; for multiple subjects **upload refs and give each a distinct name** to avoid identity bleed; iterate **conversationally** (follow-ups), and if it drifts after many edits, **start a fresh conversation** with a full description.
- **Params:** state aspect ratio in-prompt; resolution `512px / 1k / 2k / 4k`.

## Seedance 2 — video (reference-driven identity + native audio)

`seedance_2_0`. See `VIDEO_PROMPT_CONVENTIONS.md` for the full shared rules.

- **Formula (60–100 words, scene-first → camera-last):** `[Subject + appearance] + [Action] + [Environment + lighting] + [Camera move + shot size] + [Style] + [Constraints]`.
- **Lighting is the biggest quality lever** — add it first when a prompt is weak.
- **ONE camera move, ONE shot size** per prompt; name the shot size; say what the camera is **not** doing ("no cuts, no zoom") or it defaults to cutting.
- **Separate subject motion from camera motion** ("The dancer spins. Camera holds fixed framing.").
- **Rhythm words, not specs** (`slow, gentle, smooth, steady`); **avoid bare `fast`** (top quality-killer).
- **Multi-shot:** declare **shots + total duration + aspect ratio at the top**, then numbered `Shot 1 / Shot 2…`.
- **Image-to-video:** identity lives in the start frame — restate only persistent anchors and describe **only what changes**; add "keep original composition and lighting, avoid identity drift".
- **Separation of concerns (Seedance superpower):** assign identity to the start image, motion to a reference clip, pacing to audio in **separate tagged refs** — *"@Image1 identity anchor, do not alter facial proportions; follow @Video1's camera; match rhythm to @Audio1"* — don't blend roles in one blob. Reuse a clean extracted frame as the identity anchor across clips.
- **Anti-"AI look":** give motion **weight + real-time speed** (`realistic inertia, no unintended slow motion`, concrete physics like `heavy footsteps with ground impact`); add micro-life (`natural blinks, breathing, small weight shifts`); prefer **real camera operation** (`handheld micro-shake, documentary feel` or a named rig) over the frictionless glide; filmic capture (`35mm grain, slight halation, 24fps natural motion blur`); a **single motivated practical light held consistent** (also the #1 flicker fix). Iterate at 3–5s to verify face/lighting stability before scaling. See `VIDEO_PROMPT_CONVENTIONS.md` §3a.
- **Specs:** duration steps **4/5/6/8/10/12/15s** (intermediate rejected, clamps); aspect `16:9, 9:16, 4:3, 3:4, 21:9, 1:1`; up to 1080p–2K @ 24fps; **native synchronized audio** (toggleable); inputs up to 9 images / 3 videos / 3 audio.
- **When:** reference-driven identity/product video + native audio in one pass. Multi-shot narrative → **Kling 3**; photoreal hero/character shot → **Veo**.

---

## Sources (web, partly post-cutoff)

- GPT Image 2: developers.openai.com image-gen prompting guide & API docs.
- Nano Banana 2: blog.google/innovation-and-ai nano-banana-2; deepmind.google gemini-image prompt-guide; cloud.google.com ultimate prompting guide for Nano Banana.
- Seedance 2: BytePlus ModelArk docs; higgsfield.ai seedance prompting guide; apiyi.com Seedance 2.0 guide. (Seedance 2.0 / NB2 post-date Jan 2026 — treat specifics as unverified vendor claims; confirm via `models_explore`.)
