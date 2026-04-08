# He Built an AI Audience Simulator. It’s the Future of Customer Research.

![rw-book-cover](https://d24ovhgu8s7341.cloudfront.net/uploads/post/social_media_image/3471/audiebce.png)

## Metadata
- Author: [[Dan Shipper]]
- Full Title: He Built an AI Audience Simulator. It’s the Future of Customer Research.
- Category: #articles
- Summary: Michael Taylor created an AI Audience Simulator called Rally, which helps businesses test ideas by simulating real audience feedback without risks. This tool allows users to quickly and cheaply A/B test headlines and concepts, making it a valuable part of the creative process. The podcast episode featuring Michael discusses how AI can enhance customer research and improve decision-making.
- URL: https://every.to/podcast/100-ai-personas-said-you-d-click-this

## Full Document
![](https://d24ovhgu8s7341.cloudfront.net/uploads/post/cover/3471/audiebce.png)Every illustration/'AI & I.'
Prompt engineer Michael Taylor created a tool that simulates real audience feedback—without the risk

*TL;DR: Today we’re releasing a new episode of our podcast* [AI & I](https://every.to/podcast)*. I go in depth with* ***Michael Taylor****, a freelance prompt engineer and the author of our column* [Also True for Humans](https://every.to/also-true-for-humans)*. We get into how good AI can be at simulating an audience—and how we can use that to test our ideas and assumptions.* ***Watch on*** [***X***](https://x.com/danshipper/status/1894762331122655328) ***or*** [***YouTube***](https://www.youtube.com/watch?v=eREPh47BZbE)***, or listen on*** [***Spotify***](https://open.spotify.com/episode/3mn7JQCYKttIJywp78XH98?si=c4ea0ea386be42c3&nd=1&dlsi=6bfb20a0da6f4147)***.*** *Here’s a link to* [*the* ***episode transcript***](https://every.to/admin/posts/transcript-test-your-ideas-before-they-go-live/)*.*

*Was this newsletter forwarded to you?* [*Sign up*](https://every.to/account) *to get it in your inbox.*

[**Michael Taylor**](https://x.com/hammer_mt) has perfected the art of getting AI to speak in tongues. He’s taught it to mimic the voices of your customers—so you can see how they would respond before you ship.

Michael is the creator of [Rally](https://askrally.com/), a market research tool that lets you simulate an audience of AI personas. He [built a simulator](https://every.to/also-true-for-humans/i-created-a-hacker-news-simulator-to-reverse-engineer-what-goes-viral) that lets us A/B test Every’s headlines on an audience that mimics the real Hacker News audience. It’s become a part of my writing workflow, and I love it because you test your assumptions quickly, cheaply, and without any of the risks of putting something out into the world.

Besides Rally, Michael co-authored a [book](https://www.amazon.com/Prompt-Engineering-Generative-AI-Future-Proof/dp/109815343X/) on prompt engineering for O’Reilly, and he writes a [column](https://every.to/also-true-for-humans) for Every about managing AI tools like you would people. In a past life, he founded a growth marketing agency which he grew to 50 people and sold in 2020. One of the reasons I’m drawn to Michael’s work is because he has a tinkerer’s mindset. He’s always exploring the limits of what a new technology can do, and what he’s into today, everyone else will likely discover six months later. We spent an hour talking about using language models to judge your work, best practices for assessing an AI’s performance, and Michael’s flow inside [Cursor](https://www.cursor.com/). He also demos Rally live on the show, testing three different potential headlines for an Every article.

You can check out our conversation here:

If you want a quick summary, here are some of the themes we touched on:

**AI can be very good at simulating people** (00:04:30)

If you’re a regular Every reader I hope you’re using [role prompting](https://every.to/also-true-for-humans/ai-works-better-when-you-make-it-pretend), or telling the language model to respond like an expert in a specific field. You’d be surprised at how effective it is. Almost a year ago, I gave GPT-4 some information about me, like my tweets and a few journal entries, and got it to take a personality test as me. Then I had my girlfriend at the time take the test while pretending to be me. GPT-4’s responses [were more aligned to my own](https://every.to/chain-of-thought/does-gpt-4-know-me-better-than-my-girlfriend) than hers.

**Get the wisdom of the crowds** (00:08:45)

Our editor in chief **Kate Lee** and I had a difference of opinion in October last year. I wanted to describe Every as a “meta” media company, while Kate liked the prefix “multimodal.” Michael happened to be writing an article about [simulating 100 AI personas for market research](https://every.to/also-true-for-humans/how-i-made-ai-think-like-a-focus-group), so we enlisted a virtual focus group to settle the debate. The AI personas chose “multimodal,” with each one detailing the reasons for their choice, and as I read through them, I changed my mind. This was one of the pushes for Michael to build and launch Rally. I love the tool because it's a way to get fair, quantitative feedback on your ideas in a risk-free environment.

**Why your ideas still matter** (00:12:23)

This doesn’t mean that we will turn into content zombies because everyone is producing cookie-cutter content that’s been optimized for virality. The results you get from Rally are dependent on many different variables, like the demographics of the AI audience and the specific question you ask. The space of possibilities is huge, and people will start at different places within the landscape—leading them to different results. “[T]his expands the space in which you can play in, but it's still your duty to play—you still have to come up with good ideas,” Michael adds.

**Making AI into a sharper judge** (00:15:04)

Michael mentions that LLMs are better at judging copywriting than finalizing it. I push him to tell me his process because I struggle with this: Whenever I get Claude to grade my essays, the AI invariably gives me a B-plus or A-minus—and if I prompt it again after making a few edits, it bumps the grade up to an A.

Michael explains that language models are indeed bad at this kind of grading because they tend to “overestimate the middle,” giving you an average score. To get around this tendency, he creates a collection of criteria for a particular task, each one evaluated on a binary scale. For example, if one criterion for a good article is that it should be concise, he’ll get the LLM to judge on a scale of “zero” or “one” whether an article is concise. “I’ll build up maybe 20 of these for any tasks that I'm automating, then I’ll run my testing suite—and each one is an LLM judge that just checks that ‘zero’ or ‘one’—and when I combine that score together, it gives me an aggregate score that is much more reliable,” he says.

**Best practices for evaluating performance** (00:19:00)

As we go deeper on getting LLMs to be judges, Michael and I start talking about a topic I’m personally interested in: running evaluations, specifically for [Cora](https://cora.computer/), our AI email tool. Cora reads your emails and sends you a “brief” that summarizes your inbox, twice a day. We’re working on improving the quality of these summaries, and designing evals to measure the same.

In order to give the LLM an example of what a “good” summary is, I rewrite the summaries that Cora generates. It’s an interesting task because even though I can write a good summary, I often can’t articulate the rule I’m following.

With the context of my process, Michael walks me through how he would make evals for Cora. He would collect examples of the summaries Cora generated and the ones I’ve rewritten in a [Jupyter](https://jupyter.org/) notebook and ask Claude or GPT-4 what the difference between the two versions is. He would get the LLM to boil the differences down into bullet points, and each one would become a criterion for evaluation.

**Why prompt engineering won’t die** (00:27:01)

Around a year ago, a popular sentiment was that prompt engineering would become irrelevant as language models became more powerful. People assumed that the gap between your objective and the AI’s output would decrease. I think the mistake they made was underestimating the effort in articulating what your objective is.

Michael agrees with me. His theory is that this misconception took root because many early users of AI had engineering backgrounds. “You don't realize how messy the world is when you're an engineer—and I say that as someone who was a business person and now is a full-time engineer…they are completely right that for well-specified tasks, you don't need to do prompt engineering anymore…but so much of the world is completely unspecified,” he says.

**AI favors the bold, not just the big** (00:44:59)

Another popular sentiment that’s proving to be false is the assumption that in the age of AI, incumbent companies with deep pockets and distribution will inevitably win. Adopting a new technology isn’t just about resources—it’s fundamentally about risk tolerance. Established companies are averse to risk, and I think that creates a fertile ground for startups to grow.

Michael points out that while this is true, big companies are innovating faster today than they ever have. He remembers attending a conference full of Fortune 500 executives just two months after ChatGPT released—and seeing around 80 percent already working on generative AI projects.

**How Michael uses Cursor to go from idea to execution** (00:55:03)

Michael uses [Cursor](https://www.cursor.com/) to ship features for Rally. He starts by recording himself talking about an idea, uses [Gemini](https://gemini.google.com/) to transcribe the audio, and prompts Claude to generate a draft [product requirements document](https://every.to/podcast/she-built-an-ai-product-manager-bringing-in-six-figures-as-a-side-hustle-e46be9bc-f426-424d-992d-5a71fd7ac5e4). After editing the document himself, Michael uploads it to Cursor, giving the agent a free hand to execute the project. When development hits a roadblock, he resolves it by sharing the relevant context [with o1](https://every.to/chain-of-thought/openai-s-o1-model-explained).

This episode is a must watch for founders, marketers, and anyone who wants to make better decisions without long, expensive feedback loops. Here’s a link to the [episode transcript](https://every.to/admin/posts/transcript-test-your-ideas-before-they-go-live/).

You can check out the episode on X, Spotify, Apple Podcasts, or YouTube. Links are below:

* [Watch on X](https://x.com/danshipper/status/1894762331122655328)
* [Watch on YouTube](https://www.youtube.com/watch?v=eREPh47BZbE)
* [Listen on Spotify](https://open.spotify.com/episode/3mn7JQCYKttIJywp78XH98?si=c4ea0ea386be42c3&nd=1&dlsi=6bfb20a0da6f4147) (make sure to follow to help us rank!)

What do you use AI for? Have you found any interesting or surprising use cases? We want to hear from you—and we might even interview you. Reply here to talk to me!

Miss an episode? Catch up on my recent conversations with star podcaster [**Dwarkesh Patel**](https://every.to/chain-of-thought/dwarkesh-patel-s-quest-to-learn-everything), LinkedIn cofounder [**Reid Hoffman**](https://every.to/chain-of-thought/reid-hoffman-on-how-ai-might-answer-our-biggest-questions), *a16z Podcast* host [**Steph Smith**](https://every.to/chain-of-thought/the-internet-creator-s-guide-to-the-future), economist [**Tyler Cowen**](https://every.to/chain-of-thought/economist-tyler-cowen-on-how-chatgpt-is-changing-your-job), writer and entrepreneur [**David Perell**](https://every.to/chain-of-thought/how-david-perell-uses-chatgpt-to-write-for-millions), founder and newsletter operator [**Ben Tossell**](https://every.to/chain-of-thought/how-to-run-a-profitable-one-person-internet-business-using-ai), and others, and learn how *they* use AI to think, create, and relate.

If you’re enjoying my work, here are a few things I recommend:

* to Every
* Follow [me](https://twitter.com/danshipper) on X
* Subscribe to Every’s [YouTube channel](https://www.youtube.com/@EveryInc)

*Thanks to* ***Rhea Purohit*** *for editorial support.*

***Dan Shipper*** *is the cofounder and CEO of Every, where he writes the* [*Chain of Thought*](https://every.to/chain-of-thought) *column and hosts the podcast* [AI & I](https://open.spotify.com/show/5qX1nRTaFsfWdmdj5JWO1G). *You can follow him on X at* [*@danshipper*](https://twitter.com/danshipper) *and on* [*LinkedIn*](https://www.linkedin.com/in/danshipper/)*, and Every on X at* [*@every*](https://twitter.com/every) *and on* [*LinkedIn*](https://www.linkedin.com/company/everyinc/)*.*

*We* [*build AI tools*](https://every.to/studio) *for readers like you. Automate repeat writing with* [***Spiral***](https://spiral.computer/?utm_source=everyfooter)*. Organize files automatically with* [***Sparkle***](https://makeitsparkle.co/?utm_source=everyfooter)*. Write something great with* [***Lex***](https://lex.page/?utm_source=everyfooter)*. Deliver yourself from email with* [***Cora***](https://cora.computer/)*.*

*We also do AI training, adoption, and innovation for companies.* [*Work with us*](https://every.to/consulting?utm_source=emailfooter) *to bring AI into your organization.*

*Get paid for sharing Every with your friends. Join our* [*referral program*](https://every.getrewardful.com/signup)*.*
