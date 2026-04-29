---
type: "braindump"
domain: "project-specific"
project: "mcp-governance"
date: "2026-04-29"
created: "2026-04-29 10:38"
themes: ["ifttt-mcp", "agentic-automation", "real-world-triggers", "mcp-governance"]
tags: ["#braindump", "#mcp", "#ifttt", "#agentic-ai", "#automation"]
status: "captured"
energy_level: "high"
emotional_tone: "curious"
confidence: "high"
---

# Braindump: IFTTT MCP Server — What Can Claude Trigger?

## Raw Thoughts
Set up IFTTT MCP server - and see what I can trigger with it.

## Content Analysis

### Main Themes
1. **IFTTT as a general-purpose action layer for Claude** — IFTTT connects to hundreds of services via webhooks. An MCP server wrapping IFTTT would give Claude a single interface to trigger automations across smart home, productivity, communication, and IoT.
2. **Experimentation with real-world agentic actions** — this moves Claude from answering questions to taking actions in the physical and digital world. A meaningful step-up in agentic capability.
3. **MCP governance implications** — one MCP server granting access to hundreds of external services is a significant trust surface. Relevant test case for the MCP Governance project.

### What IFTTT MCP Could Trigger

**Smart Home / IoT**
- Philips Hue / LIFX — turn lights on/off, change colour
- Nest / Ecobee — set thermostat
- Ring — trigger alerts, view status
- SmartThings — broad home automation

**Notifications & Communication**
- SMS via phone number (IFTTT native notification or Twilio)
- Push notification to phone
- Send email
- Slack message to a channel
- Telegram message

**Productivity & Data**
- Add row to Google Sheets (log data, track actions)
- Create Trello card
- Create Todoist task
- Add to Notion database
- Create Google Calendar event

**COG-specific use cases**
- Auto-create Todoist tasks from COG action items
- Log processed Readwise items to a Google Sheet
- Send daily brief summary as a push notification
- "Do not disturb" light trigger during deep work sessions

### Questions Raised
- Is there an existing IFTTT MCP server (community-built), or does one need to be built?
- IFTTT uses webhook triggers — how complex is the MCP wrapper?
- What's the authentication model? IFTTT webhooks use a personal key — how is that stored in the MCP config?
- Which IFTTT applets need to be pre-configured vs dynamically triggered?
- What are the rate limits and latency on IFTTT webhooks?

### Decisions Contemplated
- Build vs find: search for existing IFTTT MCP server before building from scratch
- Scope of experiment: start with 2-3 applets (notifications, Google Sheets logging, smart home) rather than trying everything at once
- Where to store the webhook key securely in the MCP server config

## Strategic Intelligence

### Key Insights

1. **IFTTT is the fastest path to real-world Claude actions.** Rather than integrating with each service's API individually, IFTTT acts as a pre-built abstraction layer. One MCP server = access to ~700 services. The tradeoff is IFTTT latency and reliability vs direct API calls.

2. **This is a COG infrastructure upgrade, not just an experiment.** If Claude can trigger IFTTT, COG skills could gain real-world side effects: braindump → auto-create Todoist tasks; daily brief → push notification summary; process-readwise → log to tracking sheet. These close the loop between intelligence and action.

3. **Governance implication — IFTTT MCP is a broad trust grant.** From an MCP Governance standpoint, an IFTTT MCP server is unusually powerful. Approving the MCP server doesn't just grant one capability — it implicitly grants access to every IFTTT applet configured. This is a real-world example of the "blast radius" problem in MCP governance: a single server with wide permissions. Worth documenting as a case study.

### Pattern Recognition
- **Connection to MCP Governance project** — this is a live test case of the governance questions already being explored: how do you scope, audit, and authorise MCP server permissions?
- **Connection to COG agentic AI interest** — IFTTT MCP bridges the gap between Claude as a knowledge tool and Claude as an action agent
- **Connects to [[braindump-2026-04-08-0942-a2a-mcp-research-strategy]]** — the question of what Claude can *do* (not just know) via MCP

### Strategic Implications
- If the experiment works well, IFTTT MCP could be added to COG's active integrations in `MY-INTEGRATIONS.md`
- Could demonstrate a practical agentic AI use case to stakeholders at Belron — "Claude can trigger real actions, not just generate text"
- Sets up future thinking about A2A (Agent-to-Agent) where COG delegates real-world actions to sub-agents

## Action Items

### Immediate (this week)
- [ ] Search for existing IFTTT MCP server — GitHub, npm, Smithery, MCP registry 📅 2026-04-30
- [ ] If found: install and connect to Claude Code, configure 2-3 test applets (notification, Google Sheets, smart home) 📅 2026-05-02
- [ ] If not found: assess effort to build a lightweight IFTTT webhook MCP server 📅 2026-05-02

### Short-term (2 weeks)
- [ ] Test: trigger a COG action item → Todoist task automatically 📅 2026-05-09
- [ ] Test: send a push notification from a COG skill 📅 2026-05-09
- [ ] Document findings as a case study for the MCP Governance project 📅 2026-05-09

### Strategic Considerations
- If IFTTT MCP proves reliable: propose adding to COG's standard integration set
- Write up the "broad trust surface" governance finding — IFTTT as a MCP blast-radius example

## Connections
- **Related Braindumps:** [[braindump-2026-04-08-0942-a2a-mcp-research-strategy]]
- **Relevant Projects:** [[04-projects/mcp-governance/PROJECT-OVERVIEW]]
- **Knowledge Base:** [[karpathy-llm-wiki-original-post-2026-04-27]] *(IFTTT MCP is the action layer Karpathy's pattern lacks)*

## Domain Classification
- **Primary Domain:** Project-specific — MCP Governance (85%)
- **Secondary:** Professional/personal experiment (15%)
- **Reasoning:** Core questions (blast radius, trust surface, agentic action) are directly in scope for the MCP Governance project
- **Privacy Level:** private

## Processing Notes

### Emotional Context
- **Energy Level:** High — this is an "I want to try this today" idea
- **Emotional Tone:** Curious, exploratory
- **Implications:** High follow-through likelihood — low barrier to start (just search for existing server)

### Confidence Assessment
- **Overall Analysis:** 88% — idea is clear, context is rich
- **IFTTT capability claims:** 80% — based on known IFTTT service list, actual applet availability should be verified
- **Governance framing:** 90% — the blast-radius insight is solid and actionable

---

*Processed by COG Braindump Skill — 2026-04-29 10:38*
