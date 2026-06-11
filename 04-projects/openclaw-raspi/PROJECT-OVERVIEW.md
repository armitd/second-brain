---
type: "project"
title: "OpenClaw on Raspberry Pi"
status: "planning"
created: "2026-06-11"
tags: ["#project", "#personal", "#raspberry-pi", "#openclaw", "#agentic-ai", "#claude"]
---

# OpenClaw on Raspberry Pi

## What is this?

An investigation into running **OpenClaw** on a dedicated Raspberry Pi — a personal, always-on AI agent gateway that runs locally on cheap hardware and connects to cloud models (Claude by default) via API.

OpenClaw is open-source AI agent infrastructure: the Pi acts purely as a gateway and orchestration host; the actual model processing happens via cloud API. The result is a persistent personal AI agent accessible via messaging apps (Telegram, WhatsApp, Discord) for ~£50 one-time hardware cost with no ongoing infrastructure fees.

---

## Why This is Interesting

- **Always-on personal AI agent** — not a chat session you open and close, but an agent that can be triggered via Telegram message from anywhere, runs automations in the background, and persists state between interactions.
- **Claude-powered by default** — OpenClaw recommends `claude-sonnet-4-6` as its primary model with GPT-5.4-mini as fallback. This is a practical home lab for the same Claude stack relevant to Belron AI advocacy.
- **Local gateway, cloud model** — the Pi never does the heavy lifting. This makes even a Pi 4 (2–4GB RAM) sufficient. Privacy-conscious: the gateway is in your home network; only prompts and responses transit the cloud API.
- **Tangible agentic AI at home** — directly connects to the harness/agentic AI thinking in the MCP Governance project: [[03-professional/braindumps/braindump-2026-06-11-0938-harnesses-agentic-ai]]. OpenClaw on a Pi is a personal harness you can experiment with.

---

## Hardware Requirements

| Spec | Minimum | Recommended |
|---|---|---|
| **Model** | Raspberry Pi 3B+ | Pi 4 or Pi 5 |
| **RAM** | 1 GB (with swap) | 4 GB |
| **Storage** | 16 GB SD card | USB SSD (more reliable, faster) |
| **OS** | Raspberry Pi OS Lite 64-bit | Same |
| **Network** | WiFi | Ethernet (more stable) |
| **Not recommended** | Pi Zero 2 W (insufficient resources) | — |

**Estimated cost:** £35–80 one-time (Pi hardware + SD/SSD + case + power supply)

---

## Software & Architecture

- **OpenClaw** — open-source agent gateway (installed via curl, ~30 min setup)
- **Node.js 24** — runtime dependency
- **Primary model:** `claude-sonnet-4-6` via Anthropic API
- **Fallback model:** GPT-5.4-mini (optional)
- **Channels (how you interact with it):**
  - Telegram ← recommended starting point for headless Pi setup
  - WhatsApp
  - Discord
  - Webhook / local API

---

## Known Limitations to Investigate

- **SD card wear** — SD cards are slow and degrade with constant write activity. USB SSD is the better choice for a persistent service.
- **ARM binary compatibility** — some optional Go/Rust tools occasionally lack ARM builds.
- **WiFi instability** — Ethernet strongly preferred for a device running as a persistent service.
- **No local LLM** — OpenClaw docs explicitly advise against running local models on Pi hardware. Cloud API is the only practical path.

---

## Next Steps

### Research & Decision
- [ ] Read OpenClaw docs in full — understand the channel model, tool/action system, and how automations are defined 📅 2026-06-18
- [ ] Decide on hardware: Pi 4 (4GB) vs Pi 5 — check current availability and price 📅 2026-06-18
- [ ] Confirm Anthropic API key access for home use (separate from work/Belron) 📅 2026-06-18

### Setup (once hardware decided)
- [ ] Order Pi hardware + USB SSD + power supply
- [ ] Flash Raspberry Pi OS Lite 64-bit
- [ ] Follow OpenClaw install guide (docs.openclaw.ai/install/raspberry-pi)
- [ ] Configure Telegram as first channel
- [ ] Connect Claude Sonnet 4.6 via API key
- [ ] Test first automation

### First Use Cases to Try
- Personal task automations triggered via Telegram
- Morning briefing via message (simpler version of COG daily brief)
- Home network monitoring or status checks

---

## Resources

- [OpenClaw Raspberry Pi docs](https://docs.openclaw.ai/install/raspberry-pi)
- [Raspberry Pi news: Turn your Pi into an AI agent](https://www.raspberrypi.com/news/turn-your-raspberry-pi-into-an-ai-agent-with-openclaw/)
- [Adafruit install guide](https://learn.adafruit.com/openclaw-on-raspberry-pi/installing-openclaw)
- [Medium: Turning a Pi 4 into an AI Agent](https://pchojecki.medium.com/how-i-turned-a-raspberry-pi-4-into-an-ai-agent-with-openclaw-ba4f58d39f98)

---

## Notes

*Separated from Home Automation project 2026-06-11 — OpenClaw is distinct from the Home Assistant / unified home automation work.*

---

*Personal project. Created 2026-06-11.*
