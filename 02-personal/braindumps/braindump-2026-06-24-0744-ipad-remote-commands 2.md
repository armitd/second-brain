---
type: "braindump"
domain: "personal"
date: "2026-06-24"
created: "2026-06-24 07:44"
themes: ["ipad-workflow", "remote-access", "terminal-tools"]
tags: ["#braindump", "#raw-thoughts", "#personal", "#ipad", "#productivity", "#tools"]
status: "captured"
energy_level: "low"
emotional_tone: "curious"
confidence: "high"
---

# Braindump: Running Commands Remotely on iPad

## Raw Thoughts
Ways to run commands remotely on iPad:

SSH clients — Termius or Blink Shell let you SSH into your Mac from the iPad. Need to enable Remote Login on Mac (System Settings > General > Sharing > Remote Login). Works on same network; use Tailscale or Cloudflare Tunnel for anywhere access.

iSH app — runs Alpine Linux directly on the iPad itself, no server needed. Good for lightweight shell work but won't run Mac-native tools.

Claude Code web app — claude.ai/code works in iPad Safari. No terminal but can continue Claude Code sessions from the iPad.

Jump Desktop or Apple Screen Sharing (Screens app) — full remote desktop to the Mac from iPad, terminal included.

VS Code Remote / code-server — run code-server on the Mac, access full VS Code including integrated terminal from iPad Safari.

For my Obsidian vault and Claude Code workflow, Termius SSHing into the Mac is probably the most practical option.

## Content Analysis

### Main Themes
1. **SSH-based remote access:** Termius and Blink Shell are the primary tools for direct terminal access to Mac from iPad — lightweight, purpose-built for this.
2. **On-device iPad compute:** iSH gives a local Linux shell without needing the Mac at all — limited but self-contained.
3. **Claude Code continuity from iPad:** claude.ai/code works in Safari, enabling continued AI-assisted work sessions from the iPad without a terminal.

### Supporting Ideas
- Remote Login must be enabled on the Mac before any SSH approach works
- Tailscale / Cloudflare Tunnel are the "anywhere" layer for SSH when not on the home network
- VS Code Remote / code-server is the highest-capability option but requires server setup on the Mac
- Jump Desktop gives full desktop but is heavier than a terminal-only approach

### Questions Raised
- Is Tailscale already set up on the Mac? If not, that's a prerequisite for away-from-home use.
- Does the Claude Code web app (claude.ai/code) support the full MCP tool set, or is it limited compared to the CLI?
- Would iSH be sufficient for lightweight Obsidian vault text editing on the go?

### Decisions Contemplated
- **Termius SSH vs. Jump Desktop:** SSH (Termius) is lighter and terminal-focused; Jump Desktop is heavier but gives full GUI access. For terminal-only work, Termius wins.
- **iSH vs. SSH:** iSH works offline and needs no Mac to be on, but can't access Mac files or Mac-native tools. SSH needs the Mac awake and networked.

## Strategic Intelligence

### Key Insights
1. **Termius + Tailscale is the practical solution:** SSH into the Mac via Tailscale gives full terminal access from anywhere, including Claude Code CLI and Obsidian vault files, without any heavy infrastructure.
2. **claude.ai/code fills the no-terminal gap:** For reviewing or continuing AI sessions from the iPad without SSH setup, the web app is a zero-setup option — useful for quick catch-ups.
3. **iSH is a useful offline fallback:** If the Mac is off or unavailable, iSH provides a local shell environment for lightweight tasks.

### Pattern Recognition
- **Connection to Previous Thinking:** This connects to the Home Automation project — making the home Mac accessible remotely is part of a broader theme of untethering from a specific desk setup.
- **Recurring Patterns:** The preference for lightweight, terminal-first tools over full remote desktop solutions is consistent with how Claude Code and Obsidian are already being used (CLI-first, text-first).

### Strategic Implications
- Setting up Tailscale on the Mac is a one-time task that unlocks iPad terminal access from anywhere — worth doing once properly
- The Claude Code web app at claude.ai/code could meaningfully extend working sessions to the iPad without any additional setup

## Action Items

### Immediate (24-48 hours)
- [ ] Install Termius on iPad 📅 2026-06-25
- [ ] Enable Remote Login on Mac (System Settings > General > Sharing > Remote Login) 📅 2026-06-25

### Short-term (1-2 weeks)
- [ ] Set up Tailscale on Mac and iPad for away-from-home SSH access 📅 2026-07-01
- [ ] Test claude.ai/code in iPad Safari — check which tools and MCP connections are available vs. the CLI 📅 2026-07-01

### Strategic Considerations
- Once Tailscale is set up, the Mac becomes accessible from anywhere the iPad has internet — could also enable accessing the Obsidian vault from the iPad via SSH/SFTP without needing iCloud sync

## Connections
- **Relevant Projects:** [[04-projects/home-automation/PROJECT-OVERVIEW]]
- **Knowledge Base:** Remote access patterns, productivity tools

## Domain Classification
- **Primary Domain:** Personal (90%)
- **Reasoning:** Personal productivity and home tech setup; not directly work-related
- **Cross-Domain Elements:** Claude Code continuity has professional overlap (COG workflow)
- **Privacy Level:** Public

## Processing Notes
### Emotional Context
- **Energy Level:** Low — pragmatic reference capture, not an excited idea burst
- **Emotional Tone:** Curious / practical
- **Implications:** This is a tool reference note, not a strategic decision — low-urgency capture

### Confidence Assessment
- **Overall Analysis:** 92% — clear, factual content with obvious implications
- **Domain Classification:** 90% — primarily personal but with professional workflow overlap
- **Strategic Insights:** 88% — the Termius + Tailscale recommendation is solid; claude.ai/code capability question remains open
- **Areas Requiring Clarification:** Whether Tailscale is already installed on the Mac; claude.ai/code MCP tool availability

---

*Processed by COG Brain Dump Analyst*
