# Problem : https://www.algoexpert.io/questions/evaluate-expression-tree

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def evaluateExpressionTree(tree):
    """
    Recursively evaluates an expression tree and returns the result.

    Thought Process:
    1. If the current node is a leaf (non-negative value), return its value directly.
    2. Recursively evaluate the left and right subtrees to get their values.
    3. Based on the current node's value, apply the appropriate operator:
       - `-1` represents addition: `left + right`
       - `-2` represents subtraction: `left - right`
       - `-3` represents division: `left / right`
       - `-4` represents multiplication: `left * right`
    4. Return the computed result for the current subtree.

    Time Complexity: O(n), where `n` is the number of nodes in the tree.
    Space Complexity: O(h), where `h` is the height of the tree (due to recursion stack).
    """
    if tree.value >= 0:
        return tree.value

    leftTreeValue = evaluateExpressionTree(tree.left)
    rightTreeValue = evaluateExpressionTree(tree.right)

    if tree.value == -1:
        return leftTreeValue + rightTreeValue
    if tree.value == -2:
        return leftTreeValue - rightTreeValue
    if tree.value == -3:
        return int(leftTreeValue / rightTreeValue)

    return leftTreeValue * rightTreeValue