---
type: "knowledge"
created: "2026-06-14 12:49"
tags: ["#cog", "#setup", "#reference", "#architecture"]
---

# COG — Setup Overview

A summary of how the COG second brain system is built, intended for anyone needing to understand, replicate, or extend it.

---

## What Is COG?

COG is a personal second brain built on **Claude Code** (Anthropic's CLI AI agent) running inside an **Obsidian vault** stored in iCloud. It uses a skills system to perform structured workflows — daily briefs, braindumps, task sync, research — all operating directly on local markdown files.

The key design principle: **everything lives in the vault as plain markdown**. No proprietary database, no cloud lock-in beyond iCloud sync. Claude Code reads and writes files; Obsidian renders them.

---

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                  iCloud Vault                        │
│   (Obsidian + Claude Code operate on same files)    │
│                                                      │
│  .claude/skills/     ← skill definitions            │
│  .claude/settings.json ← hooks + protection rules   │
│  00-inbox/           ← profile, integrations        │
│  01-daily/           ← briefs, daybooks             │
│  02-personal/        ← personal braindumps          │
│  03-professional/    ← professional braindumps      │
│  04-projects/        ← per-project tracking         │
│  05-knowledge/       ← consolidated insights        │
│  Readwise/           ← raw content (read-only)      │
└─────────────────────────────────────────────────────┘
         │                          │
    Claude Code                 Obsidian
  (AI agent, CLI)           (Markdown editor)
         │
    ┌────┴────────────────────────────┐
    │  External integrations          │
    │  - Readwise (content layer)     │
    │  - OneDrive → PA → To Do        │
    │  - Git (auto-commit on Stop)    │
    └─────────────────────────────────┘
```

---

## Key Components

### 1. Claude Code (the AI layer)
Claude Code is Anthropic's CLI that runs AI models directly in the terminal. In COG it:
- Reads and writes vault files directly
- Executes skills on demand (user types `/skill-name`)
- Runs hooks automatically on tool events (pre/post file edits, session stop)
- Uses the vault as its working memory across sessions via a persistent memory system

**Models used:**
- Sonnet — routine tasks (briefs, filing, small edits)
- Opus — synthesis, research, architecture decisions

### 2. The Skills System
Skills are markdown files at `.claude/skills/<name>/SKILL.md`. Each skill is a structured prompt that tells Claude Code how to handle a specific workflow — what to read, what to write, how to behave.

Skills are invoked by typing `/skill-name` in a session. Some are also invoked automatically by Claude when the context matches.

**Skills in use:**

| Skill | Purpose |
|---|---|
| `daily-brief` | Finds and saves verified news against personal interests |
| `braindump` | Captures raw thoughts and structures them into the vault |
| `process-daybook` | Converts daybook entries into structured braindumps |
| `process-readwise` | Processes content from the Readwise vault layer |
| `sync-tasks` | Syncs tagged tasks to Microsoft To Do via OneDrive |
| `plan-week` | Plans the week ahead from projects and open tasks |
| `weekly-checkin` | Weekly reflection and pattern synthesis |
| `capture-notes` | Quick note capture |
| `publish-to-sharepoint` | Publishes content to SharePoint |

### 3. Hooks (Automation Layer)
Hooks are shell commands that fire automatically on tool events, configured in `.claude/settings.json`.

**Active hooks:**

| Hook | Trigger | What it does |
|---|---|---|
| `PreToolUse` | Before any Edit/Write | Blocks writes to framework files and Readwise/ — protection layer |
| `Stop` | End of every session | Runs `git add -A && git commit` — auto-commits vault changes |

**Protection rules:** The PreToolUse hook blocks writes to `.claude/skills/` (except whitelisted custom skills), `.claude/roles/`, `.claude/agents/`, `CLAUDE.md`, `AGENTS.md`, and `Readwise/`. Framework files are only updated via `/update-cog`.

### 4. Readwise (Content Layer)
Readwise is the primary raw content layer, following Karpathy's LLM Wiki pattern:

```
External content → Readwise app/extension → Readwise/ vault → COG processes on demand
```

The `Readwise/` folder contains articles, tweets, books, and full document exports. Claude Code reads directly from these files rather than fetching URLs. The folder is **read-only** — never modified by COG.

### 5. Git (Version Control + Backup)
The vault is a git repository. The Stop hook commits all changes at the end of every Claude Code session automatically:

```bash
git add -A && git commit -m "vault backup: $(date '+%Y-%m-%d %H:%M:%S')"
```

This provides a full history of every vault change, automatic backup on session end, and a safety net for rollback.

### 6. Task Sync (OneDrive → Power Automate → To Do)
Tasks created in the vault can be synced to Microsoft To Do:

```
/sync-tasks → JSON file → OneDrive/COG-Tasks/ → Power Automate → To Do (COG list)
```

- Tasks tagged `#planner` in the vault are collected by `/sync-tasks`
- A JSON file is written to `~/Library/CloudStorage/OneDrive-BelronGlobal/COG-Tasks/`
- Power Automate watches the folder ("When a file is created" trigger — free connector)
- PA creates tasks in the COG list in To Do, then deletes the JSON file
- Tasks can be promoted from To Do to the Project plan via My Tasks in the new Planner

This avoids premium PA connectors (HTTP trigger) and M365 admin requirements (OAuth consent).

---

## User Configuration Files

Three files in `00-inbox/` define how COG behaves for this user:

| File | Purpose |
|---|---|
| `MY-PROFILE.md` | Name, role, active projects, agent mode |
| `MY-INTERESTS.md` | Topics for daily brief curation |
| `MY-INTEGRATIONS.md` | Active/disabled external integrations |

Skills check these files before running — the daily brief uses interests, braindump uses projects, sync-tasks uses integration config.

---

## Content Flow Diagram

```
On the move        → Daybook → /process-daybook → Braindump
Articles/tweets    → Readwise → /process-readwise or on-demand
URLs               → /braindump [url] → Braindump
Raw thoughts       → /braindump → Braindump
Internal docs      → 00-inbox/raw/ → on-demand
                              ↓
                    05-knowledge/ (synthesis)
                              ↓
                    /sync-tasks → To Do → Project plan
```

---

## Replicating This Setup

1. **Install Claude Code** — Anthropic's CLI (`npm install -g @anthropic-ai/claude-code` or via the desktop app)
2. **Create an Obsidian vault in iCloud** — standard Obsidian setup
3. **Run COG onboarding** — `/onboard` creates profile, interests, and integrations files
4. **Configure hooks** — add the PreToolUse protection hook and Stop git-commit hook to `.claude/settings.json`
5. **Install Readwise** — connect the Obsidian Readwise plugin to sync content into `Readwise/`
6. **Set up OneDrive** — install OneDrive for Business, create the `COG-Tasks` folder
7. **Build the PA flow** — see `05-knowledge/integrations/sync-tasks-pa-flow.md`

COG is updated periodically via a shell script (`cog-update.sh`) or `/update-cog` which pulls new skills, roles, and framework files without touching user content.

---

## Design Decisions Worth Noting

- **No cloud agents for vault writes** — scheduled cloud runs (e.g. via claude.ai) don't have access to the local iCloud vault. All vault-writing skills run locally in a Claude Code session.
- **Skills over automation** — most workflows are triggered manually. COG automates the execution but the user decides when to run things. The exception is the Stop hook (always fires) and the PA flow (always watches).
- **OneDrive file drop over HTTP webhooks** — Power Automate HTTP triggers require a premium licence. OneDrive trigger is free and requires no admin consent — just delegated user permissions.
- **To Do as landing zone** — tasks land in a simple To Do list, not directly in a Project plan, keeping the COG-side simple and avoiding Project connector licence requirements. Promotion to Project plan is manual.

---

*Last updated: 2026-06-14*
