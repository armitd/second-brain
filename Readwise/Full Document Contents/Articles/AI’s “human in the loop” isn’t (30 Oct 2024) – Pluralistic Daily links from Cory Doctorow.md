# AI’s “human in the loop” isn’t (30 Oct 2024) – Pluralistic : Daily links from Cory Doctorow

![rw-book-cover](https://i0.wp.com/pluralistic.net/wp-content/uploads/2020/02/cropped-guillotine-French-Revolution.jpg?fit=192%2C192&ssl=1)

## Metadata
- Author: [[Cory Doctorow]]
- Full Title: AI’s “human in the loop” isn’t (30 Oct 2024) – Pluralistic : Daily links from Cory Doctorow
- Category: #articles
- Summary: AI systems can make fast decisions but can also be very wrong, leading to harmful outcomes. The idea of having "humans in the loop" to oversee AI may create a false sense of security, as humans often struggle to effectively supervise algorithms. This reliance on human oversight can shift responsibility for errors away from the AI creators, resulting in a lack of accountability.
- URL: https://pluralistic.net/2024/10/30/a-neck-in-a-noose/

## Full Document
[![](https://i0.wp.com/craphound.com/images/30Oct2024.jpg?w=840&ssl=1)](https://pluralistic.net/2024/10/30/a-neck-in-a-noose/)
### Today's links

* [AI's "human in the loop" isn't](https://pluralistic.net/2024/10/30/a-neck-in-a-noose/#is-also-a-human-in-the-loop): A moral crumple zone, an accountability sink, but not a supervisor.
* [Hey look at this](https://pluralistic.net/2024/10/30/a-neck-in-a-noose/#linkdump): Delights to delectate.
* [This day in history](https://pluralistic.net/2024/10/30/a-neck-in-a-noose/#retro): 2004, 2009, 2014, 2019, 2023
* [Upcoming appearances](https://pluralistic.net/2024/10/30/a-neck-in-a-noose/#upcoming): Where to find me.
* [Recent appearances](https://pluralistic.net/2024/10/30/a-neck-in-a-noose/#recent): Where I've been.
* [Latest books](https://pluralistic.net/2024/10/30/a-neck-in-a-noose/#latest): You keep readin' em, I'll keep writin' 'em.
* [Upcoming books](https://pluralistic.net/2024/10/30/a-neck-in-a-noose/#upcoming-books): Like I said, I'll keep writin' 'em.
* [Colophon](https://pluralistic.net/2024/10/30/a-neck-in-a-noose/#bragsheet): All the rest.

![A cowboy astride a racing horse, lassoing a man who is bound and gagged, his face a mask of panic. The cowboy's head has been replaced with the staring red eye of HAL 9000 from Stanley Kubrick's '2001: A Space Odyssey.' The horse is racing along a glowing platonic gridded plane as seen in the Tron movies. The background is a 'code waterfall' effect as seen in the credit sequences of the Wachowksis' 'Matrix' movies.](https://i0.wp.com/craphound.com/images/human-in-the-loop.jpg?w=840&ssl=1)A cowboy astride a racing horse, lassoing a man who is bound and gagged, his face a mask of panic. The cowboy's head has been replaced with the staring red eye of HAL 9000 from Stanley Kubrick's '2001: A Space Odyssey.' The horse is racing along a glowing platonic gridded plane as seen in the Tron movies. The background is a 'code waterfall' effect as seen in the credit sequences of the Wachowksis' 'Matrix' movies.
### AI's "human in the loop" isn't ([permalink](https://pluralistic.net/2024/10/30/a-neck-in-a-noose/#is-also-a-human-in-the-loop))

AI's ability to make – or assist with – important decisions is fraught: on the one hand, AI can *often* classify things very well, at a speed and scale that outstrips the ability of any reasonably resourced group of humans. On the other hand, AI is sometimes *very* wrong, in ways that can be terribly harmful.

Bureaucracies and the AI pitchmen who hope to sell them algorithms are very excited about the cost-savings they could realize if algorithms could be turned loose on thorny, labor-intensive processes. Some of these are relatively low-stakes and make for an easy call: Brewster Kahle recently told me about the Internet Archive's project to scan a ton of journals on microfiche they bought as a library discard. It's pretty easy to have a high-res scanner auto-detect the positions of each page on the fiche and to run the text through OCR, but a human would still need to go through all those pages, marking the first and last page of each journal and identifying the table of contents and indexing it to the scanned pages. This is something AI apparently does *very* well, and instead of scrolling through endless pages, the Archive's human operator now just checks whether the first/last/index pages the AI identified are the right ones. A project that could have taken years is being tackled with never-seen swiftness.

The operator checking those fiche indices is something AI people like to call a "human in the loop" – a human operator who assesses each judgment made by the AI and overrides it should the AI have made a mistake. "Humans in the loop" present a tantalizing solution to algorithmic misfires, bias, and unexpected errors, and so "we'll put a human in the loop" is the cure-all response to any objection to putting an imperfect AI in charge of a high-stakes application.

But it's not just AIs that are imperfect. Humans are *wildly* imperfect, and one thing they turn out to be *very* bad at is supervising AIs. In a 2022 paper for *Computer Law & Security Review*, the mathematician and public policy expert Ben Green investigates the empirical limits on human oversight of algorithms:

<https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3921216>

Green situates public sector algorithms as the latest salvo in an age-old battle in public enforcement. Bureaucracies have two conflicting, irreconcilable imperatives: on the one hand, they want to be fair, and treat everyone the same. On the other hand, they want to exercise discretion, and take account of individual circumstances when administering justice. There's no way to do both of these things at the same time, obviously.

But algorithmic decision tools, overseen by humans, seem to hold out the possibility of doing the impossible and having both objective fairness *and* subjective discretion. Because it is grounded in computable mathematics, an algorithm is said to be "objective": given two equivalent reports of a parent who may be neglectful, the algorithm will make the same recommendation as to whether to take their children away. But because those recommendations are then reviewed by a human in the loop, there's a chance to take account of special circumstances that the algorithm missed. Finally, a cake that can be both had, *and* eaten!

For the paper, Green reviewed a long list of policies – local, national, and supra-national – for putting humans in the loop and found several common ways of mandating human oversight of AI.

First, policies specify that algorithms *must* have human oversight. Many jurisdictions set out long lists of decisions that *must* be reviewed by human beings, banning "fire and forget" systems that chug along in the background, blithely making consequential decisions without anyone ever reviewing them.

Second, policies specify that humans can exercise *discretion* when they override the AI. They aren't just there to catch instances in which the AI misinterprets a rule, but rather to apply human judgment to the rules' applications.

Next, policies require human oversight to be "meaningful" – to be more than a rubber stamp. For high-stakes decisions, a human has to do a thorough review of the AI's inputs and output before greenlighting it.

Finally, policies specify that humans *can* override the AI. This is key: we've all encountered instances in which "computer says no" and the hapless person operating the computer just shrugs their shoulders apologetically. Nothing I can do, sorry!

All of this *sounds* good, but unfortunately, it doesn't work. The question of how humans in the loop *actually* behave has been thoroughly studied, published in peer-reviewed, reputable journals, and replicated by other researchers. The measures for using humans to prevent algorithmic harms represent theories, and those theories are testable, and they have been tested, and they are wrong.

For example, people (including experts) are highly susceptible to "automation bias." They defer to automated systems, even when those systems produce outputs that conflict with their own expert experience and knowledge. A study of London cops found that they "overwhelmingly overestimated the credibility" of facial recognition and assessed its accuracy at 300% better than its actual performance.

Experts who are put in charge of overseeing an automated system get out of practice, because they no longer engage in the routine steps that lead up to the conclusion. Presented with conclusions, rather than problems to solve, experts lose the facility and familiarity with how all the factors that need to be weighed to produce a conclusion fit together. Far from being the easiest step of coming to a decision, reviewing the final step of that decision without doing the underlying work can be *much harder* to do reliably.

Worse: when algorithms are made "transparent" by presenting their chain of reasoning to expert reviewers, those reviewers become *more* deferential to the algorithm's conclusion, not less – after all, now the expert has to review not just one final conclusion, but several sub-conclusions.

Even worse: when humans *do* exercise discretion to override an algorithm, it's often to inject the very bias that the algorithm is there to prevent. Sure, the algorithm might give the same recommendation about two similar parents who are facing having their children taken away, but the judge who reviews the recommendations is more likely to override it for a white parent than for a Black one.

Humans in the loop experience "a diminished sense of control, responsibility, and moral agency." That means that they feel less able to override an algorithm – and they feel less morally culpable when they sit by and let the algorithm do its thing.

All of these effects are persistent even when people know about them, are trained to avoid them, and are given explicit instructions to do so. Remember, the whole reason to introduce AI is because of human imperfection. Designing an AI to correct human imperfection that only works when its human overseer is perfect produces predictably bad outcomes.

As Green writes, putting an AI in charge of a high-stakes decision, and using humans in the loop to prevent its harms, produces a "perverse effect": "alleviating scrutiny of government algorithms without actually addressing the underlying concerns." The human in the loop creates "a false sense of security" that sees algorithms deployed for high-stakes domains, and it shifts the responsibility for algorithmic failures to the human, creating what Dan Davies calls an "accountability sink":

<https://profilebooks.com/work/the-unaccountability-machine/>

The human in the loop is a false promise, a "salve that enables governments to obtain the benefits of algorithms without incurring the associated harms."

So why are we still talking about how AI is going to replace government and corporate bureaucracies, making decisions at machine speed, overseen by humans in the loop?

Well, what if the accountability sink is a feature and not a bug. What if governments, under enormous pressure to cut costs, figure out how to also cut corners, at the expense of people with very little social capital, and blame it all on human operators? The operators become, in the phrase of Madeleine Clare Elish, "moral crumple zones":

<https://estsjournal.org/index.php/ests/article/view/260>

As Green writes:

>  The emphasis on human oversight as a protective mechanism allows governments and vendors to have it both ways: they can promote an algorithm by proclaiming how its capabilities exceed those of humans, while simultaneously defending the algorithm and those responsible for it from scrutiny by pointing to the security (supposedly) provided by human oversight. 
> 
> 

(*Image: [Cryteria](https://commons.wikimedia.org/wiki/File:HAL9000.svg), [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/deed.en), modified*)

### Hey look at this ([permalink](https://pluralistic.net/2024/10/30/a-neck-in-a-noose/#linkdump))

![](https://i0.wp.com/craphound.com/images/heylookatthis.jpg?w=840&ssl=1)
* EU to Apple: “Let Users Choose Their Software”; Apple: “Nah” <https://www.eff.org/deeplinks/2024/10/eu-apple-let-users-choose-their-software-apple-nah>
* The cult of the founders <https://www.programmablemutter.com/p/the-cult-of-the-founders>
* Bruno Pontiroli’s Absurd Portraits Highlight Quirky Behavior and Zoological Buffoonery <https://www.thisiscolossal.com/2024/10/bruno-pontiroli-histoires-naturelles-et-grotesques/>

![A Wayback Machine banner.](https://i0.wp.com/craphound.com/images/wayback-machine-hed-796x416.png?resize=796%2C416&ssl=1)A Wayback Machine banner.
### This day in history ([permalink](https://pluralistic.net/2024/10/30/a-neck-in-a-noose/#retro))

#20yrsago William Gibson on ObL tape <https://web.archive.org/web/20041016033110/https://williamgibsonbooks.com/blog/2004_10_01_archive.asp#109907889910593617>

#20yrsago Apple to iPod owners: “Eat shit and die” <https://memex.craphound.com/2004/10/30/apple-to-ipod-owners-eat-shit-and-die-updated/>

#15yrsago Hallowe’en is safe, your kids are safe, the only scary thing is the warnings <https://www.huffpost.com/entry/as-goes-halloween-so-goes_b_340163>

#15yrsago Homebrew backyard railroad recreates Disneyland <https://web.archive.org/web/20091208070906/http://cptrr.webs.com/>

#15yrsago Gang steals phone wires out from under English roads <https://news.bbc.co.uk/2/hi/uk_news/england/sussex/8333774.stm>

#10yrsago Pizzeria asks judge to find rival’s flavor to be trademark-infringing <https://www.techdirt.com/2014/10/30/pizzeria-attempts-to-trademark-flavor-pizza-yes-seriously/>

#10yrsago 100K Hungarians march against Internet tax <https://www.vice.com/en/article/huge-internet-tax-protests-galvanize-government-opposition-in-hungary/>

#10yrsago Dissecting the arguments of liberal apologists for Obama’s surveillance and secret war <https://nationalinterest.org/feature/big-brother’s-liberal-friends-11515>

#10yrsago Potato-chip surveillance: once you start, you just can’t stop <https://www.theguardian.com/commentisfree/2014/oct/27/stasi-style-outrages-low-spies-stoop-mi5>

#5yrsago The Internet Archive’s massive repository of scanned books will help Wikipedia fight the disinformation wars <https://web.archive.org/web/20191031041755/https://blog.archive.org/2019/10/29/weaving-books-into-the-web-starting-with-wikipedia/>

#5yrsago With “OK boomer,” millennials are killing intergenerational resentment <https://www.nytimes.com/2019/10/29/style/ok-boomer.html>

#5yrsago Facebook sues notorious spyware company NSO Group for 1,400 attacks on diplomats, journalists, dissidents, and government officials <https://www.reuters.com/article/us-facebook-cyber-whatsapp-nsogroup/whatsapp-sues-israels-nso-for-allegedly-helping-spies-hack-phones-around-the-world-idUSKBN1X82BE/>

#5yrsago The First Scarfolk Annual: a mysterious artifact from a curiously familiar eternal grimdark 1970s <https://memex.craphound.com/2019/10/30/the-first-scarfolk-annual-a-mysterious-artifact-from-a-curiously-familiar-eternal-grimdark-1970s/>

#1yrago Zuck's gravity-defying metaverse money-pit <https://pluralistic.net/2023/10/30/markets-remaining-irrational/#steins-law>

### Upcoming appearances ([permalink](https://pluralistic.net/2024/10/30/a-neck-in-a-noose/#upcoming))

![A photo of me onstage, giving a speech, holding a mic.](https://i0.wp.com/craphound.com/images/appearances.jpg?w=840&ssl=1)A photo of me onstage, giving a speech, holding a mic.
* TusCon (Tucson), Nov 8-10  
 <https://tusconscificon.com/>
* International Cooperative Alliance (New Delhi), Nov 24  
 <https://icanewdelhi2024.coop/welcome/pages/Programme>
* IA et “merdification“ d’internet: peut-on envisager un nouveau web? (Remote), Dec 12  
 <https://www.unige.ch/comprendre-le-numerique/conferences-publiques1/cycle-5-2024-2025/ia-et-merdification-dinternet-peut-envisager-un-nouveau-web/>
* ISSA-LA Holiday Celebration keynote (Los Angeles), Dec 18  
 <https://issala.org/event/issa-la-december-18-dinner-meeting/>

![A screenshot of me at my desk, doing a livecast.](https://i0.wp.com/craphound.com/images/recentappearances.jpg?w=840&ssl=1)A screenshot of me at my desk, doing a livecast.
### Recent appearances ([permalink](https://pluralistic.net/2024/10/30/a-neck-in-a-noose/#recent))

* Maximum Iceland Scenario – Data Caps, 3rd Party Android Stores, Nuclear Amazon (This Week in Tech)  
 <https://www.youtube.com/watch?v=P5MkCwktKz0>
* Speciale intervista a Cory Doctorow (Digitalia)  
 <https://digitalia.fm/744/>
* Was There Ever An Old, Good Internet? (David Graeber Institute)  
 <https://www.youtube.com/watch?v=T6Jlxx5TboE>

![A grid of my books with Will Stahle covers..](https://i0.wp.com/craphound.com/images/recent.jpg?w=840&ssl=1)A grid of my books with Will Stahle covers..
### Latest books ([permalink](https://pluralistic.net/2024/10/30/a-neck-in-a-noose/#latest))

* The Bezzle: a sequel to "Red Team Blues," about prison-tech and other grifts, Tor Books (US), Head of Zeus (UK), February 2024 ([the-bezzle.org](http://the-bezzle.org)). Signed, personalized copies at Dark Delicacies (<https://www.darkdel.com/store/p3062/Available_Feb_20th%3A_The_Bezzle_HB.html#/>).
* "The Lost Cause:" a solarpunk novel of hope in the climate emergency, Tor Books (US), Head of Zeus (UK), November 2023 (<http://lost-cause.org>). Signed, personalized copies at Dark Delicacies (<https://www.darkdel.com/store/p3007/Pre-Order_Signed_Copies%3A_The_Lost_Cause_HB.html#/>)
* "The Internet Con": A nonfiction book about interoperability and Big Tech (Verso) September 2023 (<http://seizethemeansofcomputation.org>). Signed copies at Book Soup (<https://www.booksoup.com/book/9781804291245>).
* "Red Team Blues": "A grabby, compulsive thriller that will leave you knowing more about how the world works than you did before." Tor Books <http://redteamblues.com>. Signed copies at Dark Delicacies (US):  [and Forbidden Planet (UK):](https://www.darkdel.com/store/p2873/Wed%2C_Apr_26th_6pm%3A_Red_Team_Blues%3A_A_Martin_Hench_Novel_HB.html#/) <https://forbiddenplanet.com/385004-red-team-blues-signed-edition-hardcover/>.
* "Chokepoint Capitalism: How to Beat Big Tech, Tame Big Content, and Get Artists Paid, with Rebecca Giblin", on how to unrig the markets for creative labor, Beacon Press/Scribe 2022 <https://chokepointcapitalism.com>
* "Attack Surface": The third Little Brother novel, a standalone technothriller for adults. The *Washington Post* called it "a political cyberthriller, vigorous, bold and savvy about the limits of revolution and resistance." Order signed, personalized copies from Dark Delicacies <https://www.darkdel.com/store/p1840/Available_Now%3A_Attack_Surface.html>
* "How to Destroy Surveillance Capitalism": an anti-monopoly pamphlet analyzing the true harms of surveillance capitalism and proposing a solution. <https://onezero.medium.com/how-to-destroy-surveillance-capitalism-8135e6744d59?sk=f6cd10e54e20a07d4c6d0f3ac011af6b>) (signed copies: <https://www.darkdel.com/store/p2024/Available_Now%3A__How_to_Destroy_Surveillance_Capitalism.html>)
* "Little Brother/Homeland": A reissue omnibus edition with a new introduction by Edward Snowden: <https://us.macmillan.com/books/9781250774583>; personalized/signed copies here: <https://www.darkdel.com/store/p1750/July%3A__Little_Brother_%26_Homeland.html>
* "Poesy the Monster Slayer" a picture book about monsters, bedtime, gender, and kicking ass. Order here: <https://us.macmillan.com/books/9781626723627>. Get a personalized, signed copy here: <https://www.darkdel.com/store/p2682/Corey_Doctorow%3A_Poesy_the_Monster_Slayer_HB.html#/>.

![A cardboard book box with the Macmillan logo.](https://i0.wp.com/craphound.com/images/upcoming-books.jpg?w=840&ssl=1)A cardboard book box with the Macmillan logo.
### Upcoming books ([permalink](https://pluralistic.net/2024/10/30/a-neck-in-a-noose/#upcoming-books))

* Picks and Shovels: a sequel to "Red Team Blues," about the heroic era of the PC, Tor Books, February 2025
* Unauthorized Bread: a middle-grades graphic novel adapted from my novella about refugees, toasters and DRM, FirstSecond, 2025

![](https://i0.wp.com/craphound.com/images/colophonimages.jpeg?w=840&ssl=1)
### Colophon ([permalink](https://pluralistic.net/2024/10/30/a-neck-in-a-noose/#bragsheet))

Today's top sources: Ellen P Goodman (<https://twitter.com/ellgood>).

**Currently writing:** 

* Enshittification: a nonfiction book about platform decay for Farrar, Straus, Giroux. Today's progress: 756 words (73825 words total).
* A Little Brother short story about DIY insulin PLANNING
* Picks and Shovels, a Martin Hench noir thriller about the heroic era of the PC. FORTHCOMING TOR BOOKS FEB 2025

**Latest podcast:** Spill, part four (a Little Brother story) <https://craphound.com/littlebrother/2024/10/28/spill-part-four-a-little-brother-story/>

![](https://i0.wp.com/craphound.com/images/by.svg.png?w=840&ssl=1)
This work – excluding any serialized fiction – is licensed under a Creative Commons Attribution 4.0 license. That means you can use it any way you like, including commercially, provided that you attribute it to me, Cory Doctorow, and include a link to pluralistic.net.

<https://creativecommons.org/licenses/by/4.0/>

Quotations and images are not included in this license; they are included either under a limitation or exception to copyright, or on the basis of a separate license. Please exercise caution.

### How to get Pluralistic:

Blog (no ads, tracking, or data-collection):

[Pluralistic.net](http://pluralistic.net)

Newsletter (no ads, tracking, or data-collection):

<https://pluralistic.net/plura-list>

Mastodon (no ads, tracking, or data-collection):

<https://mamot.fr/@pluralistic>

Medium (no ads, paywalled):

<https://doctorow.medium.com/>

Twitter (mass-scale, unrestricted, third-party surveillance and advertising):

<https://twitter.com/doctorow>

Tumblr (mass-scale, unrestricted, third-party surveillance and advertising):

<https://mostlysignssomeportents.tumblr.com/tagged/pluralistic>

"*When life gives you SARS, you make sarsaparilla*" -Joey "Accordion Guy" DeVilla
