# https://www.algoexpert.io/questions/reconstruct-bst

# TODO : Wrong Answer. Need to update

# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)


def reconstructBst(preOrderTraversalValues):
    # Write your code here.
    if len(preOrderTraversalValues) == 0:
        return None

    tree = BST(preOrderTraversalValues[0])
    for i in range(1, len(preOrderTraversalValues)):
        valueToAdd = preOrderTraversalValues[i]
        tree.insert(valueToAdd)

    return tree