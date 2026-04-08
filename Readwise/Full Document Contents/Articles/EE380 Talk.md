# EE380 Talk

![rw-book-cover](https://1.bp.blogspot.com/-VSheYLgKpZw/YZQBnN42F1I/AAAAAAAAGoQ/Yqjp5kYQcjoaAr2S9U1CSAvuhIOPnOXSACLcBGAsYHQ/w1200-h630-p-k-no-nu/ElSalvador.jpg)

## Metadata
- Author: [[David.]]
- Full Title: EE380 Talk
- Category: #articles
- Summary: Bitcoin and other cryptocurrencies contribute to significant environmental harm and enable various criminal activities, primarily driven by speculation rather than illegal transactions. The reliance on Proof-of-Work creates unsustainable energy use, while the promise of decentralization often leads to centralization in practice. Despite their initial intentions, cryptocurrencies have largely become platforms for rampant speculation rather than effective currencies.
- URL: https://blog.dshr.org/2022/02/ee380-talk.html

## Full Document
I was asked at short notice to fill in for a speaker in [Stanford's EE380](http://web.stanford.edu/class/ee380/) course who had to cancel. Below the fold is a hastily updated version of a talk from last December.

**Update 28th February**: the video of this talk is [here](https://www.youtube.com/watch?v=twrduL8aNGE).

[Slide 1: Title]  

 I apologize if this talk is a bit rough. Dennis mailed me yesterday morning asking if I could speak, so I updated a talk I gave in December to an [Institutional Investor conference](https://blog.dshr.org/2021/12/talk-at-ttivanguard-conference.html). You don't need to take notes; the text of this talk with links to the sources and much additional material will be on blog.dshr.org. I'm aiming to talk for 30 minutes and be controversial enough to spark a discussion, so please hold questions.

I'm David Rosenthal. I worked with James Gosling on CMU's Andrew project in the early 80s. I was a DE with him at Sun later in the 80s working on window systems including X, and file systems. I quit to be employee #4 at Nvidia where Curtis Priem and I did the basic I/O architecture, then was an early employee at Vitria, the second company of founders of Tibco. Before I start talking about cryptocurrencies, I should stress that I hold no long or short positions in cryptocurrencies, their derivatives or related companies; I am long Nvidia. Unlike most people discussing them, I am not "talking my book".

[Cryptocurrencies' roots](https://twitter.com/davetroy/status/1478017698676228099) lie deep in the [libertarian culture of Silicon Valley and the cypherpunks](https://www.worldcat.org/title/digital-cash-the-unknown-history-of-the-anarchists-utopians-and-technologists-who-built-cryptocurrency/oclc/1142885258&referer=brief_results). Libertarianism's attraction is based on ignoring externalities, and cryptocurrencies are no exception.

[Slide 2: Externalities]  

 Bitcoin is notorious for consuming [as much electricity as the Netherlands](https://cbeci.org/index/comparisons), but there are around 10,000 other cryptocurrencies, most using similar infrastructure and thus also in aggregate consuming unsustainable amounts of electricity. Bitcoin alone generates [as much e-waste as the Netherlands](https://doi.org/10.1016/j.resconrec.2021.105901), cryptocurrencies suffer an epidemic of [pump-and-dump schemes](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3670714) and [wash trading](https://www.bloomberg.com/news/articles/2021-10-29/here-s-a-532-million-nft-trade-that-wasn-t-what-it-appeared), they enable a [$5.2B/year ransomware industry](https://www.fincen.gov/sites/default/files/shared/Financial%20Trend%20Analysis_Ransomeware%20508%20FINAL.pdf), they have disrupted supply chains for [GPUs](https://www.pcmag.com/news/inside-the-gpu-shortage-why-you-still-cant-buy-a-graphics-card), [hard disks, SSDs](https://www.newscientist.com/article/2278696-bitcoin-rival-chia-destroyed-hard-disc-supply-chains-says-its-boss/) and other chips, they have made it impossible for web services to offer [free tiers](https://therecord.media/crypto-mining-gangs-are-running-amok-on-free-cloud-computing-platforms/), and they are responsible for a massive crime wave including [fraud](https://www.osc.gov.on.ca/quadrigacxreport/), [theft](https://davidgerard.co.uk/blockchain/2019/05/08/binance-hacked-largest-tether-exchange-cuts-off-withdrawals-for-the-next-week/), [tax evasion](https://www.washingtonpost.com/us-policy/2021/05/20/biden-tax-compliance-treasury/), funding of [rogue states such as North Korea](https://www.cnbc.com/2021/02/17/north-korean-hackers-charged-in-massive-cryptocurrency-theft-scheme.html), [drug](https://www.theguardian.com/news/2021/may/20/a-united-nations-of-how-marbella-became-a-magnet-for-gangsters) [smuggling](https://decrypt.co/7410/from-cocaine-to-crypto-the-new-escobar-family-business), and even as documented by Jameson Lopp's [list of physical attacks](https://github.com/jlopp/physical-bitcoin-attacks/blob/master/README.md), armed robbery, kidnapping, torture and murder.

[Slide 3: Alecus]

|  |
| --- |
| Alecus, El Diario de Hoy |

The attempt to force El Salvador's population to use cryptocurrency is a fiasco. They offer no significant social benefit beyond speculation; [Igor Makarov and Antoinette Schoar](https://www.nber.org/papers/w29396) write:

>  90% of transaction volume on the Bitcoin blockchain is not tied to economically meaningful activities but is the byproduct of the Bitcoin protocol design as well as the preference of many participants for anonymity. ...  
>  exchanges play a central role in the Bitcoin system. They explain 75% of real Bitcoin volume  
>  ...  
>  Our results do not support the idea that the high valuation of cryptocurrencies is based on the demand from illegal transactions. Instead, they suggest that the majority of Bitcoin transactions is linked to speculation. 

[Slide 4: "Transaction" Rate]

|  |
| --- |
| [Source](https://www.blockchain.com/charts/n-transactions) |

Bitcoin is only processing around 27K "economically meaningful" transactions/day. And 75% of those are transactions between exchanges, so only 2.5% of the "transactions" are real blockchain-based transfers involving individuals. That's less than 5 per minute.

Nakamoto's motivation for Bitcoin was distrust of institutions, especially central banks. When it launched in the early stage of the Global Financial Crisis, this had resonance. The key to a system that involves less trust is decentralization.

[Slide 5: Resilience]  

 Why do suspension bridges have stranded cables not solid rods? The major reason is that solid rods would fail suddenly and catastrophically, whereas stranded cables fail slowly and make alarming noises while they do. We build software systems out of solid rods; they fail abruptly and completely. Most are designed to perform their tasks as fast as possible, so that when they are compromised, they perform the attacker's tasks as fast as possible. Changing this, making systems that are resilient, ductile like copper not [brittle like glass](https://blog.dshr.org/2015/06/brittle-systems.html), is an extraordinarily difficult problem in software engineering. Paul Vixie [pointed out](https://queue.acm.org/detail.cfm?id=2578510) that [rate limits](https://blog.dshr.org/2018/06/rate-limits.html) are an essential part of the solution.

I got interested in it when, burnt out after three startups all of which IPO-ed, I started work at the Stanford Library on the problem of keeping digital information safe for the long term. This work won my Stanford CS co-authors (Petros Maniatis, Mema Roussopolous, TJ Giuli and Prof. Mary Baker) and I a "Best Paper" award at the 2003 SOSP for a [decentralized consensus system using Proof-of-Work](http://dx.doi.org/10.1145/945445.945451). When, five years later, Satoshi Nakamoto published the [Bitcoin protocol](https://bitcoin.org/bitcoin.pdf), a cryptocurrency based on a decentralized consensus mechanism using Proof-of-Work, I was naturally interested in how it turned out.

Decentralization is a necessary but insufficient requirement for system resilience. Centralized systems have a single locus of control. Subvert it, and the system is at your mercy. It only took six years for Bitcoin to fail Nakamto's goal of decentralization, with one mining pool controlling more than half the mining power. In the seven years since no more than five pools have always controlled a majority of the mining power.

[Slide 6: Economies of Scale]

|  |
| --- |
| [Source](https://smile.amazon.com/Increasing-Returns-Dependence-Economics-Cognition/dp/0472064967/) |

In 2014 I wrote [*Economies of Scale in Peer-to-Peer Networks*](http://blog.dshr.org/2014/10/economies-of-scale-in-peer-to-peer.html), explaining the economic cause of this failure. Briefly, this is an example of the phenomenon described by W. Brian Arthur in 1994's  [*Increasing returns and path dependence in the economy*](https://www.worldcat.org/title/increasing-returns-and-path-dependence-in-the-economy/oclc/1043354814&referer=brief_results). Information technologies have strong economies of scale, so the larger the miner the lower their costs, and thus the greater their profit, and thus the greater their market share.

"Blockchain" is unfortunately a term used to describe two completely different technologies, which have in common only that they both use a [Merkle Tree](http://www.merkle.com/papers/Protocols.pdf) data structure. *Permissioned* blockchains have a central authority controlling which network nodes can add blocks to the chain, and are thus not decentralized, whereas *permissionless* blockchains such as Bitcoin's do not; this difference is fundamental:

* Permissioned blockchains can use well-established and relatively efficient techniques such as [Byzantine Fault Tolerance](https://doi.org/10.1145/357172.357176), and thus don't have significant carbon footprints. These techniques ensure that each node in the network has performed the same computation on the same data to arrive at the *same* state for the next block in the chain. This is a *consensus* mechanism.
* In principle each node in a permissionless blockchain's network can perform a different computation on different data to arrive at a *different* state for the next block in the chain. Which of these blocks ends up in the chain is determined by a randomized, biased *election* mechanism. For example, in Proof-of-Work blockchains such as Bitcoin's a node wins election by being the first to solve a puzzle. The length of time it takes to solve the puzzle is random, but the probability of being first is biased, it is proportional to the compute power the node uses. Initially, because of network latencies, nodes may disagree as to the next block in the chain, but eventually it will become clear which block gained the most acceptance among the nodes. This is why a Bitcoin transaction should not be regarded as final until it is six blocks from the head.

[Slide 7: Blockchain Patent Filed 1990]

|  |
| --- |
| [Source](https://patentimages.storage.googleapis.com/0b/69/46/be53cde1a722f6/US5136647.pdf) |

Discussing "blockchains" and their externalities without specifying permissionless or permissioned is meaningless, they are completely different technologies. One is 30 years old, the other is 13 years old.

Because there is no central authority controlling who can participate, decentralized consensus systems must defend against Sybil attacks, in which the attacker creates a majority of seemingly independent participants which are secretly under his control. The defense is to ensure that the reward for a successful Sybil attack is less than the cost of mounting it. Thus participation in a permissionless blockchain must be expensive, so miners must be reimbursed for their costly efforts. There is no central authority capable of collecting funds from users and distributing them to the miners in proportion to these efforts. Thus miners' reimbursement must be generated organically by the blockchain itself; a permissionless blockchain needs a cryptocurrency to be secure.

Because miners' opex and capex costs cannot be paid in the blockchain's cryptocurrency, exchanges are required to enable the rewards for mining to be converted into fiat currency to pay these costs. Someone needs to be on the other side of these sell orders. The *only* reason to be on the buy side of these orders is the belief that "[number go up](https://davidgerard.co.uk/blockchain/2019/05/27/the-origin-of-number-go-up-in-bitcoin-culture/)". Thus the exchanges need to attract speculators in order to perform their function.

Thus a permissionless blockchain *requires* a cryptocurrency to function, and this cryptocurrency *requires* speculation to function.

Why are economies of scale a fundamental problem for decentralized systems? Participation must be expensive, and so will be subject to economies of scale. They will drive the system to centralize. So the expenditure in attempting to ensure that the system is decentralized is a futile waste.

Most cryptocurrencies impose these costs, as our earlier system did, using Proof-of-Work. It was a brilliant idea when [Cynthia Dwork and Moni Naor](https://dl.acm.org/citation.cfm?id=705669) originated it in 1992, being both simple and effective. But when it is required to make participation expensive enough for a trillion-dollar cryptocurrency it has an unsustainable carbon footprint.

[Slide 8: Bitcoin Energy Consumption]

|  |
| --- |
| [Source](https://cbeci.org/) |

The leading source for estimating Bitcoin's electricity consumption is the [Cambridge Bitcoin Energy Consumption Index](https://cbeci.org/index/), whose current central estimate is 117TWh/year.

Adjusting [Christian Stoll *et al*'s 2018 estimate](http://ceepr.mit.edu/files/papers/2018-018.pdf) of Bitcoin's carbon footprint to the current CBECI estimate gives a range of about 50.4 to 125.7 MtCO2/yr for Bitcoin's opex emissions, or between [Portugal and Myanmar](https://en.wikipedia.org/wiki/List_of_countries_by_carbon_dioxide_emissions). Unfortunately, this is likely to be a considerable underestimate. [*Bitcoin's growing e-waste problem*](https://doi.org/10.1016/j.resconrec.2021.105901) by Alex de Vries and Christian Stoll concludes that:

>  Bitcoin's annual e-waste generation adds up to 30.7 metric kilotons as of May 2021. This level is comparable to the small IT equipment waste produced by a country such as the Netherlands. 

That's an average of one whole MacBook Air of e-waste *per "economically meaningful" transaction*.

[Slide 9: Facebook & Google Carbon Footprints]

|  |
| --- |
| [Source](https://arxiv.org/pdf/2011.02839.pdf) |

The reason for this extraordinary waste is that the profitability of mining depends on the energy consumed per hash, and the rapid development of mining ASICs means that they rapidly become uncompetitive. de Vries and Stoll estimate that the average service life is less than 16 months. This mountain of e-waste contains embedded carbon emissions from its manufacture, transport and disposal. These graphs show that for Facebook and Google data centers, capex emissions are [at least as great as the opex emissions](https://blog.dshr.org/2021/10/cryptocurrencys-carbon-footprint.html)[[1]](https://blog.dshr.org/2022/02/ee380-talk.html#Endnote1).

Cryptocurrencies assume that society is committed to this waste of energy and hardware *forever*. Their response is frantic greenwashing, such as claiming that because Bitcoin mining allows an obsolete, uncompetitive coal-burning plant near St. Louis to *continue burning coal* it is somehow [good for the environment](https://arstechnica.com/tech-policy/2021/09/old-coal-plant-is-now-mining-bitcoin-for-a-utility-company/)[[2]](https://blog.dshr.org/2022/02/ee380-talk.html#Endnote2).

But, they argue, mining can use renewable energy. First, at present it doesn't. For example, Luxxfolio implemented their commitment to 100% renewable energy [by buying 15 megawatts of coal-fired power from the Navajo Nation!](https://davidgerard.co.uk/blockchain/2021/09/21/news-bitcoin-miners-cant-sell-their-bitcoins-sushiswap-theft-coinbase-lend-crypto-seasteading/).

Second, even if it were true that cryptocurrencies ran on renewable power, the idea that it is OK for speculation to waste vast amounts of renewable power assumes that doing so doesn't compete with more socially valuable uses for renewables, or indeed for power in general.

[Slide 10: Energy Return on Investment]

|  |
| --- |
| [Delannoy et al Fig 2](https://doi.org/10.1016/j.apenergy.2021.117843) |

Right now the world is short of power; one major reason that China banned cryptocurrency mining was that they needed their limited supplies of power to keep factories running and homes warm. Shortage of energy isn't a short-term problem. This graph is from [*Peak oil and the low-carbon energy transition: A net-energy perspective*](https://doi.org/10.1016/j.apenergy.2021.117843) by Louis Delannoy *et al* showing that as the easiest deposits are exploited first, the Energy Return On Investment, measuring the fraction of the total energy extracted delivered to consumers, decreases.

[Slide 11: Oil Energy Gross vs. Net]

|  |
| --- |
| [Delannoy et al Fig 1](https://doi.org/10.1016/j.apenergy.2021.117843) |

Delannoy *et al*'s Figure 1 shows the gross and net oil energy history and projects it to 2050. The gross energy, and thus the carbon emission, peaks around 2035, but because the energy used in extraction (the top yellow band) increases rapidly, the net energy peaks in about 5 years.

[Slide 12: CO2 Emission Trajectories]

|  |
| --- |
| [Source](https://www.economist.com/international/2021/10/23/broken-promises-energy-shortages-and-covid-19-will-hamper-cop26) |

This is a problem for two reasons. If society is to survive:

* Carbon emissions need to start decreasing *now*, not in a decade and a half.
* Renewables need to be deployed very rapidly.

Deploying renewables consumes energy, which is paid back during their initial operation. Thus the current transition to renewable power consumes energy, reducing that available for other uses[[3]](https://blog.dshr.org/2022/02/ee380-talk.html#Endnote3). The world cannot afford to waste a Netherlands' worth of energy on speculation that could instead be deploying renewables.

If cryptocurrency speculation is to continue, it needs to vastly reduce its carbon footprint by eliminating Proof-of-Work. The two major candidates are Proof-of-Space-and-Time and Proof-of-Stake.

Proof-of-Space-and-Time attempts to make participation expensive by wasting storage instead of computation. The highest-profile such effort is Bram Cohen's [*Chia*](https://www.chia.net/), funded by [Andreesen Horowitz](https://www.nytimes.com/2021/10/29/us/politics/andreessen-horowitz-lobbying-cryptocurrency.html), the ["Softbank of crypto"](https://davidgerard.co.uk/blockchain/2021/07/16/newsdefi-education-fund-latest-binance-woes-fatf-rules-developers-hate-crypto/). Chia's "space farmers" create and store "plots" consisting of large amounts of otherwise useless data.

[Slide 13: Chia]

|  |
| --- |
| [Source](https://www.coinbase.com/price/chia-network) |

The software was ingenious, but the design suffered from [naiveté about storage media and markets](https://blog.dshr.org/2018/09/chia-network.html). When it launched in May, gullible farmers rushed to buy hard disks and SSDs. By July, the capital tied up in farming hardware was around *six times* the market cap of the Chia coin. Chia's CEO [described the result](https://www.newscientist.com/article/2278696-bitcoin-rival-chia-destroyed-hard-disc-supply-chains-says-its-boss/):

>  "we've kind of destroyed the short-term supply chain" 

Disk vendors were forced to explain that Chia farming voided the media's warranty. Just as with GPUs, the used market was flooded with burnt-out storage. Chia's coin initially traded at $1934 before dropping more than 90% — last I looked it was [$81](https://www.coinbase.com/price/chia-network). I expect A16Z made money, but everyone else had to deal with the costs. Chia doesn't use much electricity, more to do with failure than with the technology, but does have a major e-waste problem.

[Slide 14: Proof of Stake Sucks]

|  |
| --- |
| [Bram Cohen's opinion](https://www.youtube.com/watch?v=2Zlcgt8FVz4) |

The costs that Proof-of-Stake imposes to make participation expensive are the risk of loss and the foregone liquidity of the "stake", an escrowed amount of the cryptocurrency itself. This has two philosophical problems:

* It isn't just that the [Gini coefficients of cryptocurrencies](https://blog.dshr.org/2018/10/gini-coefficients-of-cryptocurrencies.html) are extremely high[[4]](https://blog.dshr.org/2022/02/ee380-talk.html#Endnote4), but that Proof-of-Stake makes this a self-reinforcing problem. Because the rewards for mining new blocks, and the fees for including transactions in blocks, flow to the HODL-ers in proportion to their HODL-ings, whatever Gini coefficient the systems starts out with will always increase. Proof-of-Stake isn't effective at decentralization.
* Cryptocurrency whales are believers in "[number go up](https://davidgerard.co.uk/blockchain/2019/05/27/the-origin-of-number-go-up-in-bitcoin-culture/)". The eventual progress of their coin "to the moon!" means that the temporary costs of staking are irrelevant.

There are also a host of severe technical problems. The accomplished Ethereum team have been making a praiseworthy effort to overcome them for more than 7 years and are still [more than a year away](https://davidgerard.co.uk/blockchain/2021/06/16/news-stopping-ransomware-china-hates-miners-ecuador-cbdc-history-nfts-still-too-hard-to-buy/) from being able to migrate off Proof-of-Work.

[Slide 15:Centralization Risk]

[Yulin Cheng wrote](https://www.theblockcrypto.com/post/57508/tron-steem-takeover-crypto-exchanges-governance-reversal-soft-fork-blockchain):

>  According to the list of accounts powered up on March. 2, the three exchanges collectively put in over 42 million STEEM Power (SP).   
>    
>  With an overwhelming amount of stake, the Steemit team was then able to unilaterally implement hard fork 22.5 to regain their stake and vote out all top 20 community witnesses – server operators responsible for block production – using account @dev365 as a proxy. In the current list of Steem witnesses, Steemit and TRON’s own witnesses took up the first 20 slots. 

Vitalik Buterin pointed out that [lack of decentralization was a security risk](https://blog.dshr.org/2017/12/why-decentralize.html) in 2017, and this was amply borne out last year when [Justin Sun conspired with three exchanges](https://www.theblockcrypto.com/post/57508/tron-steem-takeover-crypto-exchanges-governance-reversal-soft-fork-blockchain), staking their customers coins to take over the Steem Proof-of-Stake blockchain. Pushing back against the economic forces centralizing these systems is extremely difficult.

[Slide 16: Top 2 ETH Pools = 53.9%]  

 The advantage of permissionless over permissioned blockchains is claimed to be decentralization. How has that worked out in practice?

As has been true for the last seven years, no more than five mining pools control the majority of the Bitcoin mining power and last November [two pools controlled the majority of Ethereum mining](https://miningpoolstats.stream/ethereum). [Makarov and Schoar](https://www.nber.org/papers/w29396) write:

>  Six out of the largest mining pools are registered in China and have strong ties to Bitmain Techonologies, which is the largest producer of Bitcoin mining hardware, 

[Slide 17: Centralized Mining]

[Makarov and Schoar](https://www.nber.org/papers/w29396) write:

>  Bitcoin mining capacity is highly concentrated and has been for the last five years. The top 10% of miners control 90% and just 0.1% (about 50 miners) control close to 50% of mining capacity. Furthermore, this concentration of mining capacity is counter cyclical and varies with the Bitcoin price. It decreases following sharp increases in the Bitcoin price and increases in periods when the price drops ... the risk of a 51% attack increases in times when the Bitcoin price drops precipitously or following the halving events. 

It isn't just the mining pools that are centralized. The top 10% of miners control 90% and just 0.1% (about 50 miners) control close to 50% of mining capacity. This centralization doesn't just increase the system's technical risk, but also its legal risk. The reason is that in almost all cryptocurrencies a transaction wishing to be confirmed is submitted to a public "mempool" of pending transactions. The mining pools choose transactions from there to include in the blocks they attempt to mine. This, as [Nicholas Weaver points out](https://www.lawfareblog.com/how-start-disrupting-cryptocurrencies-mining-money-transmission), means that mining pools are providing [money transmission services](https://www.law.cornell.edu/cfr/text/31/1010.100#ff_5) under US law:  

 [Slide 18: 31 CFR § 1010.100]

>  The term "money transmission services" means the acceptance of currency, funds, or other value that substitutes for currency from one person and the transmission of currency, funds, or other value that substitutes for currency to another location or person by any means. 

Thus, in the US, they are required to follow the Anti-Money Laundering/Know Your Customer (AML/KYC) rules as enforced by the [Financial Crimes Enforcement Network](https://en.wikipedia.org/wiki/Financial_Crimes_Enforcement_Network) (FinCEN)[[6]](https://blog.dshr.org/2022/02/ee380-talk.html#Endnote6). The only pool to [try following them](https://www.lawfareblog.com/how-start-disrupting-cryptocurrencies-mining-money-transmission):

>  [stopped doing this](https://www.theblockcrypto.com/linked/106865/marathon-ofac-bitcoin-mining-pool-taproot) because the larger Bitcoin community objects to the idea of attempting to restrict Bitcoin to legal uses! 

As [Adem Efe Gencer *et al*](https://arxiv.org/pdf/1801.03998.pdf) pointed out:

>  a Byzantine quorum system of size 20 could achieve better decentralization than proof-of-work mining at a much lower resource cost. 

Thus the only reason for the massive carbon footprint of Proof-of-Work and the complexity and risk of the alternatives is to maintain the illusion of decentralization. Alas, it is unlikely that any alternative defense against Sybil attacks will be widely enough adopted to mitigate Proof-of-Work's carbon emissions.

[Slide 19: Immutability]

|  |
| --- |
| [Source](https://davidgerard.co.uk/blockchain/2021/05/22/news-everybody-hates-chia-defi100-rugpull-china-versus-mining-china-versus-crypto/) |

Immutability is one of the two things that make the cryptocurrency crime wave so effective. These systems are brittle, make a single momentary mistake and your assets are irretrievable.

Immutability sounds like a great idea when everything is going to plan, but in the real world mistakes are inevitable. Lets take a few recent examples — the [$23M fee Bitfinex paid for a $100K transaction](https://cryptocat.news/2021/09/27/bitfinex-paid-a-colossal-23m-fee-to-send-100k-of-usdt/), or the [$19M oopsie at Indexed Finance](https://arstechnica.com/information-technology/2021/12/hackers-drain-31-million-from-cryptocurrency-service-monox-finance/), or the [$31M oopsie at MonoX](https://arstechnica.com/information-technology/2021/12/hackers-drain-31-million-from-cryptocurrency-service-monox-finance/), or the [$90M oopsie at Compound](https://www.bleepingcomputer.com/news/security/crypto-platform-mistakenly-gives-90m-to-users-asks-for-refund) and the subsequent [$67M oopsie](https://www.cnbc.com/2021/10/03/162-million-up-for-grabs-after-bug-in-defi-protocol-compound-.html), all of which left the perpetrators pleading with the benficiaries to return the loot. And in Compound's case threatening its customers with the ultimate crypto punishment, reporting them to the IRS. $12B in DeFi thefts so far, or about 5% of all the funds[[7]](https://blog.dshr.org/2022/02/ee380-talk.html#Endnote7).

[Slide 20: Trammell Hudson]

|  |
| --- |
| [Source](https://twitter.com/qrs/status/1395784294451265536) |

Vulnerabilities are equally inevitable, as we see with the [$38M, $19M and $130M hacks of Cream Finance](https://www.bloomberg.com/news/articles/2021-10-27/defi-protocol-cream-finance-loses-130-million-in-latest-hack) last year, the [$115M hack of BadgerDAO](https://www.theblockcrypto.com/post/126072/defi-protocol-badgerdao-exploited-for-120-million-in-front-end-attack), the [$196M hack of BitMart](https://www.cnbc.com/2021/12/05/hackers-take-196-million-from-crypto-exchange-bitmart-in-large-breach.html), the recent [$323M hack of Wormhole](https://arstechnica.com/information-technology/2022/02/how-323-million-in-crypto-was-stolen-from-a-blockchain-bridge-called-wormhole/), and of course the [$600M hack of Poly Network](https://mudit.blog/poly-network-largest-crypto-hack/).

Because Ethereum and similar cryptocurrencies are programming environments, their attack surface is much larger than Bitcoin's. Now that DeFi and NFT protocols are implemented as "smart contracts" in these environments, the attack surface has expanded much further. One example is the rash of hacks involving [hijacks of the Discord servers](https://www.vice.com/en/article/5dg5xq/nft-collector-iloveponzi-loses-valuable-ape-nfts-to-hackers-is-upset) of the communities surrounding them to lure victims into autheticating their wallets to malign "smart contracts". Another is the flood of ["rug-pulls" buried in the "smart contracts"](https://www.vice.com/en/article/wxdzvy/real-estate-cryptocurrency-takes-peoples-money-then-shuts-down-and-vanishes) implementing NFTs.

[Slide 21: Jacob Silverman]

> Imagine if big banks were getting hacked for tens or hundreds of millions of $$ each week but also nothing was insured, there were no systems in place to mitigate fallout, and half of the hacks were inside jobs. That's basically DeFi.
> 
> — Jacob Silverman (@SilvermanJacob) [February 3, 2022](https://twitter.com/SilvermanJacob/status/1489044950322925571?ref_src=twsrc%5Etfw)

Yet another is described in Dan Goodin's [*How $323M in crypto was stolen from a blockchain bridge called Wormhole*](https://arstechnica.com/information-technology/2022/02/how-323-million-in-crypto-was-stolen-from-a-blockchain-bridge-called-wormhole/). Because there are many competing blockchains, bridges exist to provide liquidity between them. Last month Vitalik Buterin provided a detailed explanation of why they are a [fundamental security problem](https://old.reddit.com/r/ethereum/comments/rwojtk/ama_we_are_the_efs_research_team_pt_7_07_january/hrngyk8/). A "smart contract" called a guardian locks up coins on one blockchain and unlocks the same number on another, but in this case the guardian failed to properly validate signatures.  

 [Slide 22: Wormhole Vulnerability]

![](https://pbs.twimg.com/profile_images/1547509344056381441/-u4dh93A.jpg)

[samczsun](https://twitter.com/samczsun)
[@samczsun](https://twitter.com/samczsun)

tl;dr - Wormhole didn't properly validate all input accounts, which allowed the attacker to spoof guardian signatures and mint 120,000 ETH on Solana, of which they bridged 93,750 back to Ethereum.

[Posted Feb 3, 2022 at 1:16AM](https://twitter.com/samczsun/status/1489044999211823107)

Three days later a bug in another bridge was [exploited for $4.3M](https://web3isgoinggreat.com?id=2022-02-05-0).

The centralization of Ethereum's mining pools and exchanges enabled Poly Network to persuade them to blacklist the addresses involved. This made it very difficult for the miscreant to escape with the loot, much of which was returned. But it also vividly demonstrated that in most blockchains it is the mining pools that decide which transactions make it into a block, and are thus executed. The small number of dominant mining pools can effectively prevent addresses from transacting, and can prioritize transactions from favored addresses. They can also allow transactions to avoid the public mempool, to prevent them being [front-run by bots](https://medium.com/@danrobinson/ethereum-is-a-dark-forest-ecc5f0505dff). This turned out to be useful when a small group of white hats discovered a vulnerability in a smart contract holding $9.6M.

The key point of [*Escaping the Dark Forest*](https://samczsun.com/escaping-the-dark-forest/), Samczsun's account of their night's work, is that, after the group spotted the vulnerability and built a transaction to rescue the funds, they could not put the rescue transaction in the public mempool because it would have been front-run by a bot. They had to find a miner who would put the transaction in a block *without* it appearing in the mempool. In other words, their transaction needed a dark pool. And they had to trust the cooperative miner not to front-run it.

[Slide 23: Ether Mining Pools 11/02/20]

|  |
| --- |
| [Ether miners 11/2/20](https://www.etherchain.org/miner) |

Ethereum is, fortunately, very far from decentralized, being centralized around a small number of large pools. Thus, the group needed a trusted pool not an individual miner. At the time, the three largest pools mined more than half the blocks between them, so only three calls would have been needed to have a very good chance that the transaction would appear in one of the next few blocks.

Most activity in "trustless" cryptocurrencies actually uses trusted third parties, exchanges, that are layered above the blockchain itself. These use conventional Web-based identities and provide another layer of centralization. Binance, the dominant exchange, does two out of three derivative transactions and half of all spot transactions. Adam Levitin points out that [customers are *unsecured creditors* of exchanges](https://www.creditslips.org/creditslips/2022/02/what-happens-if-a-cryptocurrency-exchange-files-for-bankruptcy.html). Exchanges are [routinely compromised](https://www.nbcnews.com/tech/security/bitcoin-crypto-exchange-hacks-little-anyone-can-do-rcna7870); in most cases immutability means the pilfered funds are not recovered.

But, more fundamentally, the entire cryptocurrency ecosystem depends upon a trusted third party, Tether, which acts as a central bank issuing the "stablecoins" that cryptocurrencies are priced against and traded in[[8]](https://blog.dshr.org/2022/02/ee380-talk.html#Endnote8). This is despite the fact that [Tether is known to be untrustworthy](https://www.bloomberg.com/news/features/2021-10-07/crypto-mystery-where-s-the-69-billion-backing-the-stablecoin-tether), having consistently lied about its reserves.

[Slide 24: Anonymity]

[Makarov and Schoar](https://www.nber.org/papers/w29396) write[[9]](https://blog.dshr.org/2022/02/ee380-talk.html#Endnote9):

>  First, non-KYC entities serve as a gateway for money laundering and other gray activities.  
>  ...  
>  Second, even if KYC entities were restricted to deal exclusively with other KYC entities, preventing inflows of tainted funds would still be nearly impossible, unless one was willing to put severe restrictions on who can transact with whom  
>  ...  
>  Finally, notice that while transacting in cash and storing cash involve substantial costs and operational risks, transacting in cryptocurrencies and storing them are essentially costless (apart from fluctuation in value). 

The other main enabler of the cryptocurrency crime spree is the prospect of transactions that aren't merely immutable but are also anonymous. Anonymity for small transactions is important, but for large transactions it provides the infrastructure for major crime. In the physical world cash is anonymous, but it has the valuable property that the cost and difficulty of transacting increase strongly with size. KYC/AML and other regulations leverage this. Cryptocurrencies lack this property. The ease with which cryptocurrency can be transferred between institutions that do, and do not, observe the KYC/AML regulations means that absent robust action by the US, the KYC/AML regime is doomed.

[Slide 25: The Coming Ransomware Storm]

Stephen Diehl writes in [*The Oncoming Ransomware Storm*](https://www.stephendiehl.com/blog/ransomware.html):

>  Go to your local bank branch and try to wire transfer $200,000 to an anonymous stranger in Russia and see how that works out. Modern ransomware could not exist without Bitcoin, it has poured gasoline on a fire we may not be able to put out.  
>    
>  When you create a loophole channel (however flawed) for parties to engage in illicit financing of anonymous entities beyond the control of law enforcement, it turns out a lot of shady businesses models that are otherwise prevented move from being impractical and risky to perversely incentivized. Ransomware is now very lucrative to the point where there is a whole secondary market of vendors selling Ransomware as a Service picks and shovels to the criminals. 

The most serious crime enabled by anonymity is ransomware, which is regularly crippling essential infrastructure such as oil pipelines and hospital systems, to say nothing of the losses to business large and small. This business is estimated to gross $5.2B/year and is growing rapidly, aided by a network of specialist service providers. This is just the ransom payments, the actual externalities include the much larger costs of recovering from the attacks.

There are cryptocurrencies that provide almost complete anonymity using sophisticated cryptography[[10]](https://blog.dshr.org/2022/02/ee380-talk.html#Endnote10). For example [Monero](https://en.wikipedia.org/wiki/Monero):

>  Observers cannot decipher addresses trading monero, transaction amounts, address balances, or transaction histories. 

Bitcoin and similar cryptocurrencies are *pseudonymous* not anonymous. Anyone can create and use an essentially unlimited number of pseudonyms (addresses), but transactions and balances using them are public. A newly minted pseudonym cannot be deanonymized, but as it becomes enmeshed in the public web of transactions maintaining anonymity takes more operational security than most users can manage.

Users are aware of the risk that their transactions can be traced, so many engage in [wash transactions](https://blog.dshr.org/2021/11/making-sure-number-go-up.html) between addresses they control, and use [mixers and tumblers](https://en.wikipedia.org/wiki/Cryptocurrency_tumbler) to mingle their coins with those of other miscreants. Because it is almost impossible to actually buy legal goods with Bitcoin, at some point a HODL-er needs to use an exchange to obtain fiat currency[[11]](https://blog.dshr.org/2022/02/ee380-talk.html#Endnote11). This risks having their identity connected into the web of transactions on the blockchain. [Makarov and Schoar](https://www.nber.org/papers/w29396) conclude:

>  90% of transaction volume on the Bitcoin blockchain is not tied to economically meaningful activities but is the byproduct of the Bitcoin protocol design as well as the preference of many participants for anonymity. 

In other words, 90% of Bitcoin's carbon footprint is used in a partially successful attempt to compensate for its deficient anonymity.

Because there are existing alternatives that provide greatly increased anonymity, attempts to mitigate the externalities of pseudonoymous cryptocurrencies are likely to be self-defeating. As the ransomware industry shows, users will migrate to these alternatives, reducing the effectiveness of chain analysis.

[Slide 26: Conclusions]  

 Although the techniques used to implement decentralization are effective in theory, at scale emergent economic effects render them ineffective. Despite this, decentralization is fundamental to the cryptocurrency ideology, making mitigation of its externalities effectively impossible. And attempts to mitigate the externalities of pseudonymous cryptocurrencies are lijkely to be self-defeating. We can conclude that:

1. Permissioned blockchains do not need a cryptocurrency to defend against Sybil attacks, and thus do not have significant externalities.
2. Permissionless blockchains require a cryptocurrency, and thus necessarily impose all the externalities I have described except the carbon footprint.
3. If successful, permissionless blockchains using Proof-of-Work, or any other way to waste a real resource as a Sybil defense, have unacceptable carbon footprints.
4. Whatever Sybil defense they use, economics forces successful permissionless blockchains to centralize; there is no justification for wasting resources in a doomed attempt at decentralization.

Don't get me wrong. I am not a fan of centralization. I started building a decentralized, permissionless system almost a quarter-century ago. It would be wonderful if we could figure out how to build a Web that would resist centralization. But all the technical and financial cleverness that's been poured into cryptocurrencies hasn't succeeded in doing that. Why? It is because [*It Isn't About The Technology*](https://blog.dshr.org/2018/01/it-isnt-about-technology.html).

I'm a big believer in Bill Joy's Law of Startups, "success is inversely proportional to the amount of money you have". For $2.5M we got Nvidia to working silicon that was revolutionary in two different respects. Right now, there is way too much money. If a system is to be decentralized, it has to have a low barrier to entry. If it has a low barrier to entry, competition will ensure it has low margins. Low margin businesses don't attract venture capital. VCs are pouring money into cryptocurrency and "web3" companies. This money is not going to build systems with low barriers to entry and thus low margins. Thus the systems that will result from this flood of money will not be decentralized, no matter what the sales pitch says.

Despite all the cleverness and hype, the technology just isn't that good. It is both extraordinarily inefficient, and extraordinarily insecure. [Nicholas Weaver](https://www.usenix.org/publications/loginonline/web3-fraud) points out that the "Ethereum computer" is 1/5000 as powerful as a Raspbery Pi. and that for the cost of 1 second of its use you can buy nearly 60 Raspberry Pis. [Moxie Marlinspike](https://moxie.org/2022/01/07/web3-first-impressions.html) points out that an NFT is a [link to a file of metadata that links to the image](https://blog.dshr.org/2021/04/nfts-and-web-archiving.html) it purports to represent, so neither is guaranteed to exist or be valid. You have only to glance at Molly White's [*Web3 is going just great*](https://web3isgoinggreat.com/) timeline wonder why anyone thinks this "wretched hive of scum and villainy" should be the future of the Web.

I hope I've said enough to start some discussion. I think there are three basic lines of argument:

* That the externalities I describe don't exist. You'll have a hard time proving that the waste of electricity and hardware, and the crime wave, are imaginary.
* That although the externalities do exist, the benefits of decentralization outweigh them. The problem here is that since the systems are not actually decentralized, we get the externalities but don't get the benefits.
* That although the externalities do exist, and the systems aren't dencentralized, they're making so much money that we shouldn't worry. The problem here is that the amount of actual money you can get out of a cryptocurrency equals the amount of actual money that has been put in, minus the actual costs of mining. So the big picture is that although there may be winners, in aggregate the system loses money.

#####  End Notes

1. Ethereum mining adds another [23.7TWh/yr](https://kylemcdonald.github.io/ethereum-emissions/) (16.5 to 32 range) for about 6.9MtCO2/yr, according to Kyle McDonald.  
   
 Doubling the carbon footprint to account for embedded emissions would put Bitcoin between Zimbabwe and Thailand. It would put Ethereum between Uruguay and Yemen, but it is likely that this would be an over-estimate, since GPUs are likely to have a somewhat longer economic life.  
   
 Note the hockey-stick on these graphs. I [wrote](https://blog.dshr.org/2021/10/cryptocurrencys-carbon-footprint.html):  
 
>  In 2017 Facebook and Google changed their capex footprint disclosure practice, resulting in an increase of 7x for Google and 12x for Facebook. It is safe to assume that neither would have done this had they believed the new practice greatly over-estimated the footprint. 

 If Google and Facebook are correctly measuring their capex emissions, and if they are representative of miners' capex emssions, cryptocurrencies' carbon footprints are vastly more than double that from their opex emssions alone.
2. And lobbying. See, for example, the way the [climate aspects of "Build Back Better" were crippled](https://www.politico.com/news/2021/11/20/manchin-coal-plant-enrich-west-virginia-523095) to facilitate the plant that is the sole customer of the company that pays Joe Manchin $500K/year transitioning to burning Manchin's waste coal to mine cryptocurrency.
3. Sweden's regulators make this point in an [open letter to the EU](https://www.fi.se/en/published/presentations/2021/crypto-assets-are-a-threat-to-the-climate-transition--energy-intensive-mining-should-be-banned/):  
 
>  Sweden needs the renewable energy targeted by crypto-asset producers for the climate transition of our essential services, and increased use by miners threatens our ability to meet the Paris Agreement. Energy-intensive mining of crypto-assets should therefore be prohibited. This is the conclusion of the director generals of both the Swedish Financial Supervisory Authority and the Swedish Environmental Protection Agency. 

 And the Norwegians [agree](https://www.euronews.com/next/2021/11/17/norway-could-back-european-bitcoin-mining-ban-as-minister-calls-energy-use-difficult-to-ju).
4. [Makarov and Schoar](https://www.nber.org/papers/w29396) write:  
 
>  We show that the balances held at intermediaries have been steadily increasing since 2014. By the end of 2020 it is equal to 5.5 million bitcoins, roughly one-third of Bitcoin in circulation. In contrast, individual investors collectively control 8.5 million bitcoins by the end of 2020. The individual holdings are still highly concentrated: the top 1000 investors control about 3 million BTC and the top 10,000 investors own around 5 million bitcoins.
5. Five years after Ethereum Classic became the remainder of the vulnerable currency, the [result was](https://www.motherjones.com/politics/2021/11/who-goes-crypto-eth-bitcoin-etc-financialization-gamestop-class-wealth/):  
 
>  from the beginning of March to the beginning of May, the value of Ethereum Classic had shot up by over 1,000 percent. It jumped from about $12 a token to over $130.
6. David Gerard provides a comprehensive overview of the latest ["regulatory clarity"](https://davidgerard.co.uk/blockchain/2021/11/24/regulatory-clarity-extreme-edition-anti-money-laundering-and-crypto-fatf-ofac-fincen/) on cryptocurrencies from the international and US government agencies:  

	* The [Financial Action Task Force](https://en.wikipedia.org/wiki/Financial_Action_Task_Force) issued [*Updated Guidance for a Risk-Based Approach for Virtual Assets and Virtual Asset Service Providers*](https://www.fatf-gafi.org/media/fatf/documents/recommendations/Updated-Guidance-VA-VASP.pdf). [Gerard writes](https://davidgerard.co.uk/blockchain/2021/11/24/regulatory-clarity-extreme-edition-anti-money-laundering-and-crypto-fatf-ofac-fincen/)  
	 
	>  The October 2021 revision is to clarify definitions, give guidance on stablecoins, note the issues of peer-to-peer transactions, and clarify the travel rule, which requires VASPs to collect and pass on information about their customers.  
	>    
	>  VASPs include crypto exchanges, crypto transfer services, crypto custody and financial services around crypto asset issuance (e.g., ICOs). VASPs must do full Know-Your-Customer (KYC), just like any other financial institution. 
	
	 As regard peer-to-peer transactions, [Gerard writes](https://davidgerard.co.uk/blockchain/2021/11/24/regulatory-clarity-extreme-edition-anti-money-laundering-and-crypto-fatf-ofac-fincen/):  
	 
	>  Jurisdictions should assess the local risks from peer-to-peer transactions, and possibly adopt optional provisions, such as restricting direct deposit of cryptos with VASPs (paragraphs 105 and 106) — [Germany](https://davidgerard.co.uk/blockchain/2021/07/03/news-binance-vs-the-world-vaneck-etf-robinhood-fined-africrypt-ponzi-mass-ransomware-attack/) and [Switzerland](https://davidgerard.co.uk/blockchain/2020/11/29/news-defi-pickled-binance-sues-forbes-crypto-ponzi-via-underwater-scooter/) have already considered such rules.
	* The US [Office of Foreign Assets Control](https://en.wikipedia.org/wiki/Office_of_Foreign_Assets_Control)'s [*Sanctions Compliance Guidance for the Virtual Currency Industry*](https://home.treasury.gov/system/files/126/virtual_currency_guidance_brochure.pdf) explains that:  
	 
	>  Members of the virtual currency industry are responsible for ensuring that they do not engage, directly or indirectly, in transactions prohibited by OFAC sanctions, such as dealings with blocked persons or property, or engaging in prohibited trade- or investment-related transactions. 
	
	 In particular, US miners are required to blacklist wallets suspected of being owned by sanctioned entities. [Gerard writes](https://davidgerard.co.uk/blockchain/2021/11/24/regulatory-clarity-extreme-edition-anti-money-laundering-and-crypto-fatf-ofac-fincen/):  
	 
	>  Sanctions are strict liability — you can be held liable even if you didn’t know you were dealing with a sanctioned entity. Penalties can be severe, but OFAC recommends voluntary self-disclosure in case of errors, and this can mitigate penalties. You will be expected to correct the root cause of the violations.
	* The US [Financial Crimes Enforcement Network](https://en.wikipedia.org/wiki/Financial_Crimes_Enforcement_Network) issued [*Advisory on Ransomware and the Use of the Financial System to Facilitate Ransom Payments*](https://www.fincen.gov/sites/default/files/advisory/2021-11-08/FinCEN%20Ransomware%20Advisory_FINAL_508_.pdf). [Gerard writes](https://davidgerard.co.uk/blockchain/2021/11/24/regulatory-clarity-extreme-edition-anti-money-laundering-and-crypto-fatf-ofac-fincen/):  
	 
	>  Insurers and and “digital forensic and incident response” companies have been getting more directly involved in ransomware payments — even paying out the ransoms. FinCEN expects such companies to: (a) register as money transmitters; (b) stop doing this.  
	>    
	>  A lot of ransomware gangs are sanctioned groups or individuals. Payments to them are sanctions violations. 
	
	 The Federal Reserve, the FDIC and the OCC have joined the party with a [*Joint Statement on Crypto-Asset Policy Sprint Initiative and Next Steps*](https://www.federalreserve.gov/newsevents/pressreleases/files/bcreg20211123a1.pdf). They:  
	 
	>  plan to provide greater clarity on whether certain activities related to crypto-assets conducted by banking organisations are legally permissible, and expectations for safety and soundness, consumer protection, and compliance with existing laws and regulations
7. In [*Really stupid “smart contract” bug let hackers steal $31 million in digital coin*](https://arstechnica.com/information-technology/2021/12/hackers-drain-31-million-from-cryptocurrency-service-monox-finance/), Dan Goodin reports that:  
 
>  blockchain-analysis company Elliptic said so-called DeFi protocols have lost $12 billion to date due to theft and fraud. Losses in the first roughly 10 months of this year reached $10.5 billion, up from $1.5 billion in 2020. 

 That is ~5% of the $237B locked up in DeFi.
8. [![](https://1.bp.blogspot.com/-9BHvnzNvwNg/YXm2rqJ8hiI/AAAAAAAAGlE/dGOCRkUl3dkWYABw4OMAFMrxbg5IgjSZwCLcBGAsYHQ/w200-h196/bitcoin-20420-peak.png)](https://1.bp.blogspot.com/-9BHvnzNvwNg/YXm2rqJ8hiI/AAAAAAAAGlE/dGOCRkUl3dkWYABw4OMAFMrxbg5IgjSZwCLcBGAsYHQ/s294/bitcoin-20420-peak.png) But the only significant social benefit of cryptocurrencies is rampant speculation, mostly in an enormous Bitcoin futures market using up to [125x leverage](https://www.coalexander.com/post/binance-still-onboarding-fiat-and-offering-50x-to-125x-leverage), based on a Bitcoin-Tether market about one-tenth the size, based on a Bitcoin-USD market about one-tenth the size again. The Bitcoin-Tether market is [highly concentrated](https://www.bloomberg.com/news/articles/2021-10-25/bitcoin-still-concentrated-in-few-hands-study-finds), [easily](https://doi.org/10.1016/j.frl.2021.101982) [manipulated](https://www.sec.gov/rules/sro/cboebzx/2021/34-93559.pdf) and rife with [pump](https://www.coalexander.com/post/the-bitcoin-ponzi-ecosystem)-and-[dump](https://www.coalexander.com/post/tether-and-bitcoin-ponzi-ecosystem-stage-2-down) [schemes](https://davidgerard.co.uk/blockchain/2020/12/18/number-go-up-new-bitcoin-peak-exactly-three-years-after-the-last-whats-happening-here/).  
   
 [*A New Wolf in Town? Pump-and-Dump Manipulation in Cryptocurrency Markets*](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3670714) by Anirudh Dhawan and Tālis J. Putniņš finds:  
 
>  Combining hand-collected data with audited data from a pump-and-dump aggregator, we identify as many as 355 cases of pump-and-dump manipulation within a period of six months on two cryptocurrency exchanges. Up to 23 million individuals are involved in these manipulations. We estimate that the 355 pumps in our sample are associated with approximately $350 million of trading on the manipulation days, and that manipulators extract profits of approximately $6 million from other participants. In all, 197 distinct cryptocurrencies or “coins” are manipulated, which implies that approximately 15% of all coins in our sample of exchanges are targeted by manipulators at least once in the six-month period. There are, on average, two pumps per day. This rate of manipulation is considerably higher than pump-and-dump manipulation in stock markets in recent decades. 

 See also [this post](https://web.archive.org/web/20211119233700/https://www.ezfka.com/2021/11/20/crypto-lending-and-why-you-should-stay-the-fuck-away-from-it/) on the strange fact that:  
 
>  The futures curve for Bitcoin has been permanently upward sloping in Contango pretty much since inception, back in 2017 meaning that the price of the future asset is higher than the spot price of the asset for pretty much 4 years  
>  ...  
>  The implication that this arbitrage opportunity persistently exists and is not hammered by investors until it closes, is that there is some form of market dislocation or systemic credit risk that cannot be properly quantified or hedged. 

 And on Celsius' offer of 17% interest on BTC loans, which clearly indicates a high degree of risk. [Note that](https://www.coindesk.com/business/2021/11/26/celsius-cfo-arrested-on-charges-tied-to-former-job-at-moshe-hogegs-firm/):  
 
>  Yaron Shalem, the chief financial officer of cryptocurrency lending platform Celsius, was one of the [seven people arrested](https://www.coindesk.com/policy/2021/11/18/crypto-heavyweight-moshe-hogeg-reportedly-arrested-in-israel/) in Tel Aviv this month in connection with Israeli crypto mogul Moshe Hogeg
9. Transaction fees make Makarov and Schoar's claim that "transacting in cryptocurrencies and storing them are essentially costless" false. The demand for transactions is variable, but the supply is fixed. Pending transactions bid their fees in a blind auction for inclusion in a block. The result is that when no-one wants to transact fees are low and when everyone does they spike enormously.  
   
 The graph shows that as the Bitcoin "price" spiked to $63K in April the frenzy drove the *average* fee per transaction over $60. User's lack of understanding of transaction fees is illustrated by Jordan Pearson and Jason Koebler's [*‘Buy the Constitution’ Aftermath: Everyone Very Mad, Confused, Losing Lots of Money, Fighting, Crying, Etc.*](https://www.vice.com/en/article/qjb8av/constitutiondao-aftermath-everyone-very-mad-confused-losing-lots-of-money-fighting-crying-etc):  
 
>  The [community of crypto investors](https://www.vice.com/en/article/xgdzbk/group-of-crypto-investors-on-discord-plans-to-buy-copy-of-us-constitution) who tried and [failed to buy](https://www.vice.com/en/article/wxd5z9/chaos-reigns-as-constitutiondao-fails-to-buy-the-constitution) a copy of the U.S. Constitution last week has descended into chaos as people are realizing today that roughly half of the donors will have the majority of their investment wiped out by cryptocurrency fees. 

 Apparently, fees averaged $50/transaction, and the $40M raised paid about $1M in fees. That is 2.5%, very similar to the "extortionate" fees charged by credit card companies that cryptocurrency enthusiasts routinely decry.   
   

|  |
| --- |
| [Source](https://cryptonews.com/news/vitalik-buterin-proposes-new-eip-to-tackle-ethereums-sky-high-gas-fees.htm) |

 Vitalik Buterin has a proposal that attempts to paper over the fundamental problem of fixed supply and variable demand, as Ruholamin Haqshanas reports in [*Vitalik Buterin Proposes New EIP to Tackle Ethereum’s Sky-High Gas Fees*](https://cryptonews.com/news/vitalik-buterin-proposes-new-eip-to-tackle-ethereums-sky-high-gas-fees.htm):  
 
>  Vitalik Buterin has put forward a new Ethereum Improvement Proposal (EIP) that aims to tackle the network's gas fee problems by adding a limit on the total transaction calldata, which would, in turn, should reduce transaction gas cost.  
>    
>  Since Ethereum can only process 15 transactions per second, gas fees tend to spike at times of network congestion. On November 9, the average transaction network fee reached USD 62 per transaction. As of now, Ethereum transactions cost around USD 44,
10. With the Taproot soft fork, explained in [*WHY YOU SHOULD CARE ABOUT TAPROOT, THE NEXT MAJOR BITCOIN UPGRADE*](https://bitcoinmagazine.com/technical/short-bitcoin-taproot-explainer), Bitcoin is making transactions slightly more difficult to trace, but still not offering the anonymity of Monero: 
>  The Taproot upgrade improves this logic by introducing [Merklelized Abstract Syntax Trees (MAST)](https://bitcointechtalk.com/what-is-a-bitcoin-merklized-abstract-syntax-tree-mast-33fdf2da5e2f?gi=e2f23abd01b6), a structure that ultimately allows Bitcoin to achieve the goal of only revealing the contract's specific spending condition that was used.  
>    
>  There are two main possibilities for complex Taproot spending: a consensual, mutually-agreed condition; or a fallback, specific condition. For instance, if a multisignature address owned by multiple people wants to spend some funds programmatically, they could set up one spending condition in which all of them agree to spend the funds or fallback states in case they can't reach a consensus.  
>    
>  If the condition everyone agrees on is used, Taproot allows it to be turned into a single signature. Therefore, the Bitcoin network wouldn't even know there was a contract being used in the first place, significantly increasing the privacy of all of the owners of the multisignature address.  
>    
>  However, if a mutual consensus isn't reached and one party spends the funds using any of the fallback methods, Taproot only reveals that specific method. As the introduction of P2SH increased the receiver's privacy by making all outputs look identical — just a hash — Taproot will increase the sender's privacy by restricting the amount of information broadcast to the network.  
>    
>  Even if you don't use complex wallet functionality like multisignature or Lightning, improving their privacy also improves yours, as it makes chain surveillance more difficult and increases the broader Bitcoin network anonymity set.
11. Whales can't get the face value of their HODL-ings. Last Friday the price crashed 20% in minutes. [David Gerard writes](https://davidgerard.co.uk/blockchain/2021/12/04/news-square-goes-block-wikipedia-nft-el-salvador-bitcoin-city-plans-where-the-chinese-mining-rigs-went/):  
 
>  Someone sold 1,500 BTC, and that triggered a cascade of sales of burnt margin-traders’ collateral of another 4,000 BTC. The Tether peg broke too. 

 That is 0.03% of the stock of BTC. [Gerard writes](https://davidgerard.co.uk/blockchain/2021/12/04/news-square-goes-block-wikipedia-nft-el-salvador-bitcoin-city-plans-where-the-chinese-mining-rigs-went/):  
 
>  The real story is that the whales — “large institutional trading firms,” ... want (or need) to realise the face value of their bitcoins, and they can’t, because there just aren’t enough actual dollars in the market. This is the same reason miners are keeping a “stockpile” of unsaleable bitcoins, as I’ve noted previously.  
>    
>  So the whales are going to Goldman Sachs to ask for a loan backed by their unsaleable bitcoins, even though the collateral can’t possibly cover for the value of the loan even if Bitcoin doesn’t crash. 

 HODL-ers wishing to cash out face significant problems, as recounted by Harry Brennan in Harry Brennan's [*‘I made $4m profit on crypto, but the bank won’t let me spend it’*](https://archive.is/J7x85):  
 
>  Digital currency traders sitting on huge gains have been turned away by banks, with financial institutions fearing they may be unwittingly taking money from law breakers who use digital currencies to hide wealth illegally.  
>  ...  
>  Clive Gawthorpe of accountant UHY Hacker Young said traders face long waits of up to 24 months to access their own money, with tax an increasing concern for banks. “Every time they trade in and out of a coin they trigger a taxable event, some dating back years – and we are talking about thousands of transactions without proper record keeping,” he said
12. Here is a list of institutions that a real-world user of cryptocurrencies as they actually exist cannot avoid trusting:  

	* The owners and operators of the dominant mining pools not to collude.
	* The operators of the exchanges not to manipulate the markets or to commit fraud.
	* The core developers of the blockchain software not to write bugs.
	* The developers of your wallet software not to write bugs.
	* The developers of the exchanges not to write bugs. And, if your cryptocurrency has Ethereum-like "smart contracts":  

	* The developers of your "smart contracts" not to write bugs.
	* The owners of the smart contracts to keep their secret key secret. Every one of these has examples where trust was misplaced.
13. In the medium term, Bitcoin and many other cryptocurrencies face two technological threats that might disrupt them and thus provide partial mitigation:  

|  |
| --- |
| [Source](https://www.quantumcryptopocalypse.com/quantum-moores-law/) |

	* **Quantum computing**. [*Quantum attacks on Bitcoin, and how to protect against them*](https://arxiv.org/abs/1710.10377) by Divesh Aggarwal *et al* describes two threats they pose in principle:  
	
		+ They can out-perform existing ASICs at Proof-of-Work, but it is likely to be many years before this threat is real.
		+ They can use [Shor's algorithm](https://en.wikipedia.org/wiki/Shor's_algorithm) to break the encryption used for cryptocurrency wallets, allowing massive theft. Aggarwal *et al* track the [likely date for this](https://www.quantumcryptopocalypse.com/quantum-moores-law/), currently projecting between 2029 and 2044. When it happens there will be an estimated [4.6 million Bitcoins up for grabs](https://blog.dshr.org/2021/11/the-65b-prize.html).
	* **The halvening**. At regular intervals Bitcoin's mining rewards are halved, with the goal that the currency eventually become fee-only. Alas, [Raphael Auer](https://www.bis.org/publ/work765.pdf) shows that a fee-only system is insecure.

###### 33 comments:

   I know the talk was on mitigating externalities, but you do touch on a number of other areas and one thing you could add is a slide on the origin of money and why crypto is not a currency. The late David Graeber wrote a great book on debt, which posits money represents debt ownership. 

    Sir, right off the top you lead with some dubious info.  
  
The ewaste paper is generally discredited because of incorrect lifetime estimates.  
25% of mining is still done by a 5 yo model (S9).  
https://compassmining.io/education/bitcoin-hashrate-percentage-s9-asic/  
  
For the energy FUD I refer you to the fine work of Nic Carter.  
https://niccarter.info  
  
Also the miningpool / 50% FUD is a fundamental misunderstanding of how mining pools work.  
As a miner, it would only take me seconds to remove my hashrate from a bad pool, and advancements like stratum V2 make these attacks impractical.   
https://braiins.com/stratum-v2  
  
  
 

    jerdavis, I see you rely on sources who are "talking their book". I prefer not to. 

    David,  
  
Fan of your work (as well as long time user of X11). :-) Thank you for sharing this talk with us.  
  
In this sentence:  
  
>And 75% of those are transactions between exchanges, so only 2.5% of the "transactions" are real blockchain-based transfers involving individuals.  
  
Did you mean "25%" instead of "2.5%"?  
  
Thank you,  
  
Ed 

    Thanks for the comprehensive information on CryptoCurrencies. This is for keeps.  
  
I feel that what has happened with Bitcoin specifically (since the stated intentions were noble) is a classic example of power law.   
It is really ironic in certain ways, that while Bitcoin was supposed to defeat concentration of power, it has led to much more damage in that department.   
  
I am however interested to know what your thoughts are on Blockchain as a data structure (going beyond the cryptocurrency) and its application in decentralisation of information/power(?).   
  
I still feel that it has many applications, without the 'proofs of x'.   
Could you kindly point me to information (other than your excellent blog) which I can deep dive into?   
  
 

    @ jerdavis  
  
Anyone who comes here thinking blurting out cult-lingo such as "FUD" comprises a rebuttal to this presentation is standing in front of the jury with their fly conspicuously down.  
  
Unplug from your MLM scheme's alien parlance, take a breather, and then try again. 

    David, thanks for sharing your presentation. It did leave me wondering... have you examined in depth any other implementations of Proof of Stake beyond Ethereum's? Because the criticism you aim at Ethereum's model doesn't occur in the same way on Cardano('s Ouroboros) which: limits rewards as pools stake (incl delegated) become too high / pool becomes saturated; doesn't require 32 ETH to run a validator; supports customizable network parameters for future-adaptability [1], such as the point of saturation; easily accommodates hard forks (using the hard fork combinator) to evolve the network's capability without forking the ledger's history. Staking occurs without relinquishing control of funds nor slashing. It operates with decentralised validators (pools) that run on low energy consumption, some even on raspberry pi's [2]. It's currently developing scaling solutions (Hydra) [3], following an incremental rollout model that have allowed multiple iterations already [4].  
  
You mentioned in your post "Alternatives To Proof-of-Work" that Cardano isn't very successful. By which metric? It has achieved #3 spot in marketcap several times (sitting currently at #6 yet is the highest marketcap for a PoS chain) and albeit imperfect, it's more capable of change than the usual suspects, BTC and ETH.   
Some of these points address a big part of the criticism of PoS you've mentioned/quoted in previous articles. It doesn't claim to be fully decentralised in all senses of the word, as some aspects of its development are centralised in a number of actors in an opensource model. [5]  
  
https://adapools.org/groups for an overview of the network.  
  
There's also extensive formal research around mitigation of adversarial behavior [6] and more relevant topics [7].  
  
Would be keen on hearing your deeper analysis on Cardano's PoS model, despite being aware it isn't perfect nor does it address some of the other criticism you raised in cryptocurrencies in general. I searched your articles and only found faint mentions of the project, apologies if I missed it. And yes. I hold ADA, so I'm talking my book. However, I tried to present fair technical arguments for furthering technical discussions.  
  
Cheers.   
  
[1] https://adapools.org/params  
[2] https://berrypool.io/  
[3] https://youtu.be/dJk5\_kB3BM4  
[4] https://roadmap.cardano.org/en/  
[5] https://cardano.org/discover-cardano#people  
[6] https://iohk.io/en/research/library/papers/consensus-reduxdistributed-ledgers-in-the-face-of-adversarial-supremacy/  
[7] https://iohk.io/en/research/library/ 

    If we just call the crypto space "entertainment" then I suppose the carbon foot print would be acceptable? I don't hear such aggressive 'footprint' arguments regarding the entertainment industry, gambling, sports, streaming video/TV, social media, etc. 

    Is there anything that prevent states from simply declaring not just mining but also transactions illegal, or that would make such law ineffective ? I mean, it wouldn't stop crime and black market, but impact all the current legal business part. 

    That was a fairly reasonable assessment of the current state of things. I'd like to respond to a few points.  
  
Number go up - It is widely understood that first layer BTC is unsuitable as a global transactional system, and the primary reason to own BTC is long term store of value. In this regard, the actual bar to clear here is not "number go up", but rather, "number not go down over the long term." On that account, so far, so good. Although still very high, volatility has been continually decreasing over time. It is plausible that over the very long term, it can become an asset stable in purchasing power. While not nearly as exciting as an asset that can rise 10000% in a year, a stable asset is still eminently useful. It remains to be seen how much market share it will poach from gold in the long run, as there are still significant tradeoffs between them.   
  
Resilience - Although large mining pools represent a \*risk\* to Bitcoin, there is no evidence of failure. A 51% attack presents temporary risks to txs, but not to the underlying integrity of balances stored on chain/nodes. The amount of mining power required to reverse txs scales with the amount of time since the tx was made. With 51% attacks being so costly to execute on BTC, it would only be a viable tactic for reversing extremely large txs. For large txs, speed is rarely of the essence, and any attack would be easily mitigated by waiting for more confirmations. The amount of txs for which an attack is viable is very small, evidence of an attack would be very obvious by reduced block time while hashpower is diverted to an alternative chain, and mitigation for those edge cases is simple. It's an attack that's trivially easy to see coming and sidestep it. There is no evidence that a 51% attack on a large BTC tx has ever even been attempted, and the simplest explanation is because it would certainly fail. If it was a viable attack vector we would have already seen attacks, as we have on smaller blockchains.  
  
Energy waste - To this point, if you do not see the long term value in the asset, then \*any\* amount of energy expenditure is too much. While BTC's energy usage is significant, energy is generally a free market and by that definition, whether the energy usage is "worth it" is simply defined by whether someone is willing to pay for it. If BTC does devalues over time, energy usage will be reduced as miners shut down, and the problem will solve itself. Likewise, if BTC continues to grow in value because people voluntarily choose to purchase it and mine it, it is de facto "worth it" to those who are engaging with the asset. There is no "shortage" of energy - there is a simply a finite amount of energy produced, and it is generally distributed to whomever is willing to pay the most for it. Markets are the most effective way to determine what a society values. The externalities here are associated with energy production, \*not\* consumption. If the world wants to reduce carbon output by taxation or regulation, it can only be effectively regulated at the supply side, not the demand side. Energy consumption is what separates us from cavemen - the problem humanity needs to solve to flourish is not how to reduce energy consumption, but how to produce energy in a less environmentally harmful way. I remain optimistic that human ingenuity will solve this problem in the long run.  
  
Overall, I agree on the lack of viability for all other cryptos. While blockchains disrupt intermediaries that extract economic rent, they also removes the protective role that intermediary plays. The overall cost of is considerable and simply not worth it for most use cases, and it will not take forever for the world to come to realize that. But it remains to be seen if a digital SoV can replace gold - such an asset does not need to scale in tx capacity, but in mkt cap and liquidity. In that regard, BTC is scaling effectively. 

    Want expecting this kind of response from you sir. Aren't you technically talking your implicitly short book also? I thought we were evaluating arguments on merits. If you flat-out discount arguments based on speaker's book, you'll only accept very one-sided takes. 

    andr3: thanks - [*Alternatives To Proof-of-Work*](https://blog.dshr.org/2021/07/alternatives-to-proof-of-work.html) needs an update - a lot has happened since last July.  
  
Jay Todd: Entertainment's externalities do include a significant carbon footprint, but they don't include a massive crime wave.  
  
Takeljoe: States can prevent transactions but it would be a lot of work, see [*Unstoppable Code?*](https://blog.dshr.org/2021/06/unstoppable-code.html). They can ban banks from facilitating transactions, which is easier and breaks the link to fiat that is needed to ensure "number go up".  
  
Wayo: 90% of "transactions" are not "economically meaningful". 75% of the rest are between exchanges. What does that leave?  
  
dmoroz: EE380 talks normally end up on YouTube after a while. 

    Hi David,  
Thanks for sharing your talk. It has given me some good points to consider.   
  
In reply to another commenter, jerdavis, you mentioned that you prefer not to rely on sources that talk their book.   
  
At first that seemed reasonable to me.   
  
Then I started to question who would would be well educated on crypto, willing to make points in favor/defense of it, and not be invested?  
  
Many of the people that would be most qualified to present additional information would be "talking their book". By discounting anyone that falls into that group, it seems to me that you conveniently get to throw out arguments without addressing them. Is this a poor take on my part?  
  
I only started looking into crypto/web3 about 8 months ago and I'm finding it difficult to get a balanced view.   
  
Here I read your take on some aspects of crypto.   
Someone else pointed out information that contradicts some of your claims.  
Saying they are talking their book doesn't explain what is incorrect, if anything, about the new assertions being presented.   
  
I'm left as lost as if I never read this post at all. 

    I'm glad I found this blog. Thank you for collecting all these in one place. I need to reach out because there's a lot we have to talk about.  
  
The idea of smart contracts is great, but the underlying architecture is awful. A lot of the problems in Web3 have to do with blockchain. It just doesn't scale, so Bitcoin failed at being a "peer to peer cash system" and became a "store of value". Meanwhile, Ethereum the "world computer" has tremendously high fees as soon as any app becomes popular. Even "scaling solutions" like Polygon can easily be flooded with transactions (like Sunflower game did four weeks ago) when transactions are cheap. This is not to mention that everyone has to store everything (sharding aside), so the economics of storage need to be cleaned up from "just store this forever".  
  
At Intercoin, we're working to fix pretty much all the problems in the space, gradually. Smart contracts should be replaced with factories (so people can trust the code again). Blockchains have to be replaced with "embarassingly parallel" distributed systems. We're building Intercloud to replace Blockchain. But in the meantime, we are building on EVM-compatible chains.  
  
https://community.intercoin.org/t/web3-moxie-signal-telegram-and-why-decentralization-matters  
  
https://community.intercoin.org/t/who-pays-for-storage-nfts-and-other-digital-content-in-2022  
  
About Bitcoin and Proof of Work, I have a more dire prediction: https://news.ycombinator.com/item?id=26220992  
  
Would you be interested in connecting to discuss this at more length? 

    There's quite a bit of one-sidedness and presumptions about why any of bitcoin exists. However, just about everything you need to know where David's head is at appear clear in just this quote: "...stopped doing this because the larger Bitcoin community objects to the idea of attempting to restrict Bitcoin to legal uses!"  
  
Exclamation and all, as if freedom of currency from government control isn't the entire point. The current alternatives are junk, as David points out. Proof of work is so far the only functioning system that is proving it cannot be stopped trivially or by a few small players, or by government at this time.  
  
What is interesting also, that "government can stop bitcoin" is completely unproven, and in fact, the opposite appears to be occurring. There is the reality of arbitrage, and the the game theory here is quite a bit more advanced than "the USA can just use enough compute power to overrun bitcoin"... There is also the reality that the 'government' at least in free nations, is literally "us", and there are plenty that are willing to fight for what a system like bitcoin provides. 

    Julian Lee's [*The World Has Been Using A Lot More Oil Than We Thought*](https://www.bloomberg.com/opinion/articles/2022-02-13/the-world-has-been-using-a-lot-more-oil-than-we-thought) adds to the evidence that the world is short of energy with some scary graphs:  
  
"Remember all that missing oil I wrote about last month? The discrepancy between where stockpiles ought to be (based on implied supply and demand balances) and the volumes that had actually been reported or measured?   
  
Well, those barrels are missing no more. As I feared, it turns out they’ve already been used up — in the refineries and petrochemicals plants of China and Saudi Arabia. That means oil balances are a lot tighter than the International Energy Agency previously thought.  
  
The group published its latest monthly report on Friday, revising its historical oil demand numbers all the way back to 2007. Yes, that’s right, for the past 15 years the world has been using more oil than the primary monitoring agency that advises consumer governments thought." 

    Allyson Versprille's [*Treasury Signals Crypto Miners Won’t Face IRS Reporting Rule*](https://www.bloomberg.com/news/articles/2022-02-11/treasury-signals-crypto-miners-won-t-face-irs-reporting-rules) reports that:  
  
"Treasury Assistant Secretary for Legislative Affairs Jonathan Davidson said the department’s view is that “ancillary parties who cannot get access to information that is useful to the IRS are not intended to be captured by the reporting requirements for brokers.” That language signals that people who use mining or staking to validate crypto transactions, as well as software and hardware providers, will be able to avoid the demands."  
  
Note that this applies to miners, not the pools. But the pools are likely outside US jurisdiction. 

    "It only took six years for Bitcoin to fail Nakamto's goal of decentralization, with one mining pool controlling more than half the mining power... Although the techniques used to implement decentralization are effective in theory, at scale emergent economic effects render them ineffective... the systems are not actually decentralized"  
  
Bitcoin remains decentralized. Empirically, Bitcoin has proved to be resistant to miner attacks. Despite the miner centralization you observe, Bitcoin has continued to operate without issue. Miner attacks take the form of re-orgs and censorship. These attacks are detectable, and Bitcoin remains healthy.  
  
If such attacks \*are\* detected, Bitcoin is not without recourse. The social-consensus layer can react to them.  
  
The Bitcoin protocol does not exist in a human-free vacuum. Social consensus is \*always\* a layer on top of what a protocol defines. The Raphael Auer paper you link makes this point: "Whether or not moving beyond pure-proof-of-work will require overarching coordination, it is noteworthy that much has already been done to protect Bitcoin and other cryptocurrencies beyond just applying the rule to follow the longest chain... [examples...] These three episodes, and others like them, show that social coordination has to be a key element of smoothly functioning cryptocurrencies."  
  
The cost to attempt a 51% attack is immense. If successful, miners would devalue both their ill-gotten gains \*and\* their mining hardware — but success is unlikely, since a social-consensus-layer fork would likely render their expense pointless. Eventually, any cost-sensitive attacker will go bankrupt.  
  
(An adversary that is \*not\* cost-sensitive could be formidable. However, this could really only be governments. Such an attack gets less likely as Bitcoin becomes more popular, since it requires essentially attacking voters' portfolios.)  
  
The culture of network participants running their own full nodes is absolutely vital. It's the economic majority of full nodes that determines the rules, not the miners. Back in 2015, a majority of miners wanted 8mb blocks, yet here we are with 1mb blocks. This dynamic is simply impossible on a permissioned blockchain.  
  
For example, when announcing Bitcoin, Satoshi commented: "The central bank must be trusted not to debase the currency, but the history of fiat currencies is full of breaches of that trust."  
  
The idea that Bitcoin offers no further protection against unilateral debasement, compared to a permissioned blockchain, is simply wrong.  
  
(Note: I \*do\* agree that Bitcoin has negative environmental externalities. Governments should regulate electricity and hardware production so that their costs capture those externalities.) 

    These are great details. But as a digital preservationist, I'm kind of surprised you missed this headline: for all the HODLing talk, all of today's Bitcoin and NFTs will go public domain in 10-15 years. This is due to the exponential growth of quantum computing and its impact on the blockchain's public key cryptography (RSA2048) foundations (https://www.sciencedirect.com/science/article/pii/S2590005621000138).  
  
Unless/until there's a major technology migration scheme for all crypto, the fuse is already lit. If you were already thinking blockchain was a Ponzi scheme, crypto asset owners will need to pawn off all of their assets to some poor sap by 2035 or risk losing everything. 

    I have been following up Chia closely and your brief discrediting of it as a failed technology is IMHO quite shallow and based on FUD.  
  
Yes, there was an initial craze caused by hype and greed. Those who dumped vast amounts of cash into plotting hardware were burned, and the price of the coin corrected to discourage buying hardware for farming. There are loads of others who have unused hardware sitting around, ready to farm, and you can't expect a quick ROI when you're competing with "basically zero cost basis to participate except electricity" folks.  
  
"The way" to farm Chia is to utilize otherwise unused resources. Old hard drives, unprovisioned storage, and so on. I have plotted almost 100 TB on an old 512GB Samsung SSD and on a commodity PC. The SSD is still working fine. If you look more closely, the news of widespread SSD failures died out. Why? Because it's not happening. It's FUD.  
  
The network space stabilized at around 30-35 EiB. Chia has a ridiculously high full node count (around 250K, IIRC). Another big deal for decentralization is that individual farmers are making blocks even when they are pooling.  
  
Ecosystem wise, we've seen a release of CATs (ERC-20 equivalent), peer-to-peer atomic trading offers and a couple of decentralized exchanges kicking off based on the trading offers.  
  
So, technology failure? I don't think so. 

    Your analysis is spot on.  
  
Although there is one final option that you did not consider:  
  
Externalities exist, and decentralization is a myth, however the externalities are temporary, and caused by the fact that the primary driver of cryptocurrencies is speculation. If speculation becomes less of the driving factor, and a more natural commodities based supply/demand curve were to dominate, then the externalities may also diminish.  
  
This is what I believe will happen with a PoW system based on the original bitcoin protocol such as BSV will achieve. 

    "Libertarianism's attraction is based on ignoring externalities, and cryptocurrencies are no exception." I am interested in this connection you make between libertarianism and externalities. Do libertarian principles lead to externalities? The problem I can see with libertarianism is that prioritizing individual rights shifts the burden of proof. It does not take into account our epistemic limitations in determining externalities. Most externalities are invisible.   
  
To compensate for this, we are taught as children that liberty must go hand in hand with responsibility. I am free to do what I want as long as I act responsibly. Cryptocurrencies were invented to take trust and responsibility out of the equation. Maybe we are learning now that this doesn't work.   
  
But that doesn't mean that decentralization, blockchain, crypto, and smart contracts will go away again. It does mean, though, that we need to learn how to use this technology. You emphasize the dichotomy between permissioned and permissionless blockchains. Could there be a space in between the two to be filled with various designs? 

    While I have some quibbles, much truth here. Though at the same time there is a "pony" to be found in the shitpile that is current cryptocoins and NFTs. I'm looking into a possible way to mining with positive rather than negative externalities. Proof of Waste, which is what Proof of Work is, might be possible with positive waste. (Strictly cryptocoins run on proof of luck, but the more work you do, the more luck you get.)  
  
The pony comes from being a low barrier to entry platform for innovation. Just as the internet let anybody try out new ideas in communications and immediately find users (who each paid for their part of the network) the coins let people try out new ideas in trust, transactions, contracts and to some extent money. That's interesting.   
  
NFTs are also a shitshow, but the pony inside is that for a long time the value of art has not been the physical object, but its provenance. Signed number prints are manufactured cheap items but people pay for their provenance. NFTs separate the physical object from the provenance, which again is interesting. 

    In [*The Staggering Ecological Impacts of Computation and the Cloud*](https://thereader.mitpress.mit.edu/the-staggering-ecological-impacts-of-computation-and-the-cloud/), Steven Gonzalez Monserrate documents the environmental impacts of "the cloud":  
  
- Carbon Emissions  
- Water use  
- Noise pollution  
- e-waste  
  
There is no reason to believe that cryptocurrency mining facilities are any better than cloud data centers from an environmental perspective, and many reasons to believe they are worse. 

    ON the surface they are the same (Computation warehouses) In reality, they are quite different.  
1) Mining can shut off in an instant and support electrical grid, cloud computing generally can not.  
2) Bandwidth requirements for mining are quite small, cloud computing is enormous. As a result Mining can locate anywhere and make use of stranded and wasted energy. Recent developments in flare gas mining reduces methane emissions, which is a worse greenhouse gas.  
3) Mining is most often done without HVAC cooling, cloud computing is not.  
4) Noise pollution. Fans certainly are loud, that is correct, but the move to immersion cooling has been a recent development.  
5) e-waste. Again, this is not actually a thing in mining, and is here is an excellent summary of what is fundamentally wrong with the ewaste argument.: https://twitter.com/nic\_\_carter/status/1493341162450698240  
  
I strongly encourage you to reach out to people actually in the industry (though they may "talk their book"). Unfortunately this paper is the all too common result of relying on only what can be found online and not vetting your sources.   
  
 

    A few reasons why mining facilities can be environmentally better than typical cloud data centers:  
  
They tend to be significantly more mobile, as they do not require high levels of data security or internet infrastructure and can be brought online extremely quick. Bandwidth requirements are minimal so there is no need to run obscene amounts of fiber to a typical crypto mine. It is possible to containerize and bring the miners to the source of the energy, as often seen with flare mitigation. It is also possible to run a crypto mine in a highly remote area, with satellite internet bandwidth being more than sufficient. We saw a mass migration of miners out of china to other areas post the china mining ban, and that hashrate was restored within weeks/months. This would have been a dramatically more difficult transition for a typical data center. It is also far easier for a miner to turn on and off at will to capture excess energy from renewable sources that would otherwise be wasted.   
  
It is far far easier for crypto miners to capture stranded or idle capacity than a data center. The extent to which this is actually happening right now is open to debate, but a mining operation is a very different beast from a datacenter and is not subject to many of the same constraints. 

    Most blockchains are very quantum-resistant as designed. They use mostly quantum-resistant symmetric encryption and quantum-resistant hashes with sufficiently large key sizes. The blockchain is fine. It's the asymmetric wallets that are the problem, and as long as they are moved to quantum-resistant cryptography before sufficiently capable quantum computers break traditional asymmetric encryption, then they, too, will be fine. There are some other minor to moderate issues to worry about, wherever quantum-susceptible cryptography exists in the cryptocurrency ecosystems, such as asymmetrically signed control messages sent on control channels and asymmetrically signed client upgrades...but again, as long as they get upgraded to quantum-resistant cryptography ahead of the big break, it's not as threatening as some make it sound. Yes, it's a huge endeavor to get everyone using cryptocurrency to move to the newer quantum-resistant ciphers...and there will be victims...but at least there is a solution and as long as you implement the solution, you'll be safe. BTW, I personally think the coming quantum cryptographic break is much, much closer. I'd be shocked if it doesn't come in 5 years. I even give a 10% chance that it's already happened but we don't know about it. 

    A follow-on, regarding Chia. I think that proof of space and time is quite interesting but have argued much with Bram on a potential serious problem. Just as bitcoin for a time resulted in botnets created to steal CPU time, I fear botnets which want to steal your disk space, which means erasing your disks until you notice. That could cause great harm. CPU stealing botnets ended when even free stolen mining became unproductive, but stolen disk space for farming should always remain productive. Even botnets could either just wipe your disk or wipe only the blocks you do not often access (which is most of them) and we would need to build detectors for that and of course make sure we don't replace backups with wiped blocks. If Chia does not become valuable this won't happen of course. 

    Thanks for the cogent analysis. It took thousands of years for banking systems to develop to the current point, balancing the many competing real work factors. "The Establishment" doesn't work perfectly for everyone, and for some people not well at all, but it does work remarkably well on balance.  
  
New solutions to problems tend to flourish in limited contexts and then, perhaps, over time evolve to work in larger domains. In the cryptocurrency case, though, the domain is sort of inherently "all of economics". 

    Wow! Cory Doctorow has a really great riff on this talk in [*Comprehensive synthesis of the technological, ecological and political critique of blockchainism*](https://pluralistic.net/2022/02/14/externalities/#dshr). Please go read it. 

  
   
 DSHR in ANWR [Full comments](https://blog.dshr.org/feeds/comments/default) * [▼](javascript:void(0))   [2022](https://blog.dshr.org/2022/)  (69)
	+ [▼](javascript:void(0))   [February](https://blog.dshr.org/2022/02/)  (7)
