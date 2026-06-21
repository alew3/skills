# Example: Character + turnaround sheet (individual skills)

## Step 1 — `character-designer` (prompt mode)

User: *"Design Pip, a 9-year-old adventurer for a children's-book style."*

IDENTITY BLOCK (≤50 words, reuse verbatim):
> Pip, a 9-year-old boy with a round face, big curious brown eyes, copper-red shoulder-length wavy hair, freckles, round glasses, wearing a mustard hooded tunic and brown satchel, small and wiry. // SCENE: setting, pose, expression only.

```
SEND VERBATIM:
Children's-book illustration. Pip, a 9-year-old boy with a round face, big curious brown eyes, copper-red shoulder-length wavy hair, freckles, round glasses, mustard hooded tunic, brown satchel, small and wiry, brave-but-warm expression. Front-facing, neutral pose, flat even lighting, plain off-white background. Soft gouache style, consistent proportions. No background scenery, no extra characters.
```
REUSE STRATEGY: Element (illustrated single subject) → register with `show_reference_elements`, then put `<<<pip>>>` in later prompts. SUGGESTED PARAMETERS: model `nano_banana_pro` · 2:3 · 2k.

## Step 2 — `character-sheet-builder` (master → derive)

Given Pip's approved master, it emits one prompt per view (not one mega-prompt):

```
SEND VERBATIM:
Using the attached image as the EXACT character reference (same face, hair, glasses, outfit, colors): re-render Pip as a side profile, 90 degrees, full body, A-pose, plain light-grey background, flat even lighting, eye-level, same scale. Change ONLY the viewing angle; everything else pixel-consistent with the reference.
```
(repeat for front, 3/4, back; then assemble) — plus an expression-sheet pass varying ONLY the expression. SUGGESTED PARAMETERS: model `nano_banana_pro` · 16:9 · 2k.
