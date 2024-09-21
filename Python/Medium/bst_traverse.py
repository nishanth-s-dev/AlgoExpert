def inOrderTraverse(tree, array):
    """
    Performs in-order traversal of a binary tree.

    Thought Process:
    1. Recursively visit the left subtree.
    2. Append the current node's value to the result array.
    3. Recursively visit the right subtree.

    This results in the nodes being visited in ascending order for a binary search tree.
    """
    if tree is not None:
        inOrderTraverse(tree.left, array)
        array.append(tree.value)
        inOrderTraverse(tree.right, array)
    return array


def preOrderTraverse(tree, array):
    """
    Performs pre-order traversal of a binary tree.

    Thought Process:
    1. Append the current node's value to the result array.
    2. Recursively visit the left subtree.
    3. Recursively visit the right subtree.

    This traversal is useful for creating a copy of the tree or for expression tree representation.
    """
    if tree is not None:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array


def postOrderTraverse(tree, array):
    """
    Performs post-order traversal of a binary tree.

    Thought Process:
    1. Recursively visit the left subtree.
    2. Recursively visit the right subtree.
    3. Append the current node's value to the result array.

    This traversal is useful for deleting trees or evaluating expression trees.
    """
    if tree is not None:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array
