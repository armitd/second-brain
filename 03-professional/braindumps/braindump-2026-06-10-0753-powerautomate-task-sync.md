---
type: "braindump"
domain: "professional"
date: "2026-06-10"
created: "2026-06-10 07:53"
themes: ["power-automate", "task-sync", "m365-integration", "cog-workflow"]
tags: ["#braindump", "#raw-thoughts", "#professional", "#power-automate", "#m365", "#tasks", "#workflow"]
status: "captured"
energy_level: "medium"
emotional_tone: "curious"
confidence: "high"
---

# Braindump: Power Automate for COG Task Sync

## Raw Thoughts

PowerAutomate task too

---

## Content Analysis

### Main Themes

1. **Power Automate as the task sync bridge** — alongside the `/publish-to-sharepoint` skill (documents), Power Automate handles the other half of the COG ↔ M365 integration: tasks. COG generates tasks as markdown checkboxes; Power Automate can move them into Microsoft To Do or Planner.

2. **The integration gap being addressed** — COG tasks live in vault files as `- [ ] item 📅 date` syntax. M365 colleagues and Copilot can't see them. Power Automate can watch for vault changes (via iCloud/OneDrive sync) and push tasks to the right M365 surface.

### Questions Raised

- Which M365 task surface is the target — Microsoft To Do (personal), Planner (team/project), or Teams Tasks?
- Should all COG tasks sync, or only tasks tagged for M365 (e.g. a specific tag or project)?
- Is iCloud accessible to Power Automate? (iCloud Drive can be mounted on Windows; OneDrive sync is more reliable as a trigger)
- Is this a one-way push (COG → M365) or bidirectional?
- Who else needs to see the tasks — just Armo, or should CCOTF/project tasks go to a shared Planner board?

### Decisions Contemplated

- **Sync surface:** To Do (personal) vs. Planner (shared/project)
- **Sync scope:** All tasks vs. filtered by project tag
- **Trigger:** File change on synced folder vs. scheduled scan vs. manual trigger

---

## Strategic Intelligence

### Key Insights

1. **Power Automate is the right tool for this** — it has native connectors for Microsoft To Do, Planner, and Teams. It can be triggered by file changes in OneDrive/SharePoint, making it a natural bridge from a synced vault folder to M365 tasks.

2. **The simplest viable flow:**
   - Vault week plan synced to OneDrive (or SharePoint via `/publish-to-sharepoint`)
   - Power Automate trigger: "when a file is modified in SharePoint/OneDrive"
   - Action: parse the file for unchecked `- [ ]` items
   - Action: create tasks in Microsoft To Do (personal list) or Planner (project board)

3. **Two-layer approach:**
   - **Personal tasks** (To Do): items from `01-daily/plans/week-plan-*.md` → Armo's personal To Do list
   - **Project tasks** (Planner): items from `04-projects/*/PROJECT-OVERVIEW.md` → shared Planner boards per project (CCOTF, MCP Governance, etc.)

4. **Markdown task parsing in Power Automate:** Requires a regex expression or a small Azure Function to extract `- [ ]` lines and their dates from Markdown. Power Automate's string functions can handle basic regex; no code deployment needed.

### Pattern Recognition

- **Connected to M365 integration discussion** — this is the task layer of the COG ↔ M365 integration strategy discussed earlier today
- **Connected to `/publish-to-sharepoint`** — documents go via the skill; tasks go via Power Automate. Together they cover the two main integration needs.

### Strategic Implications

- Once running, the week plan becomes a single source of truth that feeds both COG (for personal reflection) and M365 (for Copilot and colleague visibility) automatically
- This removes the friction of manually copying tasks between systems — the biggest barrier to actually using both

---

## Action Items

### Immediate (24-48 hours)
- [ ] Sketch the Power Automate flow logic: trigger → parse markdown → create To Do tasks 📅 2026-06-11

### Short-term (1-2 weeks)
- [ ] Build and test the Power Automate flow for week plan → Microsoft To Do sync 📅 2026-06-17
- [ ] Decide whether project tasks (CCOTF, MCP Governance) should sync to shared Planner boards 📅 2026-06-17

### Strategic Considerations
- Start with To Do (personal) — lower stakes, easier to test
- Add Planner integration once the parsing logic is proven
- Consider whether to build a COG skill (`/sync-tasks`) that wraps the Power Automate trigger via an HTTP webhook

---

## Connections
- **Related Braindump:** This session's M365/Copilot integration discussion
- **Related Skill:** [[.claude/skills/publish-to-sharepoint/SKILL.md]] — documents layer of the same integration
- **Related Project:** All active projects — tasks from each could flow to Planner boards

---

## Domain Classification
- **Primary Domain:** Professional (90%)
- **Cross-Domain Elements:** Personal task management (Getting Fit, Alps Holiday tasks could also sync to To Do)
- **Privacy Level:** internal — workflow design

---

*Processed by COG Brain Dump Analyst · 2026-06-10 07:53*
