#!/usr/bin/env python3
"""Shared utilities for skill-creator scripts."""

import re
from pathlib import Path


def parse_skill_md(skill_path: Path) -> tuple[str, str, str]:
    """Parse a SKILL.md file, returning (name, description, full_content)."""
    content = (skill_path / "SKILL.md").read_text()
    lines = content.split("\n")

    if lines[0].strip() != "---":
        raise ValueError("SKILL.md missing frontmatter (no opening ---)")

    end_idx = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_idx = i
            break

    if end_idx is None:
        raise ValueError("SKILL.md missing frontmatter (no closing ---)")

    frontmatter = "\n".join(lines[1:end_idx])
    
    # Parse name and description from frontmatter
    name_match = re.search(r'^name:\s*(.+)$', frontmatter, re.MULTILINE)
    desc_match = re.search(r'^description:\s*(.+)$', frontmatter, re.MULTILINE)
    
    name = name_match.group(1).strip() if name_match else ""
    description = desc_match.group(1).strip() if desc_match else ""
    
    return name, description, content


def validate_skill(skill_path: Path) -> tuple[bool, str]:
    """Basic validation of a skill."""
    # Check SKILL.md exists
    skill_md = skill_path / 'SKILL.md'
    if not skill_md.exists():
        return False, "SKILL.md not found"

    # Read and validate frontmatter
    content = skill_md.read_text()
    if not content.startswith('---'):
        return False, "No YAML frontmatter found"

    # Extract frontmatter
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return False, "Invalid frontmatter format"

    frontmatter_text = match.group(1)

    # Check required fields
    if 'name:' not in frontmatter_text:
        return False, "Missing required field: name"
    if 'description:' not in frontmatter_text:
        return False, "Missing required field: description"

    return True, "Valid skill"


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python utils.py <skill-path>")
        sys.exit(1)
    
    skill_path = Path(sys.argv[1])
    valid, message = validate_skill(skill_path)
    if valid:
        print(f"✓ {message}")
        name, desc, _ = parse_skill_md(skill_path)
        print(f"Name: {name}")
        print(f"Description: {desc}")
    else:
        print(f"✗ {message}")
        sys.exit(1)
