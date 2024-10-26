# https://www.algoexpert.io/questions/split-binary-tree
from collections import deque


# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


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


def getSum(node):
    if node is None:
        return 0

    return getSum(node.left) + getSum(node.right) + node.value