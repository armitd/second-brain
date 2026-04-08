# Machine Learning Reimagines the Building Blocks of Computing

![rw-book-cover](https://d2r55xnwy6nx47.cloudfront.net/uploads/2022/03/Gears_1200_social.jpg)

## Metadata
- Author: [[Nick Thieme]]
- Full Title: Machine Learning Reimagines the Building Blocks of Computing
- Category: #articles
- Summary: Researchers are combining traditional algorithms with machine learning to improve computing efficiency. By incorporating machine learning insights, algorithms with predictions can offer faster and more accurate results. This innovative approach is reimagining the fundamental building blocks of computing.
- URL: https://www.quantamagazine.org/machine-learning-reimagines-the-building-blocks-of-computing-20220315/

## Full Document
Machine Learning Reimagines the Building Blocks of Computing

*By* [Nick Thieme](https://www.quantamagazine.org/authors/nick-thieme/)

*March 15, 2022*

Traditional algorithms power complicated computational tools like machine learning. A new approach, called algorithms with predictions, uses the power of machine learning to improve algorithms.

![Illustration of gears made up of a network of connections against a black background](https://d2r55xnwy6nx47.cloudfront.net/uploads/2022/03/Gears_2560_Lede.png)Quanta Magazine; source: anttoniart/Shutterstock

 
Algorithms — the chunks of code that allow programs to sort, filter and combine data, among other things — are the standard tools of modern computing. Like tiny gears inside a watch, algorithms execute well-defined tasks within more complicated programs.

They’re ubiquitous, and in part because of this, they’ve been painstakingly optimized over time. When a programmer needs to sort a list, for example, they’ll reach for a standard “sort” algorithm that’s been used for decades.

Now researchers are taking a fresh look at traditional algorithms, using the branch of artificial intelligence known as machine learning. Their approach, called algorithms with predictions, takes advantage of the insights machine learning tools can provide into the data that traditional algorithms handle. These tools have, in a real way, rejuvenated research into basic algorithms.

Machine learning and traditional algorithms are “two substantially different ways of computing, and algorithms with predictions is a way to bridge the two,” said [Piotr Indyk](https://people.csail.mit.edu/indyk/), a computer scientist at the Massachusetts Institute of Technology. “It’s a way to combine these two quite different threads.”

The recent explosion of interest in this approach began in 2018 with [a paper](https://arxiv.org/abs/1712.01208) by [Tim Kraska](https://people.csail.mit.edu/kraska/), a computer scientist at MIT, and a team of Google researchers. In it, the authors suggested that machine learning could improve a well-studied traditional algorithm called a Bloom filter, which solves a straightforward but daunting problem.

Imagine you run your company’s IT department and you need to check if your employees are going to websites that pose a security risk. Naively, you might think you’ll need to check every site they visit against a blacklist of known sites. If the list is huge (as is likely the case for undesirable sites on the internet), the problem becomes unwieldy — you can’t check every site against a huge list in the tiny amount of time before a webpage loads.

The Bloom filter provides a solution, allowing you to quickly and accurately check whether any particular site’s address, or URL, is on the blacklist. It does this by essentially compressing the huge list into a smaller list that offers some specific guarantees.

Bloom filters never produce false negatives — if they say the site is bad, it’s bad. However, they can produce false positives, so perhaps your employees won’t be able to visit some sites they should have access to. That’s because they trade some accuracy for an enormous amount of data compression — a trick called “lossy compression.” The more that Bloom filters compress the original data, the less accurate they are, but the more space they save.

To a simple Bloom filter, every website is equally suspicious until it’s confirmed to not be on the list. But not all websites are created equal: Some are more likely than others to wind up on a blacklist, simply because of details like their domain or the words in their URL. People understand this intuitively, which is why you likely read URLs to make sure they’re safe before you click on them.

Kraska’s team developed an algorithm that can also apply this kind of logic. They called it a “learned Bloom filter,” and it combines a small Bloom filter with a recurrent neural network (RNN) — a machine learning model that learns what malicious URLs look like after being exposed to hundreds of thousands of safe and unsafe websites.

When the learned Bloom filter checks a website, the RNN acts first and uses its training to determine if the site is on the blacklist. If the RNN says it’s on the list, the learned Bloom filter rejects it. But if the RNN says the site isn’t on the list, then the small Bloom filter gets a turn, accurately but unthinkingly searching its compressed websites.

By putting the Bloom filter at the end of the process and giving it the final say, the researchers made sure that learned Bloom filters can still guarantee no false negatives. But because the RNN pre-filters true positives using what it’s learned, the small Bloom filter acts more as a backup, keeping its false positives to a minimum as well. A benign website that could have been blocked by a larger Bloom filter can now get past the more accurate learned Bloom filter. Effectively, Kraska and his team found a way to take advantage of two proven but traditionally separate ways of approaching the same problem to achieve faster, more accurate results.

Kraska’s team showed that the new approach worked, but they didn’t formalize why. That task fell to [Michael Mitzenmacher](https://www.eecs.harvard.edu/~michaelm/), an expert on Bloom filters at Harvard University, who found Kraska’s paper “innovative and exciting,” but also fundamentally unsatisfying. “They run experiments saying their algorithms work better. But what exactly does that mean?” he asked. “How do we know?”

In 2019, Mitzenmacher put forward [a formal definition](https://arxiv.org/abs/1901.00902) of a learned Bloom filter and analyzed its mathematical properties, providing a theory that explained exactly how it worked. And whereas Kraska and his team showed that it could work in one case, Mitzenmacher proved it could always work.

Mitzenmacher also improved the learned Bloom filters. He showed that adding another standard Bloom filter to the process, this time before the RNN, can pre-filter negative cases and make the classifier’s job easier. He then proved it was an improvement using the theory he developed.

The early days of algorithms with predictions have proceeded along this cyclical track — innovative ideas, like the learned Bloom filters, inspire rigorous mathematical results and understanding, which in turn lead to more new ideas. In the past few years, researchers have shown how to incorporate algorithms with predictions into [scheduling algorithms](https://arxiv.org/abs/1902.00732), [chip design](https://arxiv.org/abs/2004.10746) and [DNA-sequence searches](https://arxiv.org/abs/1910.04728).

In addition to performance gains, the field also advances an approach to computer science that’s growing in popularity: making algorithms more efficient by designing them for typical uses.

Currently, computer scientists often design their algorithms to succeed under the most difficult scenario — one designed by an adversary trying to stump them. For example, imagine trying to check the safety of a website about computer viruses. The website may be benign, but it includes “computer virus” in the URL and page title. It’s confusing enough to trip up even sophisticated algorithms.

Indyk calls this a paranoid approach. “In real life,” he said, “inputs are not generally generated by adversaries.” Most of the websites employees visit, for example, aren’t as tricky as our hypothetical virus page, so they’ll be easier for an algorithm to classify. By ignoring the worst-case scenarios, researchers can design algorithms tailored to the situations they’ll likely encounter. For example, while databases currently treat all data equally, algorithms with predictions could lead to databases that structure their data storage based on their contents and uses.

And this is still only the beginning, as programs that use machine learning to augment their algorithms typically only do so in a limited way. Like the learned Bloom filter, most of these new structures only incorporate a single machine learning element. Kraska imagines an entire system built up from several separate pieces, each of which relies on algorithms with predictions and whose interactions are regulated by prediction-enhanced components.

“Taking advantage of that will impact a lot of different areas,” Kraska said.
