---
type: "readwise-thread"
category: "tweets"
source: "readwise"
source_readwise: "Readwise/Full Document Contents/Tweets/"
date_processed: "2026-06-14"
created: "2026-06-14 20:00"
author: "Various"
tags: ["#readwise", "#thread", "#medium-relevance", "#reference"]
relevance: "medium"
related_projects: ["Contact Centre of the Future"]
status: "processed"
---

# Medium Relevance — June 2026 Batch

Items with partial relevance to Armo's interests or active projects, not warranting full dedicated booklets.

---

## 1. Salesforce Headless 360 — Agent-Native Pricing Disruption (JB/@VibeMarketer_)

**Source:** Readwise/Full Document Contents/Tweets/salesforce going headless is bigger than people realize.md

Marc Benioff announced **Salesforce Headless 360**: entire Salesforce + Agentforce + Slack platforms exposed as APIs, MCP, and CLI. No browser required. 

> "Software has been priced per seat for decades. The entire business model assumes a person logs in, clicks around, and gets value from a dashboard. Agents don't log in. They make API calls."

**So what:** One company running 50 agents that each make more API calls per day than an entire sales team does per month blows up the per-seat model. Salesforce forced this question into the open.

**CCOTF relevance:** Belron uses Salesforce Service Cloud. If Salesforce is transitioning to agent-native API billing, the contact centre licensing model changes fundamentally. Any CCOTF vendor evaluation should probe headless/API pricing tiers — the per-seat assumption may not survive the next contract cycle. Noteworthy that Salesforce now exposes MCP — directly relevant to MCP Governance project scope.

---

## 2. 21 Specialized Agents > 1 General Agent — Brain Specialization (Aakash Gupta)

**Source:** Readwise/Full Document Contents/Tweets/The reason 21 specialized agents inside Claude Code beats one....md

Neuroscience framing: the reason 21 specialized agents beats one general prompt is the same reason your brain has a dedicated face recognition area (fusiform face area). Specialization preserves signal fidelity. A region doing two jobs averages out both.

**Gabor's 21-agent dev team (referenced):** System analyst → Confluence docs. Agents file 51 Jira tickets with explicit dependencies. Figma agents drive screens via MCP. UX flow agent wires prototype arrows. Each agent: one clean context window, one job. End result: Flutter app, Firebase backend, Vertex vector DB indexing two books. Shipped to TestFlight in one podcast session. 10% of a $200 Claude Code plan burned.

> "The PMs winning the next two years are doing what evolution settled long ago. Separate the regions. Preserve the signal."

**MCP Governance relevance:** The specialization principle supports the MCP Governance case for tool-level access control. Each agent should have a clean, bounded context — not general-purpose access to all tools. This is an architectural argument for the governance layer, not just a compliance one.

→ See also: [[aakash-gupta-june-2026-06-14]]

---

## 3. Karpathy's Second Brain / NotebookLM+Claude Research Workflow

**Source:** Readwise/Full Document Contents/Tweets/You don't need to read 50 PDFs.md (Olivia Chowdhury)

Workflow: use NotebookLM as the librarian (ingest 50 PDFs) → hand Claude the synthesis question. NotebookLM gives you the library. Claude thinks with you.

8-prompt framework: insights, collective argument across sources, contradictions, blind spots, decision-changing insight, shareable synthesis, follow-up question.

Also references the Karpathy second brain architecture (same as [[karpathy-llm-knowledge-base-2026-06-14]]) as the source inspiration.

**Low COG delta:** This workflow is already implemented via process-readwise + Readwise as the ingestion layer. Useful as a prompt template for ad-hoc research synthesis when multiple PDFs need analysis in a session.

---

## 4. CyrilXBT Business OS — N8N as Automation Layer

**Source:** Readwise/Full Document Contents/Tweets/this is how the founder of obsidian actually takes notes....md (Rohit/@rohit4verse, embedding CyrilXBT guide)

CyrilXBT's business-focused guide: "How to Build an Obsidian Vault That Runs Your Entire Business While You Sleep"

Three-layer architecture:
- **Knowledge Layer:** Obsidian (plain text, machine-navigable)
- **Intelligence Layer:** Claude Code via MCP (reads files, processes information, makes connections, generates outputs — "the thinking that happens while you are not thinking")
- **Automation Layer:** **N8N** — fires workflows on schedule and on trigger without manual initiation; routes information to the right place

**COG delta:** COG uses Power Automate (via sync-tasks) and cron (via Claude Code skills) for the automation layer. N8N is open-source and more flexible for complex conditional routing. Worth noting as an alternative automation layer if COG outgrows cron-based scheduling.

---

## 5. Leopardracer: Karpathy Knowledge Galaxy

**Source:** Readwise/Full Document Contents/Tweets/ANDREJ KARPATHY IS THE GODFATHER OF MODERN AI.md (Leopardracer)

Leopardracer built a custom 3D knowledge graph ("galaxy") copying Karpathy's architecture: 378 notes, 1,854 nodes, 3,856 edges. Visualised with interactive 3D graph rather than Obsidian.

Low delta: content largely covered by [[karpathy-llm-knowledge-base-2026-06-14]] and existing Leopardracer entries. The 3D visualisation is aesthetic rather than functional at this stage.

---
*Processed from Readwise by COG*
