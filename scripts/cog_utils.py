"""Shared utilities for COG automation scripts."""

import re
import json
from pathlib import Path
from datetime import date

VAULT = Path.home() / "Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain"

_LINK_DIRS  = ["05-knowledge", "04-projects", "03-professional", "02-personal"]
_SKIP_STEMS = {
    "CLAUDE", "AGENTS", "ERRORS", "LOOPS", "MEMORY", "README",
    "SETUP", "CHANGELOG", "CONTRIBUTING", "GEMINI", "COG-VERSION",
}


def get_vault_stems(max_stems: int = 150) -> list[str]:
    """Collect existing note stems for [[wiki link]] suggestions."""
    stems: list[str] = []
    for dir_name in _LINK_DIRS:
        for path in (VAULT / dir_name).rglob("*.md"):
            s = path.stem
            if s not in _SKIP_STEMS and not s.startswith("."):
                stems.append(s)
            if len(stems) >= max_stems:
                return stems
    return stems


def slug(text: str, max_len: int = 50) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text).strip("-")
    return text[:max_len]


def load_state(path: Path) -> set[str]:
    return set(json.loads(path.read_text())) if path.exists() else set()


def save_state(path: Path, items: set[str]) -> None:
    path.write_text(json.dumps(sorted(items), indent=2))


def today_str() -> str:
    return date.today().strftime("%Y-%m-%d")
