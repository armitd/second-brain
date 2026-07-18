---
name: create-journal
description: Create a titled, capture-only journal entry in 07-journal/ — reflections and musings, never processed into actions
roles: [all]
integrations: []
---

# COG Create Journal Skill

## Purpose
Capture a musing or reflection as a titled, durable note in `07-journal/`. This is a **keep-and-reflect** layer, not a to-do layer — the entry is never run through `/braindump`, `/process-daybook`, or `/sync-tasks`, and no actions are extracted from it. Distinct from the Daybook, which is for *actionable* capture.

## When to Invoke
- User types `/create-journal` (optionally with a title and/or dictated content)
- User says "new journal entry", "journal this", "capture a musing / thought", "add to my journal"
- User dictates a reflection they want to keep with no action required

## Process Flow

### 1. Get the Date
Run `date '+%Y-%m-%d'` for the frontmatter/filename, and `date '+%e %B %Y' | sed 's/^ *//'` for the heading date (e.g. `7 July 2026`). NEVER guess the date.

### 2. Determine Title and Body
From whatever the user passed after the command:
- **Short input** (a few words) → treat it as the TITLE; the body starts empty.
- **Longer input** (a full dictated musing) → use the full text as the BODY, and generate a concise 5–8 word TITLE that captures its essence.
- **No input** → ask: *"What's this journal entry about? Give me a title, or just dictate the thought and I'll title it."*

Do **not** analyse, classify, summarise, or extract actions from the content. Capture it as-is.

### 3. Build the Filename
- Slugify the title: lowercase, spaces → hyphens, strip punctuation.
- Filename: `07-journal/YYYY-MM-DD-<slug>.md`
- If that file already exists, append `-2`, `-3`, … to keep it unique.

### 4. Write the Entry
Create the file with exactly this shape:

```markdown
---
title: "<title>"
date: "YYYY-MM-DD"
type: "journal"
tags: ["#journal"]
---

# <title>

<body>
```

- `<body>` is the dictated text. If there is no body, use the capture comment instead:
  `<!-- Just talk. No structure, no action needed — this is a keep-and-reflect note. -->`
- Optionally add ONE topical tag alongside `#journal` if the subject is obvious (e.g. `#ai`, `#ea`). Never more than two tags total.

### 5. Confirm
`Journal entry saved: 07-journal/YYYY-MM-DD-<slug>.md — kept as-is, not processed, no actions extracted.`

## Notes
- `07-journal/` is a **capture-only** layer — never process it with `/braindump` or `/process-daybook`. For actionable capture, use the Daybook (`/daybook`) instead.
- `/vault-review` may resurface old journal entries later for reflection; that is the only automated touch, and only if the user has scheduled it.
- Never create an entry for a past date unless the user explicitly asks.
- See `07-journal/README.md` for the folder convention.
