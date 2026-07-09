# Andrej Karpathy quietly published 9 rules for building AI agents

![rw-book-cover](https://pbs.twimg.com/profile_images/2057949246687449088/pXfkWgZD.jpg)

## Metadata
- Author: [[Moysei]]
- Full Title: Andrej Karpathy quietly published 9 rules for building AI agents
- Category: #tweets
- Summary: Andrej Karpathy quietly published 9 rules for building AI agents. 

Rule 1: stop writing prompts.

"If you find yourself iterating on a single message at 3 in the morning, you are still in the prompting era."

A friend who runs agent infra at a trading firm read it once and deleted half the harness his team built last quarter.

The whole paper argues most agents die from a weak harness, not a weak model. Everything you added to compensate for the model becomes dead weight the moment the model improves.

The rule near the middle, about letting the loop delete its own work and start over, is the part he screenshotted. It contradicts how almost everyone builds right now.

The closing section on where the bottleneck goes next is the whole paper in one line.

He said he read it twice, second time with his own repo open beside it.

Everyone is still tuning prompts. Karpathy already moved on.
- URL: https://twitter.com/0xMoysei/status/2073892031240294726/?rw_tt_thread=True

## Full Document
**Andrej Karpathy quietly published 9 rules for building AI agents.** 

Rule 1: stop writing prompts.

"If you find yourself iterating on a single message at 3 in the morning, you are still in the prompting era."

A friend who runs agent infra at a trading firm read it once and deleted half the harness his team built last quarter.

The whole paper argues most agents die from a weak harness, not a weak model. Everything you added to compensate for the model becomes dead weight the moment the model improves.

The rule near the middle, about letting the loop delete its own work and start over, is the part he screenshotted. It contradicts how almost everyone builds right now.

The closing section on where the bottleneck goes next is the whole paper in one line.

He said he read it twice, second time with his own repo open beside it.

Everyone is still tuning prompts. Karpathy already moved on. 

![Image](https://pbs.twimg.com/media/HMfxzGzW8AAYNHh.jpg?name=orig)

![](https://pbs.twimg.com/profile_images/2057949246687449088/pXfkWgZD.jpg)

[Moysei](https://twitter.com/0xMoysei)
[@0xMoysei](https://twitter.com/0xMoysei)

![Master Claude With Fable 5: 6 Rules Straight From Anthropic's Docs](https://pbs.twimg.com/media/HMQU-RkX0AAkhMN.jpg)

**Same model, same plan. Prompts written for Opus cut its output quality. These 6 rules restore it.** 

Fable 5 went GA on June 9 at $10 per million input tokens and $50 per million output, with a 1M context window and a 128k output ceiling. Anthropic pulled it offline, then redeployed it on July 1 with updated cybersecurity safeguards. Until July 7 you can burn up to 50% of your weekly plan limits on it at no extra cost. After that, usage credits. 

#### Anthropic shipped a prompting guide with the model, and its sharpest warning targets your existing setup: skills built for prior models are "often too prescriptive for Claude Fable 5" and can degrade output quality. Your [CLAUDE.md](http://CLAUDE.md), your skills, your saved prompts all trained the model to act like Opus. The fix takes 6 rules.

#### 1. Give It the Why

![Image](https://pbs.twimg.com/media/HMQWpozXcAAoU1t.jpg) 

Fable 5 makes decisions on its own during long runs, and each decision improves when the model knows your intent. Anthropic's own template puts the goal before the request: 

Some content could not be imported from the original document. [View content ↗](https://twitter.com/0xMoysei/status/2073892031240294726/?rw_tt_thread=True) 

Compare "write an email to a client about the delay" against "I'm renegotiating a Q3 delivery date with a client who already escalated once; they need reassurance plus a concrete new date; with that in mind, write the email." The second version lets Fable pull the right files, match the right tone, and skip the questions a weaker prompt forces. 

#### If you run a second brain or an agentic OS, this rule compounds: the why tells Fable which context files to read before it writes a single word.

#### 2. Set Explicit Negatives

Fable 5 takes unrequested actions. Anthropic's guide names 2 real cases: drafting an email nobody asked for and creating defensive git-branch backups. The counter is a boundary block that separates assessment from action: 

Some content could not be imported from the original document. [View content ↗](https://twitter.com/0xMoysei/status/2073892031240294726/?rw_tt_thread=True) 

Anthropic's docs model this pattern throughout: pair each instruction with what the model should not do. Treat it like briefing a contractor with root access to your machine. The boundaries matter more than the task description.

---

#### 3. Match the Effort Dial

Effort is Fable's primary control for intelligence against speed and cost: low, medium, high, xhigh. Anthropic recommends high as the default, xhigh for capability-sensitive work, and medium or low for routine tasks. 

The number that changes your bill: low effort on Fable 5 often exceeds xhigh performance on prior models at a fraction of the price. Running Fable on xhigh for a changelog summary wastes the exact tokens you need for the hard problems. Reserve the top of the dial for tasks that used to take a person hours or days: large code migrations, multi-stage analysis, cross-document research. 

#### The same logic picks the model. If a task fits Sonnet, use Sonnet. Fable earns its price on work the other models fail at, and testing it on simple workloads undersells it.

#### 4. Stop Over-Planning, Let It Act

Individual requests on hard tasks can run for many minutes at higher effort settings while the model gathers context, builds, and self-verifies. Front-loading a separate research phase on top of that doubles your token spend for planning the model would do anyway. 

#### Replace "research everything and make a full plan before you do anything" with one line: "when you have enough information to act, act." Fable scopes the task, asks clarifying questions when the gap is real, and executes. Plan mode still earns its place on one job: drafting the spec with a cheaper model. Run deep research on Opus 4.8, turn the output into a PRD, then hand the finished prompt to Fable for the long autonomous run. Opus does the grunt work, Fable does the build, your 50% cap survives the week.

#### 5. Make It Prove It

Models report done before done. On long agentic runs the failure mode gets expensive: a plausible status update with zero tool results behind it. Anthropic's guide includes a verification block, and in their testing it nearly eliminated fabricated status reports on tasks designed to elicit them: 

Some content could not be imported from the original document. [View content ↗](https://twitter.com/0xMoysei/status/2073892031240294726/?rw_tt_thread=True) 

#### Bake this into your skills, agents, and [CLAUDE.md](http://CLAUDE.md) rather than pasting it at the end of every prompt. A verification loop you write once beats a check you remember 6 times out of 10.

#### 6. Never Ask for Raw Reasoning

![Image](https://pbs.twimg.com/media/HMQWwHpWIAAxPVG.jpg) 

Fable 5 runs safety classifiers targeting 3 categories: offensive cybersecurity techniques, biology and life sciences methods, and extraction of the model's own thinking. A standing "explain your reasoning" line in a system prompt lands in category 3. It can trigger the reasoning\_extraction refusal, and raw chain of thought is never returned on Fable 5, period. 

#### When a classifier fires, the session reroutes to Opus 4.8 with a notification. Anthropic puts the rate around 5% of sessions. The reroute sticks: /model fable takes you back, but if the trigger stays in your context, the next request bounces you again. Audit your system prompts and [CLAUDE.md](http://CLAUDE.md) for reasoning-echo instructions and replace them with the summarized thinking display setting. You keep visibility into the model's process without tripping the classifier.

#### 7. Delete Before You Add

The guide's through-line is subtraction. Instructions that compensated for weak planning in older models now cap Fable's quality: hardcoded process steps, exhaustive formatting rules, defensive repetition. Anthropic's Alex Albert put the migration advice in 3 moves: default to high or xhigh effort, rewrite old [CLAUDE.md](http://CLAUDE.md) instructions, and let the model use more judgment. 

Fable audits its own setup better than you will. Point it at your session history: 

Some content could not be imported from the original document. [View content ↗](https://twitter.com/0xMoysei/status/2073892031240294726/?rw_tt_thread=True) 

#### One run of this across 39 sessions returns a ranked batch list: skills to create, skills to promote into automations, and stale lines in your [CLAUDE.md](http://CLAUDE.md) that steer the model wrong.

#### 8. Where to Point It Before July 7

The 50% cap rewards big swings over small queries. Three targets that justify the spend: 

* **Code review at scale.** Point Fable at your largest repo with one line: full code review, report bugs. Expect parallel reviewers, deduplicated findings ranked by severity, and a fix priority list in minutes.
* **Clone the software you pay for.** Research the target app with Opus 4.8, write the PRD, hand Fable a long-run goal prompt. One public project of this shape produced a browser game on three.js from a partially human-written PRD: 21,000 lines of TypeScript across 90+ commits.
* **Rebuild your own workflow.** Run the setup audit from rule 7, then let Fable write the [SKILL.md](http://SKILL.md) files and automations it recommended. The model that exposes the gaps closes them in the same session.

#### The model got smarter. Your prompts have to get shorter.

Thanks for reading this far. The decision left on the table is small: save this guide, run rule 7 on your own setup today, and follow for the next breakdown. The promo window closes July 7. Your move. 

[Posted Jul 2, 2026 at 10:24PM](https://twitter.com/0xMoysei/status/2072808742274392194)
