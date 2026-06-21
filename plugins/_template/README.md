# {{PLUGIN_NAME}}

{{PLUGIN_DESCRIPTION}}

## Skills

| Skill | Responsibility | Can be used independently? |
|---|---|---|
| `template-orchestrator` | Coordinates this plugin workflow. | Yes |

## Usage

Call the orchestrator when you want the full workflow:

```text
template-orchestrator
```

Call individual skills directly when you only need one stage.

## Development notes

After generating a plugin from this template:

1. Rename and refine the orchestrator skill if needed.
2. Add specialist skills under `skills/<skill-id>/SKILL.md`.
3. Add templates under `templates/`.
4. Add examples under `examples/`.
5. Update `plugin.json`.
6. Run marketplace validation.
