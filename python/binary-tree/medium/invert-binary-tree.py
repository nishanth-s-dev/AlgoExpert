# https://www.algoexpert.io/questions/invert-binary-tree

from collections import deque

def invertBinaryTree(tree):
    if tree is None:
        return tree
    queue = deque([tree])
    while queue:
        current = queue.popleft()
        current.left, current.right = current.right, current.left
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)

def invertBinaryTree(tree):
    if tree is None:
        return
    swapLeftRight(tree)
    invertBinaryTree(tree.left)
    invertBinaryTree(tree.right)

def swapLeftRight(node):
    node.left, node.right = node.right, node.left

def bfs(tree):
    if tree is None:
        print("Tree is empty")
        return
    queue = deque([tree])
    while queue:
        current = queue.popleft()
        print(current.value, end = " ")
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    print()


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

if __name__ == "__main__":
    # Create a binary tree
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)

    # Perform BFS traversal and print node values
    print("Before invert : ", end = " ")
    bfs(root)
    invertBinaryTree(root)
    print("After invert : ", end = " ")
    bfs(root)
