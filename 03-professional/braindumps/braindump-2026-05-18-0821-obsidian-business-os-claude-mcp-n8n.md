---
type: "braindump"
domain: "professional"
date: "2026-05-18"
created: "2026-05-18 08:21"
themes: ["second-brain", "agentic-ai", "obsidian", "mcp", "automation", "knowledge-architecture"]
tags: ["#braindump", "#research", "#agentic-ai", "#mcp", "#obsidian", "#n8n", "#architecture"]
status: "consolidated"
consolidated_in: "[[consolidation-2026-05-19]]"
consolidated_date: "2026-05-19"
energy_level: "high"
emotional_tone: "inspired"
confidence: "high"
source_readwise: "Readwise/Full Document Contents/Tweets/this is how the founder of obsidian actually takes notes....md"
source_author: "CyrilXBT (@cyrilXBT), saved via Rohit (@rohit4verse)"
---

# Braindump: Obsidian Business OS — Claude + MCP + N8N as a Three-Layer Architecture

## Raw Thoughts

This was flagged during Readwise processing — a thread by @CyrilXBT describing a "business operating system" built on Obsidian + Claude Code (via MCP) + N8N. It's 500+ words of structured framework thinking, not just tips. Worth capturing properly because it mirrors what COG does, describes the underlying architecture more explicitly than COG's documentation, and has direct implications for the MCP Governance project.

The piece that grabbed me: the explicit naming of three architectural layers — Knowledge, Intelligence, Automation. That's a clean model. COG essentially implements the same thing but through skills rather than N8N. The question is whether N8N adds something COG doesn't have, or whether it's solving the same problem differently.

---

## The Three-Layer Model

**Layer 1 — Knowledge:** Obsidian itself. Plain-text Markdown files, human-readable and machine-navigable. The vault is the source of truth.

**Layer 2 — Intelligence:** Claude Code connected via MCP. This is what makes the vault *active* rather than passive — Claude reads files, processes information, makes connections, generates outputs. The "thinking that happens while you are not thinking."

**Layer 3 — Automation:** N8N (self-hosted, $5/month DigitalOcean droplet). The clock and nervous system. Fires workflows on schedule and on trigger. Unlimited runs, no per-execution pricing.

The layering matters: Knowledge is static, Intelligence is on-demand, Automation is the scheduler that makes Intelligence run without human initiation.

---

## The Six Business Systems

CyrilXBT built six interconnected systems on this architecture. Each owns a function and passes information to others through the shared vault:

### 1. Client Intelligence
- **Pre-Call Brief:** Fires 30 minutes before every client call — reads client folder, produces a 5-minute briefing covering relationship timeline, open items, last communication, suggested agenda, and "the one thing to make sure you say"
- **Communication Logger:** Every logged client interaction auto-files to the client communications folder

### 2. Project Operations
- **Daily Project Pulse:** 6AM cron — reads all active project overview files, reports status, flags anything within 7 days of deadline, stuck for 5+ days, or blocked with no resolution plan
- **Project Auto-Updater:** `DONE: [project] — [deliverable]` convention in daily notes triggers automatic project task list update

### 3. Content Production
- **Morning Content Brief:** Three content angles per day, ranked by potential, with hook options and format recommendations
- **Draft Engine:** QUEUE folder pattern — drop `DRAFT-[type]-[topic].md`, system picks it up and produces a first draft in GENERATED/drafts
- **Performance Tracker:** Monday morning content analytics across all platforms

### 4. Financial Operations
- **Revenue Logging:** `RECEIVED: $[amount] — [client] — [description]` convention → auto-updates monthly tracker and client invoice folder
- **Monthly Financial Brief:** 1st of month → previous month P&L, revenue by client, trends
- **Invoice Reminder:** 25th of month → draft invoice emails for outstanding retainer amounts

### 5. Research & Intelligence
- **Daily Intelligence Brief:** Pulls news + competitor signals, synthesises into three developments + one opportunity + one risk + recommended action
- **Research Queue:** Drop `RESEARCH-[topic].md` at midnight, brief ready at 6AM

### 6. Performance & Review
- **Weekly Review:** Sunday 8PM — reads entire week across all systems, produces cross-system retrospective with three priorities for next week
- **Quarterly Business Review:** First day of each quarter — reads three months of weekly reviews, produces strategic retrospective

---

## The Two Core Patterns

**The QUEUE/GENERATED pattern:** The asynchronous communication loop between human and intelligence layer. You drop a file when a need occurs. The system processes it on its next cycle. You review results when convenient. Human and AI are never waiting on each other simultaneously — this decoupling is what makes the system feel like infrastructure rather than a tool.

**CLAUDE.md as the Business Constitution:** The single most important file. Every automated workflow reads it before doing anything. Contains: business identity, active clients, active projects, voice and communication style, revenue targets, content operation, and operating rules. The Weekly Focus section (updated every Monday) keeps the system aligned to current priorities. A precisely written CLAUDE.md makes generic AI capability into business-specific intelligence.

The N8N trigger hierarchy:
- **Cron:** Scheduled operations (6AM briefings, Sunday reviews, monthly reports, 25th invoice reminders)
- **File Watch:** Event-based (QUEUE folder, project folder changes)
- **Webhook:** External events (Stripe payment → revenue update, new calendar event → pre-call brief)

---

## Comparison to COG

| Dimension | CyrilXBT's OS | COG |
|-----------|--------------|-----|
| Knowledge layer | Obsidian vault | Obsidian vault |
| Intelligence layer | Claude Code via MCP | Claude Code skills |
| Automation layer | N8N (self-hosted) | CronCreate + RemoteTrigger (COG harness) |
| Trigger model | Cron + File Watch + Webhook | Cron + Remote + Manual |
| Async queue | QUEUE folder → GENERATED | Not explicitly modelled |
| Business constitution | CLAUDE.md | CLAUDE.md + MY-PROFILE.md |
| Multi-system orchestration | N8N workflow chains | Skill-to-skill via conversation |

**Key difference:** N8N provides webhook triggers (external events like Stripe payments triggering vault updates) that COG's harness doesn't currently support. COG's skills are richer and more conversational; N8N workflows are more reliable and schedulable without human initiation.

**Key similarity:** Both rest on the same insight — the CLAUDE.md (or MY-PROFILE.md) as persistent context that makes each automated run business-specific rather than generic.

---

## The Compounding Effect Argument

This is the most interesting strategic claim in the thread:

*"After six months of consistent use, your vault knows your business at a depth that would take a human employee years to develop."*

The mechanism: each logged interaction enriches the pre-call brief. Each content performance data point calibrates the content brief. Each research brief builds accumulated context. Each weekly review becomes material for better quarterly analysis. The system doesn't just store — it compounds.

This is the argument for why a *structured* second brain with consistent logging conventions beats an unstructured one. The conventions (`DONE:`, `RECEIVED:`, `DRAFT-[type]-[topic]`) are what make the vault machine-navigable. Without them, it's just a folder of notes.

---

## Implications for Active Projects

**MCP Governance:**
This architecture illustrates exactly what EA needs to govern — an intelligence layer (Claude via MCP) that reads vault content and produces outputs, triggered by an automation layer (N8N). The governance questions become: who approves which MCP server connections? What data is the intelligence layer allowed to read? What outputs can it write autonomously vs requiring human review? The operating rules in CLAUDE.md ("Never send communication without human review," "Escalate anything involving money, commitments, client relationships, or reputational decisions") are a practical example of governance embedded in the system itself.

**Contact Centre of the Future:**
The Client Intelligence system — pre-call brief, communication logger — is a microcosm of what a future contact centre should do for Belron's customers. A technician briefed before a customer call with the full repair history, last interaction, open warranty items, and the one thing to make sure they say. The pattern is identical; the scale is different.

**AI Damage Assessment PoC:**
The QUEUE/GENERATED pattern is an interesting UX model for the damage assessment tool — customer drops an image → system returns assessment → human technician reviews result. The asynchronous decoupling is the right mental model for high-volume assessment workflows.

---

## Questions Worth Exploring

- Does Belron's IT security posture allow a self-hosted N8N deployment, or does it need to be on Azure/GCP?
- Would a Belron-internal version of this architecture (vault + Claude Code + scheduled agents) be a viable EA productivity tool before pitching it as enterprise infrastructure?
- What are the GDPR implications of an intelligence layer reading operational files that may contain customer data?
- Is the QUEUE folder pattern worth building explicitly into COG as an async research/draft request mechanism?

---

## Source
- **Thread by:** CyrilXBT (@cyrilXBT), posted May 13, 2026
- **Saved via:** Rohit (@rohit4verse) retweet
- **Full text:** [[Readwise/Full Document Contents/Tweets/this is how the founder of obsidian actually takes notes....|Full thread →]]

---
*Captured from Readwise by COG — May 18, 2026*
