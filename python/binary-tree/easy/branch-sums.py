# Problem : https://www.algoexpert.io/questions/branch-sums

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder(root, sum=0, ans=[]):
    """
    Preorder traversal to compute the sum of all root-to-leaf paths in a binary tree.

    Thought Process:
    1. If the current node (`root`) is `None`, return immediately as there is nothing to process.
    2. Check if the current node is a leaf node (both left and right children are `None`):
       - If true, add the current path sum (`sum + root.value`) to the result list (`ans`).
       - This represents a complete path from the root to a leaf.
    3. Recursively call `preorder` on the left child, passing the updated sum.
    4. Recursively call `preorder` on the right child, passing the updated sum.

    Time Complexity: O(n), where `n` is the number of nodes in the tree.
    Space Complexity: O(h), where `h` is the height of the tree (due to recursion stack).
    """
    if not root:
        return

    if root.left is None and root.right is None:
        ans.append(sum + root.value)
        return

    preorder(root.left, sum + root.value, ans)
    preorder(root.right, sum + root.value, ans)


def branchSums(root):
    ans = []
    preorder(root, 0, ans)
    return ans