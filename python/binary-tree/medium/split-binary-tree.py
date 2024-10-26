# https://www.algoexpert.io/questions/split-binary-tree
from collections import deque


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) Time | O(n) Space
def splitBinaryTree(tree):
    if tree is None:
        return 0

    memo = dict()

    totalSum = getSum(tree)
    if totalSum % 2 == 0:
        expectedSum = totalSum // 2
        queue = deque([tree])
        while queue:
            current = queue.popleft()

            if current not in memo:
                memo[current] = getSum(current)

            currentSum = memo[current]

            if currentSum == expectedSum:
                return currentSum

            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)

    return 0


# O(n) Time | O(n) Space
# DFS Method
def splitBinaryTree(tree):
    if tree is None:
        return 0

    memo = dict()

    totalSum = getSum(tree)
    if totalSum % 2 == 0:
        if dfsHelper(tree, totalSum // 2, memo):
            return totalSum // 2

    return 0


def dfsHelper(node, expectedSum, memo):
    if node is None:
        return False

    if node not in memo:
        memo[node] = getSum(node)

    currentSum = memo[node]

    return currentSum == expectedSum or dfsHelper(node.left, expectedSum, memo) or dfsHelper(node.right, expectedSum, memo)

def getSum(node):
    if node is None:
        return 0

    return getSum(node.left) + getSum(node.right) + node.value
