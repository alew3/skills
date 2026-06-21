# alew3 skills

A GitHub-ready marketplace repository for modular AI skill plugins.

This repo is designed so you can keep adding new plugins over time. Each plugin can contain multiple focused skills, templates, examples, and one optional orchestrator skill that coordinates the full workflow.

The first included plugin is:

```text
plugins/higgsfield-seedance-video-suite
```

It contains the full Higgsfield + Seedance video workflow skill pack:

```text
user intent
→ video briefing interview
→ approved brief
→ character / subject reference
→ design / style reference
→ environment reference
→ storyboard with captions
→ final Seedance / Higgsfield prompt
→ passthrough validation
→ final handoff package
```

## Install in Claude Code

This repo is a native **Claude Code plugin marketplace** (manifest at `.claude-plugin/marketplace.json`).

**1. Add the marketplace** (run inside Claude Code — CLI, desktop app, or IDE extension):

```text
/plugin marketplace add alew3/skills
```

You can also use a full Git URL: `/plugin marketplace add https://github.com/alew3/skills.git`

**2. Install a plugin** from it:

```text
/plugin install higgsfield-seedance-video-suite@alew3-skills
```

**3. Or browse the UI** — open the plugin manager and pick from the Discover tab:

```text
/plugin
```

**Update later** to pull the newest version:

```text
/plugin marketplace update alew3-skills
```

After installing, the plugin's skills are auto-discovered from `skills/<skill-id>/SKILL.md` and become available to Claude.

> Note: `alew3/skills` is the GitHub repo path; `alew3-skills` is the marketplace name used in `/plugin install <plugin>@<marketplace>`.

## Repository structure

```text
.
├── .claude-plugin/
│   └── marketplace.json             # Claude Code marketplace manifest (read by /plugin)
├── marketplace.json                 # Custom registry index (read by scripts/validate_marketplace.py)
├── plugins/
│   ├── higgsfield-seedance-video-suite/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json          # Claude Code plugin manifest
│   │   ├── plugin.json              # Custom plugin manifest
│   │   ├── README.md
│   │   ├── skills/
│   │   ├── templates/
│   │   └── examples/
│   └── _template/                   # Template for future plugins
├── docs/
│   ├── MARKETPLACE_SPEC.md
│   ├── PLUGIN_SPEC.md
│   ├── ADDING_A_PLUGIN.md
│   └── WORKFLOW.md
├── scripts/
│   ├── create_plugin.py             # Scaffold a new plugin
│   └── validate_marketplace.py      # Validate marketplace/plugin structure
└── .github/workflows/validate.yml   # Optional GitHub Action validation
```

## Marketplace concept

This is a **local-first plugin marketplace**, not a hosted app store.

The marketplace is simply a structured repository where:

- `marketplace.json` is the public index;
- every plugin lives inside `plugins/<plugin-id>/`;
- every plugin has its own `plugin.json` manifest;
- every skill lives inside `skills/<skill-id>/SKILL.md`;
- each skill can be called independently;
- orchestrator skills can call other skills by responsibility.

## Quick start

Validate the marketplace:

```bash
python scripts/validate_marketplace.py
```

Create a new plugin:

```bash
python scripts/create_plugin.py my-new-plugin   --name "My New Plugin"   --description "What this plugin does"   --category "general"   --author "Your Name"
```

This creates:

```text
plugins/my-new-plugin/
├── plugin.json
├── README.md
├── skills/my-new-plugin-orchestrator/SKILL.md
├── templates/
└── examples/
```

Then edit the generated files and run:

```bash
python scripts/validate_marketplace.py
```

## Included plugin

### Higgsfield + Seedance Video Suite

Path:

```text
plugins/higgsfield-seedance-video-suite
```

Orchestrators:

```text
video-workflow-orchestrator   # idea → finished video
image-workflow-orchestrator   # idea → coherent image set
```

Specialist skills (all independently callable):

- `creative-brief-grill`
- `image-generator`
- `character-designer`
- `character-sheet-builder`
- `environment-sheet-builder`
- `style-board-builder`
- `prop-sheet-builder`
- `storyboard-builder`
- `video-prompt-architect`
- `audio-generator`
- `asset-approval-gate`
- `passthrough-guardian`
- `higgsfield-package-adapter`

Every skill is **dual-mode** — it drives the Higgsfield MCP **or** emits paste-ready prompts — and clarifies missing parameters first. See the plugin's [`docs/GETTING_STARTED.md`](plugins/higgsfield-seedance-video-suite/docs/GETTING_STARTED.md). Use an orchestrator for the full workflow; use specialist skills directly for a single stage.

## Adding future plugins

A good plugin should be small, focused, and composable.

Recommended plugin types:

- video workflow plugins;
- image generation plugins;
- prompt optimization plugins;
- approval / QA plugins;
- platform adapter plugins;
- teaching / course generation plugins;
- product marketing plugins;
- codebase analysis plugins.

Each plugin should answer:

1. What problem does it solve?
2. What skills does it expose?
3. Which skill is the orchestrator, if any?
4. Which skills can be called independently?
5. What templates and examples does it provide?

## Design principles

- One plugin = one coherent capability area.
- One skill = one clear responsibility.
- Orchestrators coordinate; they do not replace specialist skills.
- Final generation prompts should be isolated inside `SEND VERBATIM` blocks when passthrough matters.
- Approval gates should be explicit when generated assets affect downstream results.

## License

MIT.
