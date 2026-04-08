# A Beginner’s Guide to Language Models

![rw-book-cover](https://builtin.com/sites/www.builtin.com/files/styles/og/public/2022-12/beginners-guide-language-models_0.jpg)

## Metadata
- Author: [[Mór Kapronczay]]
- Full Title: A Beginner’s Guide to Language Models
- Category: #articles
- Summary: Language models use machine learning to predict words in sentences based on context, transforming text analysis methods. These models enable tasks like text generation, translation, and summarization, advancing natural language processing. The evolution from probabilistic models to neural networks and transformers has enhanced language model efficiency and capabilities.
- URL: https://builtin.com/data-science/beginners-guide-language-models

## Full Document
![A digital face dissolving into words and letters.](https://builtin.com/cdn-cgi/image/f=auto,quality=80,width=752,height=435/https://builtin.com/sites/www.builtin.com/files/styles/byline_image/public/2022-12/beginners-guide-language-models_0.jpg)Image: Shutterstock / Built In
Extracting information from textual data has changed dramatically over the past decade. As the term [natural language processing](https://builtin.com/data-science/introduction-nlp) has overtaken text mining as the name of the field, the methodology has changed tremendously, too. One of the main drivers of this change was the emergence of language models as a basis for many applications aiming to distill valuable insights from raw text.

#### Language Model Definition

A language model uses machine learning to conduct a probability distribution over words used to predict the most likely next word in a sentence based on the previous entry. Language models learn from text and can be used for producing original text, predicting the next word in a text, speech recognition, optical character recognition and handwriting recognition.

In learning about natural language processing, I’ve been fascinated by the evolution of language models over the past years. You may have [heard about GPT-3](https://builtin.com/machine-learning/why-gpt-3-heralds-democratic-revolution-tech) and the [potential threats it poses](https://www.telegraph.co.uk/technology/2020/08/26/forget-deepfakes-ai-generated-text-should-worried/), but how did we get this far? How can a machine produce an article that mimics a journalist?

#### What Is a Language Model?

A language model is a [probability distribution](https://builtin.com/data-science/probability-distributions-data-science) over words or word sequences. In practice, it gives the probability of a certain word sequence being “valid.” Validity in this context does not refer to grammatical validity. Instead, it means that it resembles how people write, which is what the language model learns. This is an important point. There’s no magic to a language model like other [machine learning models](https://builtin.com/machine-learning/), particularly [deep neural networks](https://builtin.com/machine-learning/what-is-deep-learning), it’s just a tool to incorporate abundant information in a concise manner that’s reusable in an out-of-sample context.

#### What Can a Language Model Do?

The abstract understanding of natural language, which is necessary to infer word probabilities from context, can be used for a number of tasks. Lemmatization or stemming aims to reduce a word to its most basic form, thereby dramatically decreasing the number of tokens. These algorithms work better if the part-of-speech role of the word is known. A verb’s postfixes can be different from a noun’s postfixes, hence the rationale for part-of-speech tagging (or [POS-tagging](https://nlp.stanford.edu/software/tagger.shtml#:~:text=A%20Part%2DOf%2DSpeech%20Tagger,like%20'noun%2Dplural'.)), a common task for a language model.

With a good language model, we can perform [extractive or abstractive summarization](https://www.machinelearningplus.com/nlp/text-summarization-approaches-nlp-example/) of texts. If we have models for different languages, a [machine translation](https://www.analyticsvidhya.com/blog/2019/01/neural-machine-translation-keras/) system can be built easily. Less straightforward use-cases include answering questions (with or without context, see the example at the end of the article). Language models can also be used for [speech recognition](https://builtin.com/artificial-intelligence/automatic-speech-recognition-cloud-communications), [OCR](https://builtin.com/data-science/python-ocr), [handwriting recognition](https://www.sciencedirect.com/science/article/abs/pii/S0031320313004494) and more. There’s a whole spectrum of opportunities.

#### Types of Language Models

There are two types of language models:

It’s important to note the difference between them.

##### Probabilistic Language Model

A simple probabilistic language modelis constructed by calculating n-gram probabilities. An n-gram is an n word sequence, n being an integer greater than zero. An n-gram’s probability is the conditional probability that the n-gram’s last word follows a particular n-1 gram (leaving out the last word). It’s the proportion of occurrences of the last word following the n-1 gram leaving the last word out. This concept is a Markov assumption. Given the n-1 gram (the present), the n-gram probabilities (future) does not depend on the n-2, n-3, etc grams (past).

There are evident drawbacks of this approach. Most importantly, only the preceding n words affect the probability distribution of the next word. Complicated texts have deep context that may have decisive influence on the choice of the next word. Thus, what the next word is might not be evident from the previous n-words, not even if n is 20 or 50. A term has influence on a previous word choice: the word Unitedis much more probable if it is followed by States of America. Let’s call this the context problem.

On top of that, it’s evident that this approach scales poorly. As size increases (n), the number of possible permutations skyrocket, even though most of the permutations never occur in the text. And all the occuring probabilities (or all n-gram counts) have to be calculated and stored.In addition, non-occurring n-grams create a sparsity problem**,** as in, the granularity of the probability distribution can be quite low. Word probabilities have few different values, therefore most of the words have the same probability.

Neural network based language modelsease the sparsity problem by the way they encode inputs. Word embedding layers create an arbitrary sized vector of each word that incorporates semantic relationships as well. These continuous vectors create the much needed granularity in the probability distribution of the next word. Moreover, the language model is a function, as all neural networks are with lots of matrix computations, so it’s not necessary to store all n-gram counts to produce the probability distribution of the next word.

Some content could not be imported from the original document. [View content ↗](https://www.youtube.com/embed/W0TcVrI_vRg?autoplay=0&start=0&rel=0) 

A tutorial on the basics of language models. | Video: Victor Lavrenko

#### Evolution of Language Models

Even though neural networks solve the sparsity problem, the context problem remains. First, language models were developed to solve the context problem more and more efficiently — bringing more and more context words to influence the probability distribution. Secondly, the goal was to create an architecture that gives the model the ability to learn which context words are more important than others.

The first model, which I outlined previously, is a dense (or hidden) layer and an output layer stacked on top of a continuous bag-of-words (CBOW) [Word2Vec model](https://builtin.com/machine-learning/nlp-word2vec-python).A CBOW Word2Vec model is trained to guess the word from context. A Skip-Gram Word2Vec model does the opposite, guessing context from the word. In practice, a CBOW Word2Vec model requires a lot of examples of the following structure to train it: the inputs are n words before and/or after the word, which is the output. We can see that the context problem is still intact.

[Recurrent neural networks (RNNs)](https://builtin.com/data-science/recurrent-neural-networks-powerhouse-language-modeling) are an improvement regarding this matter. Since RNNs can be either a long short-term memory (LSTM) or a gated recurrent unit (GRU) cell based network, they take all previous words into account when choosing the next word. AllenNLP’s [ELMo](https://allennlp.org/elmo) takes this notion a step further, utilizing a bidirectional LSTM, which takes into account the context before and after the word counts.

##### Transformers

The main drawback of RNN-based architectures stems from their sequential nature. As a consequence, training times soar for long sequences because there is no possibility for parallelization. The [solution](https://arxiv.org/pdf/1706.03762.pdf) for this problem is the [transformer architecture](https://builtin.com/artificial-intelligence/transformer-neural-network).

The GPT models from [OpenAI](https://openai.com/) and Google’s [BERT](https://ai.googleblog.com/2018/11/open-sourcing-bert-state-of-art-pre.html) utilize the transformer architecture, as well. These models also employ a mechanism called “Attention,”by which the model can learn which inputs deserve more attention than others in certain cases.

In terms of model architecture, the main quantum leaps were firstly RNNs, specifically, LSTM and GRU, solving the sparsity problem and reducing the disk space language models use, and subsequently, the transformer architecture, making parallelization possible and creating attention mechanisms. But architecture is not the only aspect a language model can excel in.

Compared to the GPT-1 architecture, GPT-3 has virtually nothing novel. But it’s huge. It has 175 billion parameters, and it was trained on the largest corpus a model has ever been trained on in common crawl. This is partly possible because of the semi-supervised training strategy of a language model. A text can be used as a training example with some words omitted. The incredible power of GPT-3 comes from the fact that it has read more or less all text that has appeared on the internet over the past years, and it has the capability to reflect most of the complexity natural language contains.

Finally, I’d like to review the [T5 model from Google](https://ai.googleblog.com/2020/02/exploring-transfer-learning-with-t5.html). Previously, language models were used for standard NLP tasks, like part-of-speech (POS) tagging or machine translation with slight modifications. With a little [retraining](https://github.com/soutsios/pos-tagger-bert), BERT can be a POS-tagger because of its abstract ability to understand the underlying structure of natural language.

With T5, there is no need for any modifications for NLP tasks. If it gets a text with some <M> tokens in it, it knows that those tokens are gaps to fill with the appropriate words. It can also answer questions. If it receives some context after the questions, it searches the context for the answer. Otherwise, it answers from its own knowledge. Fun fact: It beat its own creators in a trivia quiz.

[NLP for Beginners: A Complete Guide](https://builtin.com/machine-learning/nlp-for-beginners)

#### Future of Language Models

Personally, I think this is the field that we are closest to creating an AI. There’s a lot of buzz around AI, and many simple decision systems and almost any neural network are called AI, but this is mainly marketing. By definition, artificial intelligence involves human-like intelligence capabilities performed by a machine. While transfer learning shines in the field of computer vision, and the notion of transfer learning is essential for an AI system, the very fact that the same model can do a wide range of NLP tasks and can infer what to do from the input is itself spectacular. It brings us one step closer to actually creating human-like intelligence systems.

####  Recent Data Science articles

Built In’s expert contributor network publishes thoughtful, solutions-oriented stories written by innovative tech professionals. It is the tech industry’s definitive destination for sharing compelling, first-person accounts of problem-solving on the road to innovation.

[Learn More](https://builtin.com/expert-contributors)
