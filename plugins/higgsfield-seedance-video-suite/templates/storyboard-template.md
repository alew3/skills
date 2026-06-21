# Storyboard Sheet Template

Two deliverables: (1) the **shot list** (machine-readable rows, the handoff to `video-prompt-architect`) and (2) a single **storyboard sheet** — a titled grid of numbered, captioned panels plus a bottom info bar. This file is the sheet blueprint; for the per-shot row schema see below + `docs/VIDEO_PROMPT_CONVENTIONS.md`.

**The sheet is TEXT-HEAVY** (title, panel titles, captions, bar labels) → use **GPT Image 2** (project standard); aspect **16:9** (or 3:2). Keep the same character(s) + environment + grade across all panels. See `docs/MODEL_PROMPTING.md`.

## Shot-list rows (per shot)
| shot | dur(s) | size | camera move | subjects | action (one beat) | location | dialogue/SFX | refs_used | continuity | purpose |
|------|--------|------|-------------|----------|-------------------|----------|--------------|-----------|-----------|---------|

## Storyboard sheet layout
- TITLE BAR: "STORYBOARD – <TITLE>" + "OBJECTIVE: <...>".
- PANEL GRID: N numbered panels (e.g. 12 in a 4×3 grid). Each: number + short title (e.g. "1. INTRO – THE STAGE IS SET"), a cinematic image of the beat, and a 2–3 line caption beneath.
- BOTTOM BAR: VISUAL STYLE & TONE (text) · COLOR PALETTE (swatches) · CAMERA NOTES (text) · KEY ELEMENTS (bullets) · optional logo.

SEND VERBATIM (example filled):
```
A professional storyboard sheet, landscape, dark editorial layout. TITLE: "STORYBOARD – ALE BASKETBALL DUNK CONTEST FINALS", subtitle "OBJECTIVE: SCORE A 50 TO WIN". A 4x3 grid of 12 numbered cinematic panels, each with a short title and a 2-3 line caption beneath — 1 INTRO wide arena, 2 backstage close-up, 3 walk to court, 4 the setup at the arc, 5 close-up focus, 6 the run-up, 7 takeoff, 8 the scorpion dunk, 9 the finish at the rim, 10 scoreboard reading "50 PERFECT SCORE", 11 the reaction, 12 the champion lifting a trophy. The SAME player (black jersey number 24) and the SAME indoor arena across all panels, cinematic high-contrast dramatic lighting. BOTTOM BAR: "VISUAL STYLE & TONE: cinematic, high contrast, realistic, high energy", a COLOR PALETTE swatch strip, "CAMERA NOTES: wide + tracking shots, slow-motion dunk, tight close-ups", and "KEY ELEMENTS: pressure, focus, athleticism, crowd energy, victory". Legible captions, consistent identity across panels, no warped text.
```

NEGATIVE: inconsistent character or arena between panels, unreadable captions, single-poster composition.
