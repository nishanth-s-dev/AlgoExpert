from collections import deque


class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def getHeight(node):
    if node is None:
        return -1
    left = getHeight(node.left) if node.left is not None else -1
    right = getHeight(node.right) if node.right is not None else -1
    return max(left, right) + 1


    res = -1
    if tree is None:
        return res
    queue = deque([tree])
    while queue:
        currentNode = queue.popleft()
        left_height, right_height = 0, 0
        if currentNode.left is not None:
            left_height = getHeight(currentNode.left) + 1
            queue.append(currentNode.left)
        if currentNode.right is not None:
            right_height = getHeight(currentNode.right) + 1
            queue.append(currentNode.right)

        if left_height + right_height > res:
            res = left_height + right_height
    return res