# Workflow Architecture

This marketplace uses a modular skill architecture.

## Layers

```text
Marketplace
└── Plugin
    ├── Orchestrator skill
    ├── Specialist skill
    ├── Specialist skill
    ├── Templates
    └── Examples
```

## Full video workflow example

```text
User intent
→ video-workflow-orchestrator
→ creative-brief-grill → approved brief
→ (per character) character-designer → asset-approval-gate → character-sheet-builder → asset-approval-gate
→ (per environment) environment-sheet-builder → asset-approval-gate
→ style-board-builder → asset-approval-gate
→ storyboard-builder (shot list + keyframes) → asset-approval-gate
→ (per shot) video-prompt-architect → passthrough-guardian
→ audio-generator (optional)
→ higgsfield-package-adapter
→ final package (prompts) or rendered clips (MCP mode)
```

A project may contain multiple characters and multiple environments; design each once and reuse it across shots. The image-only path uses `image-workflow-orchestrator` (brief → style board → characters/sheets → environments → hero images).

## Dual mode

Every generation skill runs in one of two modes (see the plugin's `docs/DUAL_MODE.md`):

- **PROMPT MODE** — emit a `SEND VERBATIM:` block (only the prompt) plus optional ready-to-run MCP args.
- **MCP MODE** — drive the Higgsfield MCP: resolve model, preflight credit cost and confirm, generate, poll, approve.

Skills clarify any missing parameter (format, aspect ratio, duration, model, references) before generating.

## Approval gates

Approval gates are required when an intermediate output affects downstream generation.

Examples:

- character reference;
- product reference;
- environment sheet;
- storyboard;
- final passthrough prompt.

## Passthrough blocks

When a final prompt must be sent to a downstream tool unchanged, isolate it in a block labeled:

```text
SEND VERBATIM:
...
```

Everything outside that block is commentary or metadata.
