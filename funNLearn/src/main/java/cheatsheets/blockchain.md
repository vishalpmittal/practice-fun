## Block 
- Contents:
    - Block number
    - Nonce (another number, used to sign a block)
        - let's say signature definition is hash should start with abcd. 
        - Mining is the process to go through a range of numbers to to find a hash that starts with abcd and set Nonce as that number.
    - Data
        - depends on type of block chain
    - Hash (a unique fingerprint of the block)
    - Hash of previous block (helps in creating chain)

- Genesis Block:
    - First block in the blockchain that has 0000 as previous block hash

- hash of the block is created at the block creation, if data inside block changes, it's hash also changes.

## how blockchain works?
- Chain of blocks containing information 
- Distributed Ledger
- if any block is tempered with, the hash changes, invalidating the whole chain.

- Usage: 
    - Storing medical records
    - E-Notary
    - Collecting taxes

- To compare multiple chains, just compare the last blocks of the chains. If the hash is same means all the previous blocks in that chain are same. else there is temporing somewhere. 

## Proof of work Mechanism
- Slows down the creation of blocks. 
- so that if a block is tempered the whole chain can not regenerated.


## Distributed peer to peer network
- every peer gets a full copy of the blockchain.
- a new created block is sent to all peers, which is than validated and then added to the chain.
- all the nodes/peers have to be in consensus to add a new block 


## Smart Contracts


## Bitcoin vs. Ethereum? 
- similarities:
    cryptocurrencies, based on blockchain, decentralized ledgers

- Bitcoin block stores
    - transactional info (from, to, amount)
    - hash
- Bitcoin takes about 10 min to have proof of work and make changes to neighbor blocks

- BTC founded by Satoshi Nakamuro in 2009 vs ETH in 2013 by Bitalik Buterin
- Usage:
    - BTC: digital currency p2p transfer, transaction and storage
    - ETH : more like utility- pay fee for running something, not a digital currency
- Scripting language:
    - BTC: script language, simple smart contracts, multi-sign and escrow
    - ETH :  complex logic smart contracts, with audits 
- Inflation rate:
    - BTC: never be more than 21 Million
    - ETH: no max cap, but reduced large network upgrades, 
- rate:
    - BTC: a block every 10 mins
    - ETH: a block every 15 seconds
- Hash Algo:
    - BTC: SHA256, ASICs (Application Specific Integrated Circuit)
    - ETH: Ethash (Ethereum's proof of work algorithm)
- Speed:
    - BTC: 4 xction / sec
    - ETH: 15 xction / sec
- Network updgrades (Forks)
    - BTC: backward compatibles
    - ETH: risk of chain splits since not backward compatible, forces each node to upgrade

## Mechanism behind Bitcoin?
Once a computer successfully process a block, the block is added to blockchain. 
system generates a new bitcoin that goes to the computer as a reward. 

## how Unspent Transactions Output work? (UTXOs)
- output of a transaction with no spending currently but can spend later 
- Total wealth = Sum(all utxo's in your wallet)

- Total input to a transaction = total output of a transaction 
- A has to send 3 digi byte tokens (DGBT) to B
    - A has two unspent outputs in his wallet:
        - 1 with 2 DGBT and 1 with 1.5 DGBT
    - A creates a transaction with both outputs to send to B 
    - But A also tells blockchain about where that 0.5 DGBT will go. 



## What is the significance of the number of confirmations a transaction has? What does it mean?
- n number of Confirmations provides concensus from the network. 
- Confirmation types:
    - unconfirmed / pending
    - Confirmed
    - Rejected


