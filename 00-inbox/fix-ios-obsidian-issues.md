---
type: "task-note"
created: "2026-07-24"
tags: ["#task", "#obsidian", "#tooling", "#vault-maintenance"]
status: "open"
---

# Fix iOS Obsidian issues

- [ ] Resolve the iOS Obsidian pain: constant reload/refresh on open, and lost edits / sync conflicts

**Why:** Obsidian on iOS is painful for quick updates. Diagnosed 2026-07-24.

## Root causes (from diagnosis)
- **iCloud eviction + big vault:** iOS offloads files and re-downloads on open. Vault is ~3,233 markdown files (2,207 of them Readwise) → heavy cold-start every time iOS kills the app.
- **17 community plugins**, several heavy: Dataview and Tasks re-index all notes on launch; obsidian-git runs `refreshSourceControl` every ~7s scanning a ~21,000-file repo; plus 5 overlapping canvas/mind-map plugins.
- **Multiple sync engines fighting:** iCloud + obsidian-git (mobile) + the Mac's git backup on the same vault → conflicts (evidence: `05-knowledge/archive/icloud-conflicts-2026-07-18/`). This is the "lost all the time" symptom.

## Fix checklist (easiest first)
- [x] Quick-capture Apple Shortcut built to bypass Obsidian for adding to the lists (Reading/Listen/Watch/Places) — done 2026-07-24
- [ ] Trim the mobile plugin load: disable **obsidian-git on mobile** (redundant — iCloud syncs the phone, the Mac handles the git backup); remove genuinely-unused canvas/mind-map plugins. *Caveat: `.obsidian` config syncs across devices, so only remove what you don't use anywhere.*
- [ ] **Fix the sync fight (biggest lever):** evaluate moving to **Obsidian Sync** (~£4/mo) as the single sync engine, put the iOS vault in the app's **local** (non-iCloud) storage, and drop obsidian-git from mobile. Eliminates both the eviction-reload and the conflicts; also allows per-device plugin sets so mobile can run lean.
- [ ] Later/optional: split **Readwise** (2,207 files) into a separate vault or exclude it from mobile sync to roughly halve the mobile index.

## Notes
- No obvious project home — parked here in the inbox. Move/promote if it grows (could become a small "setup project" like Journalling Setup).
- Undated: add a due date when ready to tackle it.
