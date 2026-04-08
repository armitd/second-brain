# Overcoming the challenges of working with small data

![rw-book-cover](https://venturebeat.com/wp-content/uploads/2021/06/GettyImages-1246715578-e1624227330919.jpg?w=1200&strip=all)

## Metadata
- Author: [[Ivan Smetannikov]]
- Full Title: Overcoming the challenges of working with small data
- Category: #articles
- Summary: Join our daily and weekly newsletters for the latest updates and exclusive content on industry-leading AI coverage. Learn More
- URL: https://venturebeat.com/enterprise-analytics/overcoming-challenges-working-with-small-data/

## Full Document
![](https://venturebeat.com/wp-content/uploads/2021/06/GettyImages-1246715578-e1624227330919.jpg?fit=750%2C500&strip=all)
*To further strengthen our commitment to providing industry-leading coverage of data technology, VentureBeat is excited to welcome Andrew Brust and as a regular contributor. Watch for his articles in the [Data Pipeline](https://venturebeat.com/tag/data-pipeline/).*

Have you had trouble with airplane seats because you’re too tall? Or maybe you haven’t been able to reach the top shelf at the supermarket because you’re too short? Either way, nearly all of these things are designed with the average person’s height in mind: 170cm — or 5’ 7″.

In fact, nearly everything in our world is designed around averages.

No compatible source was found for this media.

Some content could not be imported from the original document. [View content ↗](https://imasdk.googleapis.com/js/core/bridge3.549.0_en.html#goog_1820140462) 

Most businesses only work with averages because they fit the majority of cases. They allow companies to reduce production costs and maximize profits. However, there are many scenarios where covering 70-80% of cases isn’t enough. We as an industry need to understand how to tackle the remaining cases effectively.

In this article, we’ll talk about the challenges of working with [small data](https://venturebeat.com/data-infrastructure/how-simple-data-analytics-can-put-your-data-to-work-before-you-are-ml-ready/) in two particular cases: When datasets have a few entries in general and when they are poorly represented sub-parts of bigger, biased datasets. You’ll also find applicable tips on how to approach these problems.

##### Event

Intelligent Security Summit On-Demand

Learn the critical role of AI & ML in cybersecurity and industry specific case studies. Watch on-demand sessions today.

 [Watch Here](https://avolio.swapcard.com/intelligentsecuritysummit2022/registrations/Start?utm_source=vb&utm_medium=incontent&utm_content=ondemand&utm_campaign=IS22_InContent) 

#### What is small data?

It’s important to understand the concept of small data first. Small data, as opposed to [big data](https://venturebeat.com/data-infrastructure/survival-of-the-most-informed-the-journey-to-innovation-begins-with-data/), is data that comes in small volumes that are often comprehensible to humans. Small data can also sometimes be a subset of a larger dataset that describes a particular group.

#### What are the problems with small data for real-life tasks?

There are two common scenarios for small data challenges.

**Scenario 1:** Data distribution describes the outer world pretty well, but you simply don’t have a lot of data. It might be expensive to collect, or it could describe objects that aren’t that commonly observed in the real world. For example, data about breast cancer for younger women: You will probably have a reasonable amount of data for white women aged 45-55 and older, but not for younger ones.

**Scenario 2:** You might be building a translation system for one of the low-resource languages. For example, there is a lot of available data in Italian available online, but with Rhaeto-Romance languages, the availability of useable data is more complicated.

advertisement

##### Problem 1: The model becomes prone to overfitting

When the dataset is big, you can avoid overfitting, but that is much more challenging in the case of small data. You risk making a too-complicated model that fits your data perfectly, but isn’t that effective in real-life scenarios.

**Solution:** Use simpler models. Usually, when working with small data, engineers are tempted to use complicated models to perform more complicated transformations and describe more complex dependencies. These models won’t help you with your overfitting problem when your dataset is small, and you don’t have the luxury of simply feeding more data to the algorithm.

advertisement

Apart from overfitting, you might also notice that a model trained on small data doesn’t converge very well. For such data, premature convergence can present a huge problem for developers as the model fails in local optimums really fast and it’s hard to get out of there.

In this scenario, it is possible to up-sample your dataset. There are many algorithms such as classical sampling methods like the synthetic minority oversampling technique (SMOTE) and its modern modifications and neural network-based approaches like generative adversarial networks (GANs). The solution depends on how much data you actually have. Often, stacking can help you to improve metrics and not overfit.

Another possible solution is to use transfer learning. Transfer learning can be used to effectively build solutions, even if you have a small dataset. However, to be able to perform transfer learning you need to have enough data from adjacent fields that your model can learn from.

It’s not always possible to gather this data, and even if you do, it might work only to a certain extent. There are still inherent differences between different tasks. Moreover, the proximity of different fields cannot be proven, as they cannot be measured directly. Oftentimes, this solution is also essentially a hypothesis provided by your own expertise that you are using to build a transfer learning procedure.

advertisement

##### Problem 2: The curse of dimensionality

There are lots of features but very few objects, which means that the model doesn’t learn. What can be done?

The solution is to reduce the number of features. You can apply feature extraction (construction) or feature selection, or you can use both. For most cases, it will be better to apply feature selection first.

###### Feature extraction

You use feature extraction to reduce the dimensionality of your model and improve its performance when there are small data involved. For that, you can use kernel methods, convolutional neural networks (CNNs) or even some visualization and embedding methods like PCA and t-SNE.

advertisement

In CNNs, convolutional layers work like filters. For example, for images, convolutional layers perform image feature extraction and calculate a new image in a new intermediary layer.

The problem is that for most cases with feature extraction, you lose interpretability. You can’t use the resulting model in [medical](https://venturebeat.com/ai/what-is-medical-artificial-intelligence-ai/) diagnosis because even if the accuracy of the diagnosis is supposedly improved when you give it to the doctor, he won’t be able to use it because of medical ethics. CNN-based diagnosis is hard to interpret, which means it doesn’t work for sensitive applications.

###### Feature selection

advertisement

Another approach involves the elimination of some features. For that to work, you need to choose the most useful ones and delete all the rest. For example, if before you had 300 features, after the reduction you will have 20, and the curse of dimensionality will be lifted. Most likely the problems will disappear. Moreover, unlike with feature extraction, your model will still be interpretable, so feature selection can be freely applied in sensitive applications.

How to do it? There are three main approaches, but the simplest one is to use filter methods. Let’s imagine that you want to build a model that predicts some class — for example, positive or negative test results for cancer. Here you can apply a Spearman correlation-based feature selection method. If the correlation is high, then you keep the feature. Many methods that you can use in this category come from mathematical statistics: Spearman, Pearson, Information Gain or Gini index (among others).

advertisement

How many features to keep is a different question. Usually, we decide based on the computational limitations we have and how many features we need to keep in order to meet them. Or we can just introduce some simple rule like “pick all the features with a correlation higher than 0.7”. Of course, there are some heuristics like the “broken stick algorithm” or the “elbow rule” that you can apply, but none of them guarantees the best possible result.

Another approach is to use embedded methods. These always work in pairs with some other ML models. There are many models with some embedded features that allow you to perform feature selection, like random forests. For each tree, the so-called “out-of-the-bag-error” is applied: every tree can either be right or wrong in the classification of each object. If it was right, we add scores to all its features, if not — extract.

Then, after renormalization (each feature can be presented a different number of times in the set of trees), sort them down based on the scores obtained and then cut some features you don’t need, just as in filtering methods. During the whole procedure, it uses the model directly in the feature selection process; all embedded methods usually do the same.

advertisement

Finally, we can use classic wrapper methods. Their idea is as simple as that: First, you need somehow to select a feature subset, even at random. Then, train some models on it. A common go-to model is a logistic regression, since it’s rather straightforward. After training it, you’ll get some metrics for your F1 score. Then, you can do it again and evaluate the performance.

To be honest, here, you can use any optimization algorithm to select the next subset to evaluate. The more features we have, the larger the dimensionality. So, wrappers are commonly used for cases with under 100 features. Filters work on any number of features, even a million. Embedding methods are used for intermediary cases if you know what model you’ll use later.

Also, there are hybrid (consecutive) and ensembling (parallel) methods. The simplest example of a hybrid method is the forward selection algorithm: First it selects some subset of features with a filtering method, then it adds them one by one into the resulting feature set in a wrapper way in a metric-descending order.

#### What if your data is incomplete?

So, what can be done when data is biased and not representative of the multitude? What if you haven’t caught the issue? To be honest, it’s hard to predict when it might happen.

advertisement

##### Problem 1

You know there is something you didn’t cover, or it’s rare. There is a “hill” in your data distribution you know a lot about, but you don’t know much about its “tails.”

**Solution:** You cut the “tails,” teach the model on a “hill” and then you can teach separate models on the “tails.” The problem is that if there are so few examples, then just a linear or a tree-based solution can be used; nothing else will work. You can also use just experts and build interpretable models for the “tails” with their help.

advertisement

##### Problem 2

A model is already in production, new objects arrive, and we don’t know how to classify them. Most businesses will just ignore them because it’s a cheap and convenient solution for really rare cases. For example, with NLP, although there are some more sophisticated solutions, you can still ignore unknown words and show the best-fitting result.

**Solution:** User feedback can help you include more diversity in your dataset. If your users have reported something that you don’t have in your dataset, log this object, add it to the training set and then study it closely. You can then send the collected feedback to experts to classify new objects.

##### Problem 3

advertisement

Your dataset might be incomplete, and you aren’t aware that the problem exists. We can’t predict something we don’t know about. Situations where we don’t know that we have an incomplete dataset can result in our business facing real reputational, financial and legal risks.

**Solution:** At the stage of risk assessment, you should always keep in mind that such a possibility exists. Businesses must have a necessary budget to cover such risks and a plan of action to resolve reputational crises and other related problems.

#### Solutions

Most solutions are designed to fit an average. However, in sensitive situations like those in healthcare and banking, fitting the majority isn’t enough. Small data can help us combat the problem of a “one size fits all” solution and introduce more diversity into our product design.

advertisement

Working with small data is challenging. The tools that we use today in [machine learning](https://venturebeat.com/datadecisionmakers/the-current-state-of-mlops-for-machine-learning-engineers/) (ML) are mostly designed to work with Big Data, so you have to be creative. Depending on the scenario that you’re facing, you can select different methods, from SMOTE to mathematical statistics to GAN, and adapt them to your use case.

*Ivan Smetannikov is data science team lead at Serokell*.

##### DataDecisionMakers

Welcome to the VentureBeat community!

DataDecisionMakers is where experts, including the technical people doing data work, can share data-related insights and innovation.

If you want to read about cutting-edge ideas and up-to-date information, best practices, and the future of data and data tech, join us at DataDecisionMakers.

You might even consider [contributing an article](https://venturebeat.com/contribute-to-datadecisionmakers/) of your own!

 #### Intelligent Security Summit On-Demand

 Did you miss a session at Intelligent Security Summit? Head over to the on-demand library to hear insights from experts and learn the importance of cybersecurity in your organization.
