# https://www.algoexpert.io/questions/number-of-ways-to-traverse-graph

def numberOfWaysToTraverseGraph(width, height):
    if height == 1 and width == 1:
        return 1
    if height == 0 or width == 0:
        return 0

    return numberOfWaysToTraverseGraph(width - 1, height) + numberOfWaysToTraverseGraph(width, height - 1)


def numberOfWaysToTraverseGraph(width, height, memo=None):
    if memo is None:
        memo = {}
    if height == 1 and width == 1:
        return 1
    if height == 0 or width == 0:
        return 0

    key = (min(height, width), max(height, width))
    if key not in memo:
        memo[key] = numberOfWaysToTraverseGraph(width - 1, height) + numberOfWaysToTraverseGraph(width, height - 1)

    return memo[key]