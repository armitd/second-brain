---
type: "index"
tags: ["#dayone", "#journal", "#import", "#staging"]
---

# Day One Import (staging)

Drop your Day One export here, then ask COG to process it.

## How to export from Day One (use JSON)
1. Day One → Settings → Import/Export → **Export**
2. Choose **JSON** (preferred). JSON maps each photo to its entry and carries tags, location, weather, and accurate timestamps. Markdown/plain-text is a fallback for text-only entries and cannot reliably map photos.
3. Unzip and drop the whole export into this folder — you should have a **`Journal.json`** (or several, one per journal) plus a **`photos/`** folder (and possibly `videos/`, `audios/`, `pdfs/`).

## What COG does
Say: **"process my Day One export"**. COG then, per entry in `Journal.json`:
- Creates `07-journal/YYYY-MM-DD-<slug>.md`, dated by the entry's **own `creationDate`** (converted to local time), title auto-generated from the text
- Frontmatter: `title`, `date`, `created` (entry time), `type: journal`, `source: "dayone"`, `tags: ["#journal", "#dayone", …any Day One tags]`, plus `location` / `weather` / `photos` when present
- Copies attached photos into **`07-journal/attachments/`**, renamed to match the entry (`YYYY-MM-DD-<slug>[-N].<ext>`), and embeds them with `![[…]]`. Photos are matched via the entry's `photos[].identifier` / `md5` (the export's `photos/<md5>.<type>` files)
- Body preserved verbatim (capture-only); the `dayone-moment://` photo markers in the text are replaced with the proper embeds
- Dedupes against existing `07-journal/` entries (by entry uuid / date+title) so re-running a full export won't duplicate. Same-day entries get `-2`, `-3`, … suffixes

## Notes
- This is a **staging** folder only. Entries live in `07-journal/` (no sub-folder); media lives in `07-journal/attachments/`.
- **Capture-only:** imported entries are never run through `/braindump`, `/process-daybook`, or `/sync-tasks`.
- Once processed, you can clear the raw export from here (or leave it — COG dedupes either way).
- Privacy: entries and photos land in the git-backed, synced, AI-readable vault. Export only what you're comfortable having there.
