# The March of Nines

![rw-book-cover](https://substackcdn.com/image/fetch/$s_!cYti!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F122c5064-f17e-40b6-b48d-e8e069b457ec_1024x574.jpeg)

## Metadata
- Author: [[Kevin Kelly]]
- Full Title: The March of Nines
- Category: #articles
- Summary: The "march of nines" means improving quality by adding more 9s to percentages, but each step is much harder and costlier than the last. Self-driving cars need many more nines of safety to be fully autonomous and safer than humans, which will take billions of dollars and many years. True autonomy without humans in the loop may not happen until 2036 or later due to the huge effort required.
- URL: https://kevinkelly.substack.com/p/the-march-of-nines

## Full Document
[![](https://substackcdn.com/image/fetch/$s_!cYti!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F122c5064-f17e-40b6-b48d-e8e069b457ec_1024x574.jpeg)](https://substackcdn.com/image/fetch/$s_!cYti!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F122c5064-f17e-40b6-b48d-e8e069b457ec_1024x574.jpeg)
In the modern world we measure things a lot. Even betterment is given a number so we can measure quality and progress. For instance we can designate our water tank as 90% full after a rain, or a powder 99% pure. We grade tests, performances, purity, occupancies and all kinds of qualities as a percentage of what we think is perfect. As things improve their metric will go from say 90% to 99% (pretty good out of 100% perfection). To get better we could increase the purity of a material, or the availability of electricity, from 99% to 99.9% which is even better. If we keep adding nines, we keep significantly improving as we reach, say 99.999%. With advanced knowledge and the best practices, we could keep going forward further, adding up to 6 nines or even 9 nines!

This is called the ”march of nines”, and it has been very common in high tech for many years. The companies making silicon wafers for chips, for example, have been engaged in a long struggle to add nines to the purity of their crystals. Premier web hosting companies brag about their 5 nines of uptime, hoping to reach 6 nines someday.

This lift is tremendously hard for very mundane reasons. The addition of a nine in the march of nine is not linear. It seems as if we are adding only a tiny amount with each nine, smaller and smaller, but it is the opposite. The difference between having no electricity for 1 hour a year (99.99%) versus missing one whole working day a year (99.9%) is significant, and not just a little more.

But each additional nine requires an extraordinary increase in effort. Workplace folklore suggests that each additional nine requires just as much work as the one previous. So that going from 99% to 99.9 percent requires as much time/money as going from 90 to 99%. Some technologists claim that for some cases it is even more severe and that you need an order of magnitude more effort to achieve an additional nine. To go from two nines to three, or three to four requires 10 times the time and money than the last step. This would imply that each step in the march of nines needs more resources than all the previous steps together, which is a very sobering thought.

Whether each step in the march of nines is just as much or 10 times as much previous, the reason for this expanding input is that you cannot reach the next nine simply by doing more of what you have been doing. Extrapolation doesn’t work. The only way to reach the next nine is to do something in a new way, or to re-organize what you are doing, or to invent a new thing. And that is expensive. And easy to resist because what you are currently doing is working great! If you want to move your uptime from 99.9% to 99.99% you need whole new levels of redundancy, new work flows, new degrees of monitoring, new kinds of devices, new work habits, and a new company organization. The next nine will require the same degree of effort.

Recently Andrej Karpathy, the AI superstar who worked on self-driving cars, noted that we are still stuck at a level of nines way below what we really need for self-driving cars to become mainstream. When a SDV (self-driving vehicle) is 90% accurate in its driving, it will have a human emergency minder sitting in the car, a 1:1 ratio. After tons of new research, billions of dollars, and radical innovation the accuracy reaches 99% and that co-pilot minder will move to a remote service center, as they do in Waymos. The minders are no longer in the car but they still operate a 1:1 human per car at a distance. Spend some more billions and the innovations get the SDV to 99.9%, and now one minder can mind 6 cars. As SDV marches up the nines, human minds spread and dilute their attention, till eventually only a few humans are needed for tens of thousands of cars. Only then would the average citizen be able to afford a SDV.

But each of these steps of nine require at least as much work and ingenuity as the previous work. Today human drivers are actually very good. They create a collision causing an injury only about once every 1 million miles, and they cause a fatality only about once per 100 million miles driven. In terms of injuries human drivers operate at 99.9999% safety, and for fatal collisions their performance is 99.999999% if measured per mile. That is an astounding 8 nines!

But the far side of the march of nines is a weird domain. When you reach beyond 5 nines, the chance factor of rare events balloons to such extremes that such events become so improbable as to literally defy description. You are designing for things that have never happened or been seen. The event might only happen once in a 100 billion times, or once every hundred billion samples, that it is way outside human experience. The design process starts to veer to the meaningless.

This zone of extremity at the far tail of the march of nines is yet another reason why trying to lift a system up to another step is so hard. You enter a territory governed by rare and black swan occurrences, where uncertainty is rampant, and ignorance reigns.

Yet Waymo today is actually 90% safer than humans, but that safety still hinges on some humans in the loop. It is probable that today’s tech without those humans would be less safe than human drivers, but we don’t know. And in fact, despite billions of miles driven in some form of self-driving mode with human assistance, those SDV still have not driven enough miles to give us reliable safety measurements compared to human drivers.

The feeling among some observers of SDV is that taking humans out of the loop (exposing its true level of safety if truly autonomous), means that despite appearances, SDV is [not a solved problem](https://forum.effectivealtruism.org/posts/9zLByNJkAvqdShNwq/self-driving-cars-aren-t-nearly-a-solved-problem). Tesla’s FSD is not genuine autonomy. As long as the driver can grab the wheel to steer, a human is in the loop. In other words SDV is several nines away. Which means that it will require just as much time and money and effort to solve this next step as it has taken to get SDV to where they are today. That is worth repeating: to reach full autonomy may take as much effort as has been spent getting to Waymo today.

Waymo was founded as a Google Self Driving Car Project 16 years ago and was recognized as Waymo 10 years ago, and has so far spent about $25 billion getting to their current level of nines. I believe it will take at least another decade and another $25 billion for Waymo to step up to the point where one human can facilitate 100,000 cars, while the SDV achieves all the nines they need to be genuinely autonomous and still safer than humans.

It seems we are so close to fully human-free autonomous driving – all we need is a few more nines! – but in the march of nines, those additional nines will require as much investment as we’ve spent so far. To a rough order of magnitude, I don’t expect we will reach the state where even a third of the vehicles on the road will be truly SDV (no humans in the loop) until 2036, or later.

###### Subscribe to KK

By Kevin Kelly · Hundreds of paid subscribers

Kevin Kelly's works in progress

By subscribing, you agree Substack's [Terms of Use](https://substack.com/tos), and acknowledge its [Information Collection Notice](https://substack.com/ccpa#personal-data-collected) and [Privacy Policy](https://substack.com/privacy).

##### Ready for more?

Subscribe
