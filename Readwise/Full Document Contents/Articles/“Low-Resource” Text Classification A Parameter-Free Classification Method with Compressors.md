# “Low-Resource” Text Classification: A Parameter-Free Classification Method with Compressors

![rw-book-cover](https://aclanthology.org/thumb/2023.findings-acl.426.jpg)

## Metadata
- Author: [[Zhiying Jiang]]
- Full Title: “Low-Resource” Text Classification: A Parameter-Free Classification Method with Compressors
- Category: #articles
- Document Tags: [[ifttt]] [[twitter]] 
- Summary: This paper introduces a simple and parameter-free method for text classification using compressors and k-nearest-neighbor classifier. The method achieves competitive results without the need for millions of parameters or large labeled datasets. It performs well on both in-distribution and out-of-distribution datasets, including low-resource languages.
- URL: https://aclanthology.org/2023.findings-acl.426

## Full Document
###### Abstract

Deep neural networks (DNNs) are often used for text classification due to their high accuracy. However, DNNs can be computationally intensive, requiring millions of parameters and large amounts of labeled data, which can make them expensive to use, to optimize, and to transfer to out-of-distribution (OOD) cases in practice. In this paper, we propose a non-parametric alternative to DNNs that’s easy, lightweight, and universal in text classification: a combination of a simple compressor like *gzip* with a k-nearest-neighbor classifier. Without any training parameters, our method achieves results that are competitive with non-pretrained deep learning methods on six in-distribution datasets.It even outperforms BERT on all five OOD datasets, including four low-resource languages. Our method also excels in the few-shot setting, where labeled data are too scarce to train DNNs effectively.

Anthology ID:2023.findings-acl.426Volume:[Findings of the Association for Computational Linguistics: ACL 2023](https://aclanthology.org/volumes/2023.findings-acl/)Month:JulyYear:2023Address:Toronto, CanadaVenue:[Findings](https://aclanthology.org/venues/findings/)SIG:Publisher:Association for Computational LinguisticsNote:Pages:6810–6828Language:URL:<https://aclanthology.org/2023.findings-acl.426>DOI:Bibkey:Cite (ACL):Zhiying Jiang, Matthew Yang, Mikhail Tsirlin, Raphael Tang, Yiqin Dai, and Jimmy Lin. 2023. [“Low-Resource” Text Classification: A Parameter-Free Classification Method with Compressors](https://aclanthology.org/2023.findings-acl.426). In *Findings of the Association for Computational Linguistics: ACL 2023*, pages 6810–6828, Toronto, Canada. Association for Computational Linguistics.Cite (Informal):Copy Citation:PDF:
