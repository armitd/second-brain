---
type: integrations
created: 2026-04-06
tags: ["#integrations", "#config", "#cog"]
---

# My Integrations

*COG checks this file before using any external service. Edit anytime.*

## Active

**Canva**
- Connected via Claude MCP integration
- Use for: generating presentations, posters, reports, social posts, and other branded collateral
- Brand kit ID: kAGGs2XOG3E (your Canva brand kit)

**GitHub**1

**Readwise**
- Location: `Readwise/` in vault with four subfolders:
  - `Readwise/Tweets/` — saved tweets organised by author (one file per person, all their saved tweets inside)
  - `Readwise/Full Document Contents/Tweets/` — full thread captures, one file per thread, titled by topic (190 threads; use this when looking for a specific thread or topic)
  - `Readwise/Articles/` — 21 saved articles including AI, EA, and productivity content
  - `Readwise/Books/` — 79 books with highlights across EA, health, music, fiction, and food
  - `Readwise/Full Document Contents/Articles/` — full-text article exports
  - `Readwise/Full Document Contents/Books/` — full-text book exports
- Use for: reading tweet/article/book content and highlights directly from vault instead of fetching URLs
- No API needed — read directly from vault files


**SharePoint — Document Publishing**
- method: OneDrive file drop (free PA connectors — OneDrive + SharePoint)
- drop-folder: `~/Library/CloudStorage/OneDrive-BelronGlobal/COG-Publish/`
- staging-site: *(paste your SharePoint site URL here)*
- target-folder: *(e.g. /Documents/COG)*
- setup-guide: [[05-knowledge/integrations/publish-to-sharepoint-pa-flow]]

**Microsoft To Do — Task Sync**
- method: OneDrive file drop (free PA connectors — OneDrive + Microsoft To Do Business)
- drop-folder: `~/Library/CloudStorage/OneDrive-BelronGlobal/COG-Tasks/`
- landing-list: COG (tasks land here, promote to Project plan manually via My Tasks)
- setup-guide: [[05-knowledge/integrations/sync-tasks-pa-flow]]

**Granola**
- Connected via Claude MCP integration
- Use for: retrieving meeting transcripts, notes, and meeting history

**IFTTT**
- Connected via Claude MCP integration
- Use for: applet automation, connecting services, running actions and queries

**LeanIX**
- Connected via Claude MCP integration
- Auth: API key stored in MCP server config (env var — not in vault)
- Use for: querying Belron's EA repository — applications, tech stacks, architecture decisions, initiatives, components, fact sheets
- Note: includes write-capable tools (create/update architecture decisions, tech stacks) — use with care; mutations affect the live EA repository
- Data classification: Belron Confidential — LeanIX contains non-public application portfolio data

**Lucid (Lucidchart)**
- Connected via HTTP MCP at `https://mcp.lucid.app/mcp`
- Use for: creating diagrams from natural language descriptions, searching and retrieving Lucid documents, generating org charts, creating shareable diagram links

## Disabled
- **AlignedNews**: Cancelled 2026-06-30. Contributed 0 stories in 3 of last 5 briefs; when used, surfaced X/Twitter signals only. WebSearch covers the gap. $25 pcm saving.
- **Slack**: Not confirmed during onboarding. Enable anytime by moving to Active section.
- **Linear**: Not confirmed during onboarding. Enable anytime by moving to Active section.
- **Confluence**: Not confirmed during onboarding. Enable anytime by moving to Active section.
- **ElevenLabs**: Disabled by default.

---

*Move services between Active and Disabled sections to control what COG connects to.*
