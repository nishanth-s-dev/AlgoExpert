# https://www.algoexpert.io/questions/min-number-of-coins-for-change

def minNumberOfCoinsForChange(n, denoms):
    res = _minNumberOfCoinsForChange(n, denoms, {})
    return res if res != float("inf") else -1

def _minNumberOfCoinsForChange(n, denoms, memo = {}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n < 0:
        return float("inf")
    min_change = float("inf")
    for denom in denoms:
        min_change = min(min_change, 1 + _minNumberOfCoinsForChange(n - denom, denoms, memo))
    memo[n] = min_change
    return min_change