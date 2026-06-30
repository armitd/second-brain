#!/usr/bin/env python3
"""
COG Article Processor — nightly Readwise article ingestion loop.

TRIGGER  → launchd at 23:00
DO       → scan Readwise/Articles for unprocessed items, summarise via Claude
VERIFY   → note has all 5 sections + at least 1 [[wiki link]]
ITERATE  → retry with stricter prompt (max 2 retries)
STOP     → verify passes, or article flagged as fluff
"""

import os
import re
import sys
from pathlib import Path

try:
    import anthropic
except ImportError:
    sys.exit("anthropic not installed — run: pip install anthropic")

sys.path.insert(0, str(Path(__file__).parent))
from cog_utils import VAULT, get_vault_stems, slug, load_state, save_state, today_str

# ── Config ─────────────────────────────────────────────────────────────────────

MODEL               = "claude-sonnet-4-6"
MAX_PER_RUN         = 20
MAX_CONTENT_CHARS   = 6000
MAX_RETRIES         = 2
STATE_FILE          = Path(__file__).parent / ".processed_articles.json"

READWISE_DIR        = VAULT / "Readwise" / "Articles"
READWISE_FULL_DIR   = VAULT / "Readwise" / "Full Document Contents" / "Articles"
OUTPUT_DIR          = VAULT / "05-knowledge" / "booklets" / "articles"

REQUIRED_SECTIONS   = ["Summary", "Main Claims", "Best Quote", "Open Question", "Related Notes"]

# ── Parsing ─────────────────────────────────────────────────────────────────────

def parse_readwise(path: Path) -> dict:
    text  = path.read_text(encoding="utf-8", errors="ignore")
    title = author = url = ""

    for line in text.splitlines():
        line = line.strip()
        if line.lower().startswith("url:"):
            url = line.split(":", 1)[1].strip().strip('"')
        elif line.lower().startswith("author:"):
            author = line.split(":", 1)[1].strip().strip('"')
        elif line.startswith("# ") and not title:
            title = line[2:].strip()

    if not title:
        title = path.stem.replace("-", " ").title()

    # Prefer full text if available, otherwise use highlights
    full = READWISE_FULL_DIR / path.name
    if full.exists():
        body = full.read_text(encoding="utf-8", errors="ignore")[:MAX_CONTENT_CHARS]
    else:
        body = re.sub(r"^---.*?---\s*", "", text, flags=re.DOTALL).strip()[:MAX_CONTENT_CHARS]

    return {"title": title, "author": author, "url": url, "body": body}

# ── Loop: generate → verify → iterate ──────────────────────────────────────────

_BASE_PROMPT = """\
Process this article for a second brain vault.

Title: {title}
Author: {author}
URL: {url}

Content:
{body}

Existing vault notes (use exact stems for [[wiki links]]):
{stems}

Write a note with exactly these sections. Start with a SIGNAL line.

SIGNAL: [high / medium / low / fluff]
(fluff = no original claims, purely promotional, or only repeats common knowledge)

## Summary
One sentence capturing the article's core argument.

## Main Claims
Three claims this article makes, each followed by your assessment in brackets:
[holds up] / [questionable] / [unsupported]

## Best Quote
The single strongest quote, in blockquote format with attribution.

## Open Question
One question this article raises that you don't yet have an answer to.

## Related Notes
At least one [[wiki link]] to an existing vault note. Use exact stems from the list above.

No preamble. Output SIGNAL line first, then the five sections."""

_RETRY_SUFFIX = """

PREVIOUS ATTEMPT FAILED VERIFY. Failures:
{failures}

Fix them. All 5 sections must be present. Related Notes must contain at least one [[wiki link]]."""


def _check(text: str) -> list[str]:
    failures = []
    for s in REQUIRED_SECTIONS:
        if f"## {s}" not in text:
            failures.append(f"Missing section: {s}")
    if not re.search(r"\[\[.+?\]\]", text):
        failures.append("Related Notes must contain at least one [[wiki link]]")
    return failures


def process_article(client: anthropic.Anthropic, meta: dict, stems: list[str]) -> tuple[str | None, str]:
    stems_str = "\n".join(f"- {s}" for s in stems[:100])
    failures: list[str] = []

    for attempt in range(MAX_RETRIES + 1):
        prompt = _BASE_PROMPT.format(**meta, stems=stems_str)
        if attempt > 0:
            prompt += _RETRY_SUFFIX.format(failures="\n".join(f"  {f}" for f in failures))

        resp  = client.messages.create(model=MODEL, max_tokens=1200,
                                       messages=[{"role": "user", "content": prompt}])
        text  = resp.content[0].text.strip()

        m = re.search(r"SIGNAL:\s*(high|medium|low|fluff)", text, re.IGNORECASE)
        signal = m.group(1).lower() if m else "medium"

        if signal == "fluff":
            return None, "fluff"

        failures = _check(text)
        if not failures:
            return text, signal          # STOP — verified

    return None, "verify-failed"         # give up

# ── Output ──────────────────────────────────────────────────────────────────────

_FRONTMATTER = """\
---
type: "readwise-article"
category: "articles"
source: "readwise-loop"
source_readwise: "Readwise/Articles/{filename}"
date_processed: "{today}"
created: "{today}"
title: "{title}"
author: "{author}"
url: "{url}"
signal: "{signal}"
tags: ["#readwise", "#article", "#loop"]
status: "processed"
---

# {title}

"""

def save_note(meta: dict, body: str, signal: str, filename: str) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    today = today_str()
    out   = OUTPUT_DIR / f"{slug(meta['title'])}-{today}.md"
    out.write_text(
        _FRONTMATTER.format(filename=filename, today=today, signal=signal, **meta)
        + body + "\n\n---\n*Processed by COG article loop*\n",
        encoding="utf-8",
    )
    return out

# ── Main ────────────────────────────────────────────────────────────────────────

def main() -> None:
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("ANTHROPIC_API_KEY not set")
    if not READWISE_DIR.exists():
        sys.exit(f"Readwise articles not found: {READWISE_DIR}")

    client    = anthropic.Anthropic()
    processed = load_state(STATE_FILE)
    stems     = get_vault_stems()

    queue = [p for p in READWISE_DIR.glob("*.md") if p.name not in processed][:MAX_PER_RUN]

    if not queue:
        print("Article loop: nothing new to process")
        return

    print(f"Processing {len(queue)} article(s)...")
    done = fluff = failed = 0

    for path in queue:
        meta = parse_readwise(path)
        print(f"  {meta['title'][:60]}", end=" ... ", flush=True)

        body, signal = process_article(client, meta, stems)

        if body:
            out = save_note(meta, body, signal, path.name)
            processed.add(path.name)
            print(f"[{signal}] → {out.name}")
            done += 1
        elif signal == "fluff":
            processed.add(path.name)
            print("[fluff — skipped]")
            fluff += 1
        else:
            print(f"[{signal}]")
            failed += 1

    save_state(STATE_FILE, processed)
    print(f"\nDone: {done} processed, {fluff} fluff, {failed} failed")


if __name__ == "__main__":
    main()
