---
name: sync-tasks
description: Sync open tasks from the COG vault to Microsoft To Do via OneDrive file drop
roles: [all]
integrations: ["microsoft-to-do"]
---

# COG Sync Tasks Skill

## Purpose
Send open tasks from the COG vault to Microsoft To Do. The skill writes a JSON file to a OneDrive folder; a Power Automate flow picks it up, creates the To Do tasks in the COG list, and deletes the file. No premium PA licence required.

## When to Invoke
- User types `/sync-tasks` — batch sync all `#planner` tagged tasks
- User types `/sync-tasks pick` — interactive picker from recent vault files
- User says "sync tasks to To Do", "send tasks to O365", "push tasks to Planner"

## Tagging Convention

Mark any task for sync by adding `#planner` to the task line:

```
- [ ] Request Microsoft Agent 365 demo 📅 2026-06-20 #planner
- [ ] Review MCP governance framework draft 📅 2026-06-18 #planner
```

Tasks without `#planner` are never touched. Successfully synced tasks are marked `#synced` to prevent re-sending.

## Drop Folder

All task files are written to:
```
~/Library/CloudStorage/OneDrive-BelronGlobal/COG-Tasks/
```

File naming: `cog-tasks-YYYY-MM-DD-HHMM.json`

Power Automate watches this folder and processes files as they arrive.

---

## Pre-Flight Check

Run `date '+%Y-%m-%d %H:%M'` to get the current timestamp.

Confirm the drop folder exists:
```bash
ls ~/Library/CloudStorage/OneDrive-BelronGlobal/COG-Tasks/
```

If it doesn't exist, create it:
```bash
mkdir -p ~/Library/CloudStorage/OneDrive-BelronGlobal/COG-Tasks/
```

---

## Mode 1: Batch Sync (default — `/sync-tasks`)

### Step 1: Scan for Tagged Tasks

Search the vault for all files containing `#planner`:

```bash
grep -rl "#planner" \
  "/Users/darrenarmitage/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/01-daily" \
  "/Users/darrenarmitage/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/02-personal" \
  "/Users/darrenarmitage/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/03-professional" \
  "/Users/darrenarmitage/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/04-projects" \
  "/Users/darrenarmitage/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/00-inbox" \
  2>/dev/null
```

For each matching file, read it and extract lines matching the pattern:
```
- [ ] <task text> [📅 YYYY-MM-DD] #planner
```

Per task, extract:
- **title**: task text only — strip `- [ ]`, the `📅 YYYY-MM-DD` date token, and the `#planner` tag. Trim whitespace.
- **due_date**: the `📅` date if present (`YYYY-MM-DD`), otherwise omit the field
- **source_file**: relative vault path (for notes)
- **bucket**: from bucket routing rules below

If no `#planner` tasks found:
```
No tasks tagged #planner found in the vault.

Tag any task to mark it for sync:
  - [ ] Your task 📅 2026-06-20 #planner
```
Stop.

### Step 2: Show Summary and Confirm

```
Found N task(s) to sync to Planner:

  1. [Inbox] Request Microsoft Agent 365 demo — due 2026-06-20
     Source: 01-daily/briefs/daily-brief-2026-06-14.md

  2. [MCP Governance] Review framework draft — due 2026-06-18
     Source: 04-projects/mcp-governance/...

Send to Planner? (yes/no)
```

Wait for confirmation.

### Step 3: Write JSON Drop File

Write the following JSON to `~/Library/CloudStorage/OneDrive-BelronGlobal/COG-Tasks/cog-tasks-YYYY-MM-DD-HHMM.json`:

```json
{
  "sent_at": "2026-06-14T14:30:00",
  "tasks": [
    {
      "title": "Request Microsoft Agent 365 demo",
      "due_date": "2026-06-20",
      "bucket": "Inbox",
      "notes": "Source: 01-daily/briefs/daily-brief-2026-06-14.md"
    },
    {
      "title": "Review MCP governance framework draft",
      "due_date": "2026-06-18",
      "bucket": "MCP Governance",
      "notes": "Source: 04-projects/mcp-governance/..."
    }
  ]
}
```

Use `sent_at` with the timestamp from the `date` command.

Verify the file was written:
```bash
ls -la ~/Library/CloudStorage/OneDrive-BelronGlobal/COG-Tasks/
```

### Step 4: Mark Tasks as Synced

For each successfully written task, edit the source file and replace `#planner` with `#synced` on that task line:

```
BEFORE: - [ ] Request Microsoft Agent 365 demo 📅 2026-06-20 #planner
AFTER:  - [ ] Request Microsoft Agent 365 demo 📅 2026-06-20 #synced
```

### Step 5: Confirm

```
✅ N task(s) written to OneDrive — Power Automate will create them in your COG To Do list shortly.

  → [Inbox] Request Microsoft Agent 365 demo — due 2026-06-20
  → [MCP Governance] Review framework draft — due 2026-06-18

Tasks marked #synced in source files. Check To Do (COG list) in ~1–2 minutes.
```

---

## Mode 2: Interactive Pick (`/sync-tasks pick`)

### Step 1: Scan Recent Files

Find all vault markdown files modified in the last 14 days:

```bash
find \
  "/Users/darrenarmitage/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/01-daily" \
  "/Users/darrenarmitage/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/02-personal" \
  "/Users/darrenarmitage/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/03-professional" \
  "/Users/darrenarmitage/Library/Mobile Documents/iCloud~md~obsidian/Documents/Second Brain/04-projects" \
  -name "*.md" -mtime -14 -not -path "*/.git/*" \
  2>/dev/null
```

Read each file and extract all open tasks (`- [ ]` lines). Exclude any already marked `#synced`.

### Step 2: Present Numbered List

```
Open tasks from the last 14 days — pick which to send to Planner.

  1. [Inbox] Request Microsoft Agent 365 demo — due 2026-06-20
     daily-brief-2026-06-14.md

  2. [MCP Governance] Add Composio to vendor landscape — due 2026-06-14
     braindump-2026-06-13-1517-composio.md

  3. [AI Damage Assessment] Run benchmark once Gemini 3.5 Pro hits GA — due 2026-06-21
     daily-brief-2026-06-14.md

Enter task numbers to send (e.g. 1,3 or all), or cancel:
```

### Step 3: Process Selection

- `1,3` → send tasks 1 and 3
- `all` → send all listed tasks
- `cancel` → abort

For picked tasks, determine bucket from routing rules. If source file path is ambiguous, ask: *"Which bucket? Inbox / AI Damage Assessment / MCP Governance / Contact Centre / Personal"*

### Step 4: Write, Confirm

Same as Mode 1 Steps 3–5. In pick mode, do **not** mark source files `#synced` — the user didn't tag them and may want to pick them again later.

---

## Bucket Routing Rules

| File path contains | Planner bucket |
|---|---|
| `04-projects/ai-damage-assessment` | `AI Damage Assessment` |
| `04-projects/mcp-governance` | `MCP Governance` |
| `04-projects/contact-centre` | `Contact Centre` |
| `02-personal/` | `Personal` |
| `04-projects/60th-birthday` | `Personal` |
| `04-projects/getting-fit` | `Personal` |
| `04-projects/garden` | `Personal` |
| `04-projects/home-automation` | `Personal` |
| `04-projects/alps` | `Personal` |
| `04-projects/nordics` | `Personal` |
| Anything else | `Inbox` |

---

## JSON Schema (for PA flow reference)

```json
{
  "type": "object",
  "properties": {
    "sent_at": { "type": "string" },
    "tasks": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "title":    { "type": "string" },
          "due_date": { "type": "string", "description": "YYYY-MM-DD" },
          "bucket":   { "type": "string" },
          "notes":    { "type": "string" }
        },
        "required": ["title", "bucket"]
      }
    }
  }
}
```

---

## Error Handling

| Situation | Response |
|---|---|
| Drop folder missing | Create it with `mkdir -p`, then proceed |
| No `#planner` tasks found | Stop, show tagging instructions |
| File write fails | Report error, do not modify source files |
| Old files still in COG-Tasks folder | Warn: "N file(s) already in drop folder — PA may not have processed them yet. Check Planner before syncing again." |

---

## Notes

- PA typically processes the file within 1–2 minutes of it appearing in OneDrive.
- The `#synced` tag prevents double-sending. Do not remove it unless you want the task re-sent.
- Completed tasks (`- [x]`) are never included, even if tagged `#planner`.
- The skill does not update or delete tasks already in To Do — one-way, create only.
- Tasks land in your **COG** list in To Do. Promote to your Project plan via My Tasks in Planner if needed.
- See `05-knowledge/integrations/sync-tasks-pa-flow.md` for the PA flow setup guide.
