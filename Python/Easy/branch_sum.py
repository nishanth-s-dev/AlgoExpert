# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder(root, sum=0, ans=[]):
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