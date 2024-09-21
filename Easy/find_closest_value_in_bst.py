# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findClosestValueInBstIterative(tree, target) -> int:
    current = tree
    closest = current.value
    while current:
        if abs(target - closest) > abs(target - current.value):
            closest = current.value
        if target < current.value:
            current = current.left
        elif target > current.value:
            current = current.right
        else:
            break

    return closest


def findClosestValueInBstRecursive(root, target, closest=None):
    if not root and closest:
        return closest

    if not closest or abs(root.value - target) < abs(closest - target):
        closest = root.value

    root = root.left if target < root.value else root.right
    return findClosestValueInBstRecursive(root, target, closest)

