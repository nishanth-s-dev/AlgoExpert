# https://www.algoexpert.io/questions/number-of-ways-to-make-change

def numberOfWaysToMakeChange(n, denoms, memo=None, currentIndex=0):
    if memo is None:
        memo = {}
    if n == 0:
        return 1
    if n < 0:
        return 0

    key = (currentIndex, n)
    if key in memo:
        return memo[key]

    numberOfWays = 0
    for i in range(currentIndex, len(denoms)):
        numberOfWays += numberOfWaysToMakeChange(n - denoms[i], denoms, memo, i)

    memo[n] = numberOfWays
    return numberOfWays