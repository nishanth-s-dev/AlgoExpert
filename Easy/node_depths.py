def nodeDepths(root, depth = 0):
    if not root:
        return 0
    return depth + nodeDepths(root.left, depth + 1) + nodeDepths(root.right, depth + 1)
