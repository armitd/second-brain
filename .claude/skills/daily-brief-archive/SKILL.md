---
name: daily-brief-archive
description: Archive older daily briefs into a subfolder, keeping only the 3 most recent in the main briefs folder
roles: [all]
---

# COG Daily Brief Archive Skill

## Purpose
Keep `01-daily/briefs/` tidy by moving older `daily-brief-*.md` files into `01-daily/briefs/archive/`, retaining only the 3 most recent in the main folder. Run manually whenever you want to tidy up — not triggered automatically by `daily-brief`.

## When to Invoke
- User types `/daily-brief-archive`
- User says "archive old briefs", "tidy up daily briefs", "clean up the briefs folder"

## Why only the 3 most recent stay in the main folder
The `daily-brief` skill's dedup step reads "3 most recent briefs from `01-daily/briefs/`" to avoid repeating stories. Keeping exactly those 3 in the main folder means `daily-brief` keeps working unchanged — no need to teach it to scan the archive folder too.

## Process Flow

### 1. List Candidate Files
In `01-daily/briefs/`, list files matching `daily-brief-*.md` (ignore other files like `comprehensive-analysis-*.md` — they are out of scope).

### 2. Determine What Stays
Sort matching files by the date in the filename (`YYYY-MM-DD`), most recent last. The 3 most recent stay in `01-daily/briefs/`. Everything else is a candidate for archiving.

### 3. Archive
Create `01-daily/briefs/archive/` if it doesn't exist. Move each older file there, preserving the filename.

### 4. Confirm Completion
Report:
- How many files were archived
- Which 3 files remain in the main folder
- Confirm no non-daily-brief files were touched

## Notes
- This skill only touches `01-daily/briefs/`. It does not modify `daily-brief` or any other skill.
- Safe to run repeatedly — if fewer than 3 daily briefs exist, or nothing needs archiving, just report that and do nothing.
- Never delete files — always move them into `archive/`.
