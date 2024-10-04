# Problem : https://www.algoexpert.io/questions/find-closest-value-in-bst

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def findClosestValueInBst(tree, target):
    """
    Finds the value in the Binary Search Tree (BST) that is closest to the target.

    Thought Process:
    1. Start at the root of the tree and initialize the closest value as the root's value.
    2. Traverse the tree and update the closest value based on the current node.
    3. Move left or right in the tree depending on the target's relation to the current node's value.
    4. Return the closest value found.

    Time Complexity: O(log n) on average for balanced BSTs, O(n) in the worst case for unbalanced BSTs.
    Space Complexity: O(1), as no additional space is used beyond variables.
    """
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


def findClosestValueInBst(root, target, closest=None):
    """
    Finds the value in the Binary Search Tree (BST) that is closest to the target using recursion.

    Thought Process:
    1. If the current node is None, return the closest value found so far.
    2. Update the closest value if the current node's value is closer to the target.
    3. Recursively move to the left or right child based on the target value.
    4. Continue this process until the tree is fully traversed.

    Time Complexity: O(log n) on average for balanced BSTs, O(n) in the worst case for unbalanced BSTs.
    Space Complexity: O(log n) due to the recursion stack in a balanced BST, O(n) in the worst case for unbalanced BSTs.
    """
    if not root and closest:
        return closest

    if not closest or abs(root.value - target) < abs(closest - target):
        closest = root.value

    root = root.left if target < root.value else root.right
    return findClosestValueInBst(root, target, closest)

