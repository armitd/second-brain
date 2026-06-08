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

1. **Sonos** — easiest, local, start here
2. **Philips Hue** — native integration, quick win
3. **IKEA Tradfri** — Zigbee, straightforward
4. **Google Home / Nest Doorbell** — bidirectional voice + doorbell triggers
5. **Alexa** — bidirectional voice
6. **LightwaveRF** — most complex, cloud-dependent, tackle last

---

## Notes

*Started from braindump 8 June 2026. First captured as "something like OpenClaw on a Raspi."*

---

*Personal project. Created 8 June 2026.*
