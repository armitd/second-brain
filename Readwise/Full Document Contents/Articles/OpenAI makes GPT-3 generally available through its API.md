# OpenAI makes GPT-3 generally available through its API

![rw-book-cover](https://venturebeat.com/wp-content/uploads/2021/08/GettyImages-1157449117.jpg?w=1024?w=1200&strip=all)

## Metadata
- Author: [[Kyle Wiggers]]
- Full Title: OpenAI makes GPT-3 generally available through its API
- Category: #articles
- Summary: OpenAI has made its GPT-3 language model available to all developers through its API. The model can write text, create code, and answer questions, but it still has issues with bias and harmful content. OpenAI is working on safety tools and guidelines to help developers use GPT-3 responsibly.
- URL: https://venturebeat.com/ai/openai-makes-gpt-3-generally-available-through-its-api/

## Full Document
![OpenAI logo seen displayed on a smartphone. ](https://venturebeat.com/wp-content/uploads/2021/08/GettyImages-1157449117.jpg?w=750)Image Credit: Rafael Henrique/SOPA Images/LightRocket via Getty Images
*Join our daily and weekly newsletters for the latest updates and exclusive content on industry-leading AI coverage. [Learn More](https://venturebeat.com/newsletters/?utm_source=VBsite&utm_medium=desktopNav)*

OpenAI today [removed the waitlist](https://openai.com/blog/api-no-waitlist/) for GPT-3, its large language model that can automatically [write emails and articles](https://bdtechtalks.com/2020/08/24/ai-blog-gpt-3-fake-news/), compose poetry, create code across a dozen programming languages, and more. Starting today, any developer in a [supported country](https://beta.openai.com/docs/supported-countries) can sign up to begin integrating the model with their app or service.

Built by OpenAI, GPT-3 and its fine-tuned derivatives, like [Codex](https://venturebeat.com/2021/07/18/openai-codex-shows-the-limits-of-large-language-models/), can be customized to handle applications that require a deep understanding of language, from converting natural language into software code to summarizing large amounts of text and generating answers to questions. GPT-3 has been publicly available since 2020 through the OpenAI API; as of March, OpenAI [said](https://openai.com/blog/gpt-3-apps/) that GPT-3 was being used in more than 300 different apps by “tens of thousands” of developers and producing 4.5 billion words per day.

“Safety progress” made GPT-3’s move from private beta to beta possible, according to OpenAI. Over the past year, the company has developed endpoints for “more truthful” question-answering, provided a content filter to help mitigate abuse, and implemented models — “instruct” models — that ostensibly adhere better to human instructions.

For example, OpenAI claims that the instruct models, which share the base GPT-3’s natural language generation abilities, are more adept at understanding and following directions like “Explain the moon landing to a six-year-old in a few sentences.” The question-answering endpoints allow developers to provide additional context for apps that require “high accuracy” generations based on sources of truth, like documentation and knowledge bases. And the content filter aims to detect generated text that could be sensitive coming from the API.

“We believe that by opening access to these models via an easy-to-use API, more developers will find creative ways to apply AI to a large number of useful applications and open problems,” OpenAI wrote in a blog post. “To ensure API-backed applications are built responsibly, we provide tools and help developers use best practices so they can bring their applications to production quickly and safely. As our systems evolve and we work to improve the capabilities of our safeguards, we expect to continue streamlining the process for developers, refining our usage guidelines, and allowing even more use cases over time.”

#### AI safeguards

But OpenAI admits that these improvements don’t solve the toxicity problem inherent in large language models. GPT-3 remains far from technically perfect — the model was trained on more than 600GB of text from the web, a portion of which came from communities with [gender](https://venturebeat.com/2020/08/07/researchers-quantify-bias-in-reddit-content-sometimes-used-to-train-ai/), race, [physical](https://venturebeat.com/2020/10/08/nyus-crowdsourced-questions-probe-extent-of-language-model-bias/), and religious prejudices. Studies show that it, like other large language models, amplifies the biases in data on which it was trained.

In [a paper](https://venturebeat.com/2021/02/16/ai-can-persuade-people-to-make-ethically-questionable-decisions-study-finds/), the Middlebury Institute of International Studies’ Center on Terrorism, Extremism, and Counterterrorism found that GPT-3 can generate “influential” text that could radicalize people into far-right extremist ideologies. A group at Georgetown University has used GPT-3 to generate misinformation, including stories around a false narrative, articles altered to push a bogus perspective, and tweets riffing on particular points of disinformation. More recent [work](https://venturebeat.com/2021/04/20/study-finds-that-detoxified-language-models-might-marginalize-minority-voices/) suggests that language models might struggle to understand aspects of minority dialects, forcing people using the models to switch to “white-aligned English” to ensure that the models work for them.

With the beta availability of the API, OpenAI has updated its content guidelines to clarify what kind of content its API can’t be used to generate, like that pertaining to politics, violence, harassment, hate, spam, malware, deception, and self-harm. The company says that it’s testing “targeted filters” for specific content categories with some customers and prohibiting certain types of content on its API, like adult content, where its system “is not currently able to reliably discern harmful from acceptable use.”

“Our policies have always prohibited the use of our API in ways that do not adhere to the principles described in our charter, and content like hate speech remains prohibited … We are continually working to make our content filters more robust and we intend to allow acceptable use within some categories as our system improves,” OpenAI wrote. “We’re excited to have the safeguards in place to open up GPT-3 for more developers. As our safeguards continue to improve, we will expand how the API can be used while further improving the experience for our users.”

The wider availability of GPT-3 comes after the launch of Microsoft’s Azure OpenAI Service, an offering designed to give enterprises access to GPT-3 and its derivatives along with security, compliance, governance, and other business-focused features. Microsoft has a close relationship with OpenAI, having [invested](https://venturebeat.com/2019/07/22/microsoft-invests-1-billion-in-openai-to-develop-ai-technologies-on-azure/) $1 billion in the company in 2020 and [exclusively licensed](https://venturebeat.com/2020/09/22/microsoft-gets-exclusive-license-for-openais-gpt-3-language-model/) GPT-3 to develop AI solutions for Azure customers.

**VB Daily**

Stay in the know! Get the latest news in your inbox daily

By subscribing, you agree to VentureBeat's [Terms of Service.](https://venturebeat.com/terms-of-service/)
