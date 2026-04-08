# TechScape: Why CrowdStrike-style chaos is here to stay

![rw-book-cover](https://i.guim.co.uk/img/media/3bff6b5d70168eaa7e9160f115e7493079d50a39/0_0_4000_2400/master/4000.jpg?width=1200&height=630&quality=85&auto=format&fit=crop&overlay-align=bottom%2Cleft&overlay-width=100p&overlay-base64=L2ltZy9zdGF0aWMvb3ZlcmxheXMvdGctZGVmYXVsdC5wbmc&enable=upscale&s=678513c5a5f6fefb18f9537661f11da1)

## Metadata
- Author: [[Alex Hern]]
- Full Title: TechScape: Why CrowdStrike-style chaos is here to stay
- Category: #articles
- Summary: CrowdStrike experienced a significant outage that caused widespread disruptions, revealing flaws in their update process. The company pushed an update that unexpectedly crashed systems instead of enhancing security. This incident highlights that similar cybersecurity failures are likely to occur again in the future.
- URL: https://www.theguardian.com/global/article/2024/jul/23/why-crowdstrike-style-chaos-is-here-to-stay

## Full Document
![Large queues of people at Ninoy Aquino international airport in Manila, Philippines](https://i.guim.co.uk/img/media/3bff6b5d70168eaa7e9160f115e7493079d50a39/0_0_4000_2400/master/4000.jpg?width=465&dpr=1&s=none)Passengers endured long waits at Ninoy Aquino international airport in Manila, Philippines, amid the CrowdStrike outage. Photograph: Ezra Acayan/Getty Images 
Countless theories for the cybersecurity firm’s outage are flying around, but whatever the reason, this sort of thing is likely to happen again

 **[Don’t get TechScape delivered to your inbox? Sign up for the full article here](https://ablink.editorial.theguardian.com/ss/c/TBl-lE0k4WbTlFRn6v-lQXxTpTslqnvUsR2ofAkC00vqkHXqakTSxrykj9mrdACFo11SPMvm9ONAti2JcHBqUgcduObToxycReEYHcTAh6nov_u_7l464yKkl5CZpPeg-CqG3ueb-8UiDZ4dOkhK_xu6BZysaGtGOA-w2_0KTqLsMBLqZrcGelEg-7T5C6DRfMSsX1Wcyrv2RlHjbzIGx0ePxMD7meIXmznkqCFxtrflV_YvxDV9cqXgzdq7c2-9qYTW0MyIMCG7p9sc7wIKCg/3ha/N7031ZxvS8Cv2AmB8PHP-g/h27/towm4HqYM1UtQe3kzAkaoAWT_zh9HyZuTvPyJCk6JeE)**

“Where did CrowdStrike go wrong” is, if anything, a slightly overdetermined question.

We can work backwards. Pushing an update to every single computer on your network at the same time means that by the time you discover a problem, it’s too late to limit the fallout. The alternative – a staged rollout – would see the update pushed to users in small groups, usually accelerating over time. If you begin by updating 50 systems at once, and then immediately lose all contact with every single one of them, hopefully you spot it before you update the next 50 million.

If you aren’t going to do a staged rollout, then before you push the update to users, you should test it. Normally, the extent of prerelease testing is a contested realm: there are uncountable possible configurations of hardware, software and user requirements, and any testing regime has to narrow down the ones that matter – and hope nothing falls through the cracks. Thankfully, when an update crashes 100% of the computers it is installed on and renders them inoperable until an onerous fix is manually applied, one can fairly easily conclude it was undertested.

If you aren’t going to do a staged rollout and you aren’t going to test your update before it ships, then you need to make sure it is *not broken*.

**It was broken**

![An image of a flight status board in Orlando, Florida. ](https://i.guim.co.uk/img/media/40f92cd3d018ee0cd19a8f1ec37669da50d4dcbf/0_100_3000_1800/master/3000.jpg?width=445&dpr=1&s=none)Flights at Orlando airport, Florida, were among many cancelled or delayed amid the CrowdStrike crisis. Photograph: Miguel J Rodríguez Carrillo/Getty Images 
In CrowdStrike’s defence, you can see why some of this happened the way it did. The company offers a service called “endpoint protection”, but if you’ve been around the Windows ecosystem for a few years, it might be easiest to think of it as an antivirus. It’s geared towards the corporate market, rather than consumers, and as well as guarding against common malware it attempts to prevent individual computers used by businesses from becoming footholds into the corporate network.

That not only covers PCs used by large companies that need to be able to offer a keyboard and mouse to every one of their employees, but also anyone else with massive fleets of cheap and flexible machines. If you left home on Friday, you’ll have seen what that means: advertising displays, point of sale machines and self-service kiosks were all hit.

The comparison matters because in the space CrowdStrike plays in, speed is of the essence. The worst-case scenario – at least, until last week – is a ransom worm like WannaCry or NotPetya: a piece of malware that not only wreaks critical damage on affected machines but can spread within and across corporate networks automatically. And so the frontline of the defence is operated at pace. Rather than waiting for a weekly, or even monthly, release schedule for the software update, the company pushes files daily to cover the latest threats to the systems it protects.

At the margins, even a staged rollout could cause real harm: WannaCry bricked computers across much of the NHS in the hours it was allowed to spread unchecked, before British security researcher Marcus Hutchins [accidentally stopped it in its tracks](https://www.theguardian.com/technology/2017/may/13/accidental-hero-finds-kill-switch-to-stop-spread-of-ransomware-cyber-attack) while trying to work out what made it tick. In that scenario, a staged rollout could cost lives. A delay for testing could cost more.

So, instead, the updates aren’t supposed to be able to cause this sort of problem. Rather than being new code run on each machine, they are instead more like updates to the dictionary – telling the CrowdStrike software already installed what new threats to look out for, and how to recognise them.

At the loosest end, you can think of it like, well, this article. You’re almost certainly reading these words through an application of some sort, be that a web browser, mail client, or the Guardian’s app. (If you have secured an arrangement whereby someone prints this off and delivers it with your morning coffee, congratulations.) I haven’t performed a staged rollout, or run a full test of the article, because it shouldn’t do anything.

Unfortunately, the update pushed on Friday did do something. The high-level technical details remain fuzzy, and until CrowdStrike deigns to publish a full breakdown of what it did, we’re stuck with what they’ve told us. The update, which was meant to teach the system how to spot a particular type of cyber-attack that had already been observed in the wild, instead “triggered a logic error that resulted in an operating system crash”.

I’ve been covering this sort of thing for more than a decade now and my guess is the “logic error” will turn out to be one of two things. Either something in one of the most complex systems that humanity has built in its history will have a barely comprehensible fail state and an almost inconceivable combination of bad luck will have led to something catastrophic happening; or someone did something tremendously dumb.

**Sometimes there are no lessons**

![A South Western Railway ticket machine with a notice on it. ](https://i.guim.co.uk/img/media/b895198aa31bebce0a24d67264a477fd6b39d12e/0_541_5712_3427/master/5712.jpg?width=445&dpr=1&s=none)Consumer-facing self-service kiosks, such at those operated by South Western Railway in the UK, were also hit. Photograph: Anadolu/Getty Images 
Over the last few days, there have been lots of takes:

Sign up to TechScape

Alex Hern's weekly dive in to how technology is shaping our lives

after newsletter promotion

None of them have hit home. CrowdStrike, for all the disruption, doesn’t have a huge concentration of power; it’s one of the larger companies in its sector, but it’s installed on only about 1% of all PCs. And while Microsoft has tried to [push the line that it’s only because of regulation that the failures happened](https://www.theregister.com/2024/07/22/windows_crowdstrike_kernel_eu/), the alternative – where third-party security companies can’t operate on Windows – feels mostly a world where the first big failure really does affect 100% of PCs because Microsoft has set itself up as the only line of defence.

Cybersecurity regulations really do reward companies for installing CrowdStrike, turning a complex certification process into a simple box-tick, but that’s probably good as well. “Buy the thing to make you safe” is the only reasonable demand for the vast majority of companies, and CrowdStrike did the job, except for that one unfortunate time.

But unfortunate or not, it was absolutely a security issue. There are three goals in the golden triangle of information security: confidentiality (are secrets secret), integrity (is data correct), and availability (can you use your systems). CrowdStrike failed to preserve availability, and that meant it failed to guard the information security of its customers.

In the end, the only lesson I’m comfortable with taking away is that this sort of thing is going to happen more. We’ve successfully tackled so many fail states in society that those that still hit us are increasingly going to be surprising, serious and unprepared for. Similar to how drivers get overly confident with cruise control and find themselves unable to take over in the split second before an accident, we’ve succeeded in making catastrophic IT outages rare enough that recovering from them is a marathon task.

Hooray?

#### **The wider TechScape**

![Illustration commissioned for Josh Taylor’s feature on social media algorithms](https://i.guim.co.uk/img/media/730ac82d6fdd99b0160f3046e3e578c39bb72268/2_0_5903_3543/master/5903.jpg?width=445&dpr=1&s=none)Social media automatically delivers troubling content to young men, largely without oversight. Illustration: Nash Weerasekera/The Guardian
