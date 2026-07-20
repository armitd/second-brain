---
type: "index"
tags: ["#dayone", "#journal", "#import", "#staging"]
---

# Day One Import (staging)

Drop your Day One export here, then ask COG to process it.

## How to export from Day One
1. Day One → Settings → Import/Export → **Export**
2. Choose **Markdown** (or JSON for richer metadata)
3. Unzip and drop the `.md` files (and any media) into this folder

## What COG does
- Say: **"process my Day One export"**
- COG creates one entry per file in `07-journal/YYYY-MM-DD-<slug>.md`, dated by the **entry's own date** (not the import date)
- Adds frontmatter: `title`, `date`, `type: journal`, `source: "dayone"`, `tags: ["#journal", "#dayone"]` (the `#dayone` tag + `source` field both mark it as imported), plus `location`/`weather`/`created` time when the export includes them
- Dedupes against existing `07-journal/` entries so re-running a full export won't create duplicates
- Multiple entries on the same day get `-2`, `-3`, … suffixes

## Notes
- This is a **staging** folder only. The real entries live in `07-journal/` (no sub-folder).
- **Capture-only:** imported entries are never run through `/braindump`, `/process-daybook`, or `/sync-tasks`.
- Once processed, you can clear the raw export from here (or leave it — COG dedupes either way).
- Privacy: these entries land in the git-backed, synced, AI-readable vault. Export only what you're comfortable having there.
