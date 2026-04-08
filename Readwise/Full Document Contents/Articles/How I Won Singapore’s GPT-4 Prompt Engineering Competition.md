# How I Won Singapore’s GPT-4 Prompt Engineering Competition

![rw-book-cover](https://miro.medium.com/v2/resize:fit:1036/1*RAI4cBXe1_zaxVykHz79oA.jpeg)

## Metadata
- Author: [[Sheila Teo]]
- Full Title: How I Won Singapore’s GPT-4 Prompt Engineering Competition
- Category: #articles
- Document Tags: [[ai]] 
- Summary: The author describes their experience winning Singapore's GPT-4 Prompt Engineering competition and shares the strategies they learned along the way. They highlight the importance of prompt engineering, which combines technical understanding with creativity and strategic thinking. The article covers various prompt engineering techniques, including structuring prompts using the CO-STAR framework and sectioning prompts using delimiters. The author also discusses advanced strategies such as using system prompts with LLM guardrails and analyzing datasets using only LLMs.
- URL: https://towardsdatascience.com/how-i-won-singapores-gpt-4-prompt-engineering-competition-34c195a93d41

## Full Document
#### A deep dive into the strategies and takeaways I learned along the way

![](https://miro.medium.com/v2/resize:fit:700/1*RAI4cBXe1_zaxVykHz79oA.jpeg)Celebrating a milestone — The real win was the priceless learning experience! 
Last month, I had the incredible honor of winning Singapore’s first ever GPT-4 Prompt Engineering competition, which brought together over 400 prompt-ly brilliant participants, organised by the Government Technology Agency of Singapore (GovTech).

Prompt engineering is a discipline that blends both art and science — it is as much technical understanding as it is of creativity and strategic thinking. This article is a compilation of the prompt engineering strategies and insights that I learned along the way, that push any LLM to do exactly what you need and more!

This article covers the following, with 🟢 referring to beginner-friendly prompting techniques while 🟠 refers to advanced strategies:

1. [🟢] [Structuring prompts using the CO-STAR framework](https://towardsdatascience.com/how-i-won-singapores-gpt-4-prompt-engineering-competition-34c195a93d41?source=rss----7f60cf5620c9---4#030a)

2. [🟢] [Sectioning prompts using delimiters](https://towardsdatascience.com/how-i-won-singapores-gpt-4-prompt-engineering-competition-34c195a93d41?source=rss----7f60cf5620c9---4#c8af)

3. [🟠] [Using system prompts with LLM guardrails](https://towardsdatascience.com/how-i-won-singapores-gpt-4-prompt-engineering-competition-34c195a93d41?source=rss----7f60cf5620c9---4#889c)

4. [🟠] [Analyzing datasets using only LLMs, without plugins or code](https://towardsdatascience.com/how-i-won-singapores-gpt-4-prompt-engineering-competition-34c195a93d41?source=rss----7f60cf5620c9---4#5800)

### 1. [🟢] Structuring Prompts using the CO-STAR framework

Effective prompt structuring is crucial for eliciting optimal responses from an LLM. The CO-STAR framework, a brainchild of GovTech Singapore’s Data Science & AI team, is a handy template for structuring prompts. It considers all the key aspects that influence the effectiveness and relevance of an LLM’s response, leading to more optimal responses.

![](https://miro.medium.com/v2/resize:fit:700/1*_20YO3p4S4a4BKBtFGwwuA.png)CO-STAR framework — Image by author 
Here’s how it works:

#### **(C) Context: Provide background information on the task.**

This helps the LLM understand the specific scenario being discussed, ensuring its response is relevant and aligned with your expectations.

#### **(O) Objective: Define what the task is that you want the LLM to perform.**
