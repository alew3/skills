# Dual-Mode & Clarify Protocol

Every generation skill in this suite follows the same pre-flight contract before it produces anything: **clarify → choose execution mode → execute**. This file is the single source of truth; each skill references it in one line ("Follow the clarify + dual-mode protocol in `docs/DUAL_MODE.md`") instead of restating it.

---

## Step 1 — CLARIFY before generating (never guess consequential params)

A skill must not generate (or emit a final prompt) while a **consequential** parameter is unknown or the request is ambiguous. Resolve these first.

**How to ask:** batch all open questions into **one** grouped message (don't drip one at a time), offer a sensible default per question, and keep it short. For **trivial** params, pick the obvious default and *state the assumption* instead of asking ("Assuming 16:9 — say the word for 9:16"). Only hard-block on params that materially change the output or cost.

**Required-parameter checklists** (ask any that are missing/ambiguous):

| Output | Must be known before generating |
|---|---|
| **Image** (any) | **aspect ratio / format** (1:1, 4:5, 2:3, 16:9, 9:16, 21:9…), subject & setting, **style** (photoreal vs illustration vs vector…), and in MCP mode: model + quality/resolution, count, any reference image |
| **Character** | identity anchors (see `IMAGE_PROMPT_CONVENTIONS.md` bible), realism vs stylized, reuse strategy (one-off ref vs **Soul** train vs **Element**) |
| **Character / expression sheet** | which sheet (turnaround / expression / pose), view list or emotion list, aspect ratio, master-reference availability |
| **Environment sheet** | location, key architectural anchors, time-of-day, which angles, aspect ratio |
| **Storyboard** | number of shots/panels, aspect ratio, level of finish (rough vs rendered) |
| **Video / shot** | **aspect ratio**, **duration** (and that it's an allowed step for the model), shot type & camera move, **start frame?** (text-to-video vs image-to-video), **audio?** (native vs none), model |
| **Audio** | speech vs (decline music/SFX), language, voice (preset vs cloned element), script text |

If the creative intent itself is unclear (vague subject, undefined goal, conflicting references), ask a clarifying question **before** the parameter questions — getting the wrong thing in the right format is still wrong.

---

## Step 2 — Choose EXECUTION MODE

- **MCP MODE** — the Higgsfield MCP is available *and* the user wants the actual asset now → call the mapped tool and return real media.
- **PROMPT MODE** — no MCP, or the user just wants the prompt text to run elsewhere → emit a clean `SEND VERBATIM` block and stop.

If it's unclear which the user wants, ask exactly one question: **"Generate it now via Higgsfield, or just hand you the prompt to run yourself?"** (Often combine this into the Step-1 batch.)

---

## Step 3a — PROMPT MODE output

Emit the final prompt inside a fenced, clearly-labeled block that contains **only** the prompt — no chat, no commentary, no metadata inside it:

```
SEND VERBATIM:
<the complete final prompt and nothing else>
```

Everything the user should know *about* the prompt (which model it targets, suggested aspect ratio/duration, reference images to attach, alternatives) goes **outside** the block, before or after it. The block must survive copy-paste into any tool unchanged. `passthrough-guardian` validates this.

Where it helps, also give the **ready-to-run MCP arguments** for the same prompt (so a user with the MCP can paste them), as a separate JSON block outside the VERBATIM block:

```json
{ "params": { "model": "…", "prompt": "<same text as SEND VERBATIM>", "aspect_ratio": "…" } }
```

---

## Step 3b — MCP MODE execution

1. **Resolve the model & params** per `docs/HIGGSFIELD_MCP_REFERENCE.md` — `models_explore(action:"recommend", …)` then `models_explore(action:"get", …)` to confirm exact enums (aspect_ratio, duration steps, quality/resolution, media roles). Don't invent param values.
2. **Reference media:** convert any URL/local file to a `media_id` first (`media_import_url` / `media_upload_widget`) — never pass a URL in `medias[].value`.
3. **Preflight cost:** call with `get_cost:true`, show the credit cost, and **confirm with the user before spending** (especially 4K / high quality / count>1 / video).
4. **Generate**, then **poll `job_status`** until terminal (respect `poll_after_seconds`).
5. **Route the result to `asset-approval-gate`** (approve / revise / reject) before it's used downstream.
6. **Echo the exact `params` you used** so the user can reproduce or tweak the call themselves — this keeps MCP mode and prompt mode interchangeable.
7. If a call returns a `recovery_tool`, call it immediately. Lost results → `reveal_generation` / `show_generations`.

---

## Invariants (both modes)

- **Approval gates** fire after any asset that affects downstream generation (character, any sheet, style board, storyboard, final video prompt) — in *both* modes (in prompt mode you approve the prompt; in MCP mode you approve the rendered media).
- **Asset-map authority:** once an asset is approved its number/name is locked; only `asset-approval-gate` writes asset-map entries; orchestrators read them.
- **Continuity:** thread approved references (character master, environment master, palette, aspect ratio) into every later stage — see the conventions docs.
- **Don't default to "cinematic."** State concrete lighting, lens, and composition instead (see `IMAGE_PROMPT_CONVENTIONS.md`).
