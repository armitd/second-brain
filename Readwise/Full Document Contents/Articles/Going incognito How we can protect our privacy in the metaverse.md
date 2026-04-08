# Going incognito: How we can protect our privacy in the metaverse

![rw-book-cover](https://venturebeat.com/wp-content/uploads/2022/01/GettyImages-1295980136.jpg?w=1200&strip=all)

## Metadata
- Author: [[Louis Rosenberg]]
- Full Title: Going incognito: How we can protect our privacy in the metaverse
- Category: #articles
- Summary: Join our daily and weekly newsletters for the latest updates and exclusive content on industry-leading AI coverage. Learn More The image below shows me standing in a “Virtual Escape Room” that was created by academic researchers at U.C.
- URL: https://venturebeat.com/virtual/going-incognito-how-we-can-protect-our-privacy-in-the-metaverse/

## Full Document
![Faceless person bias in AI concept image](https://venturebeat.com/wp-content/uploads/2022/01/GettyImages-1295980136.jpg?fit=750%2C386&strip=all)
The image below shows me standing in a “Virtual Escape Room” that was created by academic researchers at U.C. Berkeley’s [Center for Responsible Decentralized Intelligence](https://rdi.berkeley.edu/). The simulated world requires me to complete a series of tasks, each one unlocking a door. My goal is to move from virtual room to virtual room, unlocking doors by solving puzzles that involve creative thinking, memory skills and physical movements, all naturally integrated into the experience.

Louis Rosenberg inside a Virtual Escape Room created by researchers at U.C. Berkeley (2022)
I am proud to say I made it out of the virtual labyrinth and back to reality. Of course, this was created by a research lab, so you might expect the experience was more than it seems. And you’d be right — it was designed to demonstrate the significant privacy concerns in the metaverse. It turns out that while I was solving the puzzles, moving from room to room, the researchers were using my actions and reactions to determine a wide range of information about me. I’m talking about deeply personal data that any third party could have ascertained from my participation in a simple virtual application.

No compatible source was found for this media.

Some content could not be imported from the original document. [View content ↗](https://imasdk.googleapis.com/js/core/bridge3.556.1_en.html#goog_810613453) 

As I have been involved in virtual and augmented reality for decades and have been warning about the hidden dangers for many years, you’d think the data collected would not have surprised me. But you’d be wrong. It’s one thing to [warn about the risks](https://bigthink.com/the-future/metaverse-dystopia/) in the abstract; it’s something else to experience the [privacy issues](https://xrsi.org/publication/the-xrsi-privacy-framework) firsthand. It was quite shocking, actually.

That said, let’s get into the personal data they were able to glean from my short experience in the escape room. First, they were able to triangulate my location. As described in [a recent paper](https://arxiv.org/abs/2207.13176) about this research, metaverse applications generally ping multiple servers, which here enabled the researchers to quickly predict my location using a process called *multilateration*. Even if I had been using a VPN to hide my IP address, this technique would still have found where I was. This isn’t shocking, as most people expect their location is known when they connect online, but it is a privacy concern nonetheless.

advertisement

Join the GamesBeat community in Los Angeles this May 22-23. You’ll hear from the brightest minds within the gaming industry to share their updates on the latest developments.

 [Register Here](https://avolio.swapcard.com/gamesbeatsummit2023/index/registrations/Start?utm_source=vb&utm_medium=incontent&utm_content=registration&utm_campaign=GBS23_InContent) 

Going deeper, the researchers were able to use my interactions in the escape room to predict my height, the length of my arms (wingspan), my handedness, my age, my gender, and basic parameters about my physical fitness level, including how low I could crouch down and how quickly I could react to stimuli. They were also able to determine my visual acuity, whether I was colorblind, and the size of the room that I was interacting with, and to make basic assessments of my cognitive acuity. The researchers could have even predicted whether I had certain disabilities.

advertisement

It’s important to point out that the researchers used standard hardware and software to implement this series of tests, emulating the capabilities that a typical application developer could employ when building a virtual experience in the metaverse. It’s also important to point out that consumers currently have no way to defend against this — there is no “incognito mode” in the metaverse that conceals this information and protects the user against this type of evaluation.

Well, there wasn’t any protection until the researchers began building one — a software tool they call “MetaGuard” that can be installed on standard VR systems. As described in [a recent paper](https://arxiv.org/abs/2208.05604) by lead researchers Vivek Nair and Gonzalo Garrido of U.C. Berkeley, the tool can mask many of the parameters that were used to profile my physical characteristics in the metaverse. It works by cleverly injecting randomized offsets into the data stream, hiding physical parameters such as my height, wingspan and physical mobility, which otherwise could be used to predict age, gender and health characteristics.

MetaGuard Image from Nair and Garrido
advertisement

The free software tool also enables users to mask their handedness, the frequency range of their voice, and their physical fitness level and conceal their geospatial location by disrupting triangulation techniques. Of course, MetaGuard is just a first step in helping users protect their privacy in immersive worlds, but it’s an important demonstration, showing that consumer-level defenses could easily be deployed.

At the same time, policymakers should consider protecting basic [immersive rights](https://venturebeat.com/virtual/metaverse-we-need-guaranteed-basic-immersive-rights/) for users around the globe, guarding against invasive tracking and profiling. For example, Meta [recently announced](https://uploadvr.com/zuckerberg-eye-face-tracking-quest-3/) that its next VR headset will include face and eye tracking. While these new capabilities are likely to unlock very useful features in the metaverse, for example enabling avatars to express more realistic facial expressions, the same data could also be used to track and [profile user emotions](https://www.researchgate.net/publication/362802004_Marketing_in_the_Metaverse_A_Fundamental_Shift). This could enable platforms to build predictive models that anticipate how individual users will react to a wide range of circumstances, even enabling [adaptive advertisements](https://venturebeat.com/ai/deception-vs-authenticity-why-the-metaverse-will-change-marketing-forever/) that are optimized for persuasion.

advertisement

Personally, I believe the metaverse has the potential to be a deeply humanizing technology that presents digital content in the form most natural to our perceptual system — as immersive experiences. At the same time, the extensive data collected in virtual and augmented worlds is a significant concern and likely requires a range of solutions, from protective software tools like MetaGuard to thoughtful [metaverse regulation](https://link.springer.com/chapter/10.1007/978-3-031-15546-8_23). For those interested in pushing for a safe metaverse, I point you towards an international community effort called [Metaverse Safety Week](https://metaversesafetyweek.org/) that is happening in December.

##### DataDecisionMakers

Welcome to the VentureBeat community!

DataDecisionMakers is where experts, including the technical people doing data work, can share data-related insights and innovation.

If you want to read about cutting-edge ideas and up-to-date information, best practices, and the future of data and data tech, join us at DataDecisionMakers.

You might even consider [contributing an article](https://venturebeat.com/contribute-to-datadecisionmakers/) of your own!
