# https://cointelegraph.com/explained/erc-20-tokens-explained

![rw-book-cover](https://images.cointelegraph.com/cdn-cgi/image/format=auto,onerror=redirect,quality=90,width=1200/https://s3.cointelegraph.com/storage/uploads/view/4e35cadc379780ec66fd391edef59fb0.jpg)

## Metadata
- Author: [[Maxwell William]]
- Full Title: https://cointelegraph.com/explained/erc-20-tokens-explained
- Category: #articles
- Summary: ERC-20 tokens are tokens that are created and used exclusively on the Ethereum platform. They follow a set of standards that allow them to be shared, exchanged, and transferred. The Ethereum community has established three optional rules and six mandatory rules for ERC-20 tokens, including rules for the total supply, balance, transfer, and approval of tokens. ERC-20 tokens are used in decentralized applications (DApps) built on the Ethereum blockchain and can serve various purposes, such as currency, shares, loyalty points, or proof of ownership. Smart contracts are used to create and facilitate transactions of ERC-20 tokens.
- URL: https://cointelegraph.com/explained/erc-20-tokens-explained

## Full Document
####  Enough hypotheticals, what’s a real-world example?

*Every token on the Ethereum platform is an ERC-20 token.*

It is [numbering](https://etherscan.io/tokens) 82815 at press time, let’s take a look at some of them.

[EOS](https://eos.io/) (EOS), currently the [5th](https://coinmarketcap.com/currencies/eos/) biggest cryptocurrency with almost $12 billion in market cap, is attempting to build a network that can utilize inter-blockchain communication and is

[TRON](https://tron.network/enindex.html) (TRX) is [ranked](https://coinmarketcap.com/currencies/tron/) 10th among all the cryptocurrencies at the time of writing, and is described as a ‘open-source protocol for the digital entertainment industry.’ It aims to launch a content platform with ecosystem connecting all people creating different kinds of content.

An ‘enterprise level public blockchain platform’ [VeChain](https://www.vechain.org/) (VEN), the [15th](https://coinmarketcap.com/currencies/vechain/) cryptocurrency in terms of market cap, is planning to implement Internet of Things (IoT) technology to provide private keys for each product that make it possible to track them.

####  Are there any problems with ERC-20?

*ERC-20 is not perfect.*

There are some issues that the ERC-20 token standards do not address.

There are situations that tokens might be unintentionally destroyed when they are used as payment for a smart contract rather than using Ether. An [estimated](https://github.com/Dexaran/ERC223-token-standard) $3 million has been lost because of this.

To fix this bug, the Ethereum community is currently working on a new standard

named [ERC-223](https://medium.com/cryptomover/what-are-erc20-and-erc223-tokens-307badcca5a). These standards are not compatible with ERC-20, however, so developers are encouraged to continue using ERC-20 until compatibility is realized.

In April 2018, a number of exchanges [suspended](https://cointelegraph.com/news/multiple-exchanges-suspend-erc20-token-trading-due-to-potential-batchoverflow-bug) token deposits and withdrawals of Ethereum-based tokens due to the [batchOverflow](https://medium.com/@peckshield/alert-new-batchoverflow-bug-in-multiple-erc20-smart-contracts-cve-2018-10299-511067db6536) bug. It is described as a ‘classic integer overflow issue’ and might potentially allow an attacker to ‘possess a huge amount of tokens’.

It was [noted](https://medium.com/@peckshield/alert-new-batchoverflow-bug-in-multiple-erc20-smart-contracts-cve-2018-10299-511067db6536), that there’s no traditional security approach to fix these vulnerabilities at the moment.

####  What are the benefits of ERC-20?

*Basically, it makes everything more simple.*

Before ERC-20 tokens, developers might use other terminology in the code - e.g.

one token uses [totalAmount] while another uses [totalNumber].

Exchanges and wallets needed to build their platforms to accommodate for each

one token’s code.

With a universal standard, new tokens can be put on an exchange or transferred to

a wallet automatically, once it’s been created.

ERC-20 also makes the creation of new tokens extremely easy, and that is why Ethereum has [become](https://techcrunch.com/2017/06/08/how-ethereum-became-the-platform-of-choice-for-icod-digital-assets/) the most popular platform for ICO’s in 2017.

####  Can I lie and say I have more tokens than I really do?

*Nope.*

Before a transaction takes place, the [allowance] function checks the balance of the user’s account and will cancel the transaction if there are insufficient tokens.

We don’t allow credit in our ‘crypto-casino’, so we need to make sure that each player has enough BLU to make their bet. If they only have 1 BLU, then they can’t bet 2 BLU.

####  Is there any way to make a counterfeit token?

*Not really, because [approve] checks a transaction against the total supply of tokens.*

It makes sure that there are none missing or extra.

Another way to safeguard the integrity of our hypothetical poker game is to make sure no one brought extra BLU to the table. So, [approve] allows the exchange by checking that the total number of BLU on the table equals 10.

![Is there any way to make a counterfeit token?](https://cointelegraph.com/storage/uploads/view/9ee839b7047df962f60ef103c3172fff.png)Is there any way to make a counterfeit token?
####  How can I get ERC-20 tokens from other users?

*[transferFrom] is the function that allows a user to transfer tokens to another user.*

Good news! You won the first hand and gained 2.5 BLU from the other players.

But in order to take it from them, you need [transferFrom]. Without this, what is to stop someone else from stealing your BLU?

####  What does the function [balanceOf] do?

*When the [balanceOf] function is carried out, it returns the number of tokens a given address has in its account.*

In the first hand of our poker game, 5 of the players looked at their cards and decided not to play. Each of the remaining 5 decided to bet .5 BLU. Using [balanceOf], we see that five of the players have 1 BLU and five have .5 BLU.

![What does the function [balanceOf] do?](https://cointelegraph.com/storage/uploads/view/aa3061e268923d5fd3979802e5f35afd.jpg)What does the function [balanceOf] do?
####  What about [transfer]?

*[transfer] allows a certain number of tokens to be transferred from the total supply to a user account.*

Before the game can start, the players must receive their BLU from the dealer.

Each player gets 1 BLU.

####  Now to the mandatory rules: what is [totalSupply]?

*[totalSupply] identifies the total number of ERC-20 tokens created.*

The first thing our casino needs to have is a total of how many BLU tokens are in circulation. Let’s say our poker table has a total of 10 BLU with ten players.

![Now to the mandatory rules: what is [totalSupply]?](https://cointelegraph.com/storage/uploads/view/bb5863baa6b28c068f2cc43bc52497d8.png)Now to the mandatory rules: what is [totalSupply]?
####  Got the analogy, but how exactly would that work?

*Let’s look at each of the rules for ERC-20 in our ‘crypto-casino’ example.*

They are very important for developers to follow.

Let’s start with the optional rules:

Token Name: Blu Chip

Symbol: BLU

Decimal: 2\*

*\*We want our tokens to be divisible so that a minimum players bet is .01 BLU. We could leave the decimal at 0 and make 1 BLU the minimum or raise the decimal to 18 resulting in .000000000000000001 BLU the lowest possible division, but let’s keep it simple.*

####  What happens after a smart contract creates a token?

*This is where ERC-20 comes in.*

After a token has been created, it can be traded, spent, or given to someone else.

ERC-20 is the universal language that all tokens on the Ethereum network use. It allows one token to be traded with another.

Let’s imagine we wanted to make a crypto-casino. Just like in a brick-and-mortar casino, we want our players to use our chips, for simplicity’s sake.

So, a player exchanges their fiat for our tokens and heads to a poker table.

####  Where do smart contracts fit into all this?

*Smart contracts are used to create ERC-20 tokens.*

They are also used to facilitate transactions of tokens, and record balances of tokens in an account.

Smart contracts are written in the programming language “Solidity” on the basis of If-This-Then-That (IFTTT) logic.

Think of this as a vending machine.

![Where do smart contracts fit into all this?](https://cointelegraph.com/storage/uploads/view/dbe3a6f854b09aa99072a6b2484fa391.png)Where do smart contracts fit into all this?
####  What is Ethereum, in the first place?

*[Ethereum](https://cointelegraph.com/tags/ethereum) is a decentralized network of computers with two basic functions.*

They are: blockchain that can record transactions, and a virtual machine that can produce smart contracts.

Because of these two functions, Ethereum is able to support decentralized applications ([DApps](https://cointelegraph.com/tags/dapps)). These DApps are built on the existing Ethereum blockchain, piggybacking off of its underlying technology. In return, Ethereum charges developers for the computing power in their network, which can only be paid in Ether, the only inter-platform currency.

Depending on its purpose, DAPPs might create ERC-20 tokens to function as a currency, a share in the company, for points in a loyalty program, or even proof of ownership, say, of an amount of gold or the deed to a house.

####  What are ERC-20 tokens?

*ERC-20 tokens are tokens designed and used solely on the Ethereum platform.*

They follow a list of standards so that they can be shared, exchanged for other tokens, or transferred to a crypto-wallet.

The Ethereum community created these standards with three optional rules, and six mandatory.

**Optional**

* Token Name
* Symbol
* Decimal (up to 18)

**Mandatory**

* totalSupply
* balanceOf
* transfer
* transferFrom
* approve
* allowance

Confused? Let’s back up a little.
