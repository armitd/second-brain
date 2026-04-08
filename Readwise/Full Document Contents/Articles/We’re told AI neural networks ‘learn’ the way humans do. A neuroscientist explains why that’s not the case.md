# We’re told AI neural networks ‘learn’ the way humans do. A neuroscientist explains why that’s not the case

![rw-book-cover](https://images.theconversation.com/files/467087/original/file-20220606-14-tpqupv.jpeg?ixlib=rb-1.1.0&rect=0%2C18%2C6270%2C3130&q=45&auto=format&w=1356&h=668&fit=crop)

## Metadata
- Author: [[James Fodor]]
- Full Title: We’re told AI neural networks ‘learn’ the way humans do. A neuroscientist explains why that’s not the case
- Category: #articles
- Summary: AI systems can do human-like tasks, but they don't think like humans. AI learns differently using neural nets, not like the human brain. Humans learn through complex processes, unlike AI's statistical associations.
- URL: https://theconversation.com/were-told-ai-neural-networks-learn-the-way-humans-do-a-neuroscientist-explains-why-thats-not-the-case-183993

## Full Document
![](https://images.theconversation.com/files/467087/original/file-20220606-14-tpqupv.jpeg?ixlib=rb-1.1.0&rect=0%2C18%2C6270%2C3130&q=45&auto=format&w=1356&h=668&fit=crop) ![A 3D rendered image represents computation processing, with links coming out from a central bright 'node' in the network](https://images.theconversation.com/files/467087/original/file-20220606-14-tpqupv.jpeg?ixlib=rb-1.1.0&rect=0%2C0%2C6261%2C3732&q=20&auto=format&w=320&fit=clip&dpr=2&usm=12&cs=strip)  Shutterstock 

Recently developed artificial intelligence (AI) models are capable of many impressive feats, including recognising images and producing human-like language. But just because AI can perform human-like behaviours doesn’t mean it can think or understand like humans.

As a researcher studying how humans understand and reason about the world, I think it’s important to emphasise the way AI systems “think” and learn is fundamentally different to how humans do – and we have a long way to go before AI can truly think like us.

 ***Read more: [Robots are creating images and telling jokes. 5 things to know about foundation models and the next generation of AI](https://theconversation.com/robots-are-creating-images-and-telling-jokes-5-things-to-know-about-foundation-models-and-the-next-generation-of-ai-181150)*** 

#### A widespread misconception

Developments in AI have produced systems that can perform very human-like behaviours. The language model [GPT-3](https://www.twilio.com/blog/ultimate-guide-openai-gpt-3-language-model) can produce text that’s often indistinguishable from human speech. Another model, [PaLM](https://ai.googleblog.com/2022/04/pathways-language-model-palm-scaling-to.html), can produce explanations for jokes it has never [seen before](https://www.cnet.com/tech/services-and-software/no-joke-googles-ai-is-smart-enough-to-understand-your-humor/).

Most recently, a general-purpose AI known as Gato has been developed which can [perform hundreds of tasks](https://www.zdnet.com/article/deepminds-gato-is-mediocre-so-why-did-they-build-it/), including captioning images, answering questions, playing Atari video games, and even controlling a robot arm to stack blocks. And DALL-E is a system which has been trained to produce modified images and artwork from a text description.

![](https://pbs.twimg.com/profile_images/1513753671393484801/5lXMv-53.jpg)

[HeavensLastAngel](https://twitter.com/HvnsLstAngel)
[@HvnsLstAngel](https://twitter.com/HvnsLstAngel)

“A still of Kermit The Frog in The Matrix (1999)” #dalle

![](https://pbs.twimg.com/media/FUEBurtVUAEMbqn.jpg)

[Posted May 31, 2022 at 5:25AM](https://twitter.com/HvnsLstAngel/status/1531507253659914240)

These breakthroughs have led to some bold claims about the capability of such AI, and what it can tell us about human intelligence.

For example Nando de Freitas, a researcher at Google’s AI company DeepMind, argues scaling up existing models will be enough to produce human-level artificial intelligence. Others have [echoed](https://medium.com/@blaisea/do-large-language-models-understand-us-6f881d6d8e75) this view.

![](https://pbs.twimg.com/profile_images/1338407584370462720/WVbG5sqw.jpg)

[Nando de Freitas 🏳️‍🌈](https://twitter.com/NandoDF)
[@NandoDF](https://twitter.com/NandoDF)

Someone’s opinion article. My opinion: It’s all about scale now! The Game is Over! It’s about making these models bigger, safer, compute efficient, faster at sampling, smarter memory, more modalities, INNOVATIVE DATA, on/offline, … 1/N [thenextweb.com/news/deepminds…](https://thenextweb.com/news/deepminds-astounding-new-gato-ai-makes-fear-humans-will-never-achieve-agi)

[Posted May 14, 2022 at 8:46AM](https://twitter.com/NandoDF/status/1525397036325019649)

In all the excitement, it’s easy to assume human-like behaviour means human-like understanding. But there are several key differences between how AI and humans think and learn.

#### Neural nets vs the human brain

Most recent AI is built from [artificial neural networks](https://theconversation.com/what-is-a-neural-network-a-computer-scientist-explains-151897), or “neural nets” for short. The term “neural” is used because these networks are inspired by the human brain, in which billions of cells called neurons form complex webs of connections with one another, processing information as they fire signals back and forth.

Neural nets are a highly simplified version of the biology. A real neuron is replaced with a simple node, and the strength of the connection between nodes is represented by a single number called a “weight”.

With enough connected nodes stacked into enough layers, neural nets can be trained to recognise patterns and even “[generalise](https://medium.com/deep-learning-demystified/generalization-in-neural-networks-7765ee42ac23)” to stimuli that are similar (but not identical) to what they’ve seen before. Simply, generalisation refers to an AI system’s ability to take what it has learnt from certain data and apply it to new data.

Being able to identify features, recognise patterns, and generalise from results lies at the heart of the success of neural nets – and mimics techniques humans use for such tasks. Yet there are important differences.

Neural nets are typically trained by “[supervised learning](https://www.ibm.com/cloud/learn/supervised-learning)”. So they’re presented with many examples of an input and the desired output, and then gradually the connection weights are adjusted until the network “learns” to produce the desired output.

To learn a language task, a neural net may be presented with a sentence one word at a time, and will slowly learns to predict the next word in the sequence.

This is very different from how humans typically learn. Most human learning is “unsupervised”, which means we’re not explicitly told what the “right” response is for a given stimulus. We have to work this out ourselves.

For instance, children aren’t given instructions on how to speak, but learn this through a [complex process](https://www.abc.net.au/education/how-babies-learn-to-talk/13757672) of exposure to adult speech, imitation, and feedback.

![A toddler tries to walk outdoors, with an adult guiding it by both hands](https://images.theconversation.com/files/467090/original/file-20220606-22-7fwow4.jpeg?ixlib=rb-1.1.0&q=15&auto=format&w=754&h=424&fit=crop&dpr=3) Childrens’ learning is assisted by adults, but they’re not fed massive datasets the way AI systems are. Shutterstock 
Another difference is the sheer scale of data used to train AI. The GPT-3 model was trained on [400 billion words](https://arxiv.org/pdf/2005.14165.pdf), mostly taken from the internet. At a rate of 150 words per minute, it would take a human nearly 4,000 years to read this much text.

Such calculations show humans can’t possibly learn the same way AI does. We have to make more efficient use of smaller amounts of data.

#### Neural nets can learn in ways we can’t

An even more fundamental difference concerns the way neural nets learn. In order to match up a stimulus with a desired response, neural nets use an algorithm called “backpropagation” to pass errors backward through the network, allowing the weights to be adjusted in just the right way.

However, it’s widely recognised by neuroscientists that [backpropagation can’t be implemented](https://www.nature.com/articles/s41583-020-0277-3/) in the brain, as it would require [external signals](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0266102) that just don’t exist.

Some researchers have proposed [variations](https://www.sciencedirect.com/science/article/pii/S1364661319300129) of backpropagation could be used by the brain, but so far there is no evidence human brains can use such learning methods.

Instead, humans learn by making [structured mental concepts](https://link.springer.com/article/10.1007/s12559-014-9307-7), in which many different properties and associations are linked together. For instance, our concept of “banana” includes its shape, the colour yellow, knowledge of it being a fruit, how to hold it, and so forth.

As far as we know, AI systems do not form conceptual knowledge like this. They rely entirely on extracting complex statistical associations from their training data, and then applying these to similar contexts.

Efforts are underway to build AI that [combines different types of input](https://www.techrepublic.com/article/multimodal-learning-the-future-of-artificial-intelligence/) (such as images and text) – but it remains to be seen if this will be sufficient for these models to learn the same types of rich mental representations humans use to understand the world.

There’s still much we don’t know about how humans learn, understand and reason. However, what we do know indicates humans perform these tasks very differently to AI systems.

As such, [many researchers believe](https://www.zdnet.com/article/resisting-the-urge-to-be-impressed-and-knowing-what-we-are-talking-about-when-we-talk-about-ai/) we’ll need new approaches, and more fundamental insight into how the human brain works, before we can build machines that truly think and learn like humans.
