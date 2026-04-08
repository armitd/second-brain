# APIs in Web3 with The Graph — How It Differs from Web 2.0

![rw-book-cover](https://cdn.thenewstack.io/media/2022/02/8b3d03f4-thegraph.jpg)

## Metadata
- Author: [[Richard MacManus]]
- Full Title: APIs in Web3 with The Graph — How It Differs from Web 2.0
- Category: #articles
- Summary: Richard MacManus Richard is senior editor at The New Stack and writes a weekly column about web and application development trends. Previously he founded ReadWriteWeb in 2003 and built it into one of the world’s most influential blogs. Follow him on Twitter @ricmac.
- URL: https://thenewstack.io/apis-in-web3-with-the-graph-how-it-differs-from-web-2-0/

## Full Document
![Featued image for: APIs in Web3 with The Graph — How It Differs from Web 2.0](https://cdn.thenewstack.io/media/2022/02/8b3d03f4-thegraph-1024x562.jpg)Lead image via The Graph.
One of the stumbling blocks of developing a decentralized application (dApp) is the complexity of querying and using data from a blockchain and other “off-chain” solutions. With dApps, and particularly those running on the Ethereum blockchain, not all of the data is stored on the blockchain. There are often decentralized storage networks involved, like the The InterPlanetary File System (IPFS). Add to that the inherent complexity of blockchains — with their size, “gas fees” and other obstacles — and it makes for a difficult environment for developers to provide an API (application programming interface).

One project aiming to change this situation is [The Graph](https://thegraph.com/en/), described as “an indexing protocol for querying networks like Ethereum and IPFS.” The protocol allows developers to “build and publish open APIs, called subgraphs, making data easily accessible.”

#### Blockchain Data Difficulties

According to [documentation](https://thegraph.com/docs/en/about/introduction/) on The Graph’s website, it is “​​really difficult to read anything other than basic data directly from the blockchain.” One example they cite is the smart contract of the [Bored Ape Yacht Club](https://boredapeyachtclub.com/#/) (BAYC), a popular set of digital ape NFTs on the Ethereum blockchain. It’s relatively easy, according to The Graph, to do “basic read operations on the contract” (who owns a specific ape, and so on), but “more advanced real-world queries and operations like aggregation, search, relationships, and non-trivial filtering are not possible.”

[![bayc code](https://cdn.thenewstack.io/media/2022/02/46a7000a-bayc_code.png)](https://cdn.thenewstack.io/media/2022/02/46a7000a-bayc_code.png)
Essentially, what the Bored Ape Yacht Club puts on the blockchain is the transactional data for its apes. The [smart contract](https://etherscan.io/address/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d#code) is just over 2,000 lines of code, most of which is related to the purchasing and transferring of apes. An [analysis of the code](https://medium.com/northwest-nfts/bored-ape-yacht-club-contract-review-80dce503308e) by [Patrick Price](https://www.linkedin.com/in/patrickpr12/), who runs a software consultancy called Northwest NFTs, notes that the code isn’t entirely original. “Looking around at other NFT contracts, many of them have the same copy-pasted function,” he wrote.

The ape itself — its attributes, its visual appearance, and other data about the digital beast — is [stored on IPFS](https://artforall.io/score/bored-ape-yacht-club/0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d). The BAYC has [a web page](https://boredapeyachtclub.com/#/provenance) that lists “the provenance record of each Bored Ape that will ever exist,” which includes links to IPFS.

#### How Does The Graph Work?

What The Graph is aiming to do is index all of the bored ape data — the smart contract and all of the assets stored on IPFS and elsewhere — and then make that index available to developers. The APIs to this data, called “subgraphs,” can then be queried with a standard GraphQL API.

What each subgraph indexes is defined by a “subgraph manifest.” This file “defines the smart contracts of interest for a subgraph, the events in those contracts to pay attention to, and how to map event data to data that The Graph will store in its database.” The manifest is stored in IPFS.

[![The Graph](https://cdn.thenewstack.io/media/2022/02/c0261fca-thegraph1.png)](https://cdn.thenewstack.io/media/2022/02/c0261fca-thegraph1.png)
Similar to other blockchain projects, there is also a fairly complicated consensus mechanism at play in The Graph protocol. As [described](https://thegraph.com/blog/year-one-web3-renaissance) by [Yaniv Tal](https://www.linkedin.com/in/yanivtal9/), the project lead at The Graph, “Work on The Graph is performed by an open network of participants, including: Indexers, who run the computers that serve data; Curators, who organize data; and Delegators, who add security to the network by staking their tokens.” As at the end of 2021, according to Tal, there were “160 Indexers, 7,400+ Delegators, and 2,200+ Curators live on the network.”

As for the token, GRT, at time of writing it is ranked 53rd in market capitalization by CoinMarketCap.

Currently The Graph mainly supports Ethereum and compatible blockchains, but “Solana, Cosmos, and Polkadot integrations are on the way.” Tal also noted the importance of “access to off-chain data from places like storage networks and peer-to-peer databases,” which are also being worked on.

Up till now, The Graph has mostly focused on building up its Ethereum and IPFS data stores. But there is a lot more data in the wider blockchain world. Clearly, there is significant work to do in order to provide the type of full-featured APIs we’re used to in the Web 2.0 world.

#### Who’s Behind The Graph?

The Graph protocol is being built by a company called [Edge & Node](https://edgeandnode.com/), which Yaniv Tal is the CEO of. [Nader Dabit](https://twitter.com/dabit3), a senior engineer who I interviewed for [a recent post about Web3 architecture](https://thenewstack.io/web3-stack-what-web-2-0-developers-need-to-know/), also works for Edge & Node. The plan for the company seems to be to build products based on The Graph, as well as make investments in the nascent ecosystem.

There’s some serious API DNA in Edge & Node. Three of the founders (including Tal) worked together at MuleSoft, an API developer company acquired by Salesforce in 2018. MuleSoft was founded in 2007, near the height of Web 2.0. Readers familiar with that era may also recall that MuleSoft acquired the popular API-focused blog, [ProgrammableWeb](https://www.programmableweb.com/), in 2013.

Even though none of the Edge & Node founders were executives at MuleSoft, it’s interesting that there is a thread connecting the Web 2.0 API world and what Edge & Node hopes to build in Web3.

#### APIs the Web3 Way

There are a lot of technical challenges for the team behind The Graph protocol — not least of all trying to scale to accommodate multiple different blockchain platforms. Also, the “off-chain” data ecosystem is complex and it’s not clear how compatible different storage solutions are to each other.

But I like the approach of using a protocol to try to bring APIs into the emerging Web3 world. In his end-of-year post, Tal described crypto protocols as “a new organizational structure that allow large numbers of people to coordinate anywhere in the world.” At least in theory, this means that a corporation (like, say, MuleSoft) does not have to be the middleman between an API developer and a consumer of that API. With The Graph and its cryptocurrency token, there are financial incentives for people to run an open protocol so that middleware isn’t needed.

However, as with any other blockchain technology at this point in time, it remains to be seen whether The Graph can become as influential in Web3 as MuleSoft was in Web 2.0.
