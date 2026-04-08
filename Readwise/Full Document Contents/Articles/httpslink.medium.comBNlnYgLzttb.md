# https://link.medium.com/BNlnYgLzttb

![rw-book-cover](https://miro.medium.com/v2/da:true/resize:fit:1000/0*DnN9sdmYn5sBJYzu)

## Metadata
- Author: [[Derrick Mwiti]]
- Full Title: https://link.medium.com/BNlnYgLzttb
- Category: #articles
- Summary: Object detection with Mask R-CNN in TensorFlow
- URL: https://rsci.app.link/BNlnYgLzttb?_p=c31029c09a047af6e4038d

## Full Document
#### Object detection with Mask R-CNN in TensorFlow

![](https://miro.medium.com/v2/resize:fit:700/0*DnN9sdmYn5sBJYzu)Photo by [Joanna Kosinska](https://unsplash.com/@joannakosinska?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/s/photos/object-detection?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
Building object detection and image segmentation models is slightly different from other models. Majorly because you have to use specialized models and prepare the data in a particular way. This article will examine how to perform object detection and image segmentation on a custom dataset using the TensorFlow 2 Object Detection API.

Let’s dive right in!

### Object detection datasets

In this article, we’ll use the [Coco Car Damage Detection Dataset](https://www.kaggle.com/datasets/lplenka/coco-car-damage-detection-dataset) available on [Kaggle](https://www.kaggle.com/). It contains car images with damages. It can be used to train a model to detect damages on cars and car parts. The dataset has already been annotated, and the corresponding [COCO](https://cocodataset.org/#home) files are provided.

### Preparing datasets for object detection

If you have a custom dataset you’d like to use, then you have to do the labeling and annotation yourself. There are many tools and online platforms that can help you achieve this. If you would like to stick to open source, [Labelme](https://github.com/wkentaro/labelme) is an excellent alternative.

The video below shows how to create polygons on the car dataset. After completing an annotation, you will have to save it. Once you…
