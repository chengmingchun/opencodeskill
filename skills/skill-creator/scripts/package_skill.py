#!/usr/bin/env python3
"""Skill Packager - Creates a distributable .skill file of a skill folder."""

import fnmatch
import sys
import zipfile
from pathlib import Path


def validate_skill(skill_path):
    """Basic validation of a skill"""
    skill_path = Path(skill_path)
    skill_md = skill_path / 'SKILL.md'
    if not skill_md.exists():
        return False, "SKILL.md not found"
    return True, "Valid"


# Patterns to exclude when packaging skills.
EXCLUDE_DIRS = {"__pycache__", "node_modules", ".git"}
EXCLUDE_GLOBS = {"*.pyc"}
EXCLUDE_FILES = {".DS_Store"}


def should_exclude(path: Path) -> bool:
    """Check if a path should be excluded from the package."""
    name = path.name
    
    # Check exact matches
    if name in EXCLUDE_FILES:
        return True
    
    # Check directory matches
    if path.is_dir() and name in EXCLUDE_DIRS:
        return True
    
    # Check glob patterns
    for pattern in EXCLUDE_GLOBS:
        if fnmatch.fnmatch(name, pattern):
            return True
    
    return False


def package_skill(skill_path, output_dir=None):
    """Package a skill folder into a .skill zip file."""
    skill_path = Path(skill_path)
    
    if not skill_path.is_dir():
        print(f"Error: Path is not a directory: {skill_path}")
        return None

    # Validate
    valid, message = validate_skill(skill_path)
    if not valid:
        print(f"Error: {message}")
        return None

    # Determine output path
    if output_dir:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
    else:
        output_dir = Path.cwd()

    output_file = output_dir / f"{skill_path.name}.skill"

    # Create zip
    with zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED) as zf:
        for path in skill_path.rglob('*'):
            if should_exclude(path):
                continue
            
            arcname = path.relative_to(skill_path)
            zf.write(path, arcname)

    print(f"Package created: {output_file}")
    return output_file


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python package_skill.py <path/to/skill-folder> [output-directory]")
        sys.exit(1)

    skill_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    
    package_skill(skill_path, output_dir)
