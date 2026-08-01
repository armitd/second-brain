# from prompt → context → harness → loop → graph...

![rw-book-cover](https://pbs.twimg.com/profile_images/1578327351544360960/YFpWSWIX.jpg)

## Metadata
- Author: [[Akshay 🚀]]
- Full Title: from prompt → context → harness → loop → graph...
- Category: #tweets
- Summary: from prompt → context → harness → loop → graph engineering.

the list keeps growing, and every new term gets treated as a replacement for the last one. each layer wraps the one before it, and the cleanest way to tell them apart is to ask what a single unit of work looks like.

𝗽𝗿𝗼𝗺𝗽𝘁 𝗲𝗻𝗴𝗶𝗻𝗲𝗲𝗿𝗶𝗻𝗴 𝗶𝘀 𝘁𝗵𝗲 𝗺𝗲𝘀𝘀𝗮𝗴𝗲.

the model remembers nothing before this call, so the prompt has to carry the full universe of what it needs. a role, the background, the instructions, a few examples, a format.

when the output falls short, the skill is working out which ingredient let you down, not rewriting the instructions every time.

the unit of work is one input.

𝗰𝗼𝗻𝘁𝗲𝘅𝘁 𝗲𝗻𝗴𝗶𝗻𝗲𝗲𝗿𝗶𝗻𝗴 𝗶𝘀 𝘁𝗵𝗲 𝗺𝗲𝗺𝗼𝗿𝘆.

across many steps the window is finite and the available information is not, which forces a curation step. a curator keeps what matters, compresses what is useful but bulky, and drops the rest.

good curation is mostly about knowing what to throw away, not packing more in.

the unit of work is what stays in the window.

𝗵𝗮𝗿𝗻𝗲𝘀𝘀 𝗲𝗻𝗴𝗶𝗻𝗲𝗲𝗿𝗶𝗻𝗴 𝗶𝘀 𝘁𝗵𝗲 𝗺𝗮𝗰𝗵𝗶𝗻𝗲.

on its own a model just generates text. the harness gathers what it needs, runs it, calls tools or sub-agents, and verifies the result with tests or a judge.

that verify step is the entire difference between calling an api and running an agent.

the unit of work is one pass through the machine.

𝗹𝗼𝗼𝗽 𝗲𝗻𝗴𝗶𝗻𝗲𝗲𝗿𝗶𝗻𝗴 𝗶𝘀 𝘁𝗵𝗲 𝗿𝘂𝗻.

one pass rarely finishes the job, so something has to decide whether to run the machine again. that decision needs a goal defined upfront, brakes like max iterations and budget caps, and a completion check that is automated rather than felt.

an agent that stops asking for tools has ended its turn, which is not the same as finishing the task.

the unit of work is the whole run.

the diagram covers those four. here is the fifth.

𝗴𝗿𝗮𝗽𝗵 𝗲𝗻𝗴𝗶𝗻𝗲𝗲𝗿𝗶𝗻𝗴 𝗶𝘀 𝘁𝗵𝗲 𝗰𝗼𝗼𝗿𝗱𝗶𝗻𝗮𝘁𝗶𝗼𝗻.

once several loops have to work together, you need to say what runs when, what runs in parallel, and who checks whom. nodes do the work, edges decid...
- URL: https://twitter.com/akshay_pachaar/status/2081356379026280677/?rw_tt_thread=True

## Full Document
from prompt → context → harness → loop → graph engineering.

the list keeps growing, and every new term gets treated as a replacement for the last one. each layer wraps the one before it, and the cleanest way to tell them apart is to ask what a single unit of work looks like.

𝗽𝗿𝗼𝗺𝗽𝘁 𝗲𝗻𝗴𝗶𝗻𝗲𝗲𝗿𝗶𝗻𝗴 𝗶𝘀 𝘁𝗵𝗲 𝗺𝗲𝘀𝘀𝗮𝗴𝗲.

the model remembers nothing before this call, so the prompt has to carry the full universe of what it needs. a role, the background, the instructions, a few examples, a format.

when the output falls short, the skill is working out which ingredient let you down, not rewriting the instructions every time.

the unit of work is one input.

𝗰𝗼𝗻𝘁𝗲𝘅𝘁 𝗲𝗻𝗴𝗶𝗻𝗲𝗲𝗿𝗶𝗻𝗴 𝗶𝘀 𝘁𝗵𝗲 𝗺𝗲𝗺𝗼𝗿𝘆.

across many steps the window is finite and the available information is not, which forces a curation step. a curator keeps what matters, compresses what is useful but bulky, and drops the rest.

good curation is mostly about knowing what to throw away, not packing more in.

the unit of work is what stays in the window.

𝗵𝗮𝗿𝗻𝗲𝘀𝘀 𝗲𝗻𝗴𝗶𝗻𝗲𝗲𝗿𝗶𝗻𝗴 𝗶𝘀 𝘁𝗵𝗲 𝗺𝗮𝗰𝗵𝗶𝗻𝗲.

on its own a model just generates text. the harness gathers what it needs, runs it, calls tools or sub-agents, and verifies the result with tests or a judge.

that verify step is the entire difference between calling an api and running an agent.

the unit of work is one pass through the machine.

𝗹𝗼𝗼𝗽 𝗲𝗻𝗴𝗶𝗻𝗲𝗲𝗿𝗶𝗻𝗴 𝗶𝘀 𝘁𝗵𝗲 𝗿𝘂𝗻.

one pass rarely finishes the job, so something has to decide whether to run the machine again. that decision needs a goal defined upfront, brakes like max iterations and budget caps, and a completion check that is automated rather than felt.

an agent that stops asking for tools has ended its turn, which is not the same as finishing the task.

the unit of work is the whole run.

the diagram covers those four. here is the fifth.

𝗴𝗿𝗮𝗽𝗵 𝗲𝗻𝗴𝗶𝗻𝗲𝗲𝗿𝗶𝗻𝗴 𝗶𝘀 𝘁𝗵𝗲 𝗰𝗼𝗼𝗿𝗱𝗶𝗻𝗮𝘁𝗶𝗼𝗻.

once several loops have to work together, you need to say what runs when, what runs in parallel, and who checks whom. nodes do the work, edges decide what runs next, and shared state flows between them.

a single loop is just a one-node graph with an edge pointing back at itself, which is why graphs govern loops instead of replacing them.

the unit of work is the whole job.

here is the part that ties it together.

prompt and context both live inside the harness gather step. the harness is one pass, the loop decides whether to run that pass again, and the graph decides which loops run at all.

zoom out and the unit of work gets bigger. zoom in and you are back at the prompt.

that also tells you where to debug. find the layer whose unit of work broke, then fix that layer.

the prompt is the easiest layer to edit, which is why it keeps taking the blame for failures that live three layers up.

i also published this deep dive on graph engineering, covering the core idea, how to get started, shared state, routing you can trust, and when a graph is genuinely overkill.

the article is quoted below. 

![](https://pbs.twimg.com/profile_images/1578327351544360960/YFpWSWIX.jpg)

[Akshay 🚀](https://twitter.com/akshay_pachaar)
[@akshay\_pachaar](https://twitter.com/akshay_pachaar)

![Graph Engineering Clearly Explained ](https://pbs.twimg.com/media/HOGCCe-aUAAXzQF.jpg)

Loop engineering got about six weeks in the spotlight before the timeline moved on. 

On July 18, Peter Steinberger, the person behind OpenClaw, posted a nine-word question. "Are we still talking loops or did we shift to graphs yet?"

![Image](https://pbs.twimg.com/media/HOF0SHLbEAAfDBs.jpg) 

A few hours later, Hamel Husain published an article titled "Loop Engineering Is Dead. Enter Graph Engineering."

![Image](https://pbs.twimg.com/media/HOF0XAnacAAm-TD.jpg) 

Both were at least half joking. The field renames itself so fast that mocking the renaming has become its own genre. 

But the joke landed on something real. The moment you have several loops that need to work together, you have a coordination problem, and graphs are how engineers have always described coordination. 

That's the whole idea behind graph engineering. Now let's separate the substance from the meme. 

### First, the graph itself

A graph is three things. 

* **Nodes** are units of work, whether that's an agent, a plain model call, a deterministic function, a tool, or a human approving something.
* **Edges** decide what runs next, either in sequence, in parallel, or conditionally based on what the last node produced.
* **State** is a shared object that flows along the edges. Every node reads from it and writes to it.

Some content could not be imported from the original document. [View content ↗](https://twitter.com/akshay_pachaar/status/2081356379026280677/?rw_tt_thread=True) 

This is the starter graph almost every example uses. A researcher gathers material, a writer drafts, a reviewer judges. If the review passes, the run ends. If it fails, an edge sends the draft back to the writer. 

Three nodes, four edges, and one of those edges is a loop. 

Here's the part that reframes everything. A single agent loop is just a one-node graph with an edge pointing back to itself. Graphs don't replace loops. They connect and govern them.

![Image](https://pbs.twimg.com/media/HOF1N2SagAAzyPU.jpg) 

### The stack kept growing

The center of gravity in AI keeps drifting away from the model, and each shift picked up a name. 

* **Prompt engineering.** The words you send.
* **Context engineering.** Everything the model sees, not just your instructions.
* **Harness engineering.** The code around the model that runs tools, tracks state, and handles errors.
* **Loop engineering.** The autonomous cycle that drives one agent toward a goal.
* **Graph engineering.** The coordination layer across many loops, covering what runs when, in what order, and who checks whom.

Each layer wraps the one before it. A graph is made of loops, each loop needs a good harness, each harness call is a context problem, and every context contains prompts. Skip a lower layer and the graph just fails in a more elaborate way.

![Image](https://pbs.twimg.com/media/HOF74j8boAAI44E.jpg) 

One more thing worth being honest about. None of this is new technology. LangGraph shipped this exact model, nodes and edges over shared state, back in January 2024. Microsoft's AutoGen has GraphFlow, and Google built ADK 2.0's entire workflow runtime on the same idea. The name is new, the practice isn't, which is why one of the top replies to Hamel's post was simply "welcome back, langchain." 

So the discipline isn't inventing graphs. It's knowing when to use one, and how to keep it from rotting. That part has four hard problems. 

### Hard part 1: knowing when a node deserves to exist

The most common failure is turning "summarize this PDF" into a five-node graph with a fetcher, a chunker, a summarizer, a reviewer, and a formatter. 

A node earns its place only if it represents a real specialty, meaning a different model, a different toolset, or a genuinely separate role like a read-only reviewer. Steps you could inline into an existing loop are not nodes. 

A useful filter comes from the practitioners writing about this. If you can't draw the graph on a napkin, it's too complex. And if collapsing two nodes into one loses nothing, they were never two nodes. 

### Hard part 2: keeping shared state clean

In a loop, the failure mode is context rot. In a graph, the same disease moves into shared state. 

Every node writes to the state object, so a sloppy write in node two becomes a confident input for node five. Nobody notices until the output is wrong, and by then the bad data has flowed through half the system.

![Image](https://pbs.twimg.com/media/HOF8slQaUAE4NOB.jpg) 

The solutions are simple and boring, yet effective. Give the state a typed schema. Decide explicitly which nodes may write to which fields. Checkpoint state between nodes so you can replay a run and see exactly where it went bad. 

One caution applies to replay. Nodes after a checkpoint execute again, so any node with external side effects, like sending an email or creating a record, must be safe to run twice. 

### Hard part 3: routing you can trust

An edge is a decision, and the question is who makes it. 

If a model decides the route, you get flexibility and instability in the same package. The same state can take different paths on different runs, which makes debugging miserable.

Google's design rule for ADK 2.0 is the cleanest position in the discourse. Deterministic code should control predictable routing, and models should only handle the steps that need actual judgment. 

Route with code wherever the condition is checkable, and spend model calls only where interpretation is genuinely required. 

### Hard part 4: agents agreeing with each other

Loop engineering's sharpest rule was to never let an agent grade its own homework. 

Graphs raise the stakes. Twenty agents built on the same base model, reading the same flawed context, will happily agree with each other, and models measurably prefer their own outputs. 

The result feels like an "organized nonsense" at industrial scale, impeccable structure wrapped around a wrong answer. 

The fix is a reviewer node with teeth. Run it on a different model, give it fresh context instead of the full conversation, and anchor its verdict to evidence the graph can't fabricate, like tests that actually ran or code that actually compiled.

![Image](https://pbs.twimg.com/media/HOF9QHTakAAy_hY.jpg) 

Cognition landed in the same place after a year of running Devin, their coding agent. Their working setup lets several agents read the work and weigh in, but only one agent is ever allowed to change anything. 

That split is the useful part. Reading is safe to do in parallel, because a bad opinion costs you nothing until someone acts on it. Writing is where the damage happens, so you keep it in one place where you can see it. 

### Where the graph is overkill

The honest answer is most of the time. 

Anthropic's published numbers make the cost concrete. A single agent burns roughly 4x the tokens of a chat interaction, and multi-agent systems burn roughly 15x. Every node you add multiplies that.

![Image](https://pbs.twimg.com/media/HOGBHWcbMAAbXlV.jpg) 

The ceiling is real when the task genuinely parallelizes. Anthropic's multi-agent research system outperformed a single Opus agent by 90.2% on their internal research eval, because research fans out into independent searches naturally. But their standing advice from Building Effective Agents hasn't changed. Find the simplest solution possible, and only add complexity when the task demands it.

Even LangGraph's own guidance says the quiet part. If your agent is a straightforward loop with tools, LangGraph is overkill. 

The decision rule is pretty straightforward: Reach for a graph when the work splits into genuine specialties, needs parallel fan-out and join, needs different models per step, or needs failure isolation and auditable routing. Otherwise stay in the loop. 

### Where to start

You don't need an org chart of agents on day one. Build up to it. 

* Master a single loop first, with brakes, a real completion check, and a critic. A graph of weak loops is just distributed failure.
* Draw the graph on paper before writing code, and challenge every node to justify its existence.
* Define the state schema and write access up front. State drift is the main way graphs rot.
* Make the reviewer node a different model with fresh context, and anchor it to external evidence.
* Put budget caps on every node. A graph is many loops spending tokens in parallel, and a weak verifier now burns money concurrently.

### Key takeaway

Graph engineering isn't a new discipline replacing loop engineering. It's the name that stuck for a decision every agent builder eventually faces. When one loop stops being enough, coordination becomes the engineering. 

The word may not survive the year. The design question will. 

Here's a summary of key takeaways in graph engineering.

![Image](https://pbs.twimg.com/media/HOGBSq1bUAAmkya.jpg) 

Thanks for reading! 

Cheers :) 

Akshay. 

[Posted Jul 25, 2026 at 6:48PM](https://twitter.com/akshay_pachaar/status/2081089131808243999)
