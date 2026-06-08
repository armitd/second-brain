---
type: "project"
title: "Home Automation"
status: "planning"
created: "2026-06-08"
tags: ["#project", "#personal", "#home-automation", "#raspberry-pi"]
---

# Home Automation

## Vision

Unify all home automation networks into a single platform running on a Raspberry Pi — one dashboard, one automation engine, all devices.

**Primary use case:** Make IKEA Tradfri switches control devices across all ecosystems (not just IKEA bulbs), and simplify overall control so you're not managing seven separate apps.

---

## The Core Problem

IKEA Tradfri switches currently only control IKEA bulbs — they're siloed inside the IKEA ecosystem. The goal is to use them as universal physical controls that can trigger automations across Hue, LightwaveRF, Sonos, and everything else.

**How Home Assistant solves this:**
With a Zigbee USB dongle on the Raspi, HA intercepts every Tradfri button press as an event and can trigger *any* automation — turn on Hue lights, start a Sonos playlist, trigger a LightwaveRF scene, whatever. The IKEA switch becomes a universal remote for the whole house.

**Simplifying control:** One HA dashboard replaces seven apps. Voice control (Alexa + Google Home) still works as before, but physical switches and automations now all route through HA.

## Platform

**Home Assistant** on Raspberry Pi (4 or 5) — self-hosted, local-first, no cloud dependency.

---

## Current Device Ecosystem

| System | Hub | Protocol | HA Integration |
|--------|-----|----------|----------------|
| **Philips Hue** | Hue Bridge | Zigbee | Native — excellent |
| **Google Home Hub** | Google Home | Google/Cast | Bidirectional |
| **Nest Doorbell** | Google Home | Google/Nest | Available |
| **LightwaveRF** | LightwaveRF hub | Proprietary (UK) | Community — cloud-dependent ⚠️ |
| **Alexa** | Echo device(s) | Amazon | Bidirectional |
| **Sonos** | Sonos app | Local network | Native — excellent |
| **IKEA Home Smart** | Tradfri hub | Zigbee | Native (via hub or direct with Zigbee dongle) |

**Note:** Hue and IKEA Tradfri both use Zigbee — a Sonoff Zigbee 3.0 USB dongle (~£15) lets Home Assistant control both directly without their hubs.

---

## Hardware Needed

- [ ] Raspberry Pi 4 or 5 (4GB+ RAM recommended for HA)
- [ ] MicroSD card (32GB+) or USB SSD for reliability
- [ ] Power supply
- [ ] Optional: Sonoff Zigbee 3.0 USB dongle (for direct Zigbee control of Hue + IKEA)

---

## Next Steps

### Research & Planning
- [ ] Verify platform — confirm Home Assistant is the right choice (check OpenClaw if it exists) 📅 2026-06-15
- [ ] Check current state of LightwaveRF HA integration — community maintained, cloud-dependent 📅 2026-06-15
- [ ] Identify the first cross-network automation to build (the "proof it works" moment) 📅 2026-06-15

### Setup
- [ ] Order Raspberry Pi hardware if not already owned 📅 2026-06-22
- [ ] Install Home Assistant OS on Raspi
- [ ] Connect and configure each integration one by one
- [ ] Build first automation across two previously siloed systems

---

## Integration Priority Order

1. **IKEA Tradfri + Zigbee dongle** — highest priority; this is the core use case. Get switches controlling everything.
2. **Philips Hue** — first target for IKEA switch cross-control; native HA integration
3. **Sonos** — easy win; local, excellent HA support
4. **LightwaveRF** — next target for switch control; check integration state first ⚠️
5. **Google Home / Nest Doorbell** — doorbell trigger automations
6. **Alexa** — bidirectional voice (keep working alongside physical switches)

## First Automation to Build

IKEA Tradfri switch → turns on Philips Hue lights in the same room. Once that works, the pattern extends to every other device.

---

## Notes

*Started from braindump 8 June 2026. First captured as "something like OpenClaw on a Raspi."*

---

*Personal project. Created 8 June 2026.*
