# AI and the automation of work

![rw-book-cover](http://static1.squarespace.com/static/50363cf324ac8e905e7df861/5055cb1de4b0a751cabaedd5/6492ff3078695b7b2d072912/1688333375153/2880px-Ilia_Efimovich_Repin_%281844-1930%29_-_Volga_Boatmen_%281870-1873%29.jpg?format=1500w)

## Metadata
- Author: [[View fullsize]]
- Full Title: AI and the automation of work
- Category: #articles
- Summary: Generative AI tools like ChatGPT are being experimented with in the workplace, but they won't replace existing workflows quickly due to their complexity. Businesses require tailored solutions that consider security and management, not just general technology. Additionally, AI can produce varied responses based on patterns, which can lead to inaccuracies, highlighting the need for careful integration into specialized tasks.
- URL: https://www.ben-evans.com/benedictevans/2023/7/2/working-with-ai

## Full Document
What does that mean for generative AI in the workplace? Whatever you think will happen, it will take years, not weeks. 

First, the tools that people use for work, and the tasks that might now get a new layer of automation, are complicated and very specialised, and embody a lot of work and institutional knowledge. A lot of people are *experimenting* with ChatGPT, and seeing what it will do. If you’re reading this, you probably have too. That doesn’t mean that ChatGPT has replaced their existing workflows *yet*, and replacing or automating any of those tools and tasks is not trivial. 

There’s a huge difference between an amazing demo of a transformative technology and something that a big complicated company holding other people’s business can use. You can rarely go to a law firm and sell them an API key to GCP’s translation or sentiment analysis: you need to wrap it in control, security, versioning, management, client privilege and a whole bunch of other things that only legal software companies know about (there’s a graveyard of machine learning companies that learnt this in the last decade). Companies generally can’t buy ‘technology’. [Everlaw](https://www.everlaw.com) doesn’t sell translation and [People.ai](https://www.people.ai) doesn’t sell sentiment analysis - they sell tools and products, and often the AI is only one part of that. I don’t think a text prompt, a ‘go’ button and a black-box, general purpose text generation engine make up a product, and product takes time. 

Second, buying tools that manage big complicated things takes time even once the tool is built and has product-market fit. One of the most basic challenges in building an enterprise software startup is that startups run on an 18 month funding cycle and a lot of enterprises run on an 18 month decision cycle. SaaS itself accelerated this because you don’t need to get into the enterprise datacenter deployment schedule, but you still need purchase, integration and training, and companies with millions of customers and tens or hundreds of thousands of employees have very good reasons not to change things suddenly. The future takes a while, and the world outside Silicon Valley is complicated. 

The second objection is that part of the paradigm shift of ChatGPT and LLMs is a shift in the layer of abstraction: this looks like a much more general purpose technology. Indeed, that’s why it’s exciting. It can answer *anything,* we are told. So, you could look at that chart of 473 enterprise SaaS apps and say that ChatGPT will disrupt that and collapse many those vertical apps into one prompt box. That would mean it would move faster, and also automate much more. 

I think that misunderstands the problem. If a partner at a law firm wants a first draft of a paper, they want to be able to shape the parameters in completely different ways to a salesperson at an insurance company challenging a claim, probably with a different training set and certainly with a bunch of different tooling. Excel is ‘general purpose’ too, and so is SQL, but how many different kinds of ‘database’ are there? This is one reason I think the future of LLMs is to move from prompt boxes to GUIs and buttons - I think ‘prompt engineering’ and natural language’ are mutually contradictory. But either way, even if you can run everything as a thin wrapper on top of one giant foundational model (and there is very little agreement or clarity about this yet), even those wrappers will take time.

More fundamental, of course, there is the error rate. ChatGPT can *try* to answer ‘anything’ but the answer might be wrong. People call this hallucinations, making things up, lying or bullshitting - it’s the ‘overconfident undergraduate’ problem. I think these are all unhelpful framings: I think the best way to understand this is that when you type someone into a prompt, you’re not actually asking it to answer a question at all. Rather, you’re asking it “what sort of answers would be people be likely to produce to questions that look like this?” You’re asking it to match a pattern. 

Hence, if I ask ChatGPT4 to write a biography of myself, and then ask it again, it gives different answers. It suggests I went to Cambridge, Oxford or the LSE; my first job was in equity research, consulting or financial journalism. These are always the right pattern: it’s the right kind of university and the right kind of job (it never says Anglia Poly and then catering management). It is giving 100% correct answers to the question “what **kinds** of degrees and jobs are people **like** Benedict **likely** to have done?” It’s not doing a database lookup: it’s making a pattern. 

You can see something similar in this image I got from MidJourney. The prompt was “A photograph of advertising people discussing creativity on stage in a panel on a beach at Cannes Lions.”
