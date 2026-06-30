#!/usr/bin/env python3
"""
COG Vault Review — autonomous spaced repetition loop.

Triggered by launchd daily at 06:00. Finds notes at 7/30/90-day intervals,
generates review questions via Claude API, verifies they reference specific
content (not generic), and appends the digest to today's daybook.

Loop pattern: TRIGGER → DO → VERIFY → ITERATE → STOP
Stop condition: question passes verify, OR 2 retries exhausted per note.
"""

import os
import sys
import datetime
from pathlib import Path

try:
    import anthropic
except ImportError:
    sys.exit("anthropic package not installed. Run: pip install anthropic")


# ── Configuration ────────────────────────────────────────────────────────────

VAULT = Path.home() / "Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain"

EXCLUDE_DIRS = {
    "Readwise", ".claude", ".kiro", ".gemini", ".git",
    "01-daily", "node_modules", "scripts", "ScreenShots",
    "ClipperMaster", "memory",
}

EXCLUDE_FILES = {
    "CLAUDE.md", "AGENTS.md", "ERRORS.md", "LOOPS.md", "MEMORY.md",
    "README.md", "SETUP.md", "CHANGELOG.md", "CONTRIBUTING.md",
    "GEMINI.md", "COG-VERSION", "AGENTS.md",
}

# Spaced repetition windows: (label, min_days_ago, max_days_ago)
WINDOWS = [
    ("7 Days Ago",  6,  8),
    ("30 Days Ago", 27, 33),
    ("90 Days Ago", 83, 97),
]

MAX_NOTES_PER_WINDOW = 3
MIN_WORD_COUNT       = 150
MAX_CONTENT_CHARS    = 3500   # cap per note to keep API calls cheap
MAX_RETRIES          = 2
MODEL                = "claude-haiku-4-5-20251001"


# ── Helpers ──────────────────────────────────────────────────────────────────

def find_notes(min_days: int, max_days: int) -> list[Path]:
    now = datetime.datetime.now()
    candidates: list[Path] = []

    for path in VAULT.rglob("*.md"):
        # Skip excluded directories anywhere in path
        rel_parts = set(path.relative_to(VAULT).parts)
        if rel_parts & EXCLUDE_DIRS:
            continue
        if path.name in EXCLUDE_FILES:
            continue

        age = (now - datetime.datetime.fromtimestamp(path.stat().st_mtime)).days
        if min_days <= age <= max_days:
            candidates.append(path)

    # Prefer structured knowledge over raw captures
    def priority(p: Path) -> int:
        prefix = str(p.relative_to(VAULT))
        if prefix.startswith("05-knowledge") or prefix.startswith("04-projects"):
            return 0
        return 1

    candidates.sort(key=priority)
    return candidates[:MAX_NOTES_PER_WINDOW]


def note_title(content: str, path: Path) -> str:
    for line in content.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem.replace("-", " ").title()


def strip_frontmatter(content: str) -> str:
    if not content.startswith("---"):
        return content
    end = content.find("---", 3)
    return content[end + 3:].strip() if end != -1 else content


# ── Core loop: generate → verify → iterate ───────────────────────────────────

def generate_and_verify(client: anthropic.Anthropic, body: str, title: str) -> list[str] | None:
    """
    Returns verified questions, or None if verify fails after MAX_RETRIES.
    Hard rule: each question must reference specific content from the note,
    not be answerable from general knowledge alone.
    """
    base_prompt = (
        f"Read this note:\n\n{body}\n\n"
        "Generate 1-2 review questions. Each question MUST:\n"
        "- Name or quote something specific from this note (a fact, claim, decision, framework, or number)\n"
        "- Require having read this note to answer — not answerable from general knowledge alone\n"
        "- Be a single concise sentence\n\n"
        "Return as a bullet list starting with '- '. No preamble."
    )

    for attempt in range(MAX_RETRIES + 1):
        if attempt == 0:
            prompt = base_prompt
        else:
            prompt = (
                base_prompt
                + "\n\nPREVIOUS ATTEMPT WAS TOO GENERIC. "
                "Quote a specific fact, claim, or decision from the note directly."
            )

        # DO — generate
        gen = client.messages.create(
            model=MODEL,
            max_tokens=250,
            messages=[{"role": "user", "content": prompt}],
        )
        raw = gen.content[0].text.strip()
        questions = [
            line.lstrip("- ").strip()
            for line in raw.splitlines()
            if line.strip().startswith("-")
        ]
        if not questions:
            continue

        # VERIFY — hard rule check
        verify_prompt = (
            f'Note: "{title}"\n\n'
            f"Questions:\n{raw}\n\n"
            "For each question: does it contain a specific reference "
            "(a name, concept, claim, number, or decision from this particular note) "
            "or could someone answer it without having read this note?\n\n"
            "Reply with exactly one word: PASS or FAIL"
        )
        verdict = client.messages.create(
            model=MODEL,
            max_tokens=10,
            messages=[{"role": "user", "content": verify_prompt}],
        )
        if "PASS" in verdict.content[0].text.upper():
            return questions  # STOP — verified

        # ITERATE — loop again with stricter prompt
        if attempt == MAX_RETRIES:
            return None  # give up

    return None


# ── Output ───────────────────────────────────────────────────────────────────

def build_digest(sections: list[str], today: str, total_notes: int,
                 total_q: int, skipped: int) -> str:
    body = "\n\n".join(sections)
    return (
        f"## Vault Review — {today}\n\n"
        f"*Spaced repetition: notes from 7d / 30d / 90d windows*\n\n"
        f"{body}\n\n"
        f"---\n"
        f"*{total_notes} notes · {total_q} questions · {skipped} skipped*"
    )


# ── Main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        sys.exit("ANTHROPIC_API_KEY not set")

    client = anthropic.Anthropic(api_key=api_key)
    today = datetime.date.today().strftime("%Y-%m-%d")

    daybook = VAULT / "01-daily" / "daybooks" / f"daybook-{today}.md"
    fallback = VAULT / "01-daily" / "reviews" / f"vault-review-{today}.md"

    sections: list[str] = []
    total_notes = total_q = skipped = 0

    for label, min_days, max_days in WINDOWS:
        notes = find_notes(min_days, max_days)
        if not notes:
            continue

        lines = [f"### {label}"]
        for path in notes:
            raw_content = path.read_text(encoding="utf-8", errors="ignore")
            body = strip_frontmatter(raw_content)[:MAX_CONTENT_CHARS]

            if len(body.split()) < MIN_WORD_COUNT:
                skipped += 1
                continue

            title = note_title(raw_content, path)
            questions = generate_and_verify(client, body, title)

            if questions is None:
                skipped += 1
                print(f"  skip (verify failed): {path.name}", file=sys.stderr)
                continue

            lines.append(f"- **[[{path.stem}]]**")
            for q in questions:
                lines.append(f"  - Q: {q}")
                total_q += 1
            total_notes += 1

        if len(lines) > 1:
            sections.append("\n".join(lines))

    if not sections:
        print(f"Vault review: no notes found in any window for {today}")
        return

    digest = build_digest(sections, today, total_notes, total_q, skipped)

    if daybook.exists():
        with open(daybook, "a", encoding="utf-8") as f:
            f.write(f"\n{digest}\n")
        output = daybook
    else:
        fallback.parent.mkdir(parents=True, exist_ok=True)
        fallback.write_text(
            f"---\ntype: \"vault-review\"\ndate: \"{today}\"\n"
            f"notes_reviewed: {total_notes}\nquestions_generated: {total_q}\n---\n\n"
            f"{digest}\n",
            encoding="utf-8",
        )
        output = fallback

    print(f"Vault review complete.")
    print(f"Reviewed: {total_notes} notes | Questions: {total_q} | Skipped: {skipped}")
    print(f"Saved to: {output}")


if __name__ == "__main__":
    main()
