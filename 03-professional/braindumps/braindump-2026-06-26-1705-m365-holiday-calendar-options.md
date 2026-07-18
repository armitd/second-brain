---
type: "braindump"
domain: "professional"
date: "2026-06-24"
created: "2026-06-26 17:05"
source: "daybook"
source_file: "01-daily/daybooks/daybook-2026-06-24.md"
themes: ["m365", "calendar-management", "team-operations", "outlook", "microsoft-teams"]
tags: ["#braindump", "#from-daybook", "#professional", "#m365", "#it-guidance"]
status: "consolidated"
energy_level: "medium"
emotional_tone: "pragmatic"
confidence: "high"
consolidated_in: "[[consolidation-2026-07-18]]"
consolidated_date: "2026-07-18"
---

# Braindump: M365 Holiday Calendar Options for Belron Teams

## Raw Thoughts

**How to handle Holidays in M365**

There are a few good options within Microsoft 365, ranging from native features to lightweight add-ins. Here's a practical breakdown:

Best native M365 option: Microsoft 365 Group Calendar

A Group Calendar is associated with a Microsoft 365 Group or Microsoft Teams. All group members automatically have access to it, so you don't need to share it user by user. Each person posts their own holiday entries directly to the shared group calendar, and everyone sees them. No invites needed. This is the lowest-friction approach if your team already uses Teams or a shared M365 Group.

How to set it up: In Outlook, navigate to your team's Group, open its calendar, and each person adds their holidays there directly. It also appears as a tab within your Teams channel.

Step up: SharePoint or a Shared Mailbox Calendar

A dedicated Exchange Online Shared Mailbox acts as a central calendar. Everyone sees the same events in Outlook while admins (or designated team members) control updates. This suits teams that want one authoritative calendar rather than each person self-managing entries.

If you want more structure: a Teams App

If you also need approval workflows, leave balance tracking, or visibility across multiple teams, a lightweight Teams app may be worth it. Purpose-built leave management solutions like Time Off Manager 365 work natively within Outlook and Teams, offering automated approval workflows, Outlook calendar sync, and Teams compatibility with no switching between apps.

My recommendation for most Belron teams:

Start with the M365 Group Calendar. It requires no admin setup, no new tools, and solves the "sending invites to everyone" problem immediately. Each person simply adds their holiday to the shared group calendar rather than their personal one. If you later need approval flows or allowance tracking, a Teams app is the natural next step.

When creating the event:

1. Open Outlook Calendar and create a new event as normal for your personal calendar
2. Before saving, look for the Calendar dropdown at the top of the event form
3. You can only save to one calendar at a time from this field, so the cleanest method is the two-step approach below

The practical two-step approach:

1. Create the event on your personal calendar as usual (so your own out-of-office, free/busy status, etc. work correctly)
2. Then open the Group Calendar, create a second entry for the same dates with your name in the title (e.g. "John - Annual Leave")

Or use "Copy to my calendar" in reverse: Some teams find it easier to create the entry on the Group Calendar first, then copy it to their personal calendar using right-click > Copy to folder.

A few practical tips for the Group Calendar entries:

- Keep a consistent naming convention: "Name - Holiday" makes it scannable at a glance
- Mark them as All Day events and set show-as to Free on the group calendar (so it doesn't clutter others' free/busy)
- On your personal entry, set show-as to Out of Office so meeting scheduling works correctly for you

The slight duplication is a minor overhead, but it's far less unwieldy than sending invites to every team member.

---

## Content Analysis

### Main Themes
1. **M365 Group Calendar as the recommended baseline:** Zero admin setup, solves the "sending invites to everyone" antipattern, works within existing Teams/M365 Group structure.
2. **The two-calendar problem:** M365 doesn't let you save a single event to two calendars simultaneously — the two-step workaround (personal + group) is the practical resolution.
3. **Escalation ladder:** Group Calendar → Shared Mailbox Calendar → Teams app (when approval workflows or leave balance tracking are needed). Each step adds structure and admin overhead.

### Supporting Ideas
- "Show as Free" on the group calendar + "Out of Office" on personal calendar is the correct configuration split
- Consistent naming convention ("Name - Holiday") is essential for scannability
- Time Off Manager 365 named as the lightweight Teams app reference if the team outgrows self-managed entries
- This reads as advice written in response to a team question — likely shared with colleagues

### Questions Raised
- Which teams within Belron are currently using which approach?
- Is there a Belron-standard for holiday visibility, or is it inconsistent across opcos and functions?
- Has anyone evaluated Time Off Manager 365 or similar for the Belron context?

### Decisions Contemplated
- Whether to recommend the native M365 Group Calendar or jump straight to a Teams app with approval flows — recommendation lands on start simple, escalate if needed

---

## Strategic Intelligence

### Key Insights
1. **This is reference knowledge, not strategic thinking:** The content is a well-structured practical guide, likely written to help a colleague or team. Value is in having it filed as a reusable reference.
2. **The "two-calendar problem" is a genuine M365 limitation:** Worth knowing for any IT or ops conversation about M365 adoption — teams often try to solve this with shared invites (wrong) rather than group calendars (right).
3. **Escalation path is clear:** Group Calendar → Shared Mailbox → Teams app is a sound decision ladder that applies broadly across Belron opcos.

### Pattern Recognition
- **Recurring pattern:** Armo frequently writes advisory notes in response to operational questions. These are valuable to file — they represent reusable institutional knowledge that would otherwise be buried in email/Teams threads.

### Strategic Implications
- Low strategic weight — this is operational guidance, not architecture or project-level thinking
- Could be packaged into an internal M365 tip/guidance doc if similar questions keep surfacing

---

## Action Items

### Immediate (24–48 hours)
- None identified

### Short-term (1–2 weeks)
- [ ] If this question recurs, consider sharing as a short Teams post or pinned message in the relevant channel 📅 2026-07-10

### Strategic Considerations
- If Belron lacks a consistent holiday visibility standard across opcos, this is a quick win for IT/workplace ops to standardise

---

## Connections
- **Source:** [[daybook-2026-06-24]]
- **Related topics:** M365 administration, Belron IT standards, workplace operations

## Domain Classification
- **Primary Domain:** Professional (85%)
- **Reasoning:** Operational IT guidance written in a Belron context — not personal, not tied to a specific active project
- **Privacy Level:** public

---
*Processed by COG from daybook — 2026-06-26 17:05*
