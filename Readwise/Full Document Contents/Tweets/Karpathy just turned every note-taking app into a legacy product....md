# Karpathy just turned every note-taking app into a legacy product...

![rw-book-cover](https://pbs.twimg.com/profile_images/2021355466216062976/8MDXp7vR.jpg)

## Metadata
- Author: [[Aakash Gupta]]
- Full Title: Karpathy just turned every note-taking app into a legacy product...
- Category: #tweets
- Summary: Karpathy just turned every note-taking app into a legacy product in a single thread.

The workflow: dump raw sources into a folder, let the LLM compile a markdown wiki, maintain all the links, run data quality checks, and answer complex questions across 400K words. The human never writes or edits the wiki. The LLM does all of it autonomously.

The part people will skip past: he expected to need vector databases and RAG pipelines. He didn't. The LLM maintains its own index files and summaries, reads the relevant context on demand, and handles ~100 articles without fancy retrieval infrastructure. That's a signal about how fast in-context learning is outrunning the systems most companies are spending millions to build right now.

Then the roadmap gets wilder. Synthetic data generation plus finetuning so the LLM internalizes your research corpus into its weights. Going from "LLM reads your knowledge base" to "LLM has become your knowledge base."

Every second brain app just became a transitional technology.
- URL: https://twitter.com/aakashgupta/status/2039893404356939968/?rw_tt_thread=True

## Full Document
Karpathy just turned every note-taking app into a legacy product in a single thread.

The workflow: dump raw sources into a folder, let the LLM compile a markdown wiki, maintain all the links, run data quality checks, and answer complex questions across 400K words. The human never writes or edits the wiki. The LLM does all of it autonomously.

The part people will skip past: he expected to need vector databases and RAG pipelines. He didn't. The LLM maintains its own index files and summaries, reads the relevant context on demand, and handles ~100 articles without fancy retrieval infrastructure. That's a signal about how fast in-context learning is outrunning the systems most companies are spending millions to build right now.

Then the roadmap gets wilder. Synthetic data generation plus finetuning so the LLM internalizes your research corpus into its weights. Going from "LLM reads your knowledge base" to "LLM has become your knowledge base."

Every second brain app just became a transitional technology. 

![](https://pbs.twimg.com/profile_images/1296667294148382721/9Pr6XrPB.jpg)

[Andrej Karpathy](https://twitter.com/karpathy)
[@karpathy](https://twitter.com/karpathy)

LLM Knowledge Bases

Something I'm finding very useful recently: using LLMs to build personal knowledge bases for various topics of research interest. In this way, a large fraction of my recent token throughput is going less into manipulating code, and more into manipulating knowledge (stored as markdown and images). The latest LLMs are quite good at it. So:

Data ingest:

I index source documents (articles, papers, repos, datasets, images, etc.) into a raw/ directory, then I use an LLM to incrementally "compile" a wiki, which is just a collection of .md files in a directory structure. The wiki includes summaries of all the data in raw/, backlinks, and then it categorizes data into concepts, writes articles for them, and links them all. To convert web articles into .md files I like to use the Obsidian Web Clipper extension, and then I also use a hotkey to download all the related images to local so that my LLM can easily reference them.

IDE:

I use Obsidian as the IDE "frontend" where I can view the raw data, the the compiled wiki, and the derived visualizations. Important to note that the LLM writes and maintains all of the data of the wiki, I rarely touch it directly. I've played with a few Obsidian plugins to render and view data in other ways (e.g. Marp for slides).

Q&A:

Where things get interesting is that once your wiki is big enough (e.g. mine on some recent research is ~100 articles and ~400K words), you can ask your LLM agent all kinds of complex questions against the wiki, and it will go off, research the answers, etc. I thought I had to reach for fancy RAG, but the LLM has been pretty good about auto-maintaining index files and brief summaries of all the documents and it reads all the important related data fairly easily at this ~small scale.

Output:

Instead of getting answers in text/terminal, I like to have it render markdown files for me, or slide shows (Marp format), or matplotlib images, all of which I then view again in Obsidian. You can imagine many other visual output formats depending on the query. Often, I end up "filing" the outputs back into the wiki to enhance it for further queries. So my own explorations and queries always "add up" in the knowledge base.

Linting:

I've run some LLM "health checks" over the wiki to e.g. find inconsistent data, impute missing data (with web searchers), find interesting connections for new article candidates, etc., to incrementally clean up the wiki and enhance its overall data integrity. The LLMs are quite good at suggesting further questions to ask and look into.

Extra tools:

I find myself developing additional tools to process the data, e.g. I vibe coded a small and naive search engine over the wiki, which I both use directly (in a web ui), but more often I want to hand it off to an LLM via CLI as a tool for larger queries. 

Further explorations:

As the repo grows, the natural desire is to also think about synthetic data generation + finetuning to have your LLM "know" the data in its weights instead of just context windows.

TLDR: raw data from a given number of sources is collected, then compiled by an LLM into a .md wiki, then operated on by various CLIs by the LLM to do Q&A and to incrementally enhance the wiki, and all of it viewable in Obsidian. You rarely ever write or edit the wiki manually, it's the domain of the LLM. I think there is room here for an incredible new product instead of a hacky collection of scripts. 

[Posted Apr 2, 2026 at 8:42PM](https://twitter.com/karpathy/status/2039805659525644595)

---

To get all my takes without an algorithmic filter, subscribe to my newsletter:

[aibyaakash.com](http://www.aibyaakash.com)
