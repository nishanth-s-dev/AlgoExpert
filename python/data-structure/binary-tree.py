class Node:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def insert(self, value):
        pass

    def delete(self, value):
        pass

    def contains(self, value):
        pass

    # Traversal
    def preorder(self):
        pass

    def inorder(self):
        pass

    def postorder(self):
        pass

    def level_order(self):
        pass

    # Utility
    def find_height(self, value):
        pass

    def find_depth(self, value):
        pass

    def count_nodes(self):
        pass

    def count_leaf_nodes(self):
        pass

    def check_balanced(self):
        pass

    # Path finding
    def find_path(self, value):
        pass

    def find_all_paths(self):
        pass

    # Miscellaneous
    def mirror_tree(self):
        pass

    def convert_to_list(self):
        pass

    def lowest_common_ancestor(self):
        pass


if __name__ == '__main__':
    print("Binary Tree")