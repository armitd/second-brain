---
name: process-dayone
description: Process a Day One journal export (JSON) into 07-journal/ as date-stamped, capture-only notes — with photos, tags, location and weather, deduped by entry UUID
roles: [all]
integrations: [Day One]
---

# COG Process Day One Skill

## Purpose
Bring Day One journal entries into COG's journal layer. Day One has no live read API, so this is an **export-and-drop** workflow: the user exports from Day One, drops the export into a staging folder, and this skill files each entry into `07-journal/` as a titled, date-stamped note. Entries are **capture-only** — they are never run through `/braindump`, `/process-daybook`, or `/sync-tasks`, and no actions are extracted. This is the Day One counterpart to `/create-journal`.

## When to Invoke
- User types `/process-dayone`
- User says "process my Day One export", "import Day One", "sync my Day One journal", "bring in my Day One entries"

## Pre-Flight Check

1. **Integration check:** confirm **Day One** is Active in `00-inbox/MY-INTEGRATIONS.md`. If it is Disabled, skip silently. If not listed, it is unknown — ask before proceeding.
2. **Get the current timestamp** with `date '+%Y-%m-%d %H:%M'` (for any processing notes; entry dates always come from the export, never "now").
3. **Locate the export** in the drop folder `00-inbox/raw/dayone-import/`:
   - Preferred: one or more **`Journal.json`** files plus a **`photos/`** folder (and possibly `videos/`, `audios/`, `pdfs/`).
   - A raw `.zip` may be present — unzip it in place first.
   - Fallback: a plain-text/Markdown **`Journal.txt`** (see Fallback section — photos cannot be mapped reliably).
   - If the folder holds only its `README.md`, tell the user how to export (JSON) and drop it, then stop.

## Export Instructions (to give the user if the folder is empty)
Day One → Settings → Import/Export → Export → **JSON** (preferred — maps photos to entries and carries tags/location/weather). Unzip and drop the whole export (`Journal.json` + `photos/`) into `00-inbox/raw/dayone-import/`, then re-run.

## Process Flow (JSON)

Parse `Journal.json`. It has an `entries` array; process each entry independently.

### 1. Dedup Gate (per entry)
- Each entry has a `uuid`. Before writing, check whether any file in `07-journal/` already has `dayone_uuid: "<uuid>"` in frontmatter. If so, **skip** (already imported) — this makes re-running a full export safe.
- Secondary check: same `date` + same title already present → skip.

### 2. Derive Fields
- **Date/time:** convert `creationDate` (UTC, ISO 8601) to local time using the entry's `timeZone` (e.g. `Europe/London`). `date` = local `YYYY-MM-DD`; `created` = local `YYYY-MM-DD HH:MM`.
- **Title:** if the entry `text` starts with a Markdown `# Heading`, use that as the title. Otherwise generate a concise 5–8 word title from the first line/sentence (as `/create-journal` does). Slugify: lowercase, spaces → hyphens, strip punctuation.
- **Body:** the entry `text`, **unescaped** — Day One escapes Markdown specials, so replace `\.`→`.`, `\-`→`-`, `\#`→`#`, `\*`→`*`, `\_`→`_`, etc. Preserve the body verbatim otherwise (capture-only).
- **Tags:** `["#journal", "#dayone"]` plus any Day One `tags` (prefixed with `#`, slugified).
- **Location:** compose from `location.placeName`, `localityName`, `administrativeArea`, `country` (omit missing parts).
- **Weather:** `round(temperatureCelsius)°C` + `conditionsDescription` (e.g. `18°C Cloudy`), when present.

### 3. Photos (and other media)
- For each item in the entry's `photos` array: the file lives at `00-inbox/raw/dayone-import/photos/<md5>.<type>`.
- Copy it into `07-journal/attachments/`, renamed to match the entry: `YYYY-MM-DD-<slug>.<ext>` (append `-2`, `-3`, … for multiple photos, ordered by `orderInEntry`).
- In the body, the photo is referenced by a marker `![](dayone-moment://<IDENTIFIER>)`. Replace each marker (matching `photos[].identifier`) with an Obsidian embed `![[YYYY-MM-DD-<slug>[-N].<ext>]]`, **keeping the photo in its original position** in the text.
- If a photo has no inline marker, append the embed at the end of the body.
- Record the copied paths in a `photos:` frontmatter array.
- Handle `videos`/`audios`/`pdfs` the same way if present (copy to `attachments/`, embed/link). Note any media types skipped.

### 4. Filename & Collisions
- `07-journal/YYYY-MM-DD-<slug>.md`. If it already exists (and is a *different* entry by uuid), append `-2`, `-3`, ….

### 5. Write the Entry

```markdown
---
title: "<title>"
date: "YYYY-MM-DD"
created: "YYYY-MM-DD HH:MM"
type: "journal"
source: "dayone"
dayone_uuid: "<entry uuid>"
location: "<place, locality, area, country>"   # omit if absent
weather: "<NN°C Conditions>"                    # omit if absent
photos: ["attachments/<file>", ...]             # omit if none
tags: ["#journal", "#dayone", <any day one tags>]
---

# <title>

<unescaped body, with photo markers replaced by ![[…]] embeds in place>
```

## Fallback: Plain-Text / Markdown Export
If only `Journal.txt` (or per-journal `.md`) is present:
- Entries are concatenated under `Date:` headers. Split on those headers; parse `Date:`, `Weather:`, `Location:` lines; the remainder is the body.
- Create entries the same way, but **photos cannot be reliably mapped** to entries in this format — note which photos went unlinked and recommend a JSON re-export if photos matter.
- No `dayone_uuid` is available; dedup on `date` + title only.

## Cleanup
After a successful run, report what was filed and **offer to clear the staging leftovers** (`Journal.json`, `photos/`, `.DS_Store`, `Journal.txt`) from `00-inbox/raw/dayone-import/`, keeping its `README.md`. Never delete without confirming.

## Report Completion
```
Day One import complete.
Filed: [X] entries → 07-journal/ ([Y] with photos → 07-journal/attachments/)
Skipped: [Z] already imported (dedup by uuid)
[list new entries with dates + titles]
```

## Loop Engineering
This is a **parse-dedup-file loop with a per-entry gate**. Each entry is an independent iteration: dedup gate → derive fields → copy/embed media → write. One malformed entry must not stall the rest — skip it, note it, continue. The deterministic verifier: every written entry has a valid `date`, a `dayone_uuid` (JSON path), and any referenced `![[…]]` embed points at a file that now exists in `07-journal/attachments/`. Termination: all entries in the export processed. See `.claude/skills/loop-engineering/SKILL.md`.

## Design Principles
- **Capture-only.** Imported entries live in `07-journal/`, outside the action pipeline. Never extract tasks, never process into braindumps.
- **Entry's own date, never the import date.** Sorting and history depend on this.
- **Idempotent.** `dayone_uuid` dedup means re-importing a full export is safe.
- **Faithful.** Preserve body text verbatim (only unescaping Day One's Markdown escaping); keep photos in their original positions.
- **Privacy.** Entries and photos land in the git-backed, synced, AI-readable vault. If the user seems unaware, remind them to export only what they're comfortable storing there.
- **Never modify the raw export** until the user confirms cleanup.

## YAML Formatting Requirements
- All string values double-quoted; arrays as quoted strings (`["#journal", "#dayone"]`); URLs/paths quoted. Booleans unquoted. Ensure valid YAML so Obsidian parses the frontmatter.

## Related
- `/create-journal` — the manual counterpart (dictate a musing straight in)
- `07-journal/README.md` — journal layer convention
- `00-inbox/raw/dayone-import/README.md` — the drop-folder instructions
- `00-inbox/MY-INTEGRATIONS.md` — Day One integration entry
