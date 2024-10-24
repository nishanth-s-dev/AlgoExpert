# https://www.algoexpert.io/questions/find-successor

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


# O(n) Time | O(n) Space
def findSuccessor(tree, node):
    inorder_array = inorder_traversal(tree)
    for i in range(len(inorder_array) - 1):
        if inorder_array[i] == node:
            return inorder_array[i + 1]

    return None

def inorder_traversal(node):
    if node is None:
        return []
    return inorder_traversal(node.left) + [node] + inorder_traversal(node.right)