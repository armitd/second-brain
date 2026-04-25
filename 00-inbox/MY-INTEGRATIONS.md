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

**AlignedNews**
- API endpoint: `https://alignednews.com/v1`
- Auth: Bearer token via env var `ALIGNEDNEWS_API_KEY`

**Readwise**
- Location: `Readwise/` in vault with four subfolders:
  - `Readwise/Tweets/` — saved tweets organised by author (one file per person, all their saved tweets inside)
  - `Readwise/Full Document Contents/Tweets/` — full thread captures, one file per thread, titled by topic (75 threads; use this when looking for a specific thread or topic)
  - `Readwise/Articles/` — 20 saved articles including AI, EA, and productivity content
  - `Readwise/Books/` — 66 books with highlights across EA, health, music, fiction, and food
  - `Readwise/Full Document Contents/Articles/` — full-text article exports
  - `Readwise/Full Document Contents/Books/` — full-text book exports
- Use for: reading tweet/article/book content and highlights directly from vault instead of fetching URLs
- No API needed — read directly from vault files


## Disabled
-
- **Slack**: Not confirmed during onboarding. Enable anytime by moving to Active section.
- **Linear**: Not confirmed during onboarding. Enable anytime by moving to Active section.
- **Confluence**: Not confirmed during onboarding. Enable anytime by moving to Active section.
- **ElevenLabs**: Disabled by default.

---

*Move services between Active and Disabled sections to control what COG connects to.*
