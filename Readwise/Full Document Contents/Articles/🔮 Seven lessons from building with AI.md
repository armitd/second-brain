# 🔮 Seven lessons from building with AI

![rw-book-cover](https://substackcdn.com/image/fetch/w_1200,h_600,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2bea29b7-0b09-429e-8410-68264724b4cd_1024x1024.png)

## Metadata
- Author: [[Azeem Azhar]]
- Full Title: 🔮 Seven lessons from building with AI
- Category: #articles
- Summary: Organizations should integrate AI deeply into their workflows, not just as an add-on. By breaking tasks into smaller, modular components, teams can automate effectively and improve efficiency. Clear documentation and structured input help ensure that AI tools support human efforts, enhancing overall productivity.
- URL: https://www.exponentialview.co/p/seven-lessons-from-automating-our?utm_campaign=email-post&r=j1x1&utm_source=substack&utm_medium=email

## Full Document
[![Exponential View](https://substackcdn.com/image/fetch/w_80,h_80,c_fill,f_auto,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F46fc2cf0-7745-4c27-8875-94a97cb1fc9f_900x900.png)](https://www.exponentialview.co/)

### [Exponential View](https://www.exponentialview.co/)

##### Plus a stack of 40+ AI tools we use at Exponential View

> Before asking for more headcount and resources, teams must demonstrate why they cannot accomplish their goals using AI, explicitly showing what their area would look like if autonomous AI agents were integrated as part of the team.
> 
> 

*— Tobi Lütke, CEO of Shopify*

Tobi’s memo resonated widely because organizations now recognize what it truly means to integrate AI – not merely as an add-on but fundamentally into their operating structures.

At Exponential View, we’d embraced precisely this mindset to reimagine how we work. We consider ourselves AI-native, which means:

* We use AI reflexively; it’s a core skill for everyone.
* We’re tool-agnostic, continually evaluating and updating our stack.
* We build new workflows from scratch rather than just automating old ones.
* Our team is becoming increasingly technical – the baseline expectation for coding skills has risen significantly.
* At the same time, I’ve [encouraged my portfolio companies](https://www.exponentialview.co/p/how-to-win-as-the-world-changes) to scale through synthetic intelligence during this time of transformation.

In recent weeks, we sprinted to prototype new workflows using LLMs, automation tools and structured systems thinking. Today, I’ll share our most valuable lessons.

**At the end, you’ll get access to something unique: our internal stack of 40+ tools – everything we’re actively using, testing or intend to test – to help you decide what tools might work for you**.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7d9a9b5c-2668-4486-b74f-3e879693555d_1392x918.heic)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7d9a9b5c-2668-4486-b74f-3e879693555d_1392x918.heic)
Let’s jump into our seven lessons.

##### 1. The 5x rule

We’ve started applying a simple heuristic: if a task, or even a question, comes up five times a month, it’s a candidate for automation. This “5x rule” helps spot patterns hiding in plain sight and forces you to think in systems rather than routines. This habit sets the expectation that workflows should evolve constantly, not calcify.

Of course, we now ask the question “what do we do five times a month” more than five times a month, making that a candidate for automation.

One of my (Azeem’s) favourites is a simple workflow which does my expenses. I have to contend with dozens of invoices a month and my automations, relying on Dext and Gmail filters, are good but not great. Expense reconciliation has involved a lot of time in Gmail. My new expenses agent eliminates that repetition: it pulls out invoices, bills and receipts in my emails and puts them into a correctly structured spreadsheet. It also makes a PDF copy of the bill and sticks it into Google Drive. This saves me my least favourite hour every month.

If the bill is a plane, train or hotel booking it also dumps them into a different document. A separate agent reviews that document and turns it into a chronological, structured travel briefing which I use. With fifty travel days across ten trips to the end of June this is an enormous time saver – perhaps a dozen back-and-forths with Gmail has been replaced by the occasional check of this summary document.

##### 2. Modular workflows

One early and useful lesson in building with AI was to break down our workflows into smaller, autonomous components, rather than trying to automate an entire process in one go. This modular approach makes it easier to test individual pieces, troubleshoot in isolation and evolve parts of the system without destabilizing the whole.

This approach draws inspiration from classic software architecture: encapsulation and separation of concerns. But it also reflects how AI-native workflows behave. When you have an LLM doing part of the work, you want its task to be as narrow and unambiguous as possible. Broad instructions like “write a summary of the latest AI developments” often result in generic or unusable output. In contrast, narrower prompts like “list three key recent breakthroughs in battery technology and explain their relevance to electric vehicle adoption” yield precise answers and clearer points of failure, making them easier to improve iteratively.

One modular workflow we’ve found particularly valuable automates the discovery and initial research for potential partnerships. The first module scans our broader ecosystem, discovering companies actively engaging in areas aligned with our priorities. The second module enriches these initial leads, pinpointing key decision-makers and compiling relevant context from publicly available information. Finally, a third module– acting as our digital comms specialist – helps create outreach to get across as clearly as possible. The result is a process that frees our team to focus on building relationships rather than hunting down details.

A modular system also helps teams think like system designers. If Module A breaks, we know not to debug Module C. That clarity saves time. It also supports scale: when each unit functions independently, it’s easier to assign ownership, train interns, or plug in new AI tools.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F357858bf-45b1-4430-8c2b-8f7c982e8975_2002x1196.heic)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F357858bf-45b1-4430-8c2b-8f7c982e8975_2002x1196.heic)Some of us use Claude + Mermaid chart to sketch out projects and their modules for a visual work plan.
##### 3. LLMs as foremen, not just bricklayers

Treat the LLM as the foreman, not the worker. That is, use the model to structure the task, but don’t ask it to do everything. Once the model has identified what tasks need to be carried out, you can decide whether a given task is deterministic (in which case you may need to farm it out to traditional software code) or requires more judgement (in which case an LLM might be able to handle it.)

In practice, this means using Gemini 2.5 or Claude to first outline detailed, structured instructions which we then feed into another specialized AI or automation tool (like a Chrome extension script or a no-code platform such as n8n). While this might seem indirect at first, it’s the difference between giving vague directions and providing a clear blueprint. Clear blueprints get you consistently better outcomes.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6ea2efd9-ed20-4d1d-8535-0af6552603d4_750x1000.heic)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6ea2efd9-ed20-4d1d-8535-0af6552603d4_750x1000.heic)The masterful brickwork of the Gadi House in India, designed with artistry and engineering finesse, reminds us that the best outcomes emerge when forethought guides execution – just as LLMs should act as foremen, not bricklayers.
The biggest productivity gains come when people shift their role from doer to editor and orchestrator. When we use the LLM to lay out a framework, define categories or structure tasks, the rest of the workflow executes far more reliably.

As a result, we’ve stopped thinking of the LLM as a tool to *do* the task and started thinking of it as a tool to *define* the task.

We can use LLMs (my favourite is Gemini 2.5 Pro) to help craft specifications and of course, craft better prompts for the workflows. We’ll often use Gemini 2.0 Flash for a workflow because it is cheap and fast, but it isn’t the brightest. I’ll often have to tell Gemini 2.5 Pro that it needs to simplify the prompt because the LLM using it is not as smart as it is.

But even then, we learned that LLMs need guardrails. They excel at shaping structure, but they’re probabilistic by nature which makes them unpredictable in certain tasks. When reliability is critical, we often fall back on deterministic flows or narrow the model’s scope significantly. For instance, rather than asking it to “summarize this thread,” we might ask it to “extract three claims made by the author.” It’s a reminder that AI-native systems aren’t fully autonomous yet; they’re hybrid, blending probabilistic creativity with deterministic precision.

##### 4. Documentation as a living system

One of the earliest challenges we faced was keeping documentation up to date. Even with regular edits, specs would drift out of sync within a day or two—especially as we iterated quickly and changed components on the fly.

Our fix was surprisingly simple: get the LLM to document the system *as you build it*. Some of us use WisprFlow to capture voice notes while working, then generate summaries or system updates from the dictation. It’s not uncommon when working as a pair for someone to interrupt the conversation to talk to their computer so that it can go off and process something while the humans move on. Others drop current variables, prompts and task flows into a Google Doc and ask the LLM to rewrite the spec based on the current state of play.

The result is a lightweight, living documentation that’s never more than a few minutes out of date. It’s made onboarding smoother, debugging faster and coordination across the team much easier.

It’s also shifted how we think about memory and context. When your workflow is fluid and fast-evolving, the ability to snapshot the system on demand may be as important as the system itself.

##### 5. Research + prompting > Prompting alone

This lesson came from a failed attempt to design a new RAG (retrieval-augmented generation) pipeline for summarizing research papers.

Our colleague [Nathan Warren](https://open.substack.com/users/113368613-nathan-warren?utm_source=mentions) initially prompted Gemini for a system design using its existing knowledge. The result was superficial – a generic, unclear outline. He realized the LLM lacked up-to-date context on recent advancements. To fix this, he quickly queried the current state-of-the-art techniques from recent articles, GitHub repos and documentation, then fed that fresh context back into Gemini. With this updated information, Gemini was able to provide a detailed, actionable plan demonstrating that the key was updating the model’s knowledge to reflect the latest developments beyond its training data.

Instead of asking, “Can you draft a spec for a RAG system?,” he asked:

> Based on current best practices from LlamaIndex, ragas, and Cohere’s reranker, generate a RAG pipeline spec for summarizing long-form PDFs. The system should use sentence-level chunking, hybrid search with keyword fallback, and include evaluation metrics for factual consistency and coverage. Assume a vector DB like Weaviate or Qdrant, and an LLM like Claude 3. Add notes on scaling to 10K documents.
> 
> 

The difference was night and day. The new spec covered chunking strategy, latency considerations, and even output filtering logic. It went from generic fluff to actionable architecture.

The lesson here was that we should treat prompting as an act of curation, not just conversation. Bring the model’s recent techniques, working examples, and constraints – then let it build. The more structured your input, the more sophisticated your output.

##### 6. Time compression is the new emotional challenge

I’d set aside two hours to complete a complex, multi-step task, something that usually required switching between tools, reviewing materials and coordinating input from two people.

But with a new AI-driven workflow in place, I ran the steps through a series of modular prompts and automation scripts. The system parsed, filtered and structured the inputs with minimal human intervention. A light edit at the end and it was done in 15 minutes.

And yet, instead of feeling triumphant, I felt… unsettled. Had I missed something? Skipped a crucial step? Was the result too thin?

It wasn’t. The work was complete and it was good. But I hadn’t emotionally recalibrated to the new pace.

AI workflows compress time but my expectations didn’t keep up. The sense of “it can’t be done *yet*” lingers, even when the output is solid. It’s easy to spiral into unnecessary tweaking or double-checking just to fill the gap.

This taught me that AI doesn’t just shift how I work—it shifts my perception of work. Learning to trust the result—even when it feels “too fast”—is a new muscle. Emotional recalibration might become one of the key skills of the AI-native professional.

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff502370a-90e9-4603-9627-fa4f22e0be32_1536x1024.heic)](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff502370a-90e9-4603-9627-fa4f22e0be32_1536x1024.heic)Generated using 4o
##### 7. Humans are still core to the loop

Perhaps the most grounding reminder: our intern, Will, did stellar work. He jumped straight into one of the modules and shipped logic that’s now being used daily. His success wasn’t despite the AI tools – it was because of the scaffolding they provided.

By breaking the workflow into understandable parts, giving clear briefs generated by an LLM and providing updated documentation, we made it easier for a human contributor to plug in and deliver impact really fast.

The real unlock isn’t AI in isolation. It’s AI plus well-scaffolded humans. That’s how we scale our systems without losing our standards or our soul.

##### **Want to go deeper?**

**Here’s our [internal tool stack](https://docs.google.com/spreadsheets/d/1XD9FuYvnOIgCEylk7BrhXuBJ2q80HRCa6K1FJ83Sryc/edit?usp=sharing) — currently 40+ systems we’re using, testing, or watching closely available to members of Exponential View.** 

[![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0ed0c637-cf61-4858-9fb0-fd6fad162e83_1712x1112.heic)](https://docs.google.com/spreadsheets/d/1XD9FuYvnOIgCEylk7BrhXuBJ2q80HRCa6K1FJ83Sryc/edit?usp=sharing)
Our team members have a freedom to choose the tools they think help them get their job done, whether that is building in Python or using a higher-level framework. They can also choose the underlying model they use, although we share our experiences and evals with each other.
