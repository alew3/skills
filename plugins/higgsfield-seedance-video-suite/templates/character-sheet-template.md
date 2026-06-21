# Character Sheet Template

For a turnaround / expression / pose sheet. Build via **master → derive** (regenerate each view from the approved master), not one mega-prompt. See `docs/IMAGE_PROMPT_CONVENTIONS.md` §6.

CHARACTER: `character:<name>`
MASTER REFERENCE: [approved master image / media_id]
IDENTITY BLOCK (verbatim from character-designer): [≤50-word descriptor]
SHEET TYPE: [turnaround | expression | pose]
ASPECT RATIO: [16:9 default]

TURNAROUND VIEWS: [front, 3/4 (45°), side (90°), back] · POSE: [A-pose | T-pose]
EXPRESSION LIST (if expression sheet): [neutral, happy, angry, surprised, sad, …]

UNIFORM STAGING (identical every panel): plain light-grey seamless background, flat even studio lighting, eye-level, same scale and ground line.

SEND VERBATIM (one prompt per view, derived from the master):
[View prompt — "Using the attached master as the EXACT character reference, re-render as <view>, A-pose, full body, plain light-grey background, flat even lighting; change ONLY the viewing angle; everything else pixel-consistent."]

NEGATIVE: no background scenery, no pose/expression change between views, no color shift, no identity drift.
