# https://www.algoexpert.io/questions/find-kth-largest-value-in-bst

class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    sorted_node_values = []
    dfs(tree, sorted_node_values)
    if len(sorted_node_values) < k:
        return -1
    return sorted_node_values[k - 1]

def dfs(node, sorted_node_values):
    if node is None:
        return

    dfs(node.right, sorted_node_values)
    sorted_node_values.append(node.value)
    dfs(node.left, sorted_node_values)