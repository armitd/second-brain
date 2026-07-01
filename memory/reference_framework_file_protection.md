---
name: "Framework vs custom skill protection"
description: "Which COG skills/files are framework-managed (immutable) vs local/custom (editable), and the two lists that govern it"
type: "reference"
---

CLAUDE.md's line "Framework files are immutable: `.claude/` ..." over-generalises. Not all of `.claude/` is immutable — protection is governed by TWO separate hand-maintained lists that must stay in sync:

1. **`cog-update.sh` allowlist** — the files `/update-cog` syncs from upstream (and would overwrite). Includes ~19 framework skills, `.claude/roles/`, `.claude/agents/`, `AGENTS.md`, and **CLAUDE.md itself**.
2. **PreToolUse hook in `.claude/settings.json`** (`custom_skills` list) — the skills exempt from edit-protection.

**Local/custom skills (NOT upstream-managed, safe to edit directly):** `daybook`, `plan-week`, `process-daybook`, `process-readwise`, `publish-to-sharepoint`, `sync-tasks`, `vault-review`. These are editable and are NOT overwritten by `/update-cog`.

**Genuinely protected (do NOT edit locally):** the ~19 framework skills, `.claude/roles/`, `.claude/agents/`, `AGENTS.md`, `Readwise/`, and `CLAUDE.md`. CLAUDE.md is both synced by `cog-update.sh` AND hook-protected, so local edits are blocked and would be a fragile deviation — put durable notes in COG memory instead.

**Gotcha fixed 2026-07-01:** the hook's `custom_skills` list had drifted — `daybook` was missing (orphaned: unmanaged yet edit-blocked) and `capture-notes` was stale (no such skill). Corrected so the hook matches the true custom-skill set. If skills are added/removed, both lists above must be updated together.
