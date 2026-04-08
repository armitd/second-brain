# Biases in AI Systems

![rw-book-cover](https://cacm.acm.org/favicon.ico)

## Metadata
- Author: [[Ramya Srinivasan and Ajay Chander]]
- Full Title: Biases in AI Systems
- Category: #articles
- Summary: 1. Ali, M., Sapiezynsk, P., Bogen, M., Korolova, A., Mislove, A., Rieke, A. Discrimination through optimization: how Facebook's ad delivery can lead to biased outcomes. In Proceedings of the ACM on Human-Computer Interaction 3 (2019); https://dl.acm.org/doi/10.1145/3359301. 2. Amatriain, X.
- URL: https://cacm.acm.org/practice/biases-in-ai-systems/

## Full Document
![multicolored crystaline cubes, illustration](https://cacm.acm.org/wp-content/uploads/2021/08/072221_CACMpg45_Biases-in-AI2.jpg)multicolored crystaline cubes, illustration
A child wearing sunglasses is labeled as a “failure, loser, nonstarter, unsuccessful person.” This is just one of the many systemic biases exposed by ImageNet Roulette, an art project that applies labels to user-submitted photos by sourcing its identification system from the original ImageNet database.[7](https://cacm.acm.org/practice/biases-in-ai-systems/#R7) ImageNet, which has been one of the instrumental datasets for advancing AI, has deleted more than half a million images from its “person” category since this instance was reported in late 2019.[23](https://cacm.acm.org/practice/biases-in-ai-systems/#R23) Earlier in 2019, researchers showed how Facebook’s ad-serving algorithm for deciding who is shown a given ad exhibits discrimination based on race, gender, and religion of users.[1](https://cacm.acm.org/practice/biases-in-ai-systems/#R1) There have been reports of commercial facial-recognition software (notably Amazon’s Rekognition, among others) being biased against darker-skinned women.[6](https://cacm.acm.org/practice/biases-in-ai-systems/#R6),[22](https://cacm.acm.org/practice/biases-in-ai-systems/#R22)

These examples provide a glimpse into a rapidly growing body of work that is exposing the bias associated with AI systems, but biased algorithmic systems are not a new phenomenon. As just one example, in 1988, the U.K. Commission for Racial Equality found a British medical school guilty of discrimination because the algorithm used to shortlist interview candidates was biased against women and applicants with non-European names.[17](https://cacm.acm.org/practice/biases-in-ai-systems/#R17)

With the rapid adoption of AI across a variety of sectors, including in areas such as justice and health care, technologists and policy makers have raised concerns about the lack of accountability and bias associated with AI-based decisions. From AI researchers and software engineers to product leaders and consumers, a variety of stakeholders are involved in the AI pipeline. The necessary expertise around AI, datasets, and the policy and rights landscape that collectively helps uncover bias is not uniformly available among these stakeholders. As a consequence, bias in AI systems can compound inconspicuously.

Consider, for example, the critical role of machine learning (ML) developers in this pipeline. They are asked to: preprocess the data appropriately, choose the right models from several available ones, tune parameters, and adapt model architectures to suit the requirements of an application. Suppose an ML developer was entrusted with developing an AI model to predict which loans will default. Unaware of bias in the training data, an engineer may inadvertently train models using only the validation accuracy. Suppose the training data contained too many young people who defaulted. In this case, the model is likely to make a similar prediction about young people defaulting when applied to test data. There is thus a need to educate ML developers about the various kinds of biases that can creep into the AI pipeline.

Defining, detecting, measuring, and mitigating bias in AI systems is not an easy task and is an active area of research.[4](https://cacm.acm.org/practice/biases-in-ai-systems/#R4) A number of efforts are being undertaken across governments, nonprofits, and industries, including enforcing regulations to address issues related to bias. As work proceeds toward recognizing and addressing bias in a variety of societal institutions and pathways, there is a growing and persistent effort to ensure that computational systems are designed to address these concerns.

The broad goal of this article is to educate nondomain experts and practitioners such as ML developers about various types of biases that can occur across the different stages of the AI pipeline and suggest checklists for mitigating bias. There is a vast body of literature related to the design of fair algorithms.[4](https://cacm.acm.org/practice/biases-in-ai-systems/#R4) As this article is directed at aiding ML developers, the focus is not on the design of fair AI algorithms but rather on practical aspects that can be followed to limit and test for bias during problem formulation, data creation, data analysis, and evaluation. Specifically, the contributions can be summarized as follows:

* *Taxonomy of biases in the AI pipeline.* A structural organization of the various types of bias that can creep into the AI pipeline is provided, anchored in the various phases from data creation and problem formulation to data preparation and analysis.
* *Guidelines for bridging the gap between research and practice.* Analyses that elucidate the challenges associated with implementing research ideas in the real world are listed, as well as suggested practices to fill this gap. Guidelines that can aid ML developers in testing for various kinds of biases are provided.

The goal of this work is to enhance awareness and practical skills around bias, toward the judicious use and adoption of AI systems.

[Back to Top](https://cacm.acm.org/practice/biases-in-ai-systems/#)

##### Biases in the AI Pipeline

A typical AI pipeline starts from the data-creation stage: collecting the data; annotating or labeling it; and preparing or processing it into a format that can be consumed by the rest of the pipeline. Let’s analyze how different types of bias can be introduced in each of these steps.

**Data-creation bias.** Specific types of biases can occur during the creation of datasets.

[Back to Top](https://cacm.acm.org/practice/biases-in-ai-systems/#)

##### Sampling Bias

The bias that arises in a dataset that is created by selecting particular types of instances more than others (and thereby rendering the dataset under-representative of the real world) is called *sampling bias.* This is one of the most common types of dataset biases. Datasets are often created with a particular set of instances. For example, image datasets prefer street scenes or nature scenes.[25](https://cacm.acm.org/practice/biases-in-ai-systems/#R25) A face-recognition algorithm may be fed with more photos of light-skinned faces than dark-skinned faces, thereby leading to poor performance in recognizing darker-skinned faces.[6](https://cacm.acm.org/practice/biases-in-ai-systems/#R6) Thus, sampling bias can result in poor generalization of learned algorithms.

[Back to Top](https://cacm.acm.org/practice/biases-in-ai-systems/#)

##### Measurement Bias

Measurement bias is introduced by errors in human measurement, or because of certain intrinsic habits of people in capturing data. As an example, consider the creation of image and video datasets, where the images or videos may reflect the techniques used by the photographers. For example, some photographers might tend to take pictures of objects in similar ways; as a result, the dataset may contain object views from certain angles only. In their 2011 paper “Unbiased Look at Dataset Bias,” Torralba and Efros refer to this type of measurement bias as *capture bias.*[25](https://cacm.acm.org/practice/biases-in-ai-systems/#R25)

Another source of measurement bias could be a result of the device used to capture datasets. For example, cameras used to capture images may be defective, leading to poor-quality images and thereby contributing to biased results. These types of biases are broadly categorized as *device bias.*

A third type of measurement bias can occur when proxies are used instead of true values in creating the dataset. For example, arrest rates are often used instead of crime rates; doctor visits and medications are used as indicators of medical conditions, and so on.

[Back to Top](https://cacm.acm.org/practice/biases-in-ai-systems/#)

##### Label Bias

Label bias is associated with inconsistencies in the labeling process. Different annotators have different styles and preferences that get reflected in the labels created. A common instance of label bias arises when different annotators assign differing labels to the same type of object (for example, *grass* vs. *lawn, painting* vs. *picture*).[25](https://cacm.acm.org/practice/biases-in-ai-systems/#R25)

Yet another type of label bias can happen when the subjective biases of evaluators affect labeling. For example, in a task of annotating emotions experienced in a text, the labels could be biased by the subjective preferences of annotators such as their culture, beliefs, and introspective capabilities.[24](https://cacm.acm.org/practice/biases-in-ai-systems/#R24) *Confirmation bias*,[21](https://cacm.acm.org/practice/biases-in-ai-systems/#R21) which is the human tendency to search for, interpret, focus on, and remember information in a way that confirms one’s preconceptions, is closely related to this type of label bias. Thus, labels may be assigned based on prior belief rather than objective assessments.

A third type of label bias can arise from the peak end effect. This is a type of memory-related cognitive bias in which people judge an experience based largely on how they felt at its peak (that is, its most intense point) and at its end, rather than based on the total sum or average of every moment of the experience.[15](https://cacm.acm.org/practice/biases-in-ai-systems/#R15) For example, some annotators may give more importance to the last part of a conversation (rather than the entire conversation) in assigning a label.[24](https://cacm.acm.org/practice/biases-in-ai-systems/#R24)

[Back to Top](https://cacm.acm.org/practice/biases-in-ai-systems/#)

##### Negative Set Bias

Torralba and Efros define *negative set bias* as being introduced in the dataset as a consequence of not having enough samples representative of “the rest of the world.”[25](https://cacm.acm.org/practice/biases-in-ai-systems/#R25) The authors state that “datasets define a phenomenon (for example, object, scene, event) not just by what it is (positive instances), but also by what it is not (negative instances).” As a consequence, the learned classifiers can perform poorly in detecting negative instances.

**Biases related to problem formulation.** Biases can arise based on how a problem is defined. Consider the following example presented in *MIT Technology Review* by Karen Hao.[13](https://cacm.acm.org/practice/biases-in-ai-systems/#R13) Suppose a credit card company wants to predict a customer’s creditworthiness using AI. In order to do so, creditworthiness must be defined in a manner that can be “predicted or estimated.” The problem can be formulated based on what the company wants, say, to maximize its profit margin or to maximize the number of loans that get repaid; however, “those decisions are made for various business reasons other than fairness or discrimination,” says Cornell University’s Solan Barocas, who specializes in fairness.

[Back to Top](https://cacm.acm.org/practice/biases-in-ai-systems/#)

##### Framing Effect Bias

The previous creditworthiness example can be thought of as a type of *framing effect bias.*[21](https://cacm.acm.org/practice/biases-in-ai-systems/#R21) Based on how the problem is formulated and how information is presented, the results obtained can be different and perhaps biased. Another notable example is the COMPAS (Correctional Offender Management Profiling for Alternative Sanctions) debate[8](https://cacm.acm.org/practice/biases-in-ai-systems/#R8) concerning the definition of fairness between Northpointe (now known as Equivant), which came up with COMPAS scores for assessing risk of recidivism, and *ProPublica*, which claimed that the COMPAS system was biased. *ProPublica* claimed that Northpointe’s method was biased against black defendants as the group was associated with a higher false-positive rate. There are several metrics of fairness, and *ProPublica* stated that Northpointe’s system violated equalized odds and equality of opportunity fairness criteria. Northpointe’s main defense was that scores satisfied fairness from the viewpoint of predictive rate parity.[4](https://cacm.acm.org/practice/biases-in-ai-systems/#R4) Thus, bias can arise based on the way a problem and its success metrics are defined.

**Biases related to the algorithm/data analysis.** Several types of biases can occur in the algorithm or during data analysis.

[Back to Top](https://cacm.acm.org/practice/biases-in-ai-systems/#)

##### Sample Selection Bias

*Sample selection bias* is introduced by the selection of individuals, groups, or data for analysis in such a way that the samples are not representative of the population intended to be analyzed.[9](https://cacm.acm.org/practice/biases-in-ai-systems/#R9) In particular, sample selection bias occurs during data analysis as a result of conditioning on some variables in the dataset (for example, a particular skin color, gender, among others), which in turn can create spurious correlations. For example, in analyzing the effect of motherhood on wages, if the study is restricted to women who are already employed, then the measured effect will be biased as a result of conditioning on employed women.[9](https://cacm.acm.org/practice/biases-in-ai-systems/#R9) Common types of sample selection bias include Berkson’s paradox[20](https://cacm.acm.org/practice/biases-in-ai-systems/#R20) and sample truncation.[9](https://cacm.acm.org/practice/biases-in-ai-systems/#R9)

[Back to Top](https://cacm.acm.org/practice/biases-in-ai-systems/#)

##### Confounding Bias

Bias can arise in the AI model if the algorithm learns the wrong relations by not taking into account all the information in the data or if it misses the relevant relations between features and target outputs.[20](https://cacm.acm.org/practice/biases-in-ai-systems/#R20) *Confounding bias* originates from common causes that affect both inputs and outputs. Consider a scenario wherein admissions to a graduate school are based on the person’s previous grade point average. There might be other factors, however, such as ability to get coaching, which in turn may be dependent on sensitive attributes such as race; and these factors may determine the grade point average and admission rates.[16](https://cacm.acm.org/practice/biases-in-ai-systems/#R16) As a result, spurious relations between inputs and outputs are introduced and thus can lead to bias.

>  *Based on how the problem is formulated and how information is presented, the results obtained can be different and perhaps biased.*
> 
>  

A special type of confounding bias is the *omitted variable*, which occurs when some relevant features are not included in the analysis. This is also related to the problem of model underfitting.

Another type of confounding bias is the *proxy variable.* Even if sensitive variables such as race and gender are not considered for decision making, certain other variables used in the analysis might serve as “proxies” for those sensitive variables. For example, zip code might be indicative of race, as people of a certain race might predominantly live in a certain neighborhood. This type of bias is also commonly referred to as *indirect bias* or *indirect discrimination.*

[Back to Top](https://cacm.acm.org/practice/biases-in-ai-systems/#)

##### Design-Related Bias

Sometimes, biases occur as a result of algorithmic limitations or other constraints on the system such as computational power. A notable entry in this category is *algorithm bias*, which can be defined as bais that is solely induced or added by the algorithm. In their 1996 paper “Bias in Computer Systems,” Friedman and Nissenbaum[10](https://cacm.acm.org/practice/biases-in-ai-systems/#R10) provide an example: Software that relies on randomness for fair distributions of results is not truly random; for example, by skewing selections toward items at the end or beginning of a list, the results can become biased.

Another type of design-related bias is *ranking bias.*[18](https://cacm.acm.org/practice/biases-in-ai-systems/#R18) For example, a search engine that shows three results per screen can be understood to privilege the top three results slightly more than the next three.[10](https://cacm.acm.org/practice/biases-in-ai-systems/#R10) Ranking bias is also closely related to presentation bias,[18](https://cacm.acm.org/practice/biases-in-ai-systems/#R18) which is derived from the fact that you can receive user feedback only on items that have been presented to the user. Even among those that are shown, the probability of receiving user feedback is further affected by where the item is shown.[2](https://cacm.acm.org/practice/biases-in-ai-systems/#R2)

**Biases related to evaluation/validation.** Several types of biases result from those inherent in human evaluators, as well as in the selection of those evaluators (sample treatment bias).

[Back to Top](https://cacm.acm.org/practice/biases-in-ai-systems/#)

##### Human Evaluation Biases

Often, human evaluators are employed in validating the performance of an AI model. Phenomena such as confirmation bias, peak end effect, and prior beliefs (for example, culture) can create biases in evaluation.[15](https://cacm.acm.org/practice/biases-in-ai-systems/#R15) Human evaluators are also constrained by how much information they can recall, which can result in *recall bias.*

[Back to Top](https://cacm.acm.org/practice/biases-in-ai-systems/#)

##### Sample Treatment Bias

Sometimes, test sets selected for evaluating an algorithm may be biased.[3](https://cacm.acm.org/practice/biases-in-ai-systems/#R3) For example, in recommendation systems, some specific viewers (for example, those speaking a certain language) may be shown an advertisement, and some may not. As a consequence, the observed effects will not be representative of true effects on the general population. The bias introduced in the process of selectively subjecting some sets of people to a type of treatment is called *sample treatment bias.*

[Back to Top](https://cacm.acm.org/practice/biases-in-ai-systems/#)

##### Validation and Test Dataset Biases

Biases can also be induced from sample selection and label biases in the validation and test datasets.[25](https://cacm.acm.org/practice/biases-in-ai-systems/#R25) In general, biases associated with the dataset-creation stage could show up in the model-evaluation stage as well. Additionally, evaluation bias can result from the selection of inappropriate benchmarks/datasets for testing.

The accompanying [figure](https://dl.acm.org/cms/attachment/3d7a920c-6129-401e-8334-7a80052906f5/uf1.jpg) provides an illustration of the taxonomy of biases along the various stages of the AI pipeline as discussed in the previous sections.

Despite significant research efforts within the AI community to address bias-related challenges, several gaps impede the collective progress. Next, we highlight some of these gaps.

[![uf1.jpg](https://dl.acm.org/cms/attachment/3d7a920c-6129-401e-8334-7a80052906f5/uf1.jpg)](https://dl.acm.org/cms/attachment/3d7a920c-6129-401e-8334-7a80052906f5/uf1.jpg)
**Figure. Taxonomy of bias types along the AI pipleline.**

[Back to Top](https://cacm.acm.org/practice/biases-in-ai-systems/#)

##### Gaps Between Research and Practice

Methods to counter dataset bias issues have been proposed, as have new datasets with an emphasis on maintaining diversity. For example, the diversity-in-faces dataset consists of almost a million images of people pulled from the Yahoo! Flickr Creative Commons dataset, assembled specifically to achieve statistical parity among categories of skin tone, facial structure, age, and gender. In their 2019 paper, “Excavating AI,” Crawford and Paglen, however, question the use of cranio-metrical features used in creating this dataset, as these features could also be proxies for racial bias.[7](https://cacm.acm.org/practice/biases-in-ai-systems/#R7) The authors further provide a critical review of issues pertaining to several benchmark datasets.

“Fairness in machine learning” is an active area of research. There are also conferences and workshops dedicated to the theme. A complete overview of fairness in machine learning is beyond the scope of this survey. For an extensive overview of various algorithmic definitions of fairness and methods to achieve fairness in classification, consult Barocas et al.[4](https://cacm.acm.org/practice/biases-in-ai-systems/#R4) There are also open-source tools such as IBM’s AI Fairness 3605 that facilitates detection and mitigation of unwanted algorithmic bias. Despite these efforts, there are notable gaps, as noted by Gajane and Pechenizkiy in their 2018 paper, “On Formalizing Fairness in Prediction with Machine Learning.[11](https://cacm.acm.org/practice/biases-in-ai-systems/#R11)

**Filling the gap.** Practice guidelines have been proposed for reducing the potential bias in AI systems. These include “Factsheets for Datasets” from IBM, and “Datasheets for Datasets,” an approach for sharing essential information about datasets used to train AI models.[12](https://cacm.acm.org/practice/biases-in-ai-systems/#R12) In their 2019 paper, Mitchell et al. suggest the use of detailed documentation of released models in order to encourage transparency.[19](https://cacm.acm.org/practice/biases-in-ai-systems/#R19)

Holstein et al. identify areas of alignment and disconnect between the challenges faced by teams in practice and the solutions proposed in the fair ML research literature.[14](https://cacm.acm.org/practice/biases-in-ai-systems/#R14) The authors urge that future research should focus on supporting practitioners in collecting and curating high-quality datasets. The authors further see a need for creating domain-specific educational resources, metrics, processes, and tools. In that spirit, this article aims to be an educational resource for ML developers in understanding various sources of biases in the AI pipeline.

[Back to Top](https://cacm.acm.org/practice/biases-in-ai-systems/#)

##### Guidelines for ML Developers

While it may not be possible to eliminate all sources of bias, with certain precautionary measures, some bias issues can be reduced. Here are some key messages that could aid ML developers in identifying potential sources of bias and help in avoiding the introduction of unwanted bias:

* Incorporation of domain-specific knowledge is crucial in defining and detecting bias. It is important to understand the structural dependencies among various features in the dataset. Often, it helps to draw a structural diagram illustrating various features of interest and their interdependencies. This can then help in identifying the sources of bias.[20](https://cacm.acm.org/practice/biases-in-ai-systems/#R20)
* It is also important to understand which features of the data are deemed sensitive based on the application. For example, age may be a sensitive feature in determining who gets a loan, but not necessarily in determining who gets a medical treatment. Furthermore, there may be proxy features that, although not thought to be sensitive features, may still encode sensitive information so as to render biased predictions.
* As far as possible, datasets used for analysis should be representative of the true population under consideration. Thus, care has to be taken in constructing representative datasets.
* Appropriate standards have to be laid out for annotating the data. Rules have to defined so as to obtain consistent labels from annotators as much as possible.
* Identifying all features that may be associated with the target feature of interest is important. Omitting variables that have dependencies with the target feature leads to a biased estimate.
* Features that are associated with both input and output can lead to biased estimates. In such cases, it is important to eliminate these sources of confounding biases by appropriate data conditioning and randomization strategies in selecting input.[20](https://cacm.acm.org/practice/biases-in-ai-systems/#R20)
* Restricting data analysis to some truncated portions of the dataset can lead to unwanted selection bias. Thus, in choosing subsets of data for analysis, care must be taken not to introduce sample selection bias.
* In validating the performance of a model such as in A/B testing, care has to be taken to guard against the introduction of sample treatment bias. In other words, in testing the performance of a model, the test conditions should not be restricted to a certain subset of the population (for example, showing recommendation results to people of a certain locality only), as the results would be biased.

[Back to Top](https://cacm.acm.org/practice/biases-in-ai-systems/#)

##### Conclusion

This article provides an organization of various kinds of biases that can occur in the AI pipeline starting from dataset creation and problem formulation to data analysis and evaluation. It highlights the challenges associated with the design of bias-mitigation strategies, and it outlines some best practices suggested by researchers. Finally, a set of guidelines is presented that could aid ML developers in identifying potential sources of bias, as well as avoiding the introduction of unwanted biases. The work is meant to serve as an educational resource for ML developers in handling and addressing issues related to bias in AI systems.

Submit an Article to CACM

CACM welcomes unsolicited [submissions](https://cacm.acm.org/author-guidelines/#CACMsubmission) on topics of relevance and value to the computing community.

You Just Read

######  Biases in AI Systems

 [View in the ACM Digital Library](https://dl.acm.org/doi/10.1145/3464903) 

**©2021 ACM 0001-0782/21/8**

Permission to make digital or hard copies of part or all of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than ACM must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists, requires prior specific permission and/or fee. Request permission to publish from [permissions@acm.org](mailto:permissions@acm.org) or fax (212) 869-0481.

The Digital Library is published by the Association for Computing Machinery. Copyright © 2021 ACM, Inc.
