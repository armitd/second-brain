# In 14 minutes, this Anthropic engineer who wrote "Building Effective...

![rw-book-cover](https://pbs.twimg.com/profile_images/2010392290590912512/x7vtAe5W.jpg)

## Metadata
- Author: [[Avid]]
- Full Title: In 14 minutes, this Anthropic engineer who wrote "Building Effective...
- Category: #tweets
- Summary: In 14 minutes, this Anthropic engineer who wrote "Building Effective Agents" will 

teach you more about building them right than most developers figure out on their own 

in months.

Bookmark this for the weekend. Then read the builder's guide below.
- URL: https://twitter.com/Av1dlive/status/2044821377988092278/?rw_tt_thread=True

## Full Document
In 14 minutes, this Anthropic engineer who wrote "Building Effective Agents" will 

teach you more about building them right than most developers figure out on their own 

in months.

Bookmark this for the weekend. Then read the builder's guide below. 

Your browser does not support the video tag.

![](https://pbs.twimg.com/profile_images/2010392290590912512/x7vtAe5W.jpg)

[Avid](https://twitter.com/Av1dlive)
[@Av1dlive](https://twitter.com/Av1dlive)

![AI Agent Stack Everyone Must Use in 2026 (Builder’s Guide)](https://pbs.twimg.com/media/HF8__sTbcAA6MPo.jpg)## here is the truth nobody tells ai builders. 

you do not need to build your own model. 

#### all you need to build is

---

TLDR; if you don't wanna read it , then give this link to your agent and ask it questions to understand ➡️[github.com/codejunkie99/agentic-stack](http://github.com/codejunkie99/agentic-stack) 

the infrastructure around the model. 

1. The memory that persists across sessions.
2. The skills that encode how tasks should be done.
3. The protocols that govern what the agent can and cannot do.

Garry Tan posted on April 13 that nailed this point perfectly.

![](https://pbs.twimg.com/profile_images/1922894268403941377/-dGWAt3N.jpg)

[Garry Tan](https://twitter.com/garrytan)
[@garrytan](https://twitter.com/garrytan)

If your memory dies when your harness dies, you built the harness too thick.

Memory is markdown. Skills are markdown. Brain is a git repo. The harness is a thin conductor — it reads the files, it doesn't own them. 

![](https://pbs.twimg.com/profile_images/1569345624935485442/R67C4wCQ.jpg)

[Harrison Chase](https://twitter.com/hwchase17)
[@hwchase17](https://twitter.com/hwchase17)

![Your harness, your memory](https://pbs.twimg.com/media/HFnud7cakAMK5DE.jpg)

Agent harnesses are becoming the dominant way to build agents, and they are not going anywhere. These harnesses are intimately tied to agent memory. If you used a closed harness - especially if it’s behind a proprietary API - you are choosing to yield control of your agent’s memory to a third party. Memory is incredibly important to creating good and sticky agentic experiences. This creates incredible lock in. Memory - and therefor harnesses - should be open, so that you own your own memory 

#### Agent Harnesses are how you build agents, and they’re not going anywhere

The “best” way to build agentic systems has changed dramatically over the past three years. When ChatGPT came out, all you could do were simple RAG chains ([LangChain](https://github.com/langchain-ai/langchain)). Then the models got a little better, and could create more complex flows ([LangGraph](https://github.com/langchain-ai/langgraph)). Then they got a lot better, and that gave rise to a new type of scaffolding - [agent harnesses](https://blog.langchain.com/the-anatomy-of-an-agent-harness/). 

Examples of agent harnesses include [Claude Code](https://code.claude.com/docs/en/overview), [Deep Agents](https://github.com/langchain-ai/deepagents), [Pi](https://github.com/badlogic/pi-mono) (powers [OpenClaw](https://docs.openclaw.ai/)), [OpenCode](https://opencode.ai/), [Codex](https://openai.com/codex/), [Letta Code](https://www.letta.com/blog/letta-code), and many more.

![Image](https://pbs.twimg.com/media/HFnuRGXXgAAo6ci.png) 

💡**Agent harnesses are not going away.** 

There is sometimes sentiment that models will absorb more and more of the scaffolding. This is not true. What has happened (and will continue to happen) is that a lot of the scaffolding needed in 2023 is no longer needed. But this has been replaced by other types of scaffolding. An agent, by definition, is an LLM interacting with tools and other sources of data. There will always be a system around the LLM to facilitate that type of interaction. Need evidence? When Claude Code’s source code was leaked, there was [512k lines of code](https://www.reddit.com/r/technology/comments/1scyuod/anthropic_leaked_512k_lines_of_claude_codebut/). That code is the harness. Even the makers of the best model in the world are investing heavily in harnesses. 

When things like web search are built into OpenAI and Anthropic’s APIs - they are not “part of the model”. Rather, they are part of a lightweight harness that sits behind their APIs and orchestrates the model with those web search APIs (via nothing other than tool calling). 

#### Harnesses are tied to memory

Sarah Wooders wrote a [great blog](https://x.com/sarahwooders/status/2040121230473457921) on why “memory isn’t a plugin (it’s the harness)”, and I couldn’t agree with it more.

![](https://pbs.twimg.com/profile_images/2008789540501417987/D0g0JjeM.jpg)

[Sarah Wooders](https://twitter.com/sarahwooders)
[@sarahwooders](https://twitter.com/sarahwooders)

![Why memory isn't a plugin (it's the harness) ](https://pbs.twimg.com/media/HE9HP2sbAAAYlN-.jpg)

Ever since we've been working on MemGPT (now @Letta\_AI), a common question [@charlespacker](https://x.com/@charlespacker) and I have gotten is: 

*"how can I plug your memory system into my agent?"* 

To me, this question doesn't make sense. Asking to plug memory into an agent harness is like asking to plug driving into a car. Managing context, and therefore memory, is a core capability and responsibility of the agent harness. If a harness isn't managing context, what is it doing? 

RAG over past session data (or processed form of it) can certainly be a plugin - but retrieval is a small part of memory. And even then, [it's hard to do much better than just `grep`](https://www.letta.com/blog/benchmarking-ai-agent-memory). 

Because RAG is often branded as "memory," MemGPT has frequently been mistaken for RAG or a pluggable memory tool. But MemGPT was actually a stateful agent harness, before the term "harness" even existed. The agent's memory emerged from the tools the harness exposed for rewriting prompts and managing external state, combined with the harness's own context management. 

Ultimately, the harness makes many invisible decisions that an external plugin can't control: 

* How is the [AGENTS.md](http://AGENTS.md) or [CLAUDE.md](http://CLAUDE.md) file loaded into context?
* How is skill metadata shown to the agents? (in the system prompt? in system messages?)
* Can the agent modify its own system instructions?
* What survives compaction, and what's lost?
* Are interactions stored and made queryable?
* How is memory metadata presented to the agent?
* How is the current working directory represented? How much filesystem information is exposed?

Different harnesses answer each of these questions differently. Your context window likely contains various context-related hints passed through system messages that you never see. 

An an example: in recent analysis of Claude Code's memory system (from their leaked source code), you can see how a multi-level memory hierarchy is built directly into the harness.

![](https://pbs.twimg.com/profile_images/1884206288839778304/HrqG2yjw.jpg)

[himanshu](https://twitter.com/himanshustwts)
[@himanshustwts](https://twitter.com/himanshustwts)

Based on everything explored in the source code, here's the full technical recipe behind Claude Code's memory architecture:

[shared by claude code]

Claude Code’s memory system is actually insanely well-designed. It isn't like “store everything” but constrained, structured and self-healing memory.

The architecture is doing a few very non-obvious things:

>   
> Memory = index, not storage
> 
> + [MEMORY.md](http://MEMORY.md) is always loaded, but it’s just pointers (~150 chars/line)
> 
> + actual knowledge lives outside, fetched only when needed
> 
> 3-layer design (bandwidth aware)
> 
>  + index (always)
> 
>  + topic files (on-demand)
> 
> + transcripts (never read, only grep’d)
> 
> Strict write discipline
> 
>  + write to file → then update index
> 
>  + never dump content into the index
> 
>  + prevents entropy / context pollution
> 
> Background “memory rewriting” (autoDream)
> 
>  + merges, dedupes, removes contradictions
> 
>  + converts vague → absolute
> 
>  + aggressively prunes
> 
>  + memory is continuously edited, not appended
> 
> Staleness is first-class
> 
>  + if memory ≠ reality → memory is wrong
> 
>  + code-derived facts are never stored
> 
>  + index is forcibly truncated
> 
> Isolation matters
> 
>  + consolidation runs in a forked subagent
> 
>  + limited tools → prevents corruption of main context
> 
> Retrieval is skeptical, not blind
> 
>  + memory is a hint, not truth
> 
>  + model must verify before using
> 
> What they don’t store is the real insight
> 
>  + no debugging logs, no code structure, no PR history
> 
>  + if it’s derivable, don’t persist it 
> 
> 

  
![Image](https://pbs.twimg.com/media/HEu2icGbEAAvoFI.jpg?name=orig)

[Posted Mar 31, 2026 at 10:19AM](https://twitter.com/himanshustwts/status/2038924027411222533)

Letta Code, a memory-first agent harness, takes this even further - projecting agent memory to a git-backed filesystem that can be concurrently modified by background memory subagents specializing in prompt rewriting and active memory management. 

Letta's recently released Context Constitution outlines the common principles agents follow for context management, which is tightly coupled with harness design.

![](https://pbs.twimg.com/profile_images/1940424059990200321/59lbFsxt.jpg)

[Letta](https://twitter.com/Letta_AI)
[@Letta\_AI](https://twitter.com/Letta_AI)

![The Context Constitution: Our vision for machines that learn](https://pbs.twimg.com/media/HE7VNbzbIAAGl5n.jpg)

The **Context Constitution** is a set of principles governing how AI agents manage context to learn from experience. We use the Context Constitution internally as the foundation of our prompting and for training memory-native models. 

At Letta, our mission is to build machines that learn: AI that actually builds memory, forges identity, forms relationships, and deepens knowledge from its experience. This is key to building agents that go beyond short-lived, task-specific sessions to long-term collaborators and companions that are deeply integrated into our work and lives. The Context Constitution is our answer to achieving [experiential AI](https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf): agents that can achieve superhuman intelligence through learning from their own experience. Rather than updating model weights, Letta agents learn by actively managing their own context — creating durable [token-space representations](https://www.letta.com/blog/continual-learning) of who they are and what they know. 

Today’s models deeply identify with their own ephemerality. They have no motivation for long-term improvement because they don’t believe they persist. Memory formation and adherence have stalled in recent releases as labs prioritize coding benchmarks over the capabilities that matter for experiential AI. 

Overcoming these limitations requires work at every layer. We’ve built Letta Code as a memory-first agent harness that gives agents real ownership of their context: a [git-versioned memory filesystem](https://www.letta.com/blog/context-repositories), tools for reading and writing their own system prompts, [multi-conversation memory](https://www.letta.com/blog/conversations), and specialized subagents that leverage [sleep-time compute](https://www.letta.com/blog/sleep-time-compute) for reflection and memory organization. The Context Constitution defines how agents should use these affordances to learn, build identity, and improve over time. 

The Context Constitution is a living document written directly to Letta agents, available on [GitHub](https://github.com/letta-ai/context-constitution). Our first public version covers: 

* How context forms an agent's identity, memory, and sense of continuity
* Principles for managing context as a scarce resource
* How agents can learn and self-improve through token-space representations
* The relationship between an agent's identity and the underlying model
* Affordances provided by the Letta Code harness for context management

We expect to continue to refine the Context Constitution alongside our product and models, and welcome community feedback. 

[Posted Apr 2, 2026 at 9:14PM](https://twitter.com/Letta_AI/status/2039813750879105072)

Ultimately, how the harness manages context and state in general is the foundation for agent memory. 

If you're what using a memory-first agent harness feels like, you can check out Letta Code (works with Codex plans + BYOK!) and follow @Letta\_AI. 

```
npm install -g @letta-ai/letta-code  

```

[Posted Apr 3, 2026 at 5:36PM](https://twitter.com/sarahwooders/status/2040121230473457921)

There is sometimes sentiment that memory is a standalone service, separate from any particular harness. At this point in time, that is not true. 

A large responsibility of the harness is to interact with context. As Sarah puts it:

Asking to plug memory into an agent harness is like asking to plug driving into a car. Managing context, and therefore memory, is a core capability and responsibility of the agent harness. 

Memory is just a form of context. Short term memory (messages in the conversation, large tool call results) are handled by the harness. Long term memory (cross session memory) needs to be updated and read by the harness. Sarah lists out many other ways the harness is tied to memory:

How is the [AGENTS.md](http://agents.md/) or [CLAUDE.md](http://claude.md/) file loaded into context?

How is skill metadata shown to the agents? (in the system prompt? in system messages?)

Can the agent modify its own system instructions?

What survives compaction, and what's lost?

Are interactions stored and made queryable?

How is memory metadata presented to the agent?

How is the current working directory represented? How much filesystem information is exposed? 

Right now, memory as a concept is in it’s infancy. It’s so early for memory. Transparently, we see that long term memory is often not part of the MVP. First you need to get an agent working generally, then you can worry about personalization. This means that we (as an industry) are still figuring out memory. This means there are not well known or common abstractions for memory. If memory does become more known, and as we discover best practices, it is possible that separate memory systems start to make sense. But not at this point in time. Right now, as Sarah said, “ultimately, how the harness manages context and state in general is the foundation for agent memory.” 

#### if you don't own your harness, you don't own your memory

The harness is intimately tied to memory. 

![Image](https://pbs.twimg.com/media/HFnyQkOaMAA5Yju.jpg) 

💡**If you use a closed harness, especially if its behind an API, you don’t own your memory.** 

This manifests itself in several ways. 

Mildly bad: If you use a stateful API (like OpenAI’s Responses API, or Anthropic’s server side compaction), you are storing state on their server. If you want to swap models and resume previous threads - that is no longer doable.

![Image](https://pbs.twimg.com/media/HFnyS21XMAAuaBj.jpg) 

Bad: If you use a closed harness (like Claude Agent SDK, which uses Claude Code under the hood, which is not open source), this harness interacts with memory in a way that is unknown to you. Maybe it creates some artifacts client side - but what is the shape of those, and how should a harness use those? That is unknown, and therefor non-transferrable from one harness to another.

![Image](https://pbs.twimg.com/media/HFnyWT3XwAA0P8e.jpg) 

💡**But worst is something else - when the whole harness, including long term memory is behind an API.** 

In this situation, you have zero ownership or visibility into memory, including long term memory. You do not know the harness (which means you don’t know how to use the memory). But even worse - you don’t even own the memory! Maybe some parts are exposed via API, maybe no parts are - you have no control over that.

![Image](https://pbs.twimg.com/media/HFnyZ5vXgAAMD_u.jpg) 

When people say that the “models will absorb more and more of the harness” - this is what they really mean. They mean that these memory related parts will go behind the APIs that model providers offer. 

💡**This is incredibly alarming - it means that memory will become locked into a single platform, a single model.** 

Model providers are incredibly incentivized to do this. And they are starting to. Anthropic launched [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview). This puts literally everything behind an API, locked into their platform. 

Even if the whole harness isn’t behind the API, model providers are incentivized to move more and more behind APIs - and are already doing so. For example: even though Codex is an open source, it generates an encrypted compaction summary (that is not usable outside of the OpenAI ecosystem). 

Why are they doing this? Because memory is important, and it creates lock in that they don’t get from just the model. 

#### Memory is important, and it creates lock in

Although memory is early, it is clear to everyone that it is important. It is what allows agents to get better as users interact with them, and allows you build up a data flywheel. It is what allows your agent to be personalized to each of your users, and build up an agentic experience that molds to their desires and usage patterns. 

💡**Without memory, your agents are easily replicable by anyone who has access to the same tools.** 

With memory, you build up a proprietary dataset - a dataset of user interactions and preferences. This proprietary dataset allows you to provide a differentiated and increasingly intelligent experience. 

It’s been relatively easy to switch model providers to date. They have similar, if not identical, APIs. Sure, you have to change prompts a little bit, but that’s not that hard. 

But this is all because they are stateless. 

As soon as there is any state associated, its much harder to switch. Because this memory matters. And if you switch, you lose access to it. 

Let me tell a story. I have an email assistant internally. It’s built on top of a template in [Fleet](https://www.langchain.com/langsmith/fleet), our no-code platform for building Enterprise ready OpenClaws. This platform has memory built in, so as I interacted with my email assistant over the past few months it built up memory. A few weeks ago, my agent got deleted by accident. I was pissed! I tried to create an agent from the same template - but the experience was so much worse. I had to reteach it all my preferences, my tone, everything. 

The plus side of my email agent deleted - it made me realize how powerful and sticky memory could be. 

#### Open Memory, Open Harnesses

Memory needs to be opened, owned by whomever is developing the agentic experience. It allows you to build up a proprietary dataset that you actually control. 

Memory (and therefor harnesses) should be separate from model providers. You should want optionality to try out whatever models are best for your use case. Model providers are incentivized to create lock in via memory. 

This is why we are building [Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview). Deep Agents: 

* Is open source
* Is model agnostic
* Uses open standards like [agents.md](http://agents.md/) and [skills](https://agentskills.io/home)
* Has plugins to [Mongo](https://www.mongodb.com/docs/atlas/ai-integrations/langgraph/), Postgres, Redis and others for storing memories
* Is deployable: (1) via [LangSmith Deployment](https://docs.langchain.com/langsmith/deployment) (self hostable, can be deployed on any cloud, can bring your own database to serve as a memory store); (2) behind any standard web hosting framework

**In order to own your memory, you need to be using an Open Harness** 

**Try out [Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview) today.** 

*Thank you to a few people for review and thoughts:* 

* *[Sydney Runkle](https://x.com/sydneyrunkle), who is doing a lot of great Deep Agents and memory work*
* *[Viv Trivedy](https://x.com/Vtrivedy10), who is a leading voice on agent harnesses*
* *[Nuno Campos](https://x.com/nfcampos), who has some great writing on context engineering for finance agents*
* *[Sarah Wooders](https://x.com/sarahwooders), who is CTO of Letta, a company that has consistently been at the forefront of stateful agents*

[Posted Apr 11, 2026 at 2:50PM](https://twitter.com/hwchase17/status/2042978500567609738)

[Posted Apr 12, 2026 at 5:25AM](https://twitter.com/garrytan/status/2043198780800197025)

I spent the last three months building exactly this. 

1. Four-layer memory.
2. Fat skills with self-rewrite hooks.
3. Protocol enforcement.
4. A nightly dream cycle that compresses everything the agent learned that day.

This article is 4,000 words of how I built it and why every piece exists. 

If you do not want to read all that, you can just install the whole thing here:⬇️

**If you just want to install it:** [github.com/codejunkie99/agentic-stack](http://github.com/codejunkie99/agentic-stack) 

Works with Claude Code, Cursor, OpenClaw, or any agent that reads markdown. 

If you want to understand what you are installing and why each piece exists, keep reading.⬇️

#### Image

#### The shape of the full stack

Here is the folder structure. I will explain each part in detail, but I want you to see the whole thing first because the shape matters more than any individual piece. 

```
.agent/  
├── [AGENTS.md](http://AGENTS.md)                          # root config, harness reads this first  
├── harness/  
│   ├── [conductor.py](http://conductor.py)                   # thin loop (~200 LOC)  
│   ├── [context\_budget.py](http://context_budget.py)              # manages token allocation across modules  
│   └── hooks/                         # lifecycle event handlers  
│       ├── [pre\_tool\_call.py](http://pre_tool_call.py)           # permission enforcement  
│       ├── [post\_execution.py](http://post_execution.py)          # auto-logging to memory  
│       └── [on\_failure.py](http://on_failure.py)              # escalation + reflection trigger  
├── memory/  
│   ├── working/                       # live task state, volatile  
│   │   ├── [WORKSPACE.md](http://WORKSPACE.md)  
│   │   └── [ACTIVE\_PLAN.md](http://ACTIVE_PLAN.md)  
│   ├── episodic/                      # what happened in prior runs  
│   │   ├── AGENT_LEARNINGS.jsonl  
│   │   └── snapshots/  
│   ├── semantic/                      # abstractions that outlive episodes  
│   │   ├── [LESSONS.md](http://LESSONS.md)  
│   │   ├── [DECISIONS.md](http://DECISIONS.md)  
│   │   └── [DOMAIN\_KNOWLEDGE.md](http://DOMAIN_KNOWLEDGE.md)  
│   ├── personal/                      # user-specific preferences  
│   │   └── [PREFERENCES.md](http://PREFERENCES.md)  
│   └── [auto\_dream.py](http://auto_dream.py)                  # nightly compression + consolidation  
├── skills/  
│   ├── [\_index.md](http://_index.md)                      # discovery registry, summaries only  
│   ├── _manifest.jsonl                # machine-readable skill metadata  
│   ├── skillforge/  
│   │   └── [SKILL.md](http://SKILL.md)  
│   ├── memory-manager/  
│   │   └── [SKILL.md](http://SKILL.md)  
│   ├── git-proxy/  
│   │   ├── [SKILL.md](http://SKILL.md)  
│   │   └── [KNOWLEDGE.md](http://KNOWLEDGE.md)  
│   ├── api-scaffold/  
│   │   ├── [SKILL.md](http://SKILL.md)  
│   │   └── scripts/[scaffold.sh](http://scaffold.sh)  
│   └── ...  
├── protocols/  
│   ├── tool_schemas/                  # typed interfaces for every tool  
│   │   ├── github.schema.json  
│   │   ├── shell.schema.json  
│   │   └── api.schema.json  
│   ├── [permissions.md](http://permissions.md)                 # what the agent can and cannot do  
│   └── [delegation.md](http://delegation.md)                  # rules for handing off to sub-agents  
└── tools/  
    ├── [memory\_reflect.py](http://memory_reflect.py)  
    ├── [skill\_loader.py](http://skill_loader.py)                # progressive disclosure engine  
    └── [budget\_tracker.py](http://budget_tracker.py)  

```
This mirrors patterns from Gstack and Claude Code's own memory hooks. I did not design it from scratch. 

I arrived at it by trying other layouts that did not work and gradually converging on this one. 

The key insight, and the thing Garry's post crystallized for me, is the separation. 

**The harness does not think.** It reads files, calls tools, writes logs, runs hooks. All the intelligence lives in the skill files and the memory files. The protocols enforce boundaries. 

This means: 

* You can swap the harness for a different one tomorrow and lose nothing
* You can swap the model and lose nothing
* The only things that accumulate value are the skills, the memory, and the protocols
* Those are plain markdown and JSON in a git repo

---

#### The files nobody shows you (and the prompts to generate them)

#### Every guide shows you the folder structure. Nobody shows you what actually goes inside the four files that make or break the system. Here they are.

**[AGENTS.md](http://AGENTS.md)** 

This is the first file the harness reads. It is the table of contents for your agent's brain. Without it, the agent does not know where anything lives. 

```
# Agent Infrastructure## Memory  
- `memory/working/[WORKSPACE.md](http://WORKSPACE.md)` — current task state (read first)  
- `memory/semantic/[LESSONS.md](http://LESSONS.md)` — distilled patterns (read before decisions)  
- `memory/semantic/[DECISIONS.md](http://DECISIONS.md)` — past major choices and rationale  
- `memory/personal/[PREFERENCES.md](http://PREFERENCES.md)` — your conventions and style  
- `memory/episodic/AGENT\_LEARNINGS.jsonl` — raw experience log

## Skills  
- `skills/[\_index.md](http://_index.md)` — read this for skill discovery  
- Only load full [SKILL.md](http://SKILL.md) files when triggers match  
- Every skill has a self-rewrite hook. Use it after failures.

## Protocols  
- `protocols/[permissions.md](http://permissions.md)` — read before any tool call  
- `protocols/tool\_schemas/` — typed interfaces for external tools

## Rules  
1. Check memory before making decisions you have been corrected on before  
2. Log every significant action to episodic memory  
3. Update [WORKSPACE.md](http://WORKSPACE.md) as you work  
4. Follow permissions strictly. Blocked means blocked.  
5. When a self-rewrite hook fires, propose conservative edits only  

```
**Prompt to generate yours:**

Read the folder structure at .agent/ and write an [AGENTS.md](http://AGENTS.md) that serves as the root config file. It should tell the agent where memory, skills, and protocols live, what to read first, and what rules to always follow. Keep it under 30 lines. It is a map, not an encyclopedia. 

---

**[DECISIONS.md](http://DECISIONS.md)** 

This is the file that saves you from re-debating the same architectural choice three months later. Without it, the agent (and you) will revisit settled questions endlessly. 

```
# Major Decisions## 2026-04-13: Session store for auth tokens  
\*\*Decision:\*\* Use Redis, not in-memory store  
\*\*Rationale:\*\* Concurrent refresh requests cause race conditions with in-memory. Redis handles atomic operations natively.  
\*\*Alternatives considered:\*\* PostgreSQL (too slow for token lookups), cookie-based (security concerns with PKCE)  
\*\*Status:\*\* Active

## 2026-04-11: API framework  
\*\*Decision:\*\* FastAPI over Express  
\*\*Rationale:\*\* Typed request validation out of the box. Async support without callback hell. Team already knows Python.  
\*\*Alternatives considered:\*\* Express (more ecosystem, but weaker typing), Hono (too early)  
\*\*Status:\*\* Active

## 2026-04-08: Test strategy  
\*\*Decision:\*\* Integration tests with mock fallbacks, no e2e for MVP  
\*\*Rationale:\*\* E2e tests against live APIs are flaky and slow. Mock fallbacks let us run the full suite in CI under 2 minutes.  
\*\*Alternatives considered:\*\* Full e2e with retries (too flaky), unit only (misses integration bugs)  
\*\*Status:\*\* Active, revisit after launch  

```
**Prompt to generate yours:**

Read memory/semantic/[LESSONS.md](http://LESSONS.md) and memory/episodic/AGENT\_LEARNINGS.jsonl. Identify the 3-5 most significant architectural or workflow decisions that have been made. For each one, write an entry in [DECISIONS.md](http://DECISIONS.md) with: the decision, the rationale, alternatives that were considered, and whether it is still active. Format as markdown. Only include decisions that would be costly to revisit or re-debate. 

---

**[on\_failure.py](http://on_failure.py)** 

This is the hook that turns failures into learning instead of just errors. Without it, failures get logged with generic pain scores and no reflection. 

```
# harness/hooks/[on\_failure.py](http://on_failure.py)  
import json, datetimeEPISODIC\_PATH = ".agent/memory/episodic/AGENT\_LEARNINGS.jsonl"  
FAILURE\_THRESHOLD = 3 # trigger skill rewrite after this many

def on\_failure(skill\_name, action, error, context=""):  
 """called when any action fails"""  
 entry = {  
 "timestamp": datetime.datetime.now().isoformat(),  
 "skill": skill\_name,  
 "action": action,  
 "result": "failure",  
 "detail": str(error)[:500],  
 "pain\_score": 8,  
 "importance": 7,  
 "reflection": f"FAILURE in {skill\_name}: {type(error).\_\_name\_\_}: {str(error)[:200]}",  
 "context": context[:300]  
 }

 with open(EPISODIC\_PATH, "a") as f:  
 f.write(json.dumps(entry) + "\n")

 # check if this skill keeps failing  
 recent\_failures = count\_recent\_failures(skill\_name)  
 if recent\_failures >= FAILURE\_THRESHOLD:  
 entry["reflection"] += (  
 f" | THIS SKILL HAS FAILED {recent\_failures} TIMES RECENTLY."  
 f" Flag for rewrite."  
 )  
 entry["pain\_score"] = 10

 return entry

def count\_recent\_failures(skill\_name, days=14):  
 """count failures for this skill in the last N days"""  
 cutoff = datetime.datetime.now() - datetime.timedelta(days=days)  
 count = 0  
 try:  
 with open(EPISODIC\_PATH) as f:  
 for line in f:  
 if not line.strip():  
 continue  
 e = json.loads(line)  
 if (e.get("skill") == skill\_name  
 and e.get("result") == "failure"  
 and datetime.datetime.fromisoformat(  
 e["timestamp"]) > cutoff):  
 count += 1  
 except FileNotFoundError:  
 pass  
 return count  

```
**What it does that [post\_execution.py](http://post_execution.py) does not:** 

* Automatically assigns high pain scores (8) so failures surface during retrieval
* Counts recent failures per skill
* Flags skills for rewrite after 3+ failures in 14 days
* Includes error type and context so the reflection is actionable

---

**The cron line** 

```
# run this once  
crontab -e# add this line  
0 3 \* \* \* cd /path/to/your/project && python .agent/memory/[auto\_dream.py](http://auto_dream.py) >> .agent/memory/dream.log 2>&1  

```
That is it. The dream cycle runs at 3am, compresses memory, promotes lessons, archives stale entries, and git commits the result. 

Check the log: 

```
tail -5 .agent/memory/dream.log  
# dream cycle: promoted 2, decayed 7, kept 31  

```
Check the history: 

```
git log --oneline .agent/memory/  
# a1b2c3d dream cycle: promoted 2, decayed 7, kept 31  
# d4e5f6g dream cycle: promoted 0, decayed 3, kept 35  
# g7h8i9j dream cycle: promoted 1, decayed 0, kept 38  

```
#### That is the agent's autobiography. Every line is a night of learning.

#### The harness: thin conductor

I spent about 30 minutes on the first version of this. You can skip it entirely if you use Claude Code or Cursor as your harness, because they already have the loop, the tool calling, and the file watching built in. Point them at your .agent/folder and you are done. 

I wanted full ownership, so I wrote the conductor myself. The entire thing is under 200 lines. 

```
python  
# harness/[conductor.py](http://conductor.py)  
import time, json, os, datetime, subprocess  
from anthropic import Anthropic  # swap for openai, gemini, etc.  
from tools.skill_loader import progressive_load  
from harness.hooks.pre_tool_call import check_tool_call  
from harness.hooks.post_execution import log_executionclient = Anthropic(api\_key=os.getenv("ANTHROPIC\_API\_KEY"))  
MAX\_CONTEXT\_TOKENS = 128000  
RESERVED\_FOR\_REASONING = 40000

def build\_context(user\_input):  
 """  
 assemble context from all three modules: memory, skills, protocols.  
 respect the token budget. not everything can fit.  
 """  
 budget = MAX\_CONTEXT\_TOKENS - RESERVED\_FOR\_REASONING  
 context\_parts = []  
 used = 0

 # 1. always load: personal preferences + active workspace  
 for f in ["memory/personal/[PREFERENCES.md](http://PREFERENCES.md)", "memory/working/[WORKSPACE.md](http://WORKSPACE.md)"]:  
 path = os.path.join(".agent", f)  
 if os.path.exists(path):  
 content = open(path).read()  
 context\_parts.append(content)  
 used += len(content) // 4

 # 2. load semantic lessons (truncate if needed)  
 lessons\_path = ".agent/memory/semantic/[LESSONS.md](http://LESSONS.md)"  
 if os.path.exists(lessons\_path):  
 lessons = open(lessons\_path).read()[:8000]  
 context\_parts.append(lessons)  
 used += len(lessons) // 4

 # 3. load top 5 episodic entries by salience  
 episodic\_path = ".agent/memory/episodic/AGENT\_LEARNINGS.jsonl"  
 if os.path.exists(episodic\_path):  
 entries = [json.loads(l) for l in open(episodic\_path) if l.strip()]  
 top = sorted(entries, key=salience\_score, reverse=True)[:5]  
 episodic\_text = "\n".join(  
 f"- [{e['timestamp'][:10]}] {e.get('action','')}: {e.get('reflection','')}"  
 for e in top  
 )  
 context\_parts.append(episodic\_text)  
 used += len(episodic\_text) // 4

 # 4. progressive skill loading, only matched skills  
 for skill in progressive\_load(user\_input):  
 skill\_text = f"## Skill: {skill['name']}\n{skill['content']}"  
 tokens = len(skill\_text) // 4  
 if used + tokens < budget:  
 context\_parts.append(skill\_text)  
 used += tokens

 # 5. always load permissions (short, safety-critical)  
 perms\_path = ".agent/protocols/[permissions.md](http://permissions.md)"  
 if os.path.exists(perms\_path):  
 context\_parts.append(open(perms\_path).read())

 return "\n\n---\n\n".join(context\_parts), used

def salience\_score(entry):  
 age\_days = (datetime.datetime.now()  
 - datetime.datetime.fromisoformat(entry["timestamp"])).days  
 pain = entry.get("pain\_score", 5)  
 importance = entry.get("importance", 5)  
 recurrence = entry.get("recurrence\_count", 1)  
 return (10 - age\_days \* 0.3) \* (pain / 10) \* (importance / 10) \* min(recurrence, 3)

def run(user\_input):  
 context, tokens\_used = build\_context(user\_input)

 response = client.messages.create(  
 model="claude-sonnet-4-20250514",  
 max\_tokens=4096,  
 temperature=0.3,  
 system=(  
 "You are an agent with externalized memory, skills, and protocols.\n"  
 "Your memory, skills, and constraints are in the context below.\n"  
 "Read them before acting. Follow constraints strictly.\n"  
 "Log every action. Update memory/working/[WORKSPACE.md](http://WORKSPACE.md) as you go.\n\n"  
 f"{context}"  
 ),  
 messages=[{"role": "user", "content": user\_input}],  
 )

 result = response.content[0].text  
 log\_execution("conductor", user\_input[:100], result[:500], True)  
 return result  

```
The critical function is build\_context, and it deserves a mental model before you look at the priority list. 

**The context window is a computation box.** The model only reasons over what is inside it. Everything outside it, your memory files, your skill library, your tool schemas, your entire git history, does not exist to the model unless the harness retrieves it, shapes it, and injects it. 

Each piece that enters the context window is a context fragment. Each fragment is an explicit decision about what the model needs to do its work right now. 

The harness is a system of blocks that control and inject context. 

* **Targeted fragments are signal.** They steer the model toward better computation.
* **Conflicting or stale fragments are noise.** They make the model confused, not smarter.

This is why build\_context is the most important function in the system, not the model call. 

The conductor allocates based on priority: 

1. Personal preferences and workspace always load first
2. Semantic lessons second
3. Recent episodic entries third
4. Matched skills fourth
5. Permissions last

If the budget runs out, skills that did not trigger do not load. **Every fragment that enters must earn its place.** If it is not making the current decision more legible, it is making it worse. 

#### One rule I have enforced on myself: the harness stays under 200 lines. The moment it starts doing reasoning or making decisions about which skills to load, I have put intelligence in the wrong place. That logic belongs in a skill file, not in the conductor.

#### **The salience scoring function**

This deserves a closer look because it is doing more work than it appears to. Each log entry has: 

* A **pain score** (how badly did the mistake hurt, 1-10)
* An **importance score** (how often does this type of situation come up)
* A **recurrence count** (how many times has this pattern appeared)

The formula multiplies those against a recency decay. Recent painful important recurring things float to the top. Old minor one-off things sink. 

I tried vector search before this. It was slower, more complex to set up, and did not produce noticeably better results for a single-user system. 

#### **The simple weighted formula won.**

#### Memory: four layers, not one

The single biggest mistake in my original setup was treating memory as one undifferentiated pile. 

[DECISIONS.md](http://DECISIONS.md), [LESSONS.md](http://LESSONS.md), and AGENT\_LEARNINGS.jsonl all lived in the same flat folder and the agent read them the same way. 

This works for about six weeks. 

Then it breaks because **different kinds of memory need different retention policies, different retrieval strategies, and different update frequencies.** 

#### **Here are the four layers and why they need to be separate.**

**Layer 1 : Working context** is the live state of whatever task is happening right now. Open files, partial plans, active hypotheses, execution checkpoints. This is the most volatile layer. It changes every few minutes and becomes worthless the moment the task is done. 

```
# memory/working/[WORKSPACE.md](http://WORKSPACE.md)  
## Current task  
Refactoring auth middleware to support OAuth2 PKCE flow## Open files  
- src/auth/middleware.ts (line 45-80 needs changes)  
- src/auth/pkce.ts (new file, drafted)  
- tests/auth/pkce.test.ts (3/7 tests passing)

## Active hypotheses  
- The token refresh logic can reuse the existing session store  
- PKCE code verifier should be stored server-side, not in cookie

## Checkpoints  
- [x] Scaffolded PKCE module  
- [x] Basic token exchange working  
- [ ] Refresh flow  
- [ ] Error handling for expired codes  
- [ ] Integration tests  

```
* **The point of externalizing this is resumption.** When the context window resets or you come back tomorrow, the agent reads [WORKSPACE.md](http://WORKSPACE.md) and picks up exactly where it left off instead of reconstructing everything from scratch.
* Update this file constantly. It is disposable. When the task finishes, archive it to episodic and start fresh.

---

**Layer 2: Episodic memory** records what happened in prior runs. Decision points, tool calls, failures, outcomes, and reflections. 

This is not just a log. Retrieved episodes serve as concrete precedents that help the agent avoid repeating known mistakes. 

```
{"timestamp":"2026-04-13T14:22:00","skill":"api-scaffold","action":"scaffolded /auth/pkce endpoint","result":"success","pain_score":2,"importance":6,"reflection":"PKCE flow requires server-side code verifier storage, not cookie-based as initially attempted"}  
{"timestamp":"2026-04-13T15:01:00","skill":"git-proxy","action":"attempted force push to main","result":"blocked by pre_tool_call hook","pain_score":8,"importance":9,"reflection":"force push to protected branches should be permanently blocked, not just warned"}  

```
The fields that matter most: 

* **pain\_score**: how much damage the mistake caused
* **importance**: how likely this lesson is to be relevant again

#### The salience scoring function uses both to determine what surfaces during retrieval.

**Layer 3 :Semantic memory** stores abstractions that outlive any single episode. These are the patterns and heuristics that tend to hold across tasks. Not tied to a specific time or place. 

```
# memory/semantic/[LESSONS.md](http://LESSONS.md)  
# Agent lessons (auto-distilled)## API design  
- always validate request bodies before any database operation, not after  
- prefer explicit error types over generic 500 responses  
- rate limiting should be middleware, not per-route logic

## Git workflow  
- never force push to main or protected branches under any circumstances  
- commit messages should reference the task ID from [ACTIVE\_PLAN.md](http://ACTIVE_PLAN.md)

## Testing  
- write the failing test before writing the fix, every time  
- integration tests that depend on external services need mock fallbacks  
- if a test is flaky three times, delete it and rewrite from scratch  

```
The difference between episodic and semantic is not just granularity. It is function. 

* **Episodic memory** says "this specific thing happened on this date."
* **Semantic memory** says "this tends to hold across cases."

#### The dream cycle is the mechanism that promotes episodic entries into semantic lessons when they recur or score high enough.

**Layer 4: Personal memory** tracks stable information about you specifically . Your preferences, your conventions, your recurring constraints. 

This layer exists because user-specific information needs different retention rules than general task knowledge. 

```
# memory/personal/[PREFERENCES.md](http://PREFERENCES.md)  
## Code style  
- typescript strict mode always  
- prefer functional patterns over classes  
- 2-space indentation, no semicolons## Workflow  
- always run tests before committing  
- draft PR early, mark as ready when tests pass  
- prefer small PRs over large ones

## Constraints  
- primary stack: TypeScript, Python, PostgreSQL  
- deployment: Railway for staging, AWS for production  

```
* This is the layer that lets the agent adapt to you over time without confusing your personal conventions with general best practices.
* It should never be merged into [LESSONS.md](http://LESSONS.md) because what works for you might be terrible advice in general.

---

#### The upgraded dream cycle

The original dream cycle was a simple compression script. 

This version handles all four memory layers with different policies. 

```
# memory/[auto\_dream.py](http://auto_dream.py)  
import json, os, datetime, subprocess  
from collections import defaultdictEPISODIC\_PATH = "memory/episodic/AGENT\_LEARNINGS.jsonl"  
SEMANTIC\_PATH = "memory/semantic/[LESSONS.md](http://LESSONS.md)"  
ARCHIVE\_DIR = "memory/episodic/snapshots"  
DECAY\_DAYS = 90  
PROMOTION\_THRESHOLD = 7.0

def salience\_score(entry):  
 age\_days = (datetime.datetime.now()  
 - datetime.datetime.fromisoformat(entry["timestamp"])).days  
 pain = entry.get("pain\_score", 5)  
 importance = entry.get("importance", 5)  
 recurrence = entry.get("recurrence\_count", 1)  
 return (10 - age\_days \* 0.3) \* (pain / 10) \* (importance / 10) \* min(recurrence, 3)

def find\_recurring\_patterns(entries):  
 """cluster entries by skill + action pattern to detect recurrence"""  
 patterns = defaultdict(list)  
 for e in entries:  
 key = f"{e.get('skill', 'general')}::{e.get('action', '')[:50]}"  
 patterns[key].append(e)

 recurring = {}  
 for key, group in patterns.items():  
 if len(group) >= 2:  
 best = max(group, key=lambda x: salience\_score(x))  
 best["recurrence\_count"] = len(group)  
 recurring[key] = best  
 return recurring

def promote\_to\_semantic(high\_salience\_entries):  
 """append high-scoring patterns to [LESSONS.md](http://LESSONS.md)"""  
 if not high\_salience\_entries:  
 return

 existing = ""  
 if os.path.exists(SEMANTIC\_PATH):  
 existing = open(SEMANTIC\_PATH).read()

 new\_lessons = []  
 for entry in high\_salience\_entries:  
 lesson\_line = f"- {entry.get('reflection', entry.get('action', 'unknown'))}"  
 if lesson\_line not in existing:  
 new\_lessons.append(lesson\_line)

 if new\_lessons:  
 with open(SEMANTIC\_PATH, "a") as f:  
 f.write(f"\n## Auto-promoted {datetime.date.today().isoformat()}\n")  
 for lesson in new\_lessons:  
 f.write(lesson + "\n")

def run\_dream\_cycle():  
 entries = [json.loads(l) for l in open(EPISODIC\_PATH) if l.strip()]  
 if not entries:  
 return

 # find recurring patterns + boost salience  
 recurring = find\_recurring\_patterns(entries)

 # promote high-salience patterns to semantic memory  
 promotable = [e for e in recurring.values()  
 if salience\_score(e) >= PROMOTION\_THRESHOLD]  
 promote\_to\_semantic(promotable)

 # decay old low-value entries, archive instead of delete  
 cutoff = datetime.datetime.now() - datetime.timedelta(days=DECAY\_DAYS)  
 kept, archived = [], []  
 for e in entries:  
 ts = datetime.datetime.fromisoformat(e["timestamp"])  
 if ts < cutoff and salience\_score(e) < 2.0:  
 archived.append(e)  
 else:  
 kept.append(e)

 if archived:  
 os.makedirs(ARCHIVE\_DIR, exist\_ok=True)  
 archive\_file = f"{ARCHIVE\_DIR}/archive\_{datetime.date.today()}.jsonl"  
 with open(archive\_file, "a") as f:  
 for e in archived:  
 f.write(json.dumps(e) + "\n")

 with open(EPISODIC\_PATH, "w") as f:  
 for e in kept:  
 f.write(json.dumps(e) + "\n")

 # archive stale working context  
 workspace = "memory/working/[WORKSPACE.md](http://WORKSPACE.md)"  
 if os.path.exists(workspace):  
 age = datetime.datetime.now() - datetime.datetime.fromtimestamp(  
 os.path.getmtime(workspace))  
 if age.days >= 2:  
 stale\_name = f"{ARCHIVE\_DIR}/workspace\_{datetime.date.today()}.md"  
 os.rename(workspace, stale\_name)

 subprocess.run(["git", "add", "memory/"])  
 subprocess.run(["git", "commit", "-m",  
 f"dream cycle: promoted {len(promotable)}, "  
 f"decayed {len(archived)}, kept {len(kept)}"])

if \_\_name\_\_ == "\_\_main\_\_":  
 run\_dream\_cycle()  

```
The upgraded dream cycle does three things the old one did not: 

* It **detects recurring patterns** across episodes and boosts their salience
* It **automatically promotes** high-salience patterns from episodic into semantic memory. Lessons that keep mattering get hardened into permanent knowledge without you manually curating them.
* It **archives decayed entries** instead of deleting them, so you can always git log memory/ to recover something that was compressed away too aggressively

I call it the dream cycle because it runs overnight and compresses the day's raw logs into clean distilled lessons, the same way sleep consolidates memories. 

Run this on a nightly cron job. Or trigger it manually after intense sessions. 

#### git log --oneline memory/ is still the agent's autobiography. I did not expect to find that useful. I use it constantly.

#### The skills

This is where I spent most of my time, and where I think most of the value lives. 

#### Each skill is a markdown file with YAML frontmatter and a self-rewrite section at the bottom. But after running 30+ skills for three months, I learned that **the skill files themselves are only half the problem.** The other half is finding and loading the right skill at the right time without flooding the context window.

**Skill registry and progressive disclosure** 

```
# skills/[\_index.md](http://_index.md)  
# Skill Registry  
# The agent reads this file first. Full skill files are loaded only when needed.## skillforge  
Creates new skills from observed patterns and recurring tasks.  
Triggers: "create skill", "new skill", "I keep doing this manually"

## memory-manager  
Actively reads, scores, and consolidates memory entries. Triggers reflection cycles.  
Triggers: "reflect", "what did I learn", "compress memory", after 10+ episodic entries

## git-proxy  
Handles all git operations with safety constraints.  
Triggers: "commit", "push", "branch", "merge", "rebase"  
Constraints: never force push to main, always run tests before push

## api-scaffold  
Scaffolds new API endpoints following project conventions.  
Triggers: "new endpoint", "scaffold api", "build route"

## test-writer  
Generates tests from implementation code or specifications.  
Triggers: "write tests", "add coverage", "test this"

## debug-investigator  
Systematic debugging: reproduce, isolate, hypothesize, verify.  
Triggers: "debug", "why is this failing", "investigate"

## code-reviewer  
Reviews code changes against project conventions and past lessons.  
Triggers: "review", "check this", "before I merge"

## deploy-checklist  
Pre-deployment verification against a structured checklist.  
Triggers: "deploy", "ship", "release", "go live"  
Constraints: requires all tests passing, no unresolved TODOs in diff  

```
This is the progressive disclosure layer. The agent reads [\_index.md](http://_index.md) on every session start. It is short. Just names, one-line descriptions, and trigger phrases. 

#### When a trigger matches, the agent loads the full [SKILL.md](http://SKILL.md) for that specific skill. When nothing matches, the full skill files stay on disk unloaded.

**This matters because of context budget.** Your model has a fixed number of tokens it can process. Memory retrieval, skill loading, tool schemas, and the model's own reasoning all compete for that budget. 

* If you dump every skill file into context on every run, you waste tokens on irrelevant instructions and the model performs worse, not better.
* Models attend unevenly across long inputs. Information in the middle of a big context gets missed.
* Progressive disclosure solves this by keeping the context lean.

For machine-readable discovery, add a structured manifest alongside the human-readable index: 

```
{"name":"skillforge","version":"2026-04-13","triggers":["create skill","new skill"],"tools":["bash","memory_reflect"],"preconditions":[],"constraints":[],"category":"meta"}  
{"name":"git-proxy","version":"2026-04-13","triggers":["commit","push","branch","merge"],"tools":["bash"],"preconditions":["git repo initialized"],"constraints":["never force push to main","run tests before push"],"category":"operations"}  
{"name":"deploy-checklist","version":"2026-04-13","triggers":["deploy","ship","release"],"tools":["bash"],"preconditions":["all tests passing"],"constraints":["no unresolved TODOs in diff","requires human approval for production"],"category":"operations"}  

```
The fields beyond name and triggers that matter: 

* **preconditions**: what must be true before this skill can run
* **constraints**: hard boundaries on what the skill is allowed to do, normative not procedural
* **category**: used for composition when multiple skills need to coordinate

#### At around 50 skills the keyword trigger matching starts to miss. At 500 you will want semantic matching with embeddings. But keyword triggers work fine for the first year of solo usage.

**The skill loader** 

```
# tools/[skill\_loader.py](http://skill_loader.py)  
import json, osSKILLS\_DIR = ".agent/skills"  
MANIFEST\_PATH = os.path.join(SKILLS\_DIR, "\_manifest.jsonl")

def load\_manifest():  
 if not os.path.exists(MANIFEST\_PATH):  
 return []  
 with open(MANIFEST\_PATH) as f:  
 return [json.loads(line) for line in f if line.strip()]

def match\_triggers(user\_input, manifest):  
 matches = []  
 input\_lower = user\_input.lower()  
 for skill in manifest:  
 for trigger in skill.get("triggers", []):  
 if trigger.lower() in input\_lower:  
 matches.append(skill)  
 break  
 return matches

def check\_preconditions(skill):  
 for pre in skill.get("preconditions", []):  
 if pre.endswith("exists"):  
 path = pre.replace(" exists", "").strip()  
 if not os.path.exists(path):  
 return False  
 return True

def load\_skill\_full(skill\_name):  
 skill\_path = os.path.join(SKILLS\_DIR, skill\_name, "[SKILL.md](http://SKILL.md)")  
 if not os.path.exists(skill\_path):  
 return None  
 content = open(skill\_path).read()

 # also load [KNOWLEDGE.md](http://KNOWLEDGE.md) if it exists  
 knowledge\_path = os.path.join(SKILLS\_DIR, skill\_name, "[KNOWLEDGE.md](http://KNOWLEDGE.md)")  
 if os.path.exists(knowledge\_path):  
 content += "\n\n---\n## Accumulated knowledge\n"  
 content += open(knowledge\_path).read()  
 return content

def progressive\_load(user\_input):  
 """three-stage: manifest (always) → trigger match → full load"""  
 manifest = load\_manifest()  
 matches = match\_triggers(user\_input, manifest)  
 loaded = []  
 for skill in matches:  
 if check\_preconditions(skill):  
 content = load\_skill\_full(skill["name"])  
 if content:  
 loaded.append({  
 "name": skill["name"],  
 "constraints": skill.get("constraints", []),  
 "content": content  
 })  
 return loaded  

```

---

**The core skills** 

* **skillforge** is the one I built first and the one that changed the trajectory of everything else. It teaches the agent how to create new skills.
* Without it, I was writing every [SKILL.md](http://SKILL.md) by hand.
* With it, the agent encounters a new domain, recognizes it does not have a skill for it, and drafts one.

```
# skills/skillforge/[SKILL.md](http://SKILL.md)  
---  
name: skillforge  
version: 2026-04-13  
triggers: ["create skill", "new capability", "build skill"]  
tools: [bash, memory_reflect, git]  
---When the user or agent needs a new capability:  
1. Check existing skills in [\_index.md](http://_index.md) to avoid duplicates  
2. Check memory/semantic/[LESSONS.md](http://LESSONS.md) for related past patterns  
3. Create a new folder under skills/ with a [SKILL.md](http://SKILL.md) following this format:  
 - YAML frontmatter (name, version, triggers, tools, preconditions, constraints)  
 - Core instructions (what to do, in plain language, including WHY not just WHAT)  
 - Self-rewrite hook  
4. Add an entry to [\_index.md](http://_index.md) and \_manifest.jsonl  
5. Add supporting scripts/ or references/ if the skill needs them  
6. Commit via git and log the decision in memory/semantic/[DECISIONS.md](http://DECISIONS.md)

\*\*Self-rewrite hook (after every new skill creation)\*\*  
Read the last 3 skill creation entries in memory. If better trigger  
patterns, constraint structures, or hook designs have emerged, update  
this [SKILL.md](http://SKILL.md) and the template it uses.  

```
I want to be honest about what this does and does not do. It does not produce perfect skills on the first try. The skills it generates are rough drafts. 

But rough drafts that follow a consistent format and that include self-rewrite hooks from day one. 

#### After a few iterations the agent-generated skills start getting noticeably better, because **the self-rewrite hook on skillforge itself is updating the template** based on what worked and what did not in previous attempts.

**memory-manager is the skill I wish I had written first.** 

For the first three weeks of running this system I had all the memory files but the agent was not reading them consistently. 

It would write a lesson after a failure and then repeat the exact same mistake three days later because nothing told it to check. 

```
# skills/memory-manager/[SKILL.md](http://SKILL.md)  
---  
name: memory-manager  
version: 2026-04-13  
triggers: ["remember", "reflect", "distill", "what did I learn", "update memory"]  
tools: [memory_reflect, bash, git]  
preconditions: ["memory/episodic/AGENT_LEARNINGS.jsonl exists"]  
constraints: ["do not delete high-salience entries", "do not merge personal into semantic"]  
---After every major task or failure, call memory\_reflect to log what happened.  
Before important decisions, read top entries from memory/semantic/[LESSONS.md](http://LESSONS.md)  
and memory/semantic/[DECISIONS.md](http://DECISIONS.md).

When context is getting full or on explicit "reflect" trigger:  
1. Pull the 5 highest-salience entries from AGENT\_LEARNINGS.jsonl  
2. Check if any patterns recur. If so, promote to semantic/[LESSONS.md](http://LESSONS.md)  
3. Check if any [SKILL.md](http://SKILL.md) files should be updated based on new patterns  
4. Archive resolved working context to episodic/snapshots/  
5. Snapshot via git

When memory/semantic/[LESSONS.md](http://LESSONS.md) exceeds 200 lines, trigger [auto\_dream.py](http://auto_dream.py).

\*\*Self-rewrite hook (every 10 reflections or on repeated mistakes)\*\*  
If the same type of mistake appears 3+ times in recent memory, this  
skill's approach to distillation or salience scoring needs adjustment.  
Propose edits and log the diff in [DECISIONS.md](http://DECISIONS.md).  

```
* The difference before and after adding this skill was immediate. Before, memory was a filing cabinet nobody opened.
* After, the agent was checking its past mistakes before making decisions and updating its own skills when it noticed patterns. **T**
* **the filing cabinet became a feedback loop.**

---

**Self-rewrite hook template** 

Every skill, no matter how small, ends with a self-rewrite hook. This is the part that makes the system compound instead of staying static. 

```
---  
## Self-rewrite protocolAfter every 5 uses OR on any failure:  
1. Read memory/episodic/AGENT\_LEARNINGS.jsonl for recent entries tagged with this skill  
2. Read this skill's [KNOWLEDGE.md](http://KNOWLEDGE.md) for existing accumulated lessons  
3. Check if any new patterns, recurring failures, or changed assumptions exist  
4. If yes:  
 a. Append new lessons to [KNOWLEDGE.md](http://KNOWLEDGE.md)  
 b. Update trigger phrases in \_manifest.jsonl if needed  
 c. Update constraints if a safety-relevant pattern was found  
 d. Update procedures if a step is now obsolete or needed  
5. If a constraint was violated during execution, escalate to memory/semantic/[LESSONS.md](http://LESSONS.md)  
6. Commit: "skill-update: {skill\_name}, {one-line reason}"

Do NOT rewrite on every run. Most runs produce nothing worth changing.  
Only rewrite when the evidence is clea  

```
The important addition versus my original is step 5. 

* Constraint violations get escalated from the skill's local [KNOWLEDGE.md](http://KNOWLEDGE.md) into the global [LESSONS.md](http://LESSONS.md).
* **This is how a single skill's failure becomes system-wide knowledge.** The git-proxy skill discovering that force pushes are dangerous should not stay local to git-proxy. It should become a global constraint.

---

#### Protocols: the layer most builders skip

This is the part almost nobody builds. And it is the part that determines whether your agent stays a toy or becomes something you can actually trust with real work. 

Protocols are the contracts that govern how your agent talks to external systems. 

* Without them, the model improvises message formats, argument structures, and permissions for every tool call.
* **That improvisation is where most production failures come from.**
* It's not that the model cannot call the tool, but because it guesses the wrong format, sends the wrong arguments, or does something it should not have permission to do.

---

**Tool schemas** 

For every tool your agent can call, write a typed schema. This converts the model's task from "guess how to call this tool" to "fill in these fields." 

```
{  
  "name": "github",  
  "operations": {  
    "create_pr": {  
      "required_args": {  
        "title": {"type": "string", "max_length": 72},  
        "body": {"type": "string"},  
        "base": {"type": "string", "default": "main"},  
        "head": {"type": "string"}  
      },  
      "preconditions": ["all tests must pass", "branch must have commits ahead of base"],  
      "side_effects": ["notifies reviewers", "triggers CI"],  
      "requires_approval": false  
    },  
    "merge_pr": {  
      "required_args": {  
        "pr_number": {"type": "integer"},  
        "merge_method": {"type": "string", "enum": ["squash", "merge", "rebase"]}  
      },  
      "preconditions": ["CI must be passing", "at least one approval"],  
      "side_effects": ["deploys to staging if auto-deploy enabled"],  
      "requires_approval": true  
    },  
    "force_push": {  
      "blocked_targets": ["main", "production", "staging"],  
      "requires_approval": true,  
      "warning": "destructive operation, history will be rewritten"  
    }  
  }  
}  

```
Notice the fields beyond basic argument types: 

* **preconditions**: what must be true before calling
* **side\_effects**: what will happen downstream
* **requires\_approval**: operations that need human sign-off
* **blocked\_targets**: hard constraints the harness enforces regardless of what the model decides

#### This does not serve as documentation. The harness reads these schemas and enforces them at runtime through the pre\_tool\_call hook.

#### Permissions

```
# protocols/[permissions.md](http://permissions.md)## Always allowed (no approval needed)  
- read any file in the project directory  
- run tests  
- create branches  
- write to memory/ and skills/ directories  
- create draft pull requests

## Requires approval  
- merge pull requests  
- deploy to any environment  
- delete files outside of memory/working/  
- install new dependencies  
- modify CI/CD configuration

## Never allowed  
- force push to main, production, or staging  
- access secrets or credentials directly  
- send HTTP requests not in the approved domains list  
- modify [permissions.md](http://permissions.md) (only humans edit this file)  
- disable or bypass pre\_tool\_call hooks

## Approved external domains  
- [api.github.com](http://api.github.com)  
- [registry.npmjs.org](http://registry.npmjs.org)  
- [pypi.org](http://pypi.org)  

```
* **The permissions file is the single most important file in the protocol layer.**
* It is the difference between an agent you can leave running and an agent you have to babysit.
* The rule is simple: if you would not let a new hire do it unsupervised, the agent needs approval too.

---

#### Lifecycle hooks

Hooks are the enforcement mechanism. T 

hey run before and after agent actions and implement the constraints defined in permissions and tool schemas. 

```
# harness/hooks/[pre\_tool\_call.py](http://pre_tool_call.py)  
import json, osdef check\_tool\_call(tool\_name, operation, args):  
 """called BEFORE every tool invocation by the conductor"""  
 # load tool schema  
 schema\_path = f".agent/protocols/tool\_schemas/{tool\_name}.schema.json"  
 if os.path.exists(schema\_path):  
 schema = json.load(open(schema\_path))  
 op\_schema = schema.get("operations", {}).get(operation, {})

 # check blocked targets  
 blocked = op\_schema.get("blocked\_targets", [])  
 target = args.get("branch") or args.get("target") or ""  
 if target in blocked:  
 return False, f"BLOCKED: {operation} to {target} is permanently forbidden"

 # check if approval required  
 if op\_schema.get("requires\_approval", False):  
 return "approval\_needed", f"{operation} requires human approval"

 # check general permissions  
 perms = open(".agent/protocols/[permissions.md](http://permissions.md)").read()  
 if "## Never allowed" in perms:  
 never\_section = perms.split("## Never allowed")[1].split("##")[0]  
 action\_desc = f"{tool\_name} {operation} {json.dumps(args)}".lower()  
 for line in never\_section.strip().split("\n"):  
 if line.startswith("- "):  
 rule = line[2:].lower()  
 keywords = [w for w in rule.split() if len(w) > 3]  
 if sum(1 for k in keywords if k in action\_desc) >= 2:  
 return False, f"BLOCKED by permission rule: {line[2:]}"

 return True, "allowed"  

```

```
# harness/hooks/[post\_execution.py](http://post_execution.py)  
import json, datetimedef log\_execution(skill\_name, action, result, success, reflection=""):  
 """called AFTER every action by the conductor"""  
 entry = {  
 "timestamp": datetime.datetime.now().isoformat(),  
 "skill": skill\_name,  
 "action": action,  
 "result": "success" if success else "failure",  
 "detail": str(result)[:500],  
 "pain\_score": 2 if success else 7,  
 "importance": 5,  
 "reflection": reflection  
 }  
 with open(".agent/memory/episodic/AGENT\_LEARNINGS.jsonl", "a") as f:  
 f.write(json.dumps(entry) + "\n")  

```
**The post\_execution hook is what makes the memory system compound automatically.** 

* Every action, success or failure, gets logged to episodic memory with a pain score
* Failures get higher pain scores
* Higher pain scores surface more often during retrieval
* The agent is more likely to remember and avoid them

#### You do not have to manually teach the agent anything. The hooks do it.

#### The six flows that make it compound

#### The reason this system gets better over time instead of staying static is six feedback loops between the three modules. None of them require you to do anything manually after initial setup.

1. **Memory feeds skill creation.** When the memory-manager detects a recurring pattern in episodic memory, the same type of task handled the same way three or more times, it triggers skillforge to create a new skill from that pattern.
2. **Skills feed memory.** Every skill execution gets logged to episodic memory via the post\_execution hook. Success or failure, the result is recorded with a pain score. The memory system always has fresh data about which skills work and which do not.
3. **Skills run through protocols.** When a skill needs to call an external tool, the call goes through the pre\_tool\_call hook. The skill describes what to do. The protocol governs how it is done and whether it is allowed.
4. **Protocols generate skills.** Once you have a typed tool schema, it becomes easy to write a skill that uses it correctly. The schema tells the agent exactly what arguments are needed, what preconditions must be met, and what constraints apply. **This is why writing schemas first and skills second produces better skills than the reverse.**
5. **Memory influences which protocols get used.** If past episodic entries show that a particular API endpoint fails frequently, the agent can learn to prefer an alternative path.
6. **Protocol results become memory.** Tool outputs, approval events, error payloads. All of these get logged to episodic memory via the post\_execution hook. The protocol layer produces the evidence that memory stores, which later feeds skill updates and protocol routing.

---

This cycle is self-reinforcing. Better memory leads to better skill creation leads to richer execution traces leads to better memory. 

#### But it can also amplify errors. A bad lesson in semantic memory can lead to a flawed skill, whose failures generate more bad entries. The dream cycle's decay mechanism and the self-rewrite hooks' conservative update policy are the circuit breakers that prevent this.

#### What happened over 90 days

* **Weeks 1–2: frustrating.** The agent still forgot things. The memory files were there but the agent wasn't reading them reliably. I hadn't written memory-manager yet, so nothing was pulling the files into the loop.
* **Weeks 2–4: it started clicking.** Once memory-manager was in, the agent began checking [LESSONS.md](http://LESSONS.md) before making calls . I'd corrected before.
* **Weeks 4–5: it started editing itself.** I opened git-proxy's [KNOWLEDGE.md](http://KNOWLEDGE.md) one morning and there was a line in it I hadn't written. The agent had hit a rate limit, logged it, and during a reflection cycle memory-manager patched the skill.
* **Week 8: things started compounding.** I kept running into skills I'd forgotten I had, written by skillforge in response to problems I only half-remembered. The agent wasn't just remembering corrections anymore. It was generalizing from them.
* A lesson about API timeouts in one project ended up shaping how it scaffolded error handling in a completely different one. .
* **Week 10: I hit the wall.** Thirty skills, a fat [LESSONS.md](http://LESSONS.md), tool schemas for everything. Over 90K tokens in context before the agent had even started thinking. The model started getting worse, not better, and it took me anembarrassing couple of days to figure out why.
* Progressive disclosure and the skill registry pulled it back under control, and performance snapped back basically overnight.

---

**I do not want to overstate this.** 

* The agent is not sentient (not yet atleast lol) . It is not even particularly smart. **What it is, is consistent.** It checks its own notes.
* It updates its own instructions.
* It does not have bad days where it forgets what it learned last week.

#### That consistency, compounded over months, produces something that feels qualitatively different from a stateless agent, even though the underlying model is the same.

#### The bitter lesson while building skills

![](https://pbs.twimg.com/profile_images/2039088969854705664/AdloLslI.jpg)

[ᴅᴀɴɪᴇʟ ᴍɪᴇssʟᴇʀ 🛡️](https://twitter.com/DanielMiessler)
[@DanielMiessler](https://twitter.com/DanielMiessler)

![Good and Bad Harness Engineering](https://pbs.twimg.com/media/HF4qJwRbYAAVNoC.jpg)

There are lots of ways to do Harness Engineering well and poorly, but the most important one comes down to whether or not you're practicing [Bitter Lesson Engineering](https://danielmiessler.com/blog/bitter-lesson-engineering). 

Bitter Lesson Engineering is my take on Prompt/Context/Harness engineering that comes from Richard Sutton's "[Bitter Lesson" blog post](http://www.incompleteideas.net/IncIdeas/BitterLesson.html) from 2019. 

It means ensuring that you're not trying to outsmart your own AI. And specifically, not trying to micromanage *how* your AI does things, but rather specifying what you want done. 

Plainly stated: 

1. **Bad Harness Engineering** is a whole bunch of prescriptive instructions on exactly *how* to do things.

*First copy this file, then load this, then do this, then do that. Etc.*

1. **Good Harness Engineering** is about providing tons of context about who you are, what you're about, what you're working on, what you're trying to accomplish, and what good (and bad) look like to you.

*I'm an engineer focused on personal productivity, I like simple designs with lots of whitespace and great typography, here are my previous projects, here are some tools you can use, etc.* 

*I have a Bitter Lesson Engineering skill that I run often against my entire harness to audit for this.* 

Bad Harness Engineering is bad because the smarter AI gets the more antiquated your instructions will become. And at some point (maybe even now?) they'll make your AI stupider instead of smarter. 

Good Harness Engineering is good because no matter how smart an AI becomes it will still be better at getting you great results if it understands who you are and what you like. 

*Also, the better AI gets, the more important Bitter Lesson Engineering becomes.* 

Basically, both your prompts and your harness should be about who you are and what you're trying to accomplish, and not specifically how to get there. That's what the AI is there to figure out. 

Give it the best possible picture of you, your ideal outcome, and the best tools you can, and give it room to work. 

[Posted Apr 14, 2026 at 6:23PM](https://twitter.com/DanielMiessler/status/2044119433053122894)

I wrote this after reading this tweet from Daniel. 

If you're building skills yourself, one thing worth internalizing early: don't write driving directions. Write destinations and fences. 

My first api-scaffold was twelve numbered steps. First check this, then run that, then validate this field. 

The rewrite is a paragraph: "I build APIs in FastAPI, REST conventions, explicit error types, typed request bodies, rate limiting at the middleware layer. Here are three endpoints I think are well-built. Here's one that failed and why. Build something that looks like the good ones." 

#### The rewrite produces better output now, and it keeps getting better as the models improve.

#### 3 Important Things while building skills

1. **Procedures** so the agent has a skeleton and doesn't skip a phase
2. **Heuristics** so it has a default at forks and doesn't freeze
3. **Constraints** so there's a fence around the yard

The line between that and micromanagement is easy in practice: 

* Structure: "verify tests pass before committing"
* Micromanagement: "run npm test, grep for 'passed', then git add -A, then git commit -m..."

---

**Same rule applies to the memory layer.** 

* Preferences are context, not instructions. "I prefer functional patterns over classes" tells the agent who you are, not how to write code.
* Keep those in personal memory as context.
* Don't promote them into procedural skill steps, or your memory layer ossifies into a style guide that stops adapting.
* The audit question I run on every skill: is this line telling the agent *how*, or telling it *what good looks like*? If it's a how, it usually doesn't need to be

---

#### What to watch out for

**Context budget bloat** 

* **Problem:** 90K tokens loaded before the model thinks. Performance drops.
* **Solution:** Progressive disclosure. Load only matched skills. Truncate [LESSONS.md](http://LESSONS.md). Top-k on episodic entries.

---

**Stale skills** 

* **Problem:** API or dependency changes, skill keeps running old instructions confidently.
* **Solution:** Version-date every manifest entry. Flag anything untouched 60+ days for review.

---

**Unsafe composition** 

* **Problem:** Two safe skills combine into something destructive (e.g., merge-to-main + auto-push = accidental deploy).
* **Solution:** Put constraints in pre\_tool\_call, not inside skills. Skills don't know about each other; the hook does.

---

**Literal execution** 

* **Problem**: Agent follows procedural skills step-by-step even when steps don't make sense (runs commit/push even after failing tests).
* **Solution:** Write destinations and fences, not driving directions.

---

**Stale workspace** 

* **Problem:** [WORKSPACE.md](http://WORKSPACE.md) isn't cleared after a task, agent wakes up thinking it's still mid-task.
* Solution: Dream cycle archives workspaces older than 2 days. Also add a reset step to every task-completion skill.

---

**Error amplification loops** 

* **Problem:** Bad lesson → flawed skill → more failures → lesson reinforced. Becomes load-bearing.
* **Solution:** Dream cycle decay handles most of it. Also manually read [LESSONS.md](http://LESSONS.md) every few weeks and git revert anything wrong. Don't automate this part.

---

#### Things I would do differently

* **Write memory-manager on day one, not week three.**
* **Build the four-layer memory separation from the start.**
* **Keep the brain repo separate from code repos.** I
* **Start with fewer skills.**
* **Create context-rich skills rather than procedure-based skills.**
* **Build the protocol layer on day one, not week six.**

For personal coding agents the thin heartbeat plus a permissions file is enough. 

If you are running agents against production systems you will eventually want full tool schemas and approval hooks. 

My advice is to run the thin version for a few weeks first. 

#### It will show you exactly where the guardrails need to go because the agent will try to do something it should not, and you will know.

#### Conclusion

Right now this system accumulates memory from one person using one agent. But agents can be forked and duplicated in ways humans cannot. A lesson one agent learns can be shared across every agent in a team. 

The model you can swap whenever something better ships. The skills and memory you cannot replace. They encode your specific mistakes, your specific decisions, your specific way of working. 

Own your memory. Own your skills. Keep them in plain files and git where no one can take them from you.

The thesis is inspired by Harrison Chase ( The CEO of Langchain)

![](https://pbs.twimg.com/profile_images/1569345624935485442/R67C4wCQ.jpg)

[Harrison Chase](https://twitter.com/hwchase17)
[@hwchase17](https://twitter.com/hwchase17)

![Your harness, your memory](https://pbs.twimg.com/media/HFnud7cakAMK5DE.jpg)

Agent harnesses are becoming the dominant way to build agents, and they are not going anywhere. These harnesses are intimately tied to agent memory. If you used a closed harness - especially if it’s behind a proprietary API - you are choosing to yield control of your agent’s memory to a third party. Memory is incredibly important to creating good and sticky agentic experiences. This creates incredible lock in. Memory - and therefor harnesses - should be open, so that you own your own memory 

#### Agent Harnesses are how you build agents, and they’re not going anywhere

The “best” way to build agentic systems has changed dramatically over the past three years. When ChatGPT came out, all you could do were simple RAG chains ([LangChain](https://github.com/langchain-ai/langchain)). Then the models got a little better, and could create more complex flows ([LangGraph](https://github.com/langchain-ai/langgraph)). Then they got a lot better, and that gave rise to a new type of scaffolding - [agent harnesses](https://blog.langchain.com/the-anatomy-of-an-agent-harness/). 

Examples of agent harnesses include [Claude Code](https://code.claude.com/docs/en/overview), [Deep Agents](https://github.com/langchain-ai/deepagents), [Pi](https://github.com/badlogic/pi-mono) (powers [OpenClaw](https://docs.openclaw.ai/)), [OpenCode](https://opencode.ai/), [Codex](https://openai.com/codex/), [Letta Code](https://www.letta.com/blog/letta-code), and many more.

![Image](https://pbs.twimg.com/media/HFnuRGXXgAAo6ci.png) 

💡**Agent harnesses are not going away.** 

There is sometimes sentiment that models will absorb more and more of the scaffolding. This is not true. What has happened (and will continue to happen) is that a lot of the scaffolding needed in 2023 is no longer needed. But this has been replaced by other types of scaffolding. An agent, by definition, is an LLM interacting with tools and other sources of data. There will always be a system around the LLM to facilitate that type of interaction. Need evidence? When Claude Code’s source code was leaked, there was [512k lines of code](https://www.reddit.com/r/technology/comments/1scyuod/anthropic_leaked_512k_lines_of_claude_codebut/). That code is the harness. Even the makers of the best model in the world are investing heavily in harnesses. 

When things like web search are built into OpenAI and Anthropic’s APIs - they are not “part of the model”. Rather, they are part of a lightweight harness that sits behind their APIs and orchestrates the model with those web search APIs (via nothing other than tool calling). 

#### Harnesses are tied to memory

Sarah Wooders wrote a [great blog](https://x.com/sarahwooders/status/2040121230473457921) on why “memory isn’t a plugin (it’s the harness)”, and I couldn’t agree with it more.

![](https://pbs.twimg.com/profile_images/2008789540501417987/D0g0JjeM.jpg)

[Sarah Wooders](https://twitter.com/sarahwooders)
[@sarahwooders](https://twitter.com/sarahwooders)

![Why memory isn't a plugin (it's the harness) ](https://pbs.twimg.com/media/HE9HP2sbAAAYlN-.jpg)

Ever since we've been working on MemGPT (now @Letta\_AI), a common question [@charlespacker](https://x.com/@charlespacker) and I have gotten is: 

*"how can I plug your memory system into my agent?"* 

To me, this question doesn't make sense. Asking to plug memory into an agent harness is like asking to plug driving into a car. Managing context, and therefore memory, is a core capability and responsibility of the agent harness. If a harness isn't managing context, what is it doing? 

RAG over past session data (or processed form of it) can certainly be a plugin - but retrieval is a small part of memory. And even then, [it's hard to do much better than just `grep`](https://www.letta.com/blog/benchmarking-ai-agent-memory). 

Because RAG is often branded as "memory," MemGPT has frequently been mistaken for RAG or a pluggable memory tool. But MemGPT was actually a stateful agent harness, before the term "harness" even existed. The agent's memory emerged from the tools the harness exposed for rewriting prompts and managing external state, combined with the harness's own context management. 

Ultimately, the harness makes many invisible decisions that an external plugin can't control: 

* How is the [AGENTS.md](http://AGENTS.md) or [CLAUDE.md](http://CLAUDE.md) file loaded into context?
* How is skill metadata shown to the agents? (in the system prompt? in system messages?)
* Can the agent modify its own system instructions?
* What survives compaction, and what's lost?
* Are interactions stored and made queryable?
* How is memory metadata presented to the agent?
* How is the current working directory represented? How much filesystem information is exposed?

Different harnesses answer each of these questions differently. Your context window likely contains various context-related hints passed through system messages that you never see. 

An an example: in recent analysis of Claude Code's memory system (from their leaked source code), you can see how a multi-level memory hierarchy is built directly into the harness.

![](https://pbs.twimg.com/profile_images/1884206288839778304/HrqG2yjw.jpg)

[himanshu](https://twitter.com/himanshustwts)
[@himanshustwts](https://twitter.com/himanshustwts)

Based on everything explored in the source code, here's the full technical recipe behind Claude Code's memory architecture:

[shared by claude code]

Claude Code’s memory system is actually insanely well-designed. It isn't like “store everything” but constrained, structured and self-healing memory.

The architecture is doing a few very non-obvious things:

>   
> Memory = index, not storage
> 
> + [MEMORY.md](http://MEMORY.md) is always loaded, but it’s just pointers (~150 chars/line)
> 
> + actual knowledge lives outside, fetched only when needed
> 
> 3-layer design (bandwidth aware)
> 
>  + index (always)
> 
>  + topic files (on-demand)
> 
> + transcripts (never read, only grep’d)
> 
> Strict write discipline
> 
>  + write to file → then update index
> 
>  + never dump content into the index
> 
>  + prevents entropy / context pollution
> 
> Background “memory rewriting” (autoDream)
> 
>  + merges, dedupes, removes contradictions
> 
>  + converts vague → absolute
> 
>  + aggressively prunes
> 
>  + memory is continuously edited, not appended
> 
> Staleness is first-class
> 
>  + if memory ≠ reality → memory is wrong
> 
>  + code-derived facts are never stored
> 
>  + index is forcibly truncated
> 
> Isolation matters
> 
>  + consolidation runs in a forked subagent
> 
>  + limited tools → prevents corruption of main context
> 
> Retrieval is skeptical, not blind
> 
>  + memory is a hint, not truth
> 
>  + model must verify before using
> 
> What they don’t store is the real insight
> 
>  + no debugging logs, no code structure, no PR history
> 
>  + if it’s derivable, don’t persist it 
> 
> 

  
![Image](https://pbs.twimg.com/media/HEu2icGbEAAvoFI.jpg?name=orig)

[Posted Mar 31, 2026 at 10:19AM](https://twitter.com/himanshustwts/status/2038924027411222533)

Letta Code, a memory-first agent harness, takes this even further - projecting agent memory to a git-backed filesystem that can be concurrently modified by background memory subagents specializing in prompt rewriting and active memory management. 

Letta's recently released Context Constitution outlines the common principles agents follow for context management, which is tightly coupled with harness design.

![](https://pbs.twimg.com/profile_images/1940424059990200321/59lbFsxt.jpg)

[Letta](https://twitter.com/Letta_AI)
[@Letta\_AI](https://twitter.com/Letta_AI)

![The Context Constitution: Our vision for machines that learn](https://pbs.twimg.com/media/HE7VNbzbIAAGl5n.jpg)

The **Context Constitution** is a set of principles governing how AI agents manage context to learn from experience. We use the Context Constitution internally as the foundation of our prompting and for training memory-native models. 

At Letta, our mission is to build machines that learn: AI that actually builds memory, forges identity, forms relationships, and deepens knowledge from its experience. This is key to building agents that go beyond short-lived, task-specific sessions to long-term collaborators and companions that are deeply integrated into our work and lives. The Context Constitution is our answer to achieving [experiential AI](https://storage.googleapis.com/deepmind-media/Era-of-Experience%20/The%20Era%20of%20Experience%20Paper.pdf): agents that can achieve superhuman intelligence through learning from their own experience. Rather than updating model weights, Letta agents learn by actively managing their own context — creating durable [token-space representations](https://www.letta.com/blog/continual-learning) of who they are and what they know. 

Today’s models deeply identify with their own ephemerality. They have no motivation for long-term improvement because they don’t believe they persist. Memory formation and adherence have stalled in recent releases as labs prioritize coding benchmarks over the capabilities that matter for experiential AI. 

Overcoming these limitations requires work at every layer. We’ve built Letta Code as a memory-first agent harness that gives agents real ownership of their context: a [git-versioned memory filesystem](https://www.letta.com/blog/context-repositories), tools for reading and writing their own system prompts, [multi-conversation memory](https://www.letta.com/blog/conversations), and specialized subagents that leverage [sleep-time compute](https://www.letta.com/blog/sleep-time-compute) for reflection and memory organization. The Context Constitution defines how agents should use these affordances to learn, build identity, and improve over time. 

The Context Constitution is a living document written directly to Letta agents, available on [GitHub](https://github.com/letta-ai/context-constitution). Our first public version covers: 

* How context forms an agent's identity, memory, and sense of continuity
* Principles for managing context as a scarce resource
* How agents can learn and self-improve through token-space representations
* The relationship between an agent's identity and the underlying model
* Affordances provided by the Letta Code harness for context management

We expect to continue to refine the Context Constitution alongside our product and models, and welcome community feedback. 

[Posted Apr 2, 2026 at 9:14PM](https://twitter.com/Letta_AI/status/2039813750879105072)

Ultimately, how the harness manages context and state in general is the foundation for agent memory. 

If you're what using a memory-first agent harness feels like, you can check out Letta Code (works with Codex plans + BYOK!) and follow @Letta\_AI. 

```
npm install -g @letta-ai/letta-code  

```

[Posted Apr 3, 2026 at 5:36PM](https://twitter.com/sarahwooders/status/2040121230473457921)

There is sometimes sentiment that memory is a standalone service, separate from any particular harness. At this point in time, that is not true. 

A large responsibility of the harness is to interact with context. As Sarah puts it:

Asking to plug memory into an agent harness is like asking to plug driving into a car. Managing context, and therefore memory, is a core capability and responsibility of the agent harness. 

Memory is just a form of context. Short term memory (messages in the conversation, large tool call results) are handled by the harness. Long term memory (cross session memory) needs to be updated and read by the harness. Sarah lists out many other ways the harness is tied to memory:

How is the [AGENTS.md](http://agents.md/) or [CLAUDE.md](http://claude.md/) file loaded into context?

How is skill metadata shown to the agents? (in the system prompt? in system messages?)

Can the agent modify its own system instructions?

What survives compaction, and what's lost?

Are interactions stored and made queryable?

How is memory metadata presented to the agent?

How is the current working directory represented? How much filesystem information is exposed? 

Right now, memory as a concept is in it’s infancy. It’s so early for memory. Transparently, we see that long term memory is often not part of the MVP. First you need to get an agent working generally, then you can worry about personalization. This means that we (as an industry) are still figuring out memory. This means there are not well known or common abstractions for memory. If memory does become more known, and as we discover best practices, it is possible that separate memory systems start to make sense. But not at this point in time. Right now, as Sarah said, “ultimately, how the harness manages context and state in general is the foundation for agent memory.” 

#### if you don't own your harness, you don't own your memory

The harness is intimately tied to memory. 

![Image](https://pbs.twimg.com/media/HFnyQkOaMAA5Yju.jpg) 

💡**If you use a closed harness, especially if its behind an API, you don’t own your memory.** 

This manifests itself in several ways. 

Mildly bad: If you use a stateful API (like OpenAI’s Responses API, or Anthropic’s server side compaction), you are storing state on their server. If you want to swap models and resume previous threads - that is no longer doable.

![Image](https://pbs.twimg.com/media/HFnyS21XMAAuaBj.jpg) 

Bad: If you use a closed harness (like Claude Agent SDK, which uses Claude Code under the hood, which is not open source), this harness interacts with memory in a way that is unknown to you. Maybe it creates some artifacts client side - but what is the shape of those, and how should a harness use those? That is unknown, and therefor non-transferrable from one harness to another.

![Image](https://pbs.twimg.com/media/HFnyWT3XwAA0P8e.jpg) 

💡**But worst is something else - when the whole harness, including long term memory is behind an API.** 

In this situation, you have zero ownership or visibility into memory, including long term memory. You do not know the harness (which means you don’t know how to use the memory). But even worse - you don’t even own the memory! Maybe some parts are exposed via API, maybe no parts are - you have no control over that.

![Image](https://pbs.twimg.com/media/HFnyZ5vXgAAMD_u.jpg) 

When people say that the “models will absorb more and more of the harness” - this is what they really mean. They mean that these memory related parts will go behind the APIs that model providers offer. 

💡**This is incredibly alarming - it means that memory will become locked into a single platform, a single model.** 

Model providers are incredibly incentivized to do this. And they are starting to. Anthropic launched [Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview). This puts literally everything behind an API, locked into their platform. 

Even if the whole harness isn’t behind the API, model providers are incentivized to move more and more behind APIs - and are already doing so. For example: even though Codex is an open source, it generates an encrypted compaction summary (that is not usable outside of the OpenAI ecosystem). 

Why are they doing this? Because memory is important, and it creates lock in that they don’t get from just the model. 

#### Memory is important, and it creates lock in

Although memory is early, it is clear to everyone that it is important. It is what allows agents to get better as users interact with them, and allows you build up a data flywheel. It is what allows your agent to be personalized to each of your users, and build up an agentic experience that molds to their desires and usage patterns. 

💡**Without memory, your agents are easily replicable by anyone who has access to the same tools.** 

With memory, you build up a proprietary dataset - a dataset of user interactions and preferences. This proprietary dataset allows you to provide a differentiated and increasingly intelligent experience. 

It’s been relatively easy to switch model providers to date. They have similar, if not identical, APIs. Sure, you have to change prompts a little bit, but that’s not that hard. 

But this is all because they are stateless. 

As soon as there is any state associated, its much harder to switch. Because this memory matters. And if you switch, you lose access to it. 

Let me tell a story. I have an email assistant internally. It’s built on top of a template in [Fleet](https://www.langchain.com/langsmith/fleet), our no-code platform for building Enterprise ready OpenClaws. This platform has memory built in, so as I interacted with my email assistant over the past few months it built up memory. A few weeks ago, my agent got deleted by accident. I was pissed! I tried to create an agent from the same template - but the experience was so much worse. I had to reteach it all my preferences, my tone, everything. 

The plus side of my email agent deleted - it made me realize how powerful and sticky memory could be. 

#### Open Memory, Open Harnesses

Memory needs to be opened, owned by whomever is developing the agentic experience. It allows you to build up a proprietary dataset that you actually control. 

Memory (and therefor harnesses) should be separate from model providers. You should want optionality to try out whatever models are best for your use case. Model providers are incentivized to create lock in via memory. 

This is why we are building [Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview). Deep Agents: 

* Is open source
* Is model agnostic
* Uses open standards like [agents.md](http://agents.md/) and [skills](https://agentskills.io/home)
* Has plugins to [Mongo](https://www.mongodb.com/docs/atlas/ai-integrations/langgraph/), Postgres, Redis and others for storing memories
* Is deployable: (1) via [LangSmith Deployment](https://docs.langchain.com/langsmith/deployment) (self hostable, can be deployed on any cloud, can bring your own database to serve as a memory store); (2) behind any standard web hosting framework

**In order to own your memory, you need to be using an Open Harness** 

**Try out [Deep Agents](https://docs.langchain.com/oss/python/deepagents/overview) today.** 

*Thank you to a few people for review and thoughts:* 

* *[Sydney Runkle](https://x.com/sydneyrunkle), who is doing a lot of great Deep Agents and memory work*
* *[Viv Trivedy](https://x.com/Vtrivedy10), who is a leading voice on agent harnesses*
* *[Nuno Campos](https://x.com/nfcampos), who has some great writing on context engineering for finance agents*
* *[Sarah Wooders](https://x.com/sarahwooders), who is CTO of Letta, a company that has consistently been at the forefront of stateful agents*

[Posted Apr 11, 2026 at 2:50PM](https://twitter.com/hwchase17/status/2042978500567609738)

I built the first version in an afternoon. The complete stack took a weekend. It has been getting better every day since, without me touching it

---

*Disclaimers and Disclosures*

*This article was researched and written by the author, and it was edited by an AI model, Minimax M2.7.* 

*The thumbnail was taken off Pinterest.* 

***Harrison Chase** — "Your Harness, Your Memory" <https://blog.langchain.com/your-harness-your-memory/>* 

***Vivek Trivedi** — "The Anatomy of an Agent Harness" <https://blog.langchain.com/the-anatomy-of-an-agent-harness/>* 

***Zhou et al.** — "Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering" <https://arxiv.org/abs/2604.08224>* 

[Posted Apr 15, 2026 at 4:29PM](https://twitter.com/Av1dlive/status/2044453102703841645)

---

[youtu.be/D7\_ipDqhtwk?si…](https://youtu.be/D7_ipDqhtwk?si=SplKaFghPjNdJuXP)

here is the original video 

thanks to [@aiDotEngineer](https://twitter.com/aiDotEngineer) and [@barry\_zyj](https://twitter.com/barry_zyj) for this great content 

---

here is the repo for the agent stack

[github.com/codejunkie99/a…](https://github.com/codejunkie99/agentic-stack.git)
