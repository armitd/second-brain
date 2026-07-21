---
type: "braindump"
domain: "personal"
date: "2026-07-21"
created: "2026-07-21 08:05"
themes: ["fitness-data", "exercise-tracking", "strava", "apple-health", "smart-ring", "personal-knowledge"]
tags: ["#braindump", "#raw-thoughts", "#personal", "#wellness", "#fitness"]
status: "captured"
energy_level: "medium"
emotional_tone: "curious"
confidence: "high"
---

# Braindump: Where to Bring Exercise Data Together

## Raw Thoughts
What is the best way to capture exercise info. Most stuff happens through Strava, some through Apple Health, some isn't recorded. I'm wondering where I bring all that together — especially if I get a smart ring.

## The key realisation: there are TWO layers, don't conflate them

1. **The quantified layer** — the raw metrics and time-series: distances, pace, heart rate, HRV, sleep, recovery. This is high-volume numeric data. **COG's markdown vault is the wrong place for this.** It belongs in a health-data aggregator.
2. **The reflective / synthesis layer** — how training is going, how you felt, unrecorded sessions, goals, patterns over weeks and months. **This is exactly what COG is good at**, and what no tracker does well.

Trying to make COG hold every workout's numbers would be fighting the tool. The right model is: **aggregator holds the data, COG holds the meaning.**

## Layer 1 — pick one metrics hub: Apple Health

On iPhone, **Apple Health is the natural aggregator** and almost certainly your answer:
- **Strava can write activities to Apple Health** (enable in Strava's settings) — so runs/rides land there automatically.
- **Apple Watch** (if you have one) writes workouts, HR, etc. directly.
- **A smart ring** — most ring apps (Oura/Ultrahuman/RingConn) can write sleep/HRV/recovery to Apple Health, though *which* metrics sync varies by brand. If you buy a ring, **pick one that syncs well to Apple Health** so the hub stays complete (a point for the ring shortlist in [[braindump-2026-07-20-1542-fitness-trackers-ultrahuman]]).
- **Unrecorded sessions** — Apple Health lets you add workouts manually, or you log them in COG (see below).

So: Strava + Watch + Ring + manual → **Apple Health as the single system of record for numbers.**

> Caveat: some ring metrics stay locked in the ring's own app and don't fully export to Apple Health. Accept that the ring app may remain a second home for its deepest metrics, with the headline numbers flowing to Health.

## Layer 2 — COG holds what the trackers can't

COG's job is the narrative and synthesis, not the raw data:
- **A training/exercise log** — a maintained note (same pattern as Reading List / Places to Visit) or dated entries: what you did, how it felt, niggles, the sessions no app recorded (a walk, a kickabout, a gym session you forgot to start).
- **Weekly summaries** — pull the handful of numbers that matter (weekly distance, sessions, average recovery) from Strava/Apple Health into a weekly note, plus a line of reflection. This is where COG adds value the apps don't: joining the dots over time.
- **Goals & patterns** — a note tracking fitness goals and what the data is actually telling you (e.g. "recovery drops when I train 3 days back-to-back").

## The bridge — how data gets from the hub into COG

- **Start manual:** a weekly `/braindump` (or a line in the exercise log) summarising the week. Low effort, high value, no engineering.
- **Automate later (optional):** an **Apple Shortcut** can read specific Apple Health metrics and write a weekly summary into an iCloud vault folder — the same drop-folder-then-process pattern we built for Day One. This keeps COG's role as *summaries*, not raw dumps.
- **Strava API:** exists if you ever want richer auto-pull, but it's engineering; the Shortcut route is lighter and probably enough.

### Questions Raised
- Do you have an Apple Watch, or is the phone the only Apple Health source right now? (Changes how much lands in Health automatically.)
- Is Strava already set to write to Apple Health? (Quick toggle; makes Health the true hub.)
- What do you actually want out of it — a **record** (looking back), **motivation** (streaks/goals), or **insight** (what affects performance/recovery)? That decides how much COG structure is worth building.
- If a ring is coming, which one — and does it sync cleanly to Apple Health? (Ties to the ring shortlist.)

### Decisions Contemplated
- Apple Health as the metrics hub (leaning: yes, it's the obvious iOS aggregator).
- Whether COG gets a dedicated **EXERCISE-LOG.md** maintained list, or dated braindumps, or both.
- Manual weekly summary now vs an Apple Shortcut automation later.

## Strategic Intelligence

### Key Insights
1. **Aggregator holds the data; COG holds the meaning.** The whole problem dissolves once you stop trying to make one tool do both. Apple Health = numbers, COG = narrative + synthesis.
2. **"Unrecorded" is the gap only COG can fill.** Apps capture what you tracked; they can't capture the walk you didn't start a timer for, or how a session felt. A COG log is where the untracked and the qualitative live.
3. **A smart ring changes the mix, not the model.** It adds a *recovery/sleep* dimension to sit alongside *training load* — which is exactly the kind of cross-signal a COG weekly summary can join up ("trained hard, recovery tanked"). Choose a ring that feeds Apple Health so the hub stays whole.

### Pattern Recognition
- **Part of a clear personal-health thread this week:** fitness trackers ([[braindump-2026-07-20-1542-fitness-trackers-ultrahuman]]), mindfulness ([[braindump-2026-07-20-1050-meditation-enjoy-the-moment]]), and the treadmill setup in [[04-projects/garden-renovation/PROJECT-OVERVIEW]].
- **Same two-layer lesson as the vault itself:** raw sources live outside (Readwise, Apple Health); COG is the compiled, reflective layer on top. This is the LLM-wiki pattern applied to health data.
- **Echoes the mindful-consumption note:** use the data as *information*, not another "always optimising / what's next" anticipation loop. A weekly summary encourages reflection over obsessive checking.

### Strategic Implications
- Low cost to start (a weekly note), scalable later (a Shortcut) — no need to decide the automation now.
- The ring purchase decision and this data-architecture decision are linked: buy the ring that keeps Apple Health complete.

## Action Items

### Immediate (24-48 hours)
- [ ] **Connect Strava to Apple Health** — in Strava: Settings → Applications, Services and Devices → Health → allow Strava to write workout data to Apple Health (makes Apple Health the complete hub) 📅 2026-07-22

### Short-term (1-2 weeks)
- [x] Decide COG's structure and create `02-personal/EXERCISE-LOG.md` ✅ 2026-07-21 → [[EXERCISE-LOG]]
- [ ] Try one **weekly summary** (this week's sessions + how it felt) to test whether the reflective layer is worth keeping

### Strategic Considerations
- If a ring is on the cards, add "syncs to Apple Health" to the buying criteria.
- Only build the Apple Shortcut automation once the manual weekly habit has proven it's worth it — don't automate a habit you haven't validated.

## Connections
- **Related Braindumps:** [[braindump-2026-07-20-1542-fitness-trackers-ultrahuman]] (smart rings), [[braindump-2026-07-20-1050-meditation-enjoy-the-moment]] (data as information, not anticipation)
- **Related Project:** [[04-projects/garden-renovation/PROJECT-OVERVIEW]] (treadmill setup)
- **Knowledge Base:** [[llm-wiki-knowledge-infrastructure-framework]] (raw data outside, COG as the reflective layer)
- **Skills:** `/weekly-checkin`, `/plan-week` (natural homes for a weekly fitness summary)

## Domain Classification
- **Primary Domain:** Personal (100%)
- **Reasoning:** Personal fitness data management; no professional/project overlap (though the architecture mirrors COG's raw-vs-compiled pattern).
- **Privacy Level:** private

## Processing Notes
### Emotional Context
- **Energy Level:** Medium — practical, systems-thinking mode.
- **Emotional Tone:** Curious / organising.

### Confidence Assessment
- **Overall Analysis:** 90% — the two-layer model and Apple Health as hub are sound for an iOS user.
- **Areas Requiring Clarification:** whether you have an Apple Watch, and which ring (if any) — both affect how much auto-flows into Apple Health. Ring-to-Apple-Health sync specifics vary by brand and should be verified per device.

---

*Processed by COG Brain Dump Analyst*
