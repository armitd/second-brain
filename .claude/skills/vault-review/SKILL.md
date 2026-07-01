---
name: vault-review
description: Surface notes from 7/30/90 days ago with spaced repetition review questions to reinforce learning — designed to run autonomously on a schedule
roles: [all]
integrations: []
---

# COG Vault Review Skill

## Purpose
Implements spaced repetition from your own vault. Finds notes last modified approximately 7, 30, and 90 days ago, generates verified review questions from their actual content, and appends them to today's daybook. Designed to run autonomously on a schedule — no user action required once set up.

## When to Invoke
- User types `/vault-review`
- Scheduled cron run (daily morning routine, before the daily brief)
- User wants to resurface and reinforce past thinking

## Loop Pattern

This skill implements the autonomous loop pattern:

```
TRIGGER   → schedule (cron) or user command
DO        → find notes at 7/30/90-day intervals, generate review questions
VERIFY    → each question references specific content from the note (not a generic prompt)
ITERATE   → if generic, regenerate with stricter requirement
STOP      → all questions pass verify, or 2 retries exhausted per note
```

The verify step is what makes this skill worth running. Without it, question generation produces generic output ("What was the main point?") that teaches nothing. The hard rule: a question must be unanswerable without having read the specific note.

## Pre-Flight

1. Run `date '+%Y-%m-%d'` to get today's date. NEVER guess the date.
2. Check whether today's daybook exists at `01-daily/daybooks/daybook-YYYY-MM-DD.md`. If it doesn't exist, create it before appending — output always goes to the daybook.

## Process Flow

### 1. Find Notes to Review

Use `find` with `-mtime` to locate files modified at each interval. On macOS, `-mtime +N` means "more than N full 24-hour periods ago":

**7-day window** (modified 6-8 days ago):
```bash
find . -path "./Readwise" -prune -o -path "./.claude" -prune -o -path "./.kiro" -prune -o -path "./.gemini" -prune -o -path "./01-daily" -prune -o -name "*.md" -mtime +5 -mtime -9 -print
```

**30-day window** (modified 27-33 days ago):
```bash
find . [same prune flags] -name "*.md" -mtime +26 -mtime -34 -print
```

**90-day window** (modified 83-97 days ago):
```bash
find . [same prune flags] -name "*.md" -mtime +82 -mtime -98 -print
```

**Always exclude from results:**
- `Readwise/` — raw source files, immutable
- `.claude/`, `.kiro/`, `.gemini/` — framework files
- `01-daily/` — ephemeral daily notes (briefs, check-ins, daybooks)
- `CLAUDE.md`, `AGENTS.md`, `ERRORS.md`, `LOOPS.md` — reference docs
- Files under 150 words — too thin to generate meaningful questions

**Limit per interval:** Up to 3 notes. If more qualify, prefer files in `05-knowledge/` and `04-projects/` over `02-personal/` and `03-professional/`. Within those, pick by most recently modified within the window.

### 2. Generate Review Questions

For each qualifying note, read its content and generate 1-2 spaced repetition questions.

**Generation prompt:**
```
Read this note:

[note content]

Generate 1-2 review questions. Each question MUST:
- Name or quote something specific from this note (a fact, claim, decision, framework, or number)
- Require having read this note to answer — not answerable from general knowledge alone
- Be concise (one sentence, phrased as a direct question)

Return as a bullet list. No preamble, no explanation.
```

**VERIFY (hard rule):** After generating each question, evaluate it:
> "Does this question contain a specific reference — a name, concept, claim, number, or decision — from the note? Or could a reasonable person answer it without having read this particular note?"

- Passes: question contains a specific content reference → keep it
- Fails: question is generic → ITERATE

**ITERATE:** On failure, re-prompt with:
```
The previous question was too generic. Rewrite it to specifically reference [the most concrete claim, fact, or decision in the note — quote it directly if possible].
```

**STOP:** Question passes verify, OR 2 retries exhausted. If retries fail, log the note as "verify failed" and skip it — do not produce a generic question.

### 3. Compile Review Digest

Build the output in this format:

```markdown
## Vault Review — YYYY-MM-DD

*Spaced repetition: notes from 7d / 30d / 90d windows*

### 7 Days Ago
- **[[note-filename|Note Title]]**
  - Q: [specific review question]
  - Q: [second question, if a second was generated]

### 30 Days Ago
- **[[note-filename|Note Title]]**
  - Q: [specific review question]

### 90 Days Ago
- **[[note-filename|Note Title]]**
  - Q: [specific review question]

---
*[X] notes reviewed · [Y] questions · Skipped: [Z] (too thin or verify failed)*
```

Omit any interval section silently if no qualifying notes were found in that window.

### 4. Append to Daybook

Always write to today's daybook at `01-daily/daybooks/daybook-YYYY-MM-DD.md`.

**If the daybook doesn't exist yet:** Create it first with this content (matching the `/daybook` skill's exact template), then append the digest:

```markdown
---
type: "daybook"
date: "YYYY-MM-DD"
created: "YYYY-MM-DD"
status: "open"
---

# Daybook — DD Month YYYY

<!-- Append thoughts here throughout the day. No structure needed. Run /braindump when back at desk. -->
```

Use the full date in the heading, e.g. `# Daybook — 17 May 2026`.

Then append the digest with a blank line before the `## Vault Review` header.

### 5. Report Completion

```
Vault review complete.

Reviewed: [X] notes (7d: [a], 30d: [b], 90d: [c])
Questions: [Y] generated
Saved to: [path]

Skipped: [Z] notes — [reason: too thin / verify failed]
```

If no notes were found in any window (vault is new, or all recent notes fall outside the windows), say so and suggest checking back in a few days.

## Model Guidance

- Question generation and verify: **Haiku is sufficient** — this is short-context generation and pattern-matching, not synthesis. Do not use Sonnet or Opus for this skill.
- The verify check does not require a separate model call. Evaluate the generated question inline against the hard rule, then decide whether to iterate.

## Scheduling

This skill is designed to run automatically every morning. To schedule it:

```
/schedule vault-review — run daily at 06:00, prompt: "Run /vault-review to surface notes for spaced repetition review and append to today's daybook"
```

The scheduled cloud agent runs on Claude's infrastructure — your Mac does not need to be open.

See `LOOPS.md` in the vault root for the full loop pattern reference and scheduling guidance for all schedulable COG skills.

## Design Notes

- The 7/30/90-day intervals match standard spaced repetition intervals (Anki-style). Notes that surface repeatedly at the 90-day mark are candidates for consolidation into `05-knowledge/`.
- iCloud sync and Obsidian's mobile app may update file modification times unpredictably. If notes are consistently missing from expected windows, inspect actual `mtime` values with `stat` or `find -mtime` directly and adjust the day ranges.
- The skill does not mark notes as "reviewed." The same note will resurface again when it next hits a window. Returning to a note repeatedly is the point.
- Answers to the review questions are never generated — only questions. The user answers them, which is where the learning happens.
