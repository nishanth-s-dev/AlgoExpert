# https://www.algoexpert.io/questions/symmetrical-tree

# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def symmetricalTree(tree):
    if tree is None:
        return True
    invertTree(tree.right)
    return isSameTree(tree.left, tree.right)

def isSameTree(tree1, tree2):
    return tree1 == tree2 if tree1 is None or tree2 is None else isSameTree(tree1.left, tree2.left) and isSameTree(tree1.right, tree2.right) and tree1.value == tree2.value

def invertTree(tree):
    if tree is None:
        return
    swapNodes(tree)
    invertTree(tree.left)
    invertTree(tree.right)

def swapNodes(tree):
    tree.left, tree.right = tree.right, tree.left