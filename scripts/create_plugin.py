#!/usr/bin/env python3
"""Create a new plugin from the marketplace template."""
from __future__ import annotations

import argparse
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = ROOT / "plugins" / "_template"
PLUGINS_DIR = ROOT / "plugins"
MARKETPLACE_PATH = ROOT / "marketplace.json"
SLUG_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Create a new marketplace plugin.")
    parser.add_argument("plugin_id", help="Lowercase kebab-case plugin id, e.g. my-new-plugin")
    parser.add_argument("--name", required=True, help="Human-readable plugin name")
    parser.add_argument("--description", required=True, help="Short plugin description")
    parser.add_argument("--category", default="general", help="Marketplace category")
    parser.add_argument("--author", default="", help="Plugin author")
    parser.add_argument("--no-register", action="store_true", help="Create files but do not add to marketplace.json")
    return parser.parse_args()


def replace_in_file(path: Path, replacements: dict[str, str]) -> None:
    if not path.is_file():
        return
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return
    for old, new in replacements.items():
        text = text.replace(old, new)
    path.write_text(text, encoding="utf-8")


def main() -> int:
    args = parse_args()
    plugin_id = args.plugin_id.strip()
    if not SLUG_RE.match(plugin_id):
        print("Error: plugin_id must be lowercase kebab-case, e.g. my-new-plugin", file=sys.stderr)
        return 1

    target_dir = PLUGINS_DIR / plugin_id
    if target_dir.exists():
        print(f"Error: plugin already exists: {target_dir}", file=sys.stderr)
        return 1
    if not TEMPLATE_DIR.exists():
        print(f"Error: template directory not found: {TEMPLATE_DIR}", file=sys.stderr)
        return 1

    shutil.copytree(TEMPLATE_DIR, target_dir)

    orchestrator_old = target_dir / "skills" / "template-orchestrator"
    orchestrator_new = target_dir / "skills" / f"{plugin_id}-orchestrator"
    if orchestrator_old.exists():
        orchestrator_old.rename(orchestrator_new)

    replacements = {
        "{{PLUGIN_ID}}": plugin_id,
        "{{PLUGIN_NAME}}": args.name,
        "{{PLUGIN_DESCRIPTION}}": args.description,
        "{{PLUGIN_CATEGORY}}": args.category,
        "{{AUTHOR}}": args.author,
        "template-orchestrator": f"{plugin_id}-orchestrator",
    }
    for path in target_dir.rglob("*"):
        replace_in_file(path, replacements)

    if not args.no_register:
        marketplace = json.loads(MARKETPLACE_PATH.read_text(encoding="utf-8"))
        marketplace.setdefault("plugins", [])
        if any(p.get("id") == plugin_id for p in marketplace["plugins"]):
            print(f"Error: marketplace already contains plugin id: {plugin_id}", file=sys.stderr)
            return 1
        marketplace["plugins"].append({
            "id": plugin_id,
            "name": args.name,
            "version": "0.1.0",
            "description": args.description,
            "path": f"plugins/{plugin_id}",
            "category": args.category,
            "tags": [],
            "entry_skill": f"{plugin_id}-orchestrator",
            "skill_count": 1
        })
        MARKETPLACE_PATH.write_text(json.dumps(marketplace, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"Created plugin: plugins/{plugin_id}")
    print("Next steps:")
    print(f"- Edit plugins/{plugin_id}/plugin.json")
    print(f"- Edit plugins/{plugin_id}/README.md")
    print(f"- Edit plugins/{plugin_id}/skills/{plugin_id}-orchestrator/SKILL.md")
    print("- Run: python scripts/validate_marketplace.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
