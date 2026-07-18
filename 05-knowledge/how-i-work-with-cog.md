---
type: "knowledge"
created: "2026-06-14 12:49"
tags: ["#cog", "#workflow", "#reference"]
---

# How I Work With COG

A personal reference for my day-to-day COG workflows. Not a technical spec — just what I actually do.

---

## Daily Rhythm

### Morning
1. Start a fresh Claude Code session
2. Run `/daily-brief` — COG searches for verified news across my interests and saves to `01-daily/briefs/`
3. Read the brief, capture reactions with `/braindump` if something sparks a thought

> **Do not use a scheduled cloud agent for daily-brief.** Cloud agents run remotely without vault access. Always run it manually in session.

### During the Day
- Capture on the move → **daybook** (see below)
- Thoughts triggered by meetings, reading, conversations → `/braindump`
- Articles and content → save to **Readwise** via the app/extension

### End of Day / When Needed
- Process daybook → `/process-daybook`
- Sync tasks to To Do → `/sync-tasks`

---

## Capturing Content

### On the Move — Daybook
When I'm away from my desk and want to capture thoughts quickly:
1. Write into today's daybook file (`01-daily/daybooks/daybook-YYYY-MM-DD.md`) — freeform, no structure needed
2. Later, run `/process-daybook` — COG reads it, classifies it, runs the full braindump pipeline, and saves a structured braindump to the right vault location
3. The daybook entry gets marked `status: processed` with a link to the braindump

### Articles, Tweets, Books — Readwise
**Readwise is the primary content layer.** Everything external should go through Readwise first.

- Save articles/tweets/PDFs via the Readwise app or browser extension
- COG reads directly from `Readwise/` in the vault — no need to paste or re-upload
- When I reference something in a session, COG checks `Readwise/` before asking me to re-share it

> `Readwise/` is read-only. Never delete, rename, or modify files there.

### Confidential/Internal Docs — Raw Inbox
For documents that can't go through Readwise (Belron-internal, confidential):
- Drop into `00-inbox/raw/`
- Reference in a session and COG will process on demand

### URLs and Web Content
- `/braindump look at https://...` — COG fetches, analyses, and saves a braindump
- Suggest saving to Readwise for future reference

### Direct Thoughts
- `/braindump` — stream of consciousness, voice-to-text, rough notes — anything goes
- COG classifies, structures, and files it automatically

---

## Task Management

### Tagging Tasks for Sync
Add `#planner` to any Obsidian task to mark it for sync:

```
- [ ] Update AI advocacy talking points 📅 2026-06-16 #planner
```

### Syncing to Microsoft To Do
- `/sync-tasks` — scans vault for all `#planner` tasks, shows a summary, confirms, writes to OneDrive, marks tasks `#synced`
- `/sync-tasks pick` — browse tasks from files modified in the last 14 days and select individual ones to send (no `#synced` marking)
- Tasks appear in my **COG** list in To Do within ~2 minutes
- Power Automate watches `~/Library/CloudStorage/OneDrive-BelronGlobal/COG-Tasks/` and processes the file automatically

### From To Do to Project Plan
Tasks land in the COG list in To Do. For anything needing project tracking (timeline, milestones), promote it to my Project plan from **My Tasks** in the new Planner — everything aggregates there.

### Tag Lifecycle
```
#planner → (after /sync-tasks) → #synced
```
`#synced` prevents double-sending. Don't remove it unless re-sending is intentional.

---

## Working the Captures — Two Loops

Capture is the easy half. These are the two loops I consciously run *after* capturing. Nothing here is automated — I choose when to run each step.

### Execute Loop — capture → done
1. `/process-daybook` (or `/braindump`) — turn raw capture into a structured braindump
2. **Pull the actions** — ask COG to extract the action items; I approve which become tasks, tagged `#planner` in `00-inbox/TASKS.md`. *This is the bridge from insight to action — the step that was always missing.*
3. `/sync-tasks` — push the `#planner` tasks to my To Do "COG" list
4. `/plan-week` — when I want the week laid out across days

### Review Loop — capture → revisited
Stops captured knowledge rotting. Run when I feel like reviewing, not on a timer.
- `/vault-review` — resurfaces notes from ~7 / 30 / 90 days ago with real questions (each unanswerable without having read the note); appends to today's daybook
- `/knowledge-consolidation` — folds scattered braindumps and insights into frameworks in `05-knowledge/`

---

## Model Selection

| Task | Model |
|---|---|
| Daily briefs, filing braindumps, adding tasks, small edits | **Sonnet** (default) |
| Auto-research, weekly check-ins, position papers, architecture decisions, anything requiring synthesis across multiple sources | **Opus** |

Switch with `/model` or from the session menu.

---

## Session Hygiene

- **Use `/compact`** when a session has covered multiple distinct topics — context quality drops as sessions fill up
- **Start a new session** before substantive analytical work — don't continue a long operational session into complex synthesis
- **Use Plan Mode (Shift+Tab)** before complex skill runs (auto-research, weekly check-ins, multi-step vault writes) — think before acting
- **One scope per session** — COG only modifies files explicitly requested; related files get mentioned, not touched

---

## Key Skill Reference

| Skill | What it does |
|---|---|
| `/daily-brief` | Finds and saves verified news across my interests |
| `/braindump` | Captures and structures raw thoughts, URLs, or content |
| `/process-daybook` | Converts today's daybook into a structured braindump |
| `/process-readwise` | Processes content from the Readwise vault |
| `/sync-tasks` | Syncs `#planner` tasks to Microsoft To Do via OneDrive |
| `/sync-tasks pick` | Interactive task picker for one-off sends |
| `/weekly-checkin` | Weekly reflection and pattern review |
| `/plan-week` | Plans the week ahead from projects and tasks |
| `/vault-review` | Resurfaces 7/30/90-day-old notes with spaced-repetition review questions |
| `/knowledge-consolidation` | Folds scattered braindumps into frameworks |

---

## File Locations

| Content | Location |
|---|---|
| Daily briefs | `01-daily/briefs/daily-brief-YYYY-MM-DD.md` |
| Daybooks | `01-daily/daybooks/daybook-YYYY-MM-DD.md` |
| Personal braindumps | `02-personal/braindumps/` |
| Professional braindumps | `03-professional/braindumps/` |
| Project braindumps | `04-projects/[project]/braindumps/` |
| Consolidated insights | `05-knowledge/` |
| Raw sources (confidential) | `00-inbox/raw/` |
| Readwise content | `Readwise/` (read-only) |

---

## Rules I Don't Break

- **Never run daily-brief as a scheduled cloud agent** — it won't write to the vault
- **Never modify `Readwise/`** — it's a read-only raw source layer
- **Never modify `.claude/`, `.kiro/`, `.gemini/`, `CLAUDE.md`, `AGENTS.md`** — framework files, updated only via `/update-cog`
- **Confirm before rewriting** — adding a section to a braindump is fine; restructuring requires explicit instruction

---

*Last updated: 2026-07-18*
