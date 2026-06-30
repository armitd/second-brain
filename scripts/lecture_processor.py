#!/usr/bin/env python3
"""
COG Lecture Processor — YouTube URL to vault note loop.

TRIGGER  → launchd WatchPaths fires when lecture_queue.txt changes
DO       → yt-dlp downloads audio, faster-whisper transcribes locally (free),
           Claude structures the transcript into a vault note
VERIFY   → 4 sections present + at least 2 [[wiki links]]
ITERATE  → stricter prompt, max 3 retries
STOP     → verify passes or max retries exhausted

To queue a lecture: add a YouTube URL on a new line in scripts/lecture_queue.txt
"""

import os
import re
import sys
import subprocess
from pathlib import Path

try:
    import anthropic
except ImportError:
    sys.exit("anthropic not installed — run: pip install anthropic")

try:
    from faster_whisper import WhisperModel
except ImportError:
    sys.exit("faster-whisper not installed — run: pip install faster-whisper")

sys.path.insert(0, str(Path(__file__).parent))
from cog_utils import VAULT, get_vault_stems, slug, load_state, save_state, today_str

# ── Config ─────────────────────────────────────────────────────────────────────

MODEL               = "claude-sonnet-4-6"
WHISPER_SIZE        = "base"   # base = fast; "small" = better quality, slower
MAX_TRANSCRIPT_CHARS = 15000
MAX_RETRIES         = 3

SCRIPTS_DIR         = Path(__file__).parent
QUEUE_FILE          = SCRIPTS_DIR / "lecture_queue.txt"
WORK_DIR            = SCRIPTS_DIR / ".work"
STATE_FILE          = SCRIPTS_DIR / ".processed_lectures.json"
OUTPUT_DIR          = VAULT / "05-knowledge" / "booklets" / "lectures"

REQUIRED_SECTIONS   = ["Key Concepts", "Quotes", "Self-Test Questions", "Related Notes"]

# ── Queue ───────────────────────────────────────────────────────────────────────

def read_queue() -> list[str]:
    if not QUEUE_FILE.exists():
        return []
    return [
        line.strip() for line in QUEUE_FILE.read_text().splitlines()
        if line.strip() and not line.strip().startswith("#")
    ]

# ── Download & transcribe ───────────────────────────────────────────────────────

def get_title(url: str) -> str:
    r = subprocess.run(
        ["yt-dlp", "--get-title", "--no-playlist", url],
        capture_output=True, text=True, timeout=30,
    )
    return r.stdout.strip() if r.returncode == 0 else "Untitled Lecture"


def download_audio(url: str) -> Path | None:
    WORK_DIR.mkdir(parents=True, exist_ok=True)
    r = subprocess.run(
        [
            "yt-dlp", "-x",
            "--audio-format", "mp3",
            "--audio-quality", "5",
            "--no-playlist",
            "-o", str(WORK_DIR / "%(id)s.%(ext)s"),
            url,
        ],
        capture_output=True, text=True, timeout=600,
    )
    if r.returncode != 0:
        print(f"    yt-dlp failed: {r.stderr[:200]}", file=sys.stderr)
        return None
    files = sorted(WORK_DIR.glob("*.mp3"), key=lambda p: p.stat().st_mtime)
    return files[-1] if files else None


def transcribe(audio: Path) -> str | None:
    try:
        model    = WhisperModel(WHISPER_SIZE, device="cpu", compute_type="int8")
        segments, _ = model.transcribe(str(audio), beam_size=1)
        return " ".join(seg.text for seg in segments).strip()
    except Exception as e:
        print(f"    Whisper failed: {e}", file=sys.stderr)
        return None

# ── Loop: generate → verify → iterate ──────────────────────────────────────────

_BASE_PROMPT = """\
Process this lecture transcript for a second brain vault.

Lecture: {title}
Source: {url}

Transcript:
{transcript}

Existing vault notes (use exact stems for [[wiki links]]):
{stems}

Write a note with exactly these 4 sections:

## Key Concepts
Five concepts from this lecture, each explained in 2-3 plain-language sentences.
Number them 1-5.

## Quotes
Three memorable quotes worth keeping. Format each as:
> "quote text" — [~timestamp if estimable from context]

## Self-Test Questions
Five questions to test understanding in a week.
Each must be answerable specifically from this lecture.

## Related Notes
At least two [[wiki links]] to related existing vault notes.
Use exact stems from the list provided above.

No preamble. Output the 4 sections only."""

_RETRY_SUFFIX = """

PREVIOUS ATTEMPT FAILED VERIFY. Failures:
{failures}

Fix them. All 4 sections must be present. Related Notes needs at least 2 [[wiki links]]."""


def _check(text: str) -> list[str]:
    failures = []
    for s in REQUIRED_SECTIONS:
        if f"## {s}" not in text:
            failures.append(f"Missing section: {s}")
    n = len(re.findall(r"\[\[.+?\]\]", text))
    if n < 2:
        failures.append(f"Need at least 2 [[wiki links]], found {n}")
    return failures


def process_lecture(client: anthropic.Anthropic, title: str, url: str,
                    transcript: str, stems: list[str]) -> str | None:
    stems_str = "\n".join(f"- {s}" for s in stems[:100])
    body      = transcript[:MAX_TRANSCRIPT_CHARS]
    failures: list[str] = []

    for attempt in range(MAX_RETRIES + 1):
        prompt = _BASE_PROMPT.format(title=title, url=url, transcript=body, stems=stems_str)
        if attempt > 0:
            prompt += _RETRY_SUFFIX.format(failures="\n".join(f"  {f}" for f in failures))

        resp     = client.messages.create(model=MODEL, max_tokens=2000,
                                          messages=[{"role": "user", "content": prompt}])
        text     = resp.content[0].text.strip()
        failures = _check(text)

        if not failures:
            return text          # STOP — verified

    return None                  # give up after MAX_RETRIES

# ── Output ──────────────────────────────────────────────────────────────────────

_FRONTMATTER = """\
---
type: "lecture-note"
category: "lectures"
source: "lecture-loop"
source_url: "{url}"
date_processed: "{today}"
created: "{today}"
title: "{title}"
tags: ["#lecture", "#loop"]
status: "processed"
---

# {title}

"""

def save_note(title: str, url: str, body: str) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    today = today_str()
    out   = OUTPUT_DIR / f"{slug(title)}-{today}.md"
    out.write_text(
        _FRONTMATTER.format(today=today, title=title, url=url)
        + body + "\n\n---\n*Processed by COG lecture loop*\n",
        encoding="utf-8",
    )
    return out

# ── Main ────────────────────────────────────────────────────────────────────────

def main() -> None:
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("ANTHROPIC_API_KEY not set")

    urls = read_queue()
    if not urls:
        print("Lecture loop: queue is empty")
        return

    processed = load_state(STATE_FILE)
    pending   = [u for u in urls if u not in processed]

    if not pending:
        print("Lecture loop: all queued URLs already processed")
        return

    client = anthropic.Anthropic()
    stems  = get_vault_stems()

    print(f"Processing {len(pending)} lecture(s)...")
    done = failed = 0

    for url in pending:
        print(f"\n  {url}")

        print("    Fetching title ...", end=" ", flush=True)
        title = get_title(url)
        print(title[:60])

        print("    Downloading audio ...", end=" ", flush=True)
        audio = download_audio(url)
        if not audio:
            failed += 1
            continue
        print(f"done ({audio.stat().st_size // 1024} KB)")

        print("    Transcribing ...", end=" ", flush=True)
        transcript = transcribe(audio)
        audio.unlink(missing_ok=True)
        if not transcript:
            failed += 1
            continue
        print(f"done ({len(transcript.split())} words)")

        print("    Generating note ...", end=" ", flush=True)
        body = process_lecture(client, title, url, transcript, stems)

        if body:
            out = save_note(title, url, body)
            processed.add(url)
            print(f"done → {out.name}")
            done += 1
        else:
            print("verify failed after retries")
            failed += 1

    save_state(STATE_FILE, processed)

    if WORK_DIR.exists() and not any(WORK_DIR.iterdir()):
        WORK_DIR.rmdir()

    print(f"\nLecture loop complete: {done} processed, {failed} failed")


if __name__ == "__main__":
    main()
