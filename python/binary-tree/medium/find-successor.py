# https://www.algoexpert.io/questions/find-successor

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent

# O(h) Time | O(1) Space
def findSuccessor(tree, node):
    if node.right is not None:
        return getLeftMostChild(node.right)

    return getRightMostParent(node)


def getLeftMostChild(node):
    if node is None:
        return node

    currentNode = node
    while currentNode.left:
        currentNode = currentNode.left

    return currentNode


def getRightMostParent(node):
    currentNode = node

    while currentNode.parent is not None and currentNode.parent.right == currentNode:
        currentNode = currentNode.parent

    return currentNode.parent

# O(n) Time | O(n) Space
# def findSuccessor(tree, node):
#     inorder_array = inorder_traversal(tree)
#     for i in range(len(inorder_array) - 1):
#         if inorder_array[i] == node:
#             return inorder_array[i + 1]
#
#     return None
#
# def inorder_traversal(node):
#     if node is None:
#         return []
#     return inorder_traversal(node.left) + [node] + inorder_traversal(node.right)