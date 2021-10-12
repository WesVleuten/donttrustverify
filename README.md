# Don't Trust, Verify

> “I'll just challenge the group to one other thing: how do you know it ends at 21 million? You all read the algorithms? You guys all believe that? I don't know, I've always been a skeptic of stuff like that,” said the JPMorgan Chase (JPM) CEO at an Institute for International Finance event on Oct. 11.

*Brian Cheung, "JPMorgan CEO Jamie Dimon questions 21 million bitcoin cap", Yahoo Finance, October 11, 2021, <https://au.finance.yahoo.com/news/jp-morgan-ceo-jamie-dimon-questions-21-million-bitcoin-cap-201117274.html>*

As someone who likes Bitcoin and its properties, I must admit, I never truly verified the maximum capacity of the protocol. Thank you Jamie Dimon for inspiring me to do so.

## main.py

In this file I reimplemented the Bitcoin issuance function in python, all variables and functions taken fron the bitcoin core code have their sources above them, making it easily verifiyable that I did this correctly.

Running this file will produce the maximum capacity of the Bitcoin protocol.

However, comparing it to mainchain has some nuances missing:

- The coinbase of block 0 is not spendable, thus removing 50 BTC fron the capacity
- One missing, unrecoverable satoshi due to a miner not taking the whole reward <https://mempool.space/block/124724>

```
$ ./main.py
Totals
6930000 height
2099999997690000 sat
20999999.9769 BTC
```

