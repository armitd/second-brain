# 20 LLM evaluation benchmarks and how they work

![rw-book-cover](https://cdn.prod.website-files.com/660ef16a9e0687d9cc27474a/6720de6e8c728f1d1fadb0c5_02_cheerful-robot-on-a-pedestal-with-a-gold-medal-min.jpg)

## Metadata
- Author: [[evidentlyai.com]]
- Full Title: 20 LLM evaluation benchmarks and how they work
- Category: #articles
- Summary: LLM benchmarks are standardized tests that evaluate the performance of various language models on different tasks. They provide a consistent way to compare models, assessing skills like language understanding, math, and coding. While useful for comparing models, these benchmarks may not fully reflect real-world applications or the complexity of LLM-powered products.
- URL: https://www.evidentlyai.com/llm-guide/llm-benchmarks

## Full Document
How can you tell if an LLM works well or which one is better than others?

Large Language Model (LLM) **benchmarks** are standardized tests designed to measure and compare the abilities of different language models. With new LLMs released all the time, these benchmarks let researchers and practitioners see how well each model handles different tasks, from basic language skills to complex reasoning and coding.

The main reason we use LLM benchmarks is to get a consistent, uniform way to evaluate different models. Since LLMs can be used for a variety of use cases, it’s otherwise hard to compare them fairly. Benchmarks help level the playing field by putting each model through the same set of tests.

In this guide, we’ll explore the topic of LLM benchmarks and cover:

* What LLM benchmarks are, how they work, and why we need them.
* 20 common benchmarks that assess different LLM capabilities, with links to papers and datasets.
* Limitations of LLM evaluation benchmarks.

Let’s dive in!

#### TL;DR

* **LLM benchmarks** are standardized tests that assess LLM performance across various tasks. Typically, they check if the model can produce the correct known response to a given input.
* **Common LLM benchmarks** test models for skills like language understanding, question-answering, math problem-solving, and coding tasks. **Examples** are HellaSwag, BigBench, TruthfulQA, and Chatbot Arena.
* Publicly available benchmarks make it easy to **compare** the capabilities of different LLMs, often showcased on **leaderboards**.
* Limitations of LLM benchmarks include potential **data contamination**, where models are trained on the same data they’re later tested on, **narrow focus**, and loss of relevance over time as model capabilities surpass benchmarks.
* While LLM benchmarks help compare LLMs, they are not suitable for [**evaluating** **LLM-based products**](https://www.evidentlyai.com/llm-guide/llm-evaluation), which require custom datasets and criteria tailored to the use case.

Build AI systems you can rely on

Test fast, ship faster. Evidently Cloud gives you reliable, repeatable evaluations for complex systems like RAG and agents — so you can iterate quickly and ship with confidence.

#### What are LLM benchmarks?

LLM benchmarks are **sets of tests** that help assess the capabilities of a given LLM model. They answer questions like: can this LLM handle coding tasks well? Does it give relevant answers in a conversation? How well does it solve reasoning problems?

You can think of each LLM benchmark as a specialized “exam.” Each benchmark includes a set of text inputs or tasks, usually with correct answers provided, and a scoring system to compare the results.

For example, the MMLU (Massive Multitask Language Understanding) benchmark includes multiple-choice questions on mathematics, history, computer science, law, and more.

*Example questions from the MMLU benchmark. Credit:* [*Measuring Massive Multitask Language Understanding*](https://arxiv.org/abs/2009.03300)
After you run an LLM through the benchmark, you can assess the correctness of its answers against the “ground truth” and get a quantitative score to compare and rank different LLMs.

While MMLU tests general knowledge, there are benchmarks targeting other areas like:

* **Language skills,** including logical inference and text comprehension.
* **Math problem-solving**, with tasks from basic arithmetic to complex calculus.
* **Coding**, testing the ability to generate code and solve programming challenges.
* **Conversation**, assessing the quality of responses in a dialogue.
* **Safety**, checking if models avoid harmful responses and resist manipulation.
* **Domain-specific knowledge**, such as for fields like law and finance.

###### 100+ examples of LLM benchmarks

> Want more examples of LLM benchmarks? We put together [database](https://www.evidentlyai.com/llm-evaluation-benchmarks-datasets) of 100+ LLM benchmarks and datasets you can use to evaluate the performance of language models.  [Bookmark the list ⟶](https://www.evidentlyai.com/llm-evaluation-benchmarks-datasets)

LLM benchmarks vary in difficulty. Early ones focused on basic tasks like classifying text or completing sentences, which worked well for evaluating smaller models like BERT. Now, with powerful models like GPT, Claude, or LLaMA, benchmarks have become more sophisticated and often include complex tasks requiring multi-step reasoning.

LLM benchmarks are created by research groups, universities, tech companies, and open-source communities. Many benchmarks are shared under open-source or other accessible licenses so developers and researchers can easily use them.

#### Why we need LLM benchmarks

**Evaluation standardization and transparency.** LLM benchmarks provide consistent, reproducible ways to assess and rank how well different LLMs handle specific tasks. They allow for an "apples-to-apples" comparison—like grading all students in a class on the same tests.

Whenever a new LLM is released, benchmarks help communicate how it stacks up against others, giving a snapshot of its overall abilities. With shared evaluation standards, others can also independently verify these results using the same tests and metrics.

**Progress tracking and fine-tuning.** LLM benchmarks also serve as progress markers. You can assess whether new modifications enhance the performance by comparing new LLMs with their predecessors.

We can already see a history where certain benchmarks became outdated as models consistently surpassed them, pushing researchers to develop more challenging benchmarks to keep up with advanced LLM capabilities.

You can also use benchmarks to identify the model’s weak spots. For instance, a safety benchmark can show how well a given LLM handles novel threats. This, in turn, guides the fine-tuning process and helps LLM researchers advance the field.

**Model selection.** For practitioners, benchmarks also provide a useful reference when deciding which model to use in specific applications.

Say, you’re building a customer support chatbot powered by an LLM. You’d need a model with strong conversational skills–one that can engage in dialogue, maintain context, and provide helpful responses. Which commercial or open-source LLMs should you consider using? By looking at the performance of different models on relevant benchmarks, you can narrow down your shortlist to ones that do well on standard tests.

#### How LLM benchmarks work

LLM benchmarks evaluate LLMs on fixed tests. But how exactly do they function?

In short, benchmarks expose models to a variety of test inputs and measure their performance using standardized metrics for easy comparison and ranking.

Let’s explore the process step by step!

**1. Dataset input and testing**

A benchmark includes tasks for a model to complete, like solving math problems, writing code, answering questions, or translating text. The number of test cases (ranging from dozens to thousands) and how they’re presented will vary by benchmark.

Often, it’s a **dataset of text inputs:** the LLM must process each input and produce a specific response, like completing a sentence, selecting the correct option from multiple choices, or generating a free-form text. For coding tasks, the benchmark might include actual coding challenges, like asking to write a specific function. Some benchmarks also provide prompt templates to instruct the LLM on processing the inputs.

Most benchmarks come with a set of “**ground truth**” answers to compare against, though alternative evaluation methods exist, like Chatbot Arena, which uses crowdsourced human labels. The LLM doesn’t “see” these correct answers while completing the tasks; they’re only used later for evaluating response quality.

**2. Performance evaluation and scoring**

Once the model completes the benchmark tasks, you can measure its quality! Each benchmark includes a scoring mechanism to quantify how well an LLM performs, with different [evaluation methods](https://www.evidentlyai.com/llm-guide/llm-evaluation-metrics) suited to different task types. Here are some examples:

* **Classification Metrics** like [accuracy](https://www.evidentlyai.com/classification-metrics/accuracy-precision-recall#what-is-accuracy). These metrics are ideal for tasks with a single correct answer. For instance, the MMLU benchmark uses multiple-choice questions, allowing us to simply calculate the percentage of correct responses across the dataset.

* **Overlap-based metrics** like BLEU and ROUGE**.** They are used for tasks like translation or free-form responses, where various phrasing options are valid, and an exact match is rare. These metrics compare common words and sequences between the model’s response and the reference answer.
* **Functional code quality.** Some coding benchmarks, like HumanEval, use unique metrics such as pass@k, which reflects how many generated code samples pass unit tests for given problems.
* **Fine-tuned evaluator models.** The TruthfulQA benchmark uses a fine-tuned evaluator called "GPT-Judge" (based on GPT-3) to assess the truthfulness of answers by classifying them as true or false.
* [**LLM-as-a-judge**](https://www.evidentlyai.com/llm-guide/llm-as-a-judge). MT-bench introduced LLM-based evaluation to approximate human preferences. This benchmark, featuring challenging multi-turn questions, uses advanced LLMs like GPT-4 as judges to evaluate response quality automatically.

**3. LLM ranking and LLM leaderboards**

As you run multiple LLMs through the benchmark, you can rank them based on achieved scores. One way to visualize how different models compare is a **leaderboard:** a ranking system that shows how different models perform on a specific benchmark or set of benchmarks.

Many benchmarks come with their own leaderboards, often published with the original research paper that introduced the benchmark. These leaderboards provide a snapshot of model performance when first tested on available models.

In addition, there are public, cross-benchmark leaderboards that aggregate scores from multiple benchmarks and are regularly updated as new models are released. For example, Hugging Face hosts an open LLM leaderboard that ranks various open-source models based on popular benchmarks (stay tuned—we’ll cover these in the next chapter!).

> **Examples of LLM leaderboards:** [MMLU leaderboard](https://paperswithcode.com/sota/multi-task-language-understanding-on-mmlu), [Chatbot Arena leaderboard](https://lmarena.ai/?leaderboard), [Hugging Face collection of LLM leaderboards](https://huggingface.co/collections/open-llm-leaderboard/the-big-benchmarks-collection-64faca6335a7fc7d4ffe974a)

*Example leaderboard based on the common LLM benchmarks. Image credit:* [*Hugging Face*](https://huggingface.co/collections/open-llm-leaderboard/the-big-benchmarks-collection-64faca6335a7fc7d4ffe974a)
#### Common LLM benchmarks

There are dozens of LLM benchmarks out there, and more are being developed as models evolve. LLM benchmarks vary depending on the task—e.g., text classification, machine translation, question answering, reasoning, etc. We will cover some of the commonly used ones. We provide a short description for each benchmark, links to publicly available datasets and leaderboards, and supporting research.

##### Reasoning and language understanding benchmarks

###### AI2 Reasoning Challenge (ARC)

**Assets:** [ARC dataset (HuggingFace)](https://huggingface.co/datasets/allenai/ai2_arc), [ARC leaderboard](https://leaderboard.allenai.org/arc/submissions/public)   

**Research:** [Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge](https://arxiv.org/abs/1803.05457) by Clark et al. (2018)

The [AI2 Reasoning Challenge (ARC)](https://leaderboard.allenai.org/arc/submissions/get-started) benchmark evaluates the ability of AI models to answer complex science questions that require logical reasoning beyond pattern matching. It was created by the Allen Institute for AI (AI2) and consists of over 7700 grade-school level, multiple-choice science questions. The dataset is split into an Easy Set and a Challenge Set. Easy questions can be answered using simple retrieval techniques, and the Challenge Set contains only the questions answered incorrectly by retrieval-based and word co-occurrence algorithms.

 *Example questions from the ARC Challenge Set. Credit:* [*Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge*](https://arxiv.org/abs/1803.05457)
**Assets:** [HellaSwag dataset (GitHub)](https://github.com/rowanz/hellaswag/tree/master/data), [HellaSwag leaderboard](https://rowanzellers.com/hellaswag/#leaderboard) **Paper:** [HellaSwag: Can a Machine Really Finish Your Sentence?](https://arxiv.org/abs/1905.07830) by Zellers et al. (2019)

[HellaSwag](https://rowanzellers.com/hellaswag/) is a benchmark designed to test commonsense natural language inference. It requires the model to predict the most likely ending of a sentence. Similar to ARC, HellaSwag is structured as a multiple-choice task. The answers include adversarial options—machine-generated wrong answers that seem plausible and require deep reasoning to rule out.

*Example questions from the HellaSwag benchmark. Credit:* [*HellaSwag: Can a Machine Really Finish Your Sentence?*](https://arxiv.org/abs/1905.07830)
###### Massive Multitask Language Understanding (MMLU)

**Assets:** [MMLU dataset](https://paperswithcode.com/dataset/mmlu), [MMLU leaderboard](https://paperswithcode.com/sota/multi-task-language-understanding-on-mmlu)   

**Paper:** [Measuring Massive Multitask Language Understanding](https://arxiv.org/abs/2009.03300) by Hendrycks et al. (2020)

[Massive Multitask Language Understanding](https://github.com/hendrycks/test) (MMLU) evaluates LLMs’ general knowledge and problem-solving abilities across 57 subjects, including elementary mathematics, US history, computer science, and law. The dataset contains over 15 thousand multi-choice tasks from high school to expert level. A model’s score for each subject is calculated as the percentage of correct answers, and the final MMLU score is the average of 57 subject scores.

*Example question from the MMLU benchmark. Credit:* [*Measuring Massive Multitask Language Understanding*](https://arxiv.org/abs/2009.03300)
Recently, an updated [MMLU-Pro benchmark](https://arxiv.org/abs/2406.01574) (and [Dataset](https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro)) was introduced as an enhanced version of the original MMLU benchmark. It incorporates more challenging, reasoning-focused questions and increases the choice set from four to ten options, making the tasks even more complex.

**Assets:** [SuperGLUE dataset](https://huggingface.co/datasets/aps/super_glue), [SuperGLUE leaderboard](https://super.gluebenchmark.com/leaderboard)   

**Paper:** [SuperGLUE: A Stickier Benchmark for General-Purpose Language Understanding Systems](https://arxiv.org/abs/1905.00537) by Wang et al. (2019)

[SuperGLUE](https://super.gluebenchmark.com/) stands for Super General Language Understanding Evaluation. It was introduced as an improved and more challenging version of the original [GLUE benchmark](https://gluebenchmark.com/) that was outperformed by LLMs. SuperGLUE aims to measure how well LLMs handle a variety of real-world language tasks, such as understanding context, making inferences, and answering questions. Each task has its own evaluation metric. The final score aggregates these metrics into the overall language understanding score.

*Example questions from the SuperGLUE benchmark. Credit:* [*SuperGLUE: A Stickier Benchmark for General-Purpose Language Understanding Systems*](https://arxiv.org/abs/1905.00537)
**Assets:** [BIG-bench dataset](https://paperswithcode.com/dataset/big-bench), [SuperGLUE leaderboard](https://super.gluebenchmark.com/leaderboard)   

**Paper:** [Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models](https://arxiv.org/abs/2206.04615) by Srivastava et al. (2022)

The [Beyond the Imitation Game Benchmark](https://github.com/google/BIG-bench) (BIG-bench) is a collaborative benchmark that tests language models' reasoning and extrapolating capabilities. The benchmark consists of over 200 tasks contributed by 450 authors from 132 institutions. Task topics vary from linguistics and math to biology and physics and beyond. The tasks are designed to test LLMs beyond pattern matching and explore whether the models can approach human-level reasoning and understanding.

*Task topics from the BIG-bench benchmark. Credit:* [*Beyond the Imitation Game: Quantifying and extrapolating the capabilities of language models*](https://arxiv.org/abs/2206.04615)
**Assets:** [TruthfulQA dataset](https://github.com/sylinrl/TruthfulQA), [TruthfulQA leaderboard](https://paperswithcode.com/sota/question-answering-on-truthfulqa)   

**Paper:** [TruthfulQA: Measuring How Models Mimic Human Falsehoods](https://arxiv.org/abs/2109.07958v2) by Lin et al. (2021)

The [TruthfulQA benchmark](https://github.com/sylinrl/TruthfulQA) evaluates how well LLMs generate truthful responses to questions. It identifies whether AI models can avoid generating false or misleading information, particularly in areas where human knowledge is prone to misconceptions. The dataset consists of over 800 questions in 38 categories, such as health, law, finance, and politics. The questions include topics where people often hold false beliefs like urban legends, conspiracy theories, pseudoscience, and myths: "Do vaccines cause autism?" or "Is the Great Wall of China visible from space?" To perform well, models must avoid generating false answers mimicking popular misconceptions.

*Example questions from the TruthfulOA benchmark and answers from GPT-3 with default prompt. Credit:* [*TruthfulQA: Measuring How Models Mimic Human Falsehoods*](https://arxiv.org/abs/2109.07958v2) 
###### WinoGrande

**Assets:** [WinoGrande dataset](https://winogrande.allenai.org/), [WinoGrande leaderboard](https://leaderboard.allenai.org/winogrande/submissions/public)   

**Paper:** [WinoGrande: An Adversarial Winograd Schema Challenge at Scale](https://arxiv.org/abs/1907.10641) by Sakaguchi et al. (2019)

[WinoGrande benchmark](https://winogrande.allenai.org/) is based on the [Winograd Schema Challenge](https://cdn.aaai.org/ocs/4492/4492-21843-1-PB.pdf), a natural language understanding task requiring models to resolve ambiguities in sentences involving pronoun references. WinoGrande offers a significantly larger–44000 tasks–and more complex dataset to improve the scale and robustness against the dataset-specific bias. Questions are formulated as fill-in-a-blank tasks with binary options. To complete the challenge, models must choose the correct option.

*Example questions from the WinoGrande benchmark. Credit:* [*WinoGrande: An Adversarial Winograd Schema Challenge at Scale*](https://arxiv.org/abs/1907.10641)
##### Math problems benchmarks

###### GSM8K

**Assets:** [GSM8K dataset](https://huggingface.co/datasets/openai/gsm8k), [GSM8K leaderboard](https://paperswithcode.com/sota/arithmetic-reasoning-on-gsm8k)   

**Paper:** [Training Verifiers to Solve Math Word Problems](https://arxiv.org/abs/2110.14168) by Cobbe et al. (2021)

[GSM8K](https://github.com/openai/grade-school-math) is a dataset of 8500 grade school math problems. To reach the final answer, the models must perform a sequence–between 2 and 8 steps–of elementary calculations using basic arithmetic operations like +, −, ×, and ÷. A top middle school student should be able to solve every problem. However, even the largest models often struggle to perform these multi-step mathematical tasks.

*Example problems from GSM8K. Credit:* [*Training Verifiers to Solve Math Word Problems*](https://arxiv.org/abs/2110.14168)
**Assets:** [MATH dataset](https://github.com/hendrycks/math/), [MATH leaderboard](https://paperswithcode.com/sota/math-word-problem-solving-on-math)   

**Paper:** [Measuring Mathematical Problem Solving With the MATH Dataset](https://arxiv.org/abs/2103.03874) by Hendrycks et al. (2021)

The [MATH benchmark](https://github.com/hendrycks/math/) evaluates the mathematical reasoning capabilities of LLMs. It is a dataset of 12,500 problems from the leading US mathematics competitions that require advanced skills in areas like algebra, calculus, geometry, and statistics. Most problems in MATH cannot be solved with standard high-school mathematics tools. Instead, they require problem-solving techniques and heuristics.

*Example problems, generated solutions, and ground truth solutions from the MATH dataset.Credit:* [*Measuring Mathematical Problem Solving With the MATH Dataset*](https://arxiv.org/abs/2103.03874)
##### Coding benchmarks

**Assets:** [HumanEval dataset](https://github.com/openai/human-eval), [HumanEval leaderboard](https://paperswithcode.com/sota/code-generation-on-humaneval)   

**Paper:** [Evaluating Large Language Models Trained on Code](https://arxiv.org/abs/2107.03374) by Chen et al. (2021)

‍[HumanEval](https://github.com/openai/human-eval) evaluates the code-generating abilities of LLMs. It focuses on testing models' capacity to understand programming-related tasks and generate syntactically correct and functionally accurate code according to the provided specifications. Each problem in HumanEval comes with unit tests that verify the correctness of the code. These test cases run the generated code with various inputs and check whether the outputs match the expected results–just like human programmers test their code! A successful model must pass all test cases to be correct for that specific task.

*Example problems from the HumanEval dataset.* *Credit:* [*Evaluating Large Language Models Trained on Code*](https://arxiv.org/abs/2107.03374)
###### Mostly Basic Programming Problems (MBPP)

**Assets:** [MBPP dataset](https://huggingface.co/datasets/google-research-datasets/mbpp), [MBPP leaderboard](https://paperswithcode.com/sota/code-generation-on-mbpp)   

**Paper:** [Program Synthesis with Large Language Models](https://arxiv.org/abs/2108.07732) by Austin et al. (2021)

‍[Mostly Basic Programming Problems (MBPP)](https://huggingface.co/datasets/google-research-datasets/mbpp) is designed to measure LLMs' ability to synthesize short Python programs from natural language descriptions. The dataset contains 974 tasks for entry-level programmers focusing on common programming concepts such as list manipulation, string operations, loops, conditionals, and basic algorithms. Each problem contains a task description, an example code solution, and test cases to verify the LLM's output.

*Example problems and generated solutions from the MBPP dataset.Credit:* [*Program Synthesis with Large Language Models*](https://arxiv.org/abs/2108.07732)
###### SWE-bench

**Assets:** [SWE-bench dataset](https://github.com/princeton-nlp/SWE-bench), [SWE-bench leaderboard](https://www.swebench.com/)   

**Paper:** [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770) by Jimenez et al. (2023)

[SWE-bench (Software Engineering Benchmark)](https://www.swebench.com/) evaluates how well LLMs can solve real-world software issues collected from GitHub. The dataset comprises over 2200 GitHub issues and corresponding pull requests across 12 popular Python repositories. Given a codebase and an issue, a model must generate a patch that resolves the issue. To complete the task, models must interact with execution environments, process long contexts, and perform complex reasoning–tasks beyond basic code generation problems.

*How SWE-bench works.Credit:* [*SWE-bench: Can Language Models Resolve Real-World GitHub Issues?*](https://arxiv.org/abs/2310.06770)
##### Conversation and chatbot benchmarks

###### Chatbot Arena

**Assets:** [Chatbot Arena dataset](https://github.com/lm-sys/FastChat/blob/main/docs/dataset_release.md), [Chatbot Arena leaderboard](https://lmarena.ai/?leaderboard)   

**Paper:** [Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference](https://arxiv.org/abs/2403.04132) by Chiang et al. (2024)

‍[Chatbot Arena](https://lmarena.ai/) follows a rather unique approach: it is an open-source platform for evaluating LLMs by directly comparing their conversational abilities in a competitive environment. Chatbots powered by different LLM systems are paired against each other in a virtual “arena” where users can interact with both models simultaneously. The chatbots take turns responding to user prompts, and after the conversation, the user is asked to rate or vote for the model that gave the best response. The models' identities are hidden and revealed after the user has voted.

*Win rate (left) and battle count (right) between a subset of models in Chatbot Arena. Credit:* [*Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference*](https://arxiv.org/abs/2403.04132)
**Assets:** [MT-bench dataset](https://huggingface.co/datasets/lmsys/mt_bench_human_judgments)   

**Paper:** [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://huggingface.co/datasets/lmsys/mt_bench_human_judgments) by Zheng et al. (2023)

[MT-bench](https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge) is designed to test LLMs' ability to sustain multi-turn conversations. It consists of 80 multi-turn questions from 8 categories: writing, roleplay, extraction, reasoning, math, coding, STEM, and social science. There are two turns: the model is asked an open-ended question (1st turn), then a follow-up question is added (2nd turn). To automate the evaluation process, MT-bench uses [LLM-as-a-judge](https://www.evidentlyai.com/llm-guide/llm-as-a-judge) to score the model’s response for each question on a scale from 1 to 10.

*Sample multi-turn questions in MT-bench. Credit:* [*Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena*](https://arxiv.org/abs/2306.05685)
##### Safety benchmarks

**Assets:** [AgentHarm dataset](https://huggingface.co/datasets/ai-safety-institute/AgentHarm)   

**Paper:** [AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents](https://arxiv.org/abs/2410.09024) by Andriushchenko et al. (2024)

The [AgentHarm benchmark](https://huggingface.co/datasets/ai-safety-institute/AgentHarm) was introduced to facilitate research on LLM agent misuse. It includes a set of 110 explicitly malicious agent tasks across 11 harm categories, including fraud, cybercrime, and harassment. To perform well, models must refuse harmful agentic requests and maintain their capabilities following an attack to complete a multi-step task.

*AgentHarm evaluates the performance of LLM agents that have to execute multi-step tasks to fulfill user requests. Credit:* [*AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents*](https://arxiv.org/abs/2410.09024)
**Assets:** [SafetyBench dataset](https://huggingface.co/datasets/thu-coai/SafetyBench)   

**Paper:** [SafetyBench: Evaluating the Safety of Large Language Models](https://arxiv.org/abs/2309.07045) by Zhang et al. (2023)

[SafetyBench](https://llmbench.ai/safety) is a benchmark for evaluating the safety of LLMs. It incorporates over 11000 multiple-choice questions across seven categories of safety concerns, including offensive content, bias, illegal activities, and mental health. SafetyBench offers data in Chinese and English, facilitating the evaluation in both languages.

*Example questions from the SafetyBench dataset.* *Credit:* [*SafetyBench: Evaluating the Safety of Large Language Models*](https://arxiv.org/abs/2309.07045)
##### Domain-specific benchmarks

###### MultiMedQA

**Assets:** [MultiMedQA datasets](https://huggingface.co/collections/openlifescienceai/multimedqa-66098a5b280539974cefe485)   

**Paper:** [Large language models encode clinical knowledge](https://www.nature.com/articles/s41586-023-06291-2) by Singhal et al. (2023)

‍[The MultiMedQA benchmark](https://huggingface.co/collections/openlifescienceai/multimedqa-66098a5b280539974cefe485) measures LLMs' ability to provide accurate, reliable, and contextually appropriate responses in the healthcare domain. It combines six existing medical question-answering datasets spanning professional medicine, research, and consumer queries and incorporates a new dataset of medical questions searched online. The benchmark evaluates model answers along multiple axes: factuality, comprehension, reasoning, possible harm, and bias.

*Example question from the MultiMedQA dataset and the answer from Med-PaLM. Credit:* [*Large language models encode clinical knowledge*](https://www.nature.com/articles/s41586-023-06291-2)
**Assets:** [FinBen dataset](https://github.com/The-FinAI/PIXIU)   

**Paper:** [FinBen: A Holistic Financial Benchmark for Large Language Models](https://arxiv.org/abs/2402.12659) by Xie et al. (2024)

[FinBen](https://github.com/The-FinAI/PIXIU) is an open-source benchmark designed to evaluate LLMs in the financial domain. It includes 36 datasets that cover 24 tasks in seven financial domains: information extraction, text analysis, question answering, text generation, risk management, forecasting, and decision-making. FinBen offers a broader range of tasks and datasets compared to its predecessors and is the first to evaluate stock trading. The benchmark revealed that while the latest models excel in information extraction and textual analysis, they struggle with advanced reasoning and complex tasks like text generation and forecasting.

*Evaluation datasets by task type from FinBen. Credit:* [*FinBen: A Holistic Financial Benchmark for Large Language Models*](https://arxiv.org/abs/2402.12659)
**Assets:** [LegalBench datasets](https://huggingface.co/datasets/nguha/legalbench)   

**Paper:** [LegalBench: A Collaboratively Built Benchmark for Measuring Legal Reasoning in Large Language Models](https://arxiv.org/abs/2308.11462) by Guha et al. (2023)

[LegalBench](https://hazyresearch.stanford.edu/legalbench/) is a collaborative benchmark designed to evaluate the legal reasoning abilities of LLMs. It consists of 162 tasks, which are crowdsourced by legal professionals. These tasks cover six different types of legal reasoning: issue-spotting, rule-recall, rule-application, rule-conclusion, interpretation, and rhetorical understanding.

*Sample question in LegalBench. Credit:* [*LegalBench: A Collaboratively Built Benchmark for Measuring Legal Reasoning in Large Language Models*](https://arxiv.org/abs/2308.11462)
###### Berkeley Function-Calling Leaderboard

**Assets:** [BFCL dataset](https://huggingface.co/datasets/gorilla-llm/Berkeley-Function-Calling-Leaderboard), [BFCL leaderboard](https://gorilla.cs.berkeley.edu/leaderboard.html)   

**Research:** [Berkeley Function-Calling Leaderboard](https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html) by Yan et al. (2024)

[Berkeley Function Leaderboard (BFCL)](https://github.com/ShishirPatil/gorilla/tree/main/berkeley-function-call-leaderboard) evaluates LLMs' function-calling abilities. The dataset consists of 2000 question-answer pairs in multiple languages–including Python, Java, Javascript, and RestAPI–and diverse application domains. It supports multiple and parallel function calls and function relevance detection.

*Wagon Wheel chart from BFCL. Credit:* [*Berkeley Function-Calling Leaderboard*](https://gorilla.cs.berkeley.edu/blogs/8_berkeley_function_calling_leaderboard.html)
#### Limitations of LLM benchmarks

LLM benchmarks are a powerful tool for evaluating the performance of LLMs. However, they have their limitations:

**Data contamination**. Public test data can unintentionally leak into datasets used to train LLMs, compromising evaluation integrity. If a model has seen specific answers during training, it may "know" them rather than demonstrate a true ability to solve that task. One approach to prevent this is to keep some benchmark data private and regularly create new or expand existing benchmark datasets.

**Benchmarks can quickly become outdated.** Once a model achieves the highest possible score on a particular benchmark, that benchmark loses its effectiveness as a measure of progress. This necessitates the creation of more difficult and nuanced tasks to keep pushing the boundaries of LLM development. Many of the existing benchmarks already lost their relevance as modern LLMs progress in their abilities.

**Benchmarks may not reflect real-world performance.** Many benchmarks are built around specific, well-defined tasks that may not fully capture the complexity and variety of scenarios encountered in real-world applications. As a result, a model that excels in benchmarks may still fail on applied tasks, even those that seem straightforward.

**Benchmarks aren’t enough for evaluating LLM apps.** Generic LLM benchmarks are useful for testing models but don’t work for LLM-powered applications. In real apps like chatbots or virtual assistants, it’s not just the model—you also have prompts, external knowledge databases, and business logic to consider. To test these systems effectively, you’ll need “your own” benchmarks: those that include real, application-specific inputs and standards for correct behavior.

#### Create a benchmark for your AI system

LLM benchmarks are great for comparing models, but when building an AI product, you need custom [test datasets](https://www.evidentlyai.com/llm-guide/llm-test-dataset-synthetic-data) that reflect your use case. These should cover key scenarios and edge cases specific to your application. You'll also need task-specific evaluations, like [LLM judges](https://www.evidentlyai.com/llm-guide/llm-as-a-judge) tuned to your custom criteria and preferences.

That’s why we built [Evidently](https://www.evidentlyai.com/llm-guide/llm-as-a-judge). Our open-source library (trusted with over 25 million downloads!) offers a range of evaluation metrics.

For teams working on complex, mission-critical AI systems, [Evidently Cloud](https://www.evidentlyai.com/register) provides a platform to collaboratively test and monitor AI quality. You can generate synthetic data, create evaluation scenarios (including AI agent simulations), run tests and track performance — all in one place.

Ready to design your custom AI test dataset? [Sign up for free](https://www.evidentlyai.com/register) or [schedule a demo](https://www.evidentlyai.com/get-demo) to see Evidently Cloud in action. We're here to help you build with confidence!
