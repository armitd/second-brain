# Meet the startup that helped Microsoft build the world of Flight Simulator

![rw-book-cover](https://techcrunch.com/wp-content/uploads/2020/08/Annotation-2020-08-14-180005.jpg)

## Metadata
- Author: [[Frederic Lardinois]]
- Full Title: Meet the startup that helped Microsoft build the world of Flight Simulator
- Category: #articles
- Summary: Microsoft's new Flight Simulator uses advanced technology to create a realistic world, thanks in part to the Austrian startup Blackshark.ai. This company, made up of about 50 people, utilized AI to reconstruct 1.5 billion buildings globally from 2D satellite images. Blackshark.ai aims to create a near-real-time digital twin of our planet, expanding its technology beyond gaming into areas like autonomous driving and geographical analysis.
- URL: https://techcrunch.com/2020/08/17/meet-the-startup-that-helped-microsoft-build-the-world-of-flight-simulator/

## Full Document
![](https://techcrunch.com/wp-content/uploads/2020/08/Annotation-2020-08-14-180005.jpg)Image Credits:TechCrunch
Microsoft’s new Flight Simulator is a [technological marvel](https://techcrunch.com/2020/07/30/microsofts-new-flight-simulator-is-a-beautiful-work-in-progress/) that sets a new standard for the genre. But to recreate a world that feels real and alive and contains billions of buildings all in the right spots, Microsoft and Asobo Studios relied on the work of multiple partners.

One of those is the small Austrian startup [Blackshark.ai](https://blackshark.ai/) from Graz that, with a team of only about 50 people, recreated every city and town around the world with the help of AI and massive computing resources in the cloud.

Ahead of the launch of the new Flight Simulator, we sat down with Blackshark co-founder and CEO Michael Putz to talk about working with Microsoft and the company’s broader vision.

[![](https://techcrunch.com/wp-content/uploads/2020/08/ezgif-4-6790f152bc53.gif)](https://techcrunch.com/wp-content/uploads/2020/08/ezgif-4-6790f152bc53.gif)Image Credits: Microsoft
Blackshark is actually a spin-off of game studio [Bongfish](https://www.bongfish.com/our-games/), the maker of World of Tanks: Frontline, Motocross Madness and the Stoked snowboarding game series. As Putz told me, it was actually Stoked that set the company on the way to what would become Blackshark.

“One of the first games we did in 2007 was a snowboarding game called Stoked and S Stoked Bigger Edition, which was one of the first games having a full 360-degree mountain where you could use a helicopter to fly around and drop out, land everywhere and go down,” he explained. “The mountain itself was procedurally constructed and described — and also the placement of obstacles of vegetation, of other snowboarders and small animals had been done procedurally. Then we went more into the racing, shooting, driving genre, but we still had this idea of positional placement and descriptions in the back of our minds.”

Bongfish returned to this idea when it worked on World of Tanks, simply because of how time-consuming it is to build such a huge map where every rock is placed by hand.

Based on this experience, Bongfish started building an in-house AI team. That team used a number of machine-learning techniques to build a system that could learn from how designers build maps and then, at some point, build its own AI-created maps. The team actually ended up using this for some of its projects before Microsoft came into the picture.

“By random chance, I met someone from Microsoft who was looking for a studio to help them out on the new Flight Simulator. The core idea of the new Flight Simulator simulator was to use Bing Maps as a playing field, as a map, as a background,” Putz explained.

But Bing Maps’ photogrammetry data only yielded exact 1:1 replicas of 400 cities — for the vast majority of the planet, though, that data doesn’t exist. Microsoft and Asobo Studios needed a system for building the rest.

This is where Blackshark comes in. For Flight Simulator, the studio reconstructed 1.5 billion buildings from 2D satellite images.

Now, while Putz says he met the Microsoft team by chance, there’s a bit more to this. Back in the day, there was a Bing Maps team in Graz, which developed the first cameras and 3D versions of Bing Maps. And while Google Maps won the market, Bing Maps actually beat Google with its 3D maps. Microsoft then launched a research center in Graz and when that closed, Amazon and others came in to snap up the local talent.

“So it was easy for us to fill positions like a PhD in rooftop reconstruction,” Putz said. “I didn’t even know this existed, but this was exactly what we needed — and we found two of them.

“It’s easy to see why reconstructing a 3D building from a 2D map would be hard. Even figuring out a building’s exact outline isn’t easy.

[![](https://techcrunch.com/wp-content/uploads/2020/08/Annotation-2020-08-17-091038.jpg)](https://techcrunch.com/wp-content/uploads/2020/08/Annotation-2020-08-17-091038.jpg)Image Credits: Blackshark.ai
“What we do basically in Flight Simulator is we look at areas, 2D areas and then finding out footprints of buildings, which is actually a computer vision task,” said Putz. “But if a building is obstructed by a shadow of a tree, we actually need machine learning because then it’s not clear anymore what is part of the building and what is not because of the overlap of the shadow — but then machine learning completes the remaining part of the building. That’s a super simple example.”

While Blackshark was able to rely on some other data, too, including photos, sensor data and existing map data, it has to make a determination about the height of the building and some of its characteristics based on very little information.

The obvious next problem is figuring out the height of a building. If there is existing GIS data, then that problem is easy to solve, but for most areas of the world, that data simply doesn’t exist or isn’t readily available. For those areas, the team takes the 2D image and looks for hints in the image, like shadows. To determine the height of a building based on a shadow, you need the time of day, though, and the Bing Maps images aren’t actually timestamped. For other use cases the company is working on, Blackshark has that and that makes things a lot easier. And that’s where machine learning comes in again.

[![](https://techcrunch.com/wp-content/uploads/2020/08/Annotation-2020-08-15-092533-1.jpg)](https://techcrunch.com/wp-content/uploads/2020/08/Annotation-2020-08-15-092533-1.jpg)Image Credits: Blackshark.ai
“Machine learning takes a slightly different road,” noted Putz. “It also looks at the shadow, we think — because it’s a black box, we don’t really know what it’s doing. But also, if you look at a flat rooftop, like a skyscraper versus a shopping mall. Both have mostly flat rooftops, but the rooftop furniture is different on a skyscraper than on a shopping mall. This helps the AI to learn when you label it the right way.”

And then, if the system knows that the average height of a shopping mall in a given area is usually three floors, it can work with that.

One thing Blackshark is very open about is that its system will make mistakes — and if you buy Flight Simulator, you will see that there are obvious mistakes in how some of the buildings are placed. Indeed, Putz told me that he believes one of the hardest challenges in the project was to convince the company’s development partners and Microsoft to let them use this approach.

“You’re talking 1.5 billion buildings. At these numbers, you cannot do traditional Q&A anymore. And the traditional finger-pointing in like a level of Halo or something where you say ‘this pixel is not good, fix it,’ does not really work if you develop on a statistical basis like you do with AI. So it might be that 20% of the buildings are off — and it actually is the case I guess in the Flight Simulator — but there’s no other way to tackle this challenge because outsourcing to hand-model 1.5 billion buildings is, just from a logistical level and also budget level, not doable.”

Over time, that system will also improve, and because Microsoft streams a lot of the data to the game from Azure, users will surely see changes over time.

[![](https://techcrunch.com/wp-content/uploads/2020/08/Annotation-2020-08-17-090907.jpg)](https://techcrunch.com/wp-content/uploads/2020/08/Annotation-2020-08-17-090907.jpg)Image Credits: Blackshark.ai
Labeling, though, is still something the team has to do simply to train the model, and that’s actually an area where Blackshark has made a lot of progress, though Putz wouldn’t say too much about it because it’s part of the company’s secret sauce and one of the main reasons why it can do all of this with just about 50 people.

“Data labels had not been a priority for our partners,” he said. “And so we used our own live labeling to basically label the entire planet by two or three guys […] It puts a very powerful tool and user interface in the hands of the data analysts. And basically, if the data analyst wants to detect a ship, he tells the learning algorithm what the ship is and then he gets immediate output of detected ships in a sample image.”

From there, the analyst can then train the algorithm to get even better at detecting a specific object like a ship, in this example, or a mall in Flight Simulator. Other geospatial analysis companies tend to focus on specific niches, Putz also noted, while the company’s tools are agnostic to the type of content being analyzed.

[![](https://techcrunch.com/wp-content/uploads/2020/08/Annotation-2020-08-15-092616-2.jpg)](https://techcrunch.com/wp-content/uploads/2020/08/Annotation-2020-08-15-092616-2.jpg)Image Credits: Blackshark.ai
And that’s where Blackshark’s bigger vision comes in. Because while the company is now getting acclaim for its work with Microsoft, Blackshark also works with other companies around reconstructing city scenes for autonomous driving simulations, for example.

“Our bigger vision is a near-real-time digital twin of our planet, particularly the planet’s surface, which opens up a trillion use cases where traditional photogrammetry like a Google Earth or what Apple Maps is doing is not helping because those are just simplified for photos clued on simple geometrical structures. For this we have our cycle where we have been extracting intelligence from aerial data, which might be 2D images, but it also could be 3Dpoint counts, which are already doing another project. And then we are visualizing the semantics.”

Those semantics, which describe the building in very precise detail, have one major advantage over photogrammetry: Shadow and light information is essentially baked into the images, making it hard to relight a scene realistically. Since Blackshark knows everything about that building it is constructing, it can then also place windows and lights in those buildings, which creates the surprisingly realistic night scenes in Flight Simulator.

Point clouds, which aren’t being used in Flight Simulator, are another area Blackshark is focusing on right now. Point clouds are very hard to read for humans, especially once you get very close. Blackshark uses its AI systems to analyze point clouds to find out how many stories a building has.

“The whole company was founded on the idea that we need to have a huge advantage in technology in order to get there, and especially coming from video games, where huge productions like in Assassin’s Creed or GTA are now hitting capacity limits by having thousands of people working on it, which is very hard to scale, very hard to manage over continents and into a timely delivered product. For us, it was clear that there need to be more automated or semi-automated steps in order to do that.”

And though Blackshark found its start in the gaming field — and while it is working on this with Microsoft and Asobo Studios — it’s actually not focused on gaming but instead on things like autonomous driving and geographical analysis. Putz noted that another good example for this is Unreal Engine, which started as a game engine and is now everywhere.

“For me, having been in the games industry for a long time, it’s so encouraging to see, because when you develop games, you know how groundbreaking the technology is compared to other industries,” said Putz. “And when you look at simulators, from military simulators or industrial simulators, they always kind of look like shit compared to what we have in driving games. And the time has come that the game technologies are spreading out of the game stack and helping all those other industries. I think Blackshark is one of those examples for making this possible.”

> [Microsoft’s new Flight Simulator is a beautiful work in progress](https://techcrunch.com/2020/07/30/microsofts-new-flight-simulator-is-a-beautiful-work-in-progress/)
> 
>
