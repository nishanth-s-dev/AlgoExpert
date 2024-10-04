# https://www.algoexpert.io/questions/validate-bst

# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree, min_value=float('-inf'), max_value=float('inf')):
    if tree is None:
        return True
    if tree.value < min_value or tree.value >= max_value:
        return False

    leftTree = validateBst(tree.left, min_value, tree.value)
    rightTree = validateBst(tree.right, tree.value, max_value)

    return leftTree and rightTree