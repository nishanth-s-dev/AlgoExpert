# https://www.algoexpert.io/questions/height-balanced-binary-tree

from collections import deque

class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# O(n) Time | O(1) Space
def heightBalancedBinaryTree(tree):
    if tree is None:
        return None

    queue = deque([tree])
    while queue:
        current = queue.popleft()

        leftHeight = getHeight(current.left)
        rightHeight = getHeight(current.right)

        if abs(leftHeight - rightHeight) > 1:
            return False

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)

    return True


def getHeight(node):
    return 0 if node is None else max(getHeight(node.left), getHeight(node.right)) + 1



def main():
    # Creating a height-balanced tree
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.right = BinaryTree(6)

    # Test case for a height-balanced tree
    print("Is the tree height-balanced?", heightBalancedBinaryTree(root))  # Expected: True

    # Creating an unbalanced tree
    unbalancedRoot = BinaryTree(1)
    unbalancedRoot.left = BinaryTree(2)
    unbalancedRoot.left.left = BinaryTree(3)
    unbalancedRoot.left.left.left = BinaryTree(4)

    # Test case for an unbalanced tree
    print("Is the tree height-balanced?", heightBalancedBinaryTree(unbalancedRoot))  # Expected: False


if __name__ == "__main__":
    main()
