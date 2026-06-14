---
name: sync-tasks
description: Sync open tasks from the COG vault to Microsoft Planner via Power Automate webhook
roles: [all]
integrations: ["microsoft-365-planner"]
---

# COG Sync Tasks Skill

## Purpose
Send open tasks from the COG vault to Microsoft Planner via a Power Automate webhook. Two modes: batch sync all tasks tagged `#planner`, or interactively pick individual tasks to send.

## When to Invoke
- User types `/sync-tasks` — batch sync all `#planner` tagged tasks
- User types `/sync-tasks pick` — interactive picker from recent vault files
- User says "sync tasks to Planner", "send tasks to O365", "push tasks"

## Tagging Convention

Tasks are marked for sync by adding `#planner` to the task line:

```
- [ ] Request Microsoft Agent 365 demo 📅 2026-06-20 #planner
- [ ] Review MCP governance framework draft 📅 2026-06-18 #planner
```

Tasks without `#planner` are never touched by this skill. Tasks already synced are marked `#synced` by the skill after a successful push.

## Pre-Flight Check

### 1. Get Webhook URL

Read `00-inbox/MY-INTEGRATIONS.md` and find the `planner-webhook-url` under the Microsoft 365 / Power Automate section.

If not found:
```
No Planner webhook URL configured.

Add the following to the Microsoft 365 section of 00-inbox/MY-INTEGRATIONS.md:

**Microsoft 365 — Planner Sync**
- planner-webhook-url: https://prod-xx.westeurope.logic.azure.com/...

See 05-knowledge/integrations/sync-tasks-pa-flow.md for setup instructions.
```
Stop.

### 2. Get Current Date

Run `date '+%Y-%m-%d'` to get today's date for reporting.

---

## Mode 1: Batch Sync (default — `/sync-tasks`)

### Step 1: Scan the Vault for Tagged Tasks

Use Bash to find all files containing `#planner`:

```bash
grep -rl "#planner" \
  "/path/to/vault/01-daily" \
  "/path/to/vault/02-personal" \
  "/path/to/vault/03-professional" \
  "/path/to/vault/04-projects" \
  "/path/to/vault/00-inbox" \
  2>/dev/null
```

For each file found, read it and extract lines matching:
```
- [ ] <task text> [optional 📅 YYYY-MM-DD] #planner
```

Extract per task:
- **title**: the task text (strip the `- [ ]` prefix, the `📅 YYYY-MM-DD` date, and the `#planner` tag)
- **due_date**: the `📅` date if present, otherwise null
- **source_file**: the file path
- **bucket**: determined by bucket routing rules (see below)

If no `#planner` tasks found:
```
No tasks tagged #planner found in the vault.

To mark a task for sync, add #planner to any task line:
  - [ ] Your task 📅 2026-06-20 #planner
```
Stop.

### Step 2: Show Summary Before Sending

Display the tasks about to be synced:

```
Found N tasks to sync to Planner:

  1. [Inbox] Request Microsoft Agent 365 demo — due 2026-06-20
     Source: 01-daily/briefs/daily-brief-2026-06-14.md

  2. [MCP Governance] Review framework draft — due 2026-06-18
     Source: 04-projects/mcp-governance/planning/...

Send these N tasks to Planner? (yes/no)
```

Wait for confirmation before proceeding.

### Step 3: POST to Power Automate Webhook

Send a single HTTP POST to the webhook URL with this JSON payload:

```json
{
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
      "notes": "Source: 04-projects/mcp-governance/planning/..."
    }
  ]
}
```

Use Bash with curl:
```bash
curl -s -o /tmp/pa_response.json -w "%{http_code}" \
  -X POST \
  -H "Content-Type: application/json" \
  -d '<JSON payload>' \
  '<webhook URL>'
```

### Step 4: Handle Response

- **HTTP 200 or 202:** Success → proceed to Step 5
- **HTTP 400:** Bad request — report the response body, do not mark tasks as synced
- **HTTP 4xx/5xx or curl failure:** Report the error, do not mark tasks as synced

### Step 5: Mark Tasks as Synced

For each successfully synced task, edit the source file to replace `#planner` with `#synced` on that task line:

```
BEFORE: - [ ] Request Microsoft Agent 365 demo 📅 2026-06-20 #planner
AFTER:  - [ ] Request Microsoft Agent 365 demo 📅 2026-06-20 #synced
```

This prevents the task from being re-sent on the next sync run.

### Step 6: Confirm Completion

```
✅ N tasks synced to Planner.

  → [Inbox] Request Microsoft Agent 365 demo — due 2026-06-20
  → [MCP Governance] Review framework draft — due 2026-06-18

Tasks marked #synced in source files.
```

---

## Mode 2: Interactive Pick (`/sync-tasks pick`)

### Step 1: Scan Recent Files for Open Tasks

Find all vault files modified in the last 14 days:

```bash
find "/path/to/vault/01-daily" \
     "/path/to/vault/02-personal" \
     "/path/to/vault/03-professional" \
     "/path/to/vault/04-projects" \
     -name "*.md" -newer "/path/to/vault/.claude/settings.json" \
     -not -path "*/.git/*" \
     2>/dev/null | head -50
```

Actually use `find ... -mtime -14` to get files modified in last 14 days.

Read each file and extract ALL open tasks (`- [ ]` lines), regardless of `#planner` tag. Exclude tasks already marked `#synced`.

### Step 2: Present Numbered List

```
Open tasks from the last 14 days — pick which to send to Planner.

  1. [Inbox] Request Microsoft Agent 365 demo — due 2026-06-20
     daily-brief-2026-06-14.md

  2. [MCP Governance] Add Composio to vendor landscape — due 2026-06-14
     mcp-governance/braindumps/braindump-2026-06-13...md

  3. [AI Damage Assessment] Run benchmark test once Gemini 3.5 Pro hits GA — due 2026-06-21
     daily-brief-2026-06-14.md

  4. [Inbox] Update AI advocacy talking points re: export controls — due 2026-06-16
     daily-brief-2026-06-14.md

Enter task numbers to send (e.g. 1,3 or all), or 'cancel':
```

### Step 3: Process Selection

Wait for user response:
- `1,3` → send tasks 1 and 3
- `all` → send all listed tasks
- `cancel` or `none` → abort

For each selected task, determine bucket using routing rules (below). If the bucket is ambiguous (e.g. a mixed file), ask: "Which bucket for '[task title]'? (Inbox / AI Damage Assessment / MCP Governance / Contact Centre / Personal)"

### Step 4: POST and Confirm

Same as Mode 1 Steps 3–6 above. In pick mode, do **not** modify the source files (the user didn't tag them, so don't mark them `#synced` unless they explicitly added `#planner` — just send them).

---

## Bucket Routing Rules

Determine the target Planner bucket from the source file path:

| File path contains | Bucket |
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

## JSON Payload Schema

The webhook expects this exact structure:

```json
{
  "tasks": [
    {
      "title": "string — task text, clean (no markdown, no emoji dates, no tags)",
      "due_date": "string — YYYY-MM-DD, or omit if no due date",
      "bucket": "string — one of: Inbox, AI Damage Assessment, MCP Governance, Contact Centre, Personal",
      "notes": "string — source file path for traceability"
    }
  ]
}
```

`title` is required. All other fields are optional but should be included when available.

---

## Error Handling

| Situation | Response |
|---|---|
| Webhook URL not configured | Stop, show setup instructions |
| No `#planner` tasks found (batch mode) | Stop, show tagging instructions |
| curl fails (network) | Report error, do not modify source files |
| PA returns 4xx/5xx | Report error body, do not modify source files |
| PA returns 200/202 but no body | Treat as success |
| Source file not writable | Report which files couldn't be updated, but count the sync as successful |

---

## Notes

- The `#synced` tag prevents double-sending. Do not remove it manually unless you want the task re-sent.
- Completed tasks (`- [x]`) are never synced, even if they have `#planner`.
- The skill does not update or delete tasks already in Planner — it only creates new ones.
- Task completion in Planner does not flow back to the vault (one-way sync only).
- See `05-knowledge/integrations/sync-tasks-pa-flow.md` for the Power Automate flow setup guide.
