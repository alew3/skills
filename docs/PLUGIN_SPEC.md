# Plugin Spec

A plugin is a folder that packages a coherent group of skills.

## Required files

```text
plugin.json
README.md
```

## Recommended directories

```text
skills/
templates/
examples/
docs/
```

## `plugin.json`

Example:

```json
{
  "schema_version": "0.1.0",
  "id": "my-plugin",
  "name": "My Plugin",
  "version": "0.1.0",
  "description": "What this plugin does.",
  "author": "Your Name",
  "license": "MIT",
  "category": "general",
  "tags": ["example"],
  "entry_skill": "my-plugin-orchestrator",
  "skills": [
    {
      "name": "my-plugin-orchestrator",
      "path": "skills/my-plugin-orchestrator/SKILL.md",
      "responsibility": "Coordinates this plugin's workflow.",
      "can_be_called_independently": true
    }
  ]
}
```

## Skill file format

Each skill should be a Markdown file with YAML-style frontmatter:

```markdown
---
name: my-skill
description: Use this skill when...
---

You are the My Skill specialist.

Your responsibility is...
```

## Responsibility boundaries

Each skill should have one primary job.

Good examples:

- `creative-brief-grill`: interviews the user;
- `image-generator`: creates image prompts;
- `asset-approval-gate`: manages approval loops;
- `passthrough-guardian`: validates final prompts.

Avoid giant skills that do everything.

## Orchestrator skills

An orchestrator skill coordinates other skills.

It should:

- detect the workflow mode;
- call specialist skills by responsibility;
- maintain approval gates;
- preserve user intent;
- produce a final package when appropriate.

It should not duplicate all specialist instructions.
