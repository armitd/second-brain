# New ‘Liquid’ AI Learns Continuously From Its Experience of the World

![rw-book-cover](https://singularityhub.com/uploads/2021/01/white-blue-liquid-ink-cloud-swirl-water.jpg)

## Metadata
- Author: [[Jason Dorrier]]
- Full Title: New ‘Liquid’ AI Learns Continuously From Its Experience of the World
- Category: #articles
- Summary: For all its comparisons to the human brain, AI still isn’t much like us. Maybe that’s alright. In the animal kingdom, brains come in all shapes and sizes.
- URL: https://singularityhub-com.cdn.ampproject.org/c/s/singularityhub.com/2021/01/31/new-liquid-ai-learns-as-it-experiences-the-world-in-real-time/amp/

## Full Document
![](data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjM5MSIgd2lkdGg9IjY5NiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiB2ZXJzaW9uPSIxLjEiLz4=)![ai learning white blue liquid ink cloud swirl water](https://singularityhub-com.cdn.ampproject.org/i/s/singularityhub.com/uploads/2021/01/white-blue-liquid-ink-cloud-swirl-water.jpg)ai learning white blue liquid ink cloud swirl water
For all its comparisons to the human brain, AI still isn’t much like us. Maybe that’s alright. In the animal kingdom, brains come in all shapes and sizes. So, in a new machine learning approach, engineers did away with the human brain and all its beautiful complexity—turning instead to the brain of a lowly worm for inspiration.

Turns out, simplicity has its benefits. The resulting neural network is efficient, transparent, and here’s the kicker: It’s a lifelong learner.

Whereas most machine learning algorithms can’t hone their skills beyond an initial training period, the researchers say the new approach, [called a liquid neural network](https://news.mit.edu/2021/machine-learning-adapts-0128), has a kind of built-in “neuroplasticity.” That is, as it goes about its work—say, in the future, maybe driving a car or directing a robot—it can learn from experience and adjust its connections on the fly.

In a world that’s noisy and chaotic, such adaptability is essential.

##### **Worm-Brained Driver**

The algorithm’s architecture was inspired by the mere 302 neurons making up the nervous system of *C. elegans*, a tiny nematode (or worm).

In [work published last year](https://www.nature.com/articles/s42256-020-00237-3), the group, which includes researchers from MIT and Austria’s Institute of Science and Technology, said that despite its simplicity, *C. elegans* is capable of surprisingly interesting and varied behavior. So, they developed equations to mathematically model the worm’s neurons and then built them into a neural network.

Their worm-brain algorithm was much simpler than other cutting-edge machine learning algorithms, and yet it was still able to accomplish similar tasks, like keeping a car in its lane.

“Today, deep learning models with many millions of parameters are often used for learning complex tasks such as autonomous driving,” Mathias Lechner, a PhD student at Austria’s Institute of Science and Technology and study author, [said](https://ist.ac.at/en/news/new-deep-learning-models/). “However, our new approach enables us to reduce the size of the networks by two orders of magnitude. Our systems only use 75,000 trainable parameters.”

Now, in a [new paper](https://arxiv.org/pdf/2006.04439.pdf), the group takes their worm-inspired system further by adding a wholly new capability.

##### **Old Worm, New Tricks**

The output of a neural network—turn the steering wheel to the right, for instance—depends on a set of [weighted connections](https://hackernoon.com/everything-you-need-to-know-about-neural-networks-8988c3ee4491) between the network’s “neurons.”

In our brains, it’s the same. Each brain cell is connected to many other cells. Whether or not a particular cell fires depends on the sum of the signals it’s receiving. Beyond some threshold—or weight—the cell fires a signal to its own network of downstream connections.

In a neural network, these weights are called parameters. As the system feeds data through the network, its parameters converge on the configuration yielding the best results.

Usually, a neural network’s parameters are locked into place after training, and the algorithm’s put to work. But in the real world, this can mean it’s a bit brittle—show an algorithm something that deviates too much from its training, and it’ll break. Not an ideal result.

In contrast, in a liquid neural network, the parameters are allowed to continue changing over time and with experience. The AI learns on the job.

This adaptibility means the algorithm is less likely to break as the world throws new or noisy information its way—like, for example, when rain obscures an autonomous car’s camera. Also, in contrast to bigger algorithms, whose inner workings are largely inscrutable, the algorithm’s simple architecture allows researchers to peer inside and audit its decision-making.

Neither its new ability nor its still-diminutive stature seemed to hold the AI back. The algorithm performed as well or better than other state-of-the art time-sequence algorithms in predicting next steps in a series of events.

“Everyone talks about scaling up their network,” said Ramin Hasani, [the study’s](https://arxiv.org/pdf/2006.04439.pdf) lead author. “We want to scale down, to have fewer but richer nodes.”

An adaptable algorithm that consumes relatively little computing power would make an ideal robot brain. Hasani believes the approach may be useful in other applications that involve real-time analysis of new data like video processing or financial analysis.

He plans to continue dialing in the approach to make it practical.

“We have a provably more expressive neural network that is inspired by nature. But this is just the beginning of the process,” Hasani said. “The obvious question is how do you extend this? We think this kind of network could be a key element of future intelligence systems.”

##### **Is Bigger Better?**

At a time when big players like OpenAI and Google are regularly making headlines with gargantuan machine learning algorithms, it’s a fascinating example of an alternative approach headed in the opposite direction.

OpenAI’s [GPT-3 algorithm](https://singularityhub.com/2020/06/18/openais-new-text-generator-writes-even-more-like-a-human/) collectively dropped jaws last year, both for its size—at the time, a record-setting 175 billion parameters—and [its abilities](https://singularityhub.com/2020/10/23/an-ai-wrote-this-short-film-and-its-sort-of-fascinating/). A recent Google algorithm topped the charts at [over a trillion parameters](https://www.google.com/amp/s/venturebeat.com/2021/01/12/google-trained-a-trillion-parameter-ai-language-model/amp/).

Yet critics worry the drive toward ever-bigger AI is wasteful, expensive, and consolidates research in the hands of a few companies with cash to fund large-scale models. Further, these huge models are “black boxes,” their actions largely impenetrable. This can be especially problematic when unsupervised models are [trained on the unfiltered internet](https://www.technologyreview.com/2021/01/29/1017065/ai-image-generation-is-racist-sexist/). There’s no telling (or perhaps, controlling) what bad habits they’ll pick up.

Increasingly, academic researchers are aiming to address some of these issues. As companies like OpenAI, Google, and Microsoft push to prove the bigger-is-better hypothesis, it’s possible serious AI innovations in efficiency will emerge elsewhere—not despite a lack of resources but *because* of it. As they say, necessity is the mother of invention.

*Image Credit: [benjamin henon](https://unsplash.com/@benjaminhenon?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) / [Unsplash](https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)*
