# Adding a New Plugin

## Option 1: Use the generator

```bash
python scripts/create_plugin.py my-plugin   --name "My Plugin"   --description "A plugin for my workflow"   --category "general"   --author "Your Name"
```

Then edit:

```text
plugins/my-plugin/plugin.json
plugins/my-plugin/README.md
plugins/my-plugin/skills/my-plugin-orchestrator/SKILL.md
```

Validate:

```bash
python scripts/validate_marketplace.py
```

## Option 2: Copy the template manually

```bash
cp -R plugins/_template plugins/my-plugin
```

Then replace all placeholders:

```text
{{PLUGIN_ID}}
{{PLUGIN_NAME}}
{{PLUGIN_DESCRIPTION}}
{{PLUGIN_CATEGORY}}
{{AUTHOR}}
```

## Checklist

Before committing a plugin:

- [ ] Plugin folder uses lowercase kebab-case.
- [ ] `plugin.json` is valid JSON.
- [ ] `README.md` explains how to use the plugin.
- [ ] Each skill has a clear responsibility.
- [ ] Each skill has frontmatter with `name` and `description`.
- [ ] The orchestrator skill is identified, if one exists.
- [ ] Examples show real usage.
- [ ] Templates are reusable.
- [ ] `python scripts/validate_marketplace.py` passes.

## When to create a new plugin vs a new skill

Create a new skill when it belongs to an existing workflow.

Create a new plugin when it represents a new capability area, such as:

- a new platform adapter;
- a new generation model family;
- a new business workflow;
- a new teaching workflow;
- a new content format;
- a new QA/validation system.
