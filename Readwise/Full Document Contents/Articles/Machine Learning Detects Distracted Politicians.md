# Machine Learning Detects Distracted Politicians

![rw-book-cover](https://hackaday.com/wp-content/uploads/2022/01/The-Flemish-Scrollers-Dries-Depoorter.png)

## Metadata
- Author: [[Donald Papp]]
- Full Title: Machine Learning Detects Distracted Politicians
- Category: #articles
- Summary: [Dries Depoorter] has a knack for highly technical projects with a solid artistic bent to them, and this piece is no exception.
- URL: https://hackaday.com/2022/01/17/machine-learning-detects-distracted-politicians/

## Full Document
![People in meeting, with highlights of detected phones and identities](https://hackaday.com/wp-content/uploads/2022/01/The-Flemish-Scrollers-Dries-Depoorter.png?w=606)
[Dries Depoorter] has a knack for highly technical projects with a solid artistic bent to them, and this piece is no exception. [The Flemish Scrollers](https://driesdepoorter.be/theflemishscrollers/) is a software system that watches live streamed sessions of the Flemish government, and uses Python and machine learning to identify and highlight politicians who pull out phones and start scrolling. The results? Pushed out live on Twitter and Instagram, naturally. The project started back in July 2021, and has been dutifully running ever since, so by now we expect that holding one’s phone where the camera can see it is probably considered a rookie mistake.

This project can also be considered a good example of how to properly handle confidence in results depending on the application. In this case, false negatives (a politician is using a phone, but the software doesn’t detect it properly) are much more acceptable than false positives (a member gets incorrectly identified, or is wrongly called-out for using a mobile device when they are not.)

[Keras](https://keras.io/), an open-source software library, is used for the object detection and facial recognition (GitHub repository for Keras is [here](https://github.com/keras-team/keras).) We’ve seen it used in everything from [bat detection](https://hackaday.com/2017/08/10/we-should-stop-here-its-bat-country/) to [automatic trash sorting](https://hackaday.com/2019/09/01/automate-sorting-your-trash-with-some-healthy-machine-learning/), so if you’re interested in machine learning applications, give it a peek.
