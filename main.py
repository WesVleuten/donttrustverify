#!/usr/bin/env python3

# Sat per coin
# https://github.com/bitcoin/bitcoin/blob/6f0cbc75be7644c276650fd98bfdb6358b827399/src/consensus/amount.h#L14
COIN = 100000000

# Main chain subsidy halving interval
# https://github.com/bitcoin/bitcoin/blob/6f0cbc75be7644c276650fd98bfdb6358b827399/src/chainparams.cpp#L67
nSubsidyHalvingInterval = 210000

# Block subsidy algorithm
# https://github.com/bitcoin/bitcoin/blob/6f0cbc75be7644c276650fd98bfdb6358b827399/src/validation.cpp#L1068
def getblocksubsidy(nHeight):
    halvings = (int)(nHeight / nSubsidyHalvingInterval)

    if halvings >= 64:
        return 0

    nSubsidy = 50 * COIN
    nSubsidy >>= halvings
    return nSubsidy

# Custom code that will speed run though all subsidy giving blocks
height = 0
total = 0
while True:
    subsidy = getblocksubsidy(height)
    if subsidy == 0:
        # no subsidy given, we're done.
        break
    total += subsidy
    height += 1

print('Totals')
print(height, 'height')
print(total, 'sat')
print(total / COIN, 'BTC')
