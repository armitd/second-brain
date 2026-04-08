# What Can Language Models Actually Do?

![rw-book-cover](https://d24ovhgu8s7341.cloudfront.net/uploads/post/social_media_image/3465/IMG_4571.png)

## Metadata
- Author: [[Dan Shipper]]
- Full Title: What Can Language Models Actually Do?
- Category: #articles
- Summary: Language models can compress and summarize text to make it easier for readers to understand. They can provide comprehensive summaries or engaging headlines, depending on the need. This ability helps enhance human creativity by delivering knowledge in a useful format.
- URL: https://every.to/chain-of-thought/what-can-language-models-actually-do-371b969e-d470-4639-a9fa-f873c133c19b

## Full Document
![](https://d24ovhgu8s7341.cloudfront.net/uploads/post/cover/3465/IMG_4571.png)DALL-E/Every illustration.
Language models as text compressors

*The world has changed considerably since our last* [*”think week”*](https://every.to/context-window/thinking-up-the-future) *five months ago—and so has Every. We’ve added new* [*business*](https://every.to/on-every/introducing-every-studio) [*units*](https://every.to/on-every/introducing-every-consulting)*,* [*launched*](https://every.to/p/introducing-cora-manage-your-inbox-with-ai) [*new*](https://every.to/on-every/introducing-spiral-v2) [*products*](https://every.to/on-every/introducing-extendable-articles)*, and brought on new teammates. So we've been taking this week to come up with new ideas and products that can help us improve how we do our work and, more importantly, your experience as a member of our community. In the meantime, we’re re-upping four pieces by* ***Dan Shipper*** *that cover basic, powerful questions about AI. (Dan hasn’t been publishing at his regular cadence because he’s working on a longer piece. Look out for that in Q2.) Yesterday we re-published his* [*jargon-free explainer*](https://every.to/chain-of-thought/how-language-models-work-ea805869-4778-4fb8-ad8f-2d10cc439b4c) *of how language models work. Today we’re re-upping his* [*piece*](https://every.to/chain-of-thought/what-can-language-models-actually-do) *about how language models function as compressors—or summarizers—of text.*—[*Kate Lee*](https://every.to/on-every/kate-lee-joins-every-as-editor-in-chief)

*Was this newsletter forwarded to you?* [*Sign up*](https://every.to/account) *to get it in your inbox.*

I want to help save our idea of human creativity. Artificial intelligence can write, illustrate, design, code, and much more. But rather than eliminating the need for human creativity, these new powers can help us redefine and expand it.

We need to do a [technological dissection](https://every.to/chain-of-thought/chatgpt-and-the-future-of-the-human-mind) of language models, defining what they can do well—and what they can’t. By doing so, we can isolate our own role in the creative process.

If we can do that, we’ll be able to wield language models for creative work—and still call it creativity.

To start, let’s talk about what language models *can* do.

#### The psychology and behavior of language models

The current generation of language models is called *transformers*, and in order to understand what they do, we need to take that word seriously. What kind of *transformations* can transformers do?

Mathematically, language models are recursive next-token predictors. They are given a sequence of text and predict the next bit of text in the sequence. This process runs over and over in a loop, building upon its previous outputs self-referentially until it reaches a stopping point. It’s sort of like a snowball rolling downhill and picking up more and more snow along the way.

But this question is best asked at a higher level than simply mathematical possibility. Instead, what are the inputs and outputs we observe from today’s language models? And what can we infer about how they think?

In essence, we need to study LLMs’ behavior and psychology, rather than their biology and physics.

This is a sketch based on experience. It’s a framework I’ve built for the purposes of doing great creative work with AI.

#### A framework for what language models do

Language models transform text in the following ways:

* Compression: They compress a big prompt into a short response.
* Expansion: They expand a short prompt into a long response.
* Translation: They convert a prompt in one form into a response in another form.

These are manifestations of their outward behavior. From there, we can infer a property of their psychology—the underlying thinking process that creates their behavior:

* Remixing: They mix two or more texts (or learned representations of texts) together and interpolate between them.

I’m going to break down these elements in successive parts of this series over the next few weeks. None of these answers are final, so consider this a public exploration that’s open for critique. Today, I want to talk to you about the first operation: compression.

##### Language models as compressors

Language models can take any piece of text and make it smaller:

[![](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/3082/optimized_5Tq2gD1Muk2a4tRNN8xPnFbmHeiVTj7FMvby7V2WLDYlNve_z5zZ-o1ZzEQZd3lAWmurtaG5API_Ql_N1gUJtjbmKtwtcCLo88wOj2i_nfJSvnisC3BtBXwBtPj7sCQgiWunuMtpGnyaYrt7.png)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/3082/optimized_5Tq2gD1Muk2a4tRNN8xPnFbmHeiVTj7FMvby7V2WLDYlNve_z5zZ-o1ZzEQZd3lAWmurtaG5API_Ql_N1gUJtjbmKtwtcCLo88wOj2i_nfJSvnisC3BtBXwBtPj7sCQgiWunuMtpGnyaYrt7.png?link=true)
*Source: All images courtesy of the author.*

This might seem simple, but, in fact, it’s a marvel. Language models can take a big chunk of text and smush it down like a foot crushing a can of Coke. Except it doesn’t come out crushed—it comes out as a perfectly packaged and proportional mini-Coke. And it’s even drinkable! This is a Willy Wonka-esque magic trick, without the Oompa Loompas.

Language model compression comes in many different flavors. A common one is what I’ll call *comprehensive* compression, or summarization.

##### Language models are comprehensive compressors

Humans comprehensively compress things all the time—it’s called summarization. Language models are good at it in the same way a fifth grader summarizes a children’s novel for a book report, or the app [Blinkist](https://www.blinkist.com/en/lp) summarizes nonfiction books for busy professionals.

This kind of summarizing is intended to take a source text, pick out the ideas that explain its main points for a general reader, and reconstitute those into a compressed form for faster consumption:

[![](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/3082/optimized_w_s9uA9XpkcOlUPDUuSl9Z8UQKrOEbk0AKBHQ7dQ4CPc3vMkvDPNvInQjD4P5ZCKI1rJIoPO84N_Hid5w9JcfH7B_rgAsQkDItxz6LUjnStpzPST4CGlY3WvAsvN6c8vzfyDYp0PD_WDoe-t.png)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/3082/optimized_w_s9uA9XpkcOlUPDUuSl9Z8UQKrOEbk0AKBHQ7dQ4CPc3vMkvDPNvInQjD4P5ZCKI1rJIoPO84N_Hid5w9JcfH7B_rgAsQkDItxz6LUjnStpzPST4CGlY3WvAsvN6c8vzfyDYp0PD_WDoe-t.png?link=true)
These summaries are intended to be both comprehensive (they note all the main ideas) and helpful for the average reader (they express the main ideas at a high level with little background knowledge assumed).In the same way, a language model like Anthropic’s Claude, given the text of the Ursula K. LeGuin classic *A Wizard of Earthsea*, will easily output a comprehensive summary of the book’s main plot points:

[![](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/3082/optimized_uassCnZHIUzfN-VWOs7NJKIbTfvpmLpvA6w_Mo4sV19DMzfWk5OQSkxQdMpxJLT7sm4D9qzhFNTYMLotq3Uh6W5LlGjIgLTqWN4SnXje2si9VXZEf_QPm1Mq53Pzy1CCnfF2s8VrUgAD0v3F.png)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/3082/optimized_uassCnZHIUzfN-VWOs7NJKIbTfvpmLpvA6w_Mo4sV19DMzfWk5OQSkxQdMpxJLT7sm4D9qzhFNTYMLotq3Uh6W5LlGjIgLTqWN4SnXje2si9VXZEf_QPm1Mq53Pzy1CCnfF2s8VrUgAD0v3F.png?link=true)
But comprehensive compression isn’t the only thing language models can do. You can compress text without being comprehensive—which creates room for totally different forms of compression.

##### Language models are engaging compressors

If we require our compression to be *interesting* instead of comprehensive, compressions look less like book reports and more like email subject lines, article headlines, book titles, and subtitles. If we graphed them by how much attention is required to consume them, it would look like this:

[![](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/3082/optimized__kGHAQPp70xruKbqa5tWJ3NtBnSYsRARHLKHN0nBiw6b3uZs77KBc5xIO3MQK72fsrBF0d2DYChCkCs6nMoKR8lMG3e6dtk_Wg-TFC1iY9cJW8peMSN6TpfRlrG1QlMWXzCN-Zuhg3m_-_sm.png)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/3082/optimized__kGHAQPp70xruKbqa5tWJ3NtBnSYsRARHLKHN0nBiw6b3uZs77KBc5xIO3MQK72fsrBF0d2DYChCkCs6nMoKR8lMG3e6dtk_Wg-TFC1iY9cJW8peMSN6TpfRlrG1QlMWXzCN-Zuhg3m_-_sm.png?link=true)
Through this lens, book titles are just as much a *compression* as a kid’s book report; they just prioritize different requirements for what the compression is trying to capture. Language models excel at this type of compression, too.For example, at Every we use an internal AI tool to help us turn the content of our stories into headlines. It’s specifically aimed at interestingness, as opposed to comprehensiveness. When I fed it the text of *A Wizard of Earthsea*, it suggested these titles:

* *The Shadow's Name*
* *The Warrior Mage's Shadow Quest*
* *The Shadow Defeated*

These are pretty good! But language model compression doesn’t stop at just these two dimensions of compression.

##### Language models compress over many different dimensions

There are many dimensions along which compression can be run. Here are some examples of headlines, all written by Claude:

* Clickbaiting: "You Won’t Believe What This Young Wizard Discovered on a Shadow Isle!"
* Intrigue: "Secrets of the Shadowy Mage Isle"
* Vibe-y: "chill wizard explores shady island, finds self"
* Alliteration: "The Wizard’s Winding, Wondrous Wanderings"
* Snark: "Oh, Another 'Chosen One' Wizard Story Set on an Island, How Original"
* Paranoia: "They’re Watching: A Wizard’s Harrowing Shadow Odyssey"
* Pessimism: "The Gloomy Account of a Doomed Mage on Hopeless Shadow Rock"
* Confusion: "Wait, What's Happening? A Wizard Goes Somewhere Shadowy, I Think?"
* Absurdist: "Schrödinger's Wizard Simultaneously Visits and Doesn't Visit Shadow Isle"
* Ironic detachment: "I Guess This Wizard Goes to Some Dumb Island or Whatever"
* Gaslighting: "There Is No Shadow Isle, You're Just Imagining Things"

When we started talking about compression, we began with this graphic:

[![](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/3082/optimized_5Tq2gD1Muk2a4tRNN8xPnFbmHeiVTj7FMvby7V2WLDYlNve_z5zZ-o1ZzEQZd3lAWmurtaG5API_Ql_N1gUJtjbmKtwtcCLo88wOj2i_nfJSvnisC3BtBXwBtPj7sCQgiWunuMtpGnyaYrt7.png)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/3082/optimized_5Tq2gD1Muk2a4tRNN8xPnFbmHeiVTj7FMvby7V2WLDYlNve_z5zZ-o1ZzEQZd3lAWmurtaG5API_Ql_N1gUJtjbmKtwtcCLo88wOj2i_nfJSvnisC3BtBXwBtPj7sCQgiWunuMtpGnyaYrt7.png?link=true)
If we wanted to revise it with our expanded idea of compression along many different dimensions, we might do something like this:

[![](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/3082/optimized_OKU6HsLebi076ER9vDOH8wi2jlAdXuOBo03WDkkl_He5UBjTjgNIsiOAUzWI1l1m-ehac54bQvFm534VO9Z_58f6eL_B5lpDANUv3M4SFQrWGzA2VSFq5JDM7htLUNhOkgMF9B9QOkW9IO8g.png)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/3082/optimized_OKU6HsLebi076ER9vDOH8wi2jlAdXuOBo03WDkkl_He5UBjTjgNIsiOAUzWI1l1m-ehac54bQvFm534VO9Z_58f6eL_B5lpDANUv3M4SFQrWGzA2VSFq5JDM7htLUNhOkgMF9B9QOkW9IO8g.png?link=true)
Language model compression doesn’t just turn a large gray rectangle into a small gray rectangle. It can turn it into a tiny rectangle, or a red rectangle with rounded corners, or an elongated rectangle with a gradient fill.Each of the outputs of compression carry some [family resemblance](https://en.wikipedia.org/wiki/Family_resemblance) to the original input. In other words, there’s always some amount of common overlap between the prompt and response, but the exact overlap (and the areas of difference) is going to depend on the type of compression you’re running.

The dimensions of compression can also be arbitrarily specific and combined together. Here are some example prompts:

* A tweet in the style of Dan Shipper but with more snark and paranoia
* Analysis in the style of George Saunders but make it gaslight-y
* A book summary in the style of a Scott Alexander book review, but make it concise

For example, using the last prompt as a jumping-off point, here’s a concise book summary of *A Wizard of Earthsea* that Claude created in the style of Scott Alexander from [Slate Star Codex](https://www.astralcodexten.com/):

> “*A Wizard of Earthsea* is about the dangers of power without wisdom. 

> The young wizard Ged, in a fit of youthful pride and anger, summons a shadow creature from the realm of the dead. This goes about as well as you would expect. The shadow hunts Ged across the world and he must flee from it, until finally his old master tells him that he can't run away from his own shadow. Ged realizes that the only way out is through—he has to turn around, chase down the shadow, and reintegrate it into himself. 

> This is a pretty standard "power corrupts" story, but it's unusually wise in depicting Ged's flaw not as a desire for power itself, but as a lack of education in how to use power. Ged isn't evil, he's just young and dumb. 

> His eventual victory comes from understanding how the universe works, not from overwhelming firepower. The real treasure was the wisdom he gained along the way. 

> Le Guin once said her books were about ‘the journey that is inward, and not the other journey.’

>  *A Wizard of Earthsea* literalizes this, as Ged sails further and further away from the known lands in pursuit of his shadow, only to realize he has to integrate it back into himself. We all have to take this journey eventually. The shadow represents the parts of ourselves we try to deny and push away. But there's no escape—in the end, the only way to grow is to acknowledge your shadow, accept it, and become whole.”

I don’t know if this is *exactly* what Scott Alexander would write about *A Wizard of Earthsea*, but it’s certainly in the neighborhood. There are a few things it gets right. The first line is a concise, engaging summary of the book’s main point, which Alexander does better than almost anyone. And the line, “This is a pretty standard ‘power corrupts’ story,” feels very much like his voice.

So we’ve made some progress. Our concept of language models as compressors now includes the idea that they “compress” text across an arbitrary number of dimensions or requirements.

When is that useful in creative work?

#### Why compression is useful

Let’s start with comprehensive compressions like book reports. If we graphed them by the amount of depth they convey and attention they require, they would probably be on the bottom-left quadrant of the graph—little depth, little attention required:

[![](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/3082/optimized_6EJj3n9akrpUg9nu5qAyleKxHZQ6cdsMZAVN3mKvY3BYAJYg-Xd03Udvk0QEloY1Fy8gkTUl3goo3-C8wJmRHxBLLCHz6I9xMWB9qqWNz0X7ToGoJmfx1ZIuOIQp0DP8Nz6qIcYesFtvGxD5.png)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/3082/optimized_6EJj3n9akrpUg9nu5qAyleKxHZQ6cdsMZAVN3mKvY3BYAJYg-Xd03Udvk0QEloY1Fy8gkTUl3goo3-C8wJmRHxBLLCHz6I9xMWB9qqWNz0X7ToGoJmfx1ZIuOIQp0DP8Nz6qIcYesFtvGxD5.png?link=true)
Things that exist in this bottom-left quadrant have a pejorative connotation because they require a low level of engagement with a complex idea:

[![](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/3082/optimized_3M4JAHr1E5nt3YvrHsyz2-XIIAYeDDus_ivuTrl9ETp1h-ZHeuTYCo1kiOBfyM6eA8H8GoHOCsPrGUQDRt1iwE6LzPLVW_ZyYoLctD8t440ic_L7e9oJlHzyfC1fJNZ2ldZ02_GkHFKKXEEd.png)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/3082/optimized_3M4JAHr1E5nt3YvrHsyz2-XIIAYeDDus_ivuTrl9ETp1h-ZHeuTYCo1kiOBfyM6eA8H8GoHOCsPrGUQDRt1iwE6LzPLVW_ZyYoLctD8t440ic_L7e9oJlHzyfC1fJNZ2ldZ02_GkHFKKXEEd.png?link=true)
Comprehensive compressions are the McDonald’s french fries of the intellectual landscape: ubiquitous, tasty, cheap, and low status.But this kind of summary is an important output of creative work because it respects the fundamentally limited attention of human beings. Humans need to roam widely over the intellectual landscape before they go deep, and this kind of summary allows us to sample ideas that might be useful without a lot of investment. In that way, it’s like a mini-advertisement for the idea it contains—like a blooming flower is an advertisement for nectar.

The trouble is that doing compressions like this is, generally, drudgery. Anyone who has had to write a summary of their essay for an X post, or has needed to spend a few hours rereading a complex topic so that they could summarize it in a few sentences, will know what I mean.

But language models are good at compression that sits more at the bottom of the funnel of engagement with ideas, too. They help you go deeper into the nuances of an idea instead of just skimming the surface:

[![](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/3082/optimized_ukoK7wB42Y5ERJGdtc41beWx5guJA9Z3rySS5NZD2Y7J5vPMsfekC_P5F5qjmQNXZ4QiJiAcyzjuOwN3lC6G8cW0cHeNueeUl44zZ6pEySP7g2j6W76cmyg3v3vJtNjgYnlDBHxK00sbGm0i.png)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/3082/optimized_ukoK7wB42Y5ERJGdtc41beWx5guJA9Z3rySS5NZD2Y7J5vPMsfekC_P5F5qjmQNXZ4QiJiAcyzjuOwN3lC6G8cW0cHeNueeUl44zZ6pEySP7g2j6W76cmyg3v3vJtNjgYnlDBHxK00sbGm0i.png?link=true)
In a needle-in-the-haystack compression, they can find the answer to a difficult question in a long piece of text. For example, I’ve long been a fan of Ludwig Wittgenstein’s philosophical thinking, but his writing is incredibly dense. I’ve fed one of his books into Claude and gotten answers to specific questions—which is a compression of the book into a form that’s usable for me:

[![](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/3082/optimized_8CzHL8ArJppRiG8gKmDaQ2IrCphVWNYAMo7WfMVJo8QltTF7TRhzFSAhs3cfcIM8RR3rHzGldmuIJPrCA3YepyPp-dpRfb65Dm9Qc7mqgkf5UVLBENjgE9PjTaVP-YRTjntaIRj8QlXYwFM1.png)](https://d24ovhgu8s7341.cloudfront.net/uploads/editor/posts/3082/optimized_8CzHL8ArJppRiG8gKmDaQ2IrCphVWNYAMo7WfMVJo8QltTF7TRhzFSAhs3cfcIM8RR3rHzGldmuIJPrCA3YepyPp-dpRfb65Dm9Qc7mqgkf5UVLBENjgE9PjTaVP-YRTjntaIRj8QlXYwFM1.png?link=true)
Instead of puzzling over the text, I can think up new ideas and create new pieces of writing that were previously impossible. There’s too much information to consume, and it’s too complicated for me to understand without this kind of support.Once you start to look at things this way, you’ll see compression everywhere. Emails are often compressions of what people said in meetings. Poems are compressions of sensory experiences. Good decisions are compressions of the results of previous decisions. Basic programming is compressions of Stack Overflow answers.

This view of the world will help you see a significant chunk of the situations in which language models can be useful for creative work.

As the cognitive scientist Alison Gopnik has written, language models are [cultural technologies](https://every.to/chain-of-thought/chatgpt-and-the-future-of-the-human-mind?sid=41918). They give us the best of what humanity knows about any topic—in the right form for any given context. In that way, language models are an extension of a trend that started with writing itself and has extended to the printing press, the internet, and finally our present moment with AI.

This is a superpower for creatives:

Knowledge can make its way to you—wherever you are, whenever you need it, compressed in just the right format for you to use.

What do you want to make with it?

***Dan Shipper*** *is the cofounder and CEO of Every, where he writes the* [*Chain of Thought*](https://every.to/chain-of-thought) *column and hosts the podcast* [AI & I](https://open.spotify.com/show/5qX1nRTaFsfWdmdj5JWO1G). *You can follow him on X at* [*@danshipper*](https://twitter.com/danshipper) *and on* [*LinkedIn*](https://www.linkedin.com/in/danshipper/)*, and Every on X at* [*@every*](https://twitter.com/every) *and on* [*LinkedIn*](https://www.linkedin.com/company/everyinc/)*.*

*We* [*build AI tools*](https://every.to/studio) *for readers like you. Automate repeat writing with* [***Spiral***](https://spiral.computer/?utm_source=everyfooter)*. Organize files automatically with* [***Sparkle***](https://makeitsparkle.co/?utm_source=everyfooter)*. Write something great with* [***Lex***](https://lex.page/?utm_source=everyfooter)*. Deliver yourself from email with* [***Cora***](https://cora.computer/)*.*

*We also do AI training, adoption, and innovation for companies.* [*Work with us*](https://every.to/consulting?utm_source=emailfooter) *to bring AI into your organization.*

*Get paid for sharing Every with your friends. Join our* [*referral program*](https://every.getrewardful.com/signup)*.*
