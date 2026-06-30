---
type: "braindump"
domain: "professional"
date: "2026-06-27"
created: "2026-06-29 11:31"
source: "daybook"
source_file: "01-daily/daybooks/daybook-2026-06-27.md"
themes: ["guild-governance", "cog-automation", "o365-integration"]
tags: ["#braindump", "#from-daybook", "#guild", "#cog", "#o365"]
status: "captured"
energy_level: "medium"
emotional_tone: "curious"
confidence: "medium"
---

# Braindump: Guild Stakeholder Mapping + COG Loops + O365 Integration

## Raw Thoughts

*Captured in daybook 2026-06-27. Processed 2026-06-29.*

**Guild.**

- Who are our stakeholders?
  - JB, SS, Helen, Dan?, Business?
- Group Members: Salesforce product team, Will Porter (Product Owner), Solution Architects (Steve HS), Brad (EA), John P (EA - Data), Trudi King (SA lead), Mani Singh (Data), Jerry Kofi?, Suresh Naguru, Wreford Laurence, Ronan Williams
- Who decided the Guild should be set up? Who had the vision? (Is Dan involved?)
- What is the mandate? Build a model, Design a Process, share experience and knowledge.
- What is the objective?
- French team — do we really need to have them in the guild? Feels too early.
- Adjustment Programme general — who is running it? Who owns it? Scope. Relationship to Guild.
- Helen — Stakeholder management. What's her relationship to the guild/AP etc? What's her stakeholder role?

**New item** — Adding Loops to COG — with Python and scripts for triggers.
- I like the processes — "put a file in a directory" triggering the process. How to integrate that into COG.
- Also how to play that into O365 — trigger in COG → auto file uploads to OneDrive, creates files and tasks.

**New item** — Obsidian learning. Teach myself Obsidian.

**Personal:**
- Sort out kadai — cleaning plus wooden lid.
- Garden job — sand and varnish wooden tables etc in garden.

---

## Content Analysis

### Main Themes

1. **Guild governance and stakeholder clarity:** A Salesforce/EA Guild has been set up but the mandate, ownership, and stakeholder map are unclear. Key open questions: who initiated it, what the Adjustment Programme relationship is, and whether the French team should be included yet.

2. **COG automation expansion:** The loops idea (Python scripts triggered by file system events) is worth building into COG's architecture. The file-drop trigger model ("put a file in a directory and it processes") is the cleanest UX pattern. *Note: this was implemented in this session (June 28–29) — launchd agents, Python scripts, and the lecture queue are now live.*

3. **O365 integration as a COG extension:** Extending COG triggers into the Microsoft 365 ecosystem — auto-file uploads to OneDrive, task creation — is a natural next step once the local loop infrastructure is stable.

### Supporting Ideas
- The Guild membership list is large and diverse (EA, SA, Data, Product, Salesforce team). Size and diversity risk without clear mandate = governance by committee.
- "Adjustment Programme" appears to be an umbrella programme that the Guild sits within — but ownership and scope are unresolved.
- Obsidian self-learning is a natural companion to COG usage — understanding the underlying tool better is leverage.
- The kadai and garden table items are personal action items, not professional.

### Questions Raised
- Who initiated the Guild? Is this a Dan-sponsored initiative or bottom-up from the EA/SA community?
- What is the formal mandate — "build a model, design a process, share knowledge" is a starting point but not a measurable objective.
- Is the French team involvement premature, or is there a specific reason they were included early?
- What is Helen's formal role — stakeholder manager for the Guild, or for the broader Adjustment Programme?
- How does the O365 integration fit the MCP Governance programme? (COG → OneDrive triggers are agent-to-system calls and fall under the same governance scope.)

### Decisions Contemplated
- Whether to include French team in the Guild at this stage (leaning: too early).
- Whether the Guild should report to the Adjustment Programme or operate independently.
- How far to take the O365 COG integration — light touch (OneDrive file drop) vs. full task/calendar integration.

---

## Strategic Intelligence

### Key Insights

1. **The Guild has no clear owner and that is the risk.** A large multi-discipline group (EA + SA + Data + Product + Salesforce team) without a named sponsor and explicit mandate becomes a talking shop. The EA's role here is to push for a written mandate and a named accountable owner before the Guild consumes significant time.

2. **COG loops are now live — the O365 extension is the logical next phase.** The local Python loop infrastructure (launchd, file watch, API calls) was implemented in the June 28–29 session. The O365 integration would extend the same pattern into the corporate ecosystem: drop a file to OneDrive → COG processes it → creates a task in Planner or a note in SharePoint. This is distinct from the local vault loops and requires an O365 API layer.

3. **"Obsidian learning" is a proxy for COG depth.** The note to teach himself Obsidian suggests there are COG/vault capabilities being underused because the underlying tool isn't fully understood. A focused Obsidian learning investment (dataview queries, graph view, canvas) would unlock more of what's already built.

### Pattern Recognition
- **Connection to MCP Governance:** The O365 trigger idea is an agent-to-enterprise-system call, which is exactly the governance territory MCP Governance covers. The "trigger in COG → creates tasks in O365" pattern should be designed with the same identity/audit principles as the CCOTF enterprise integration gateway.
- **Connection to EA Effectiveness Framework:** The Guild ambiguity (no mandate, no owner) is a classic EA governance gap — precisely the scenario where an Architecture Contract (Principle 8, Tier 2) would add value.

### Strategic Implications
- Resolve Guild mandate before investing EA time in it. One meeting to establish: sponsor, written mandate, and scope boundary relative to the Adjustment Programme.
- O365 integration for COG is a medium-term project — needs O365 API access scoping first.
- Personal items (kadai, garden table) are unrelated to professional strategy.

---

## Action Items

### Immediate (24–48 hours)
- [ ] Find out who initiated the Guild and confirm Dan's involvement 📅 2026-07-01
- [ ] Ask Helen directly: what is her formal role relative to the Guild and Adjustment Programme? 📅 2026-07-01

### Short-term (1–2 weeks)
- [ ] Draft a one-page Guild mandate proposal (sponsor, objective, scope, cadence, French team decision) 📅 2026-07-06
- [ ] Explore O365 API options for COG trigger → OneDrive/Planner integration 📅 2026-07-13
- [ ] Start Obsidian learning — begin with Dataview basics 📅 2026-07-06

### Personal
- [ ] Sort out kadai — clean and get wooden lid 📅 2026-07-06
- [ ] Sand and varnish wooden garden tables 📅 2026-07-13

### Strategic Considerations
- The Guild governance question has EA Effectiveness Framework implications: arriving with a draft mandate is more valuable than attending as an observer. Own the artefact, don't just participate in the conversation.
- O365 integration scope should be assessed through the MCP Governance lens before building — if COG-to-O365 triggers are agent-to-system calls, they need the same identity/audit controls as any other governed integration.

---

## Connections
- **Source:** [[daybook-2026-06-27]]
- **Related frameworks:** [[ea-effectiveness-framework]] (Guild mandate = Architecture Contract opportunity), [[agentic-ai-governance-framework]] (O365 trigger governance)
- **COG loops (implemented):** loops are now live as of 2026-06-28 via launchd agents

## Domain Classification
- **Primary Domain:** Professional (85%)
- **Secondary:** Personal (15%) — kadai and garden items
- **Reasoning:** Guild governance, COG architecture, and O365 integration are all professional. Personal items are minor captures.
- **Privacy Level:** Internal — Guild member names and stakeholder observations are internal to Belron

---
*Processed by COG from daybook — 2026-06-29 11:31*
