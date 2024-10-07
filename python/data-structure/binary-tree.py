from collections import deque


class Node:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

    def __str__(self):
        return f"Value: {self.value}"

class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)

    def insert(self, value):
        new_node = Node(value)
        queue = [self.root]
        while queue:
            current_node = queue.pop(0)
            if current_node.left is None:
                current_node.left = new_node
                break
            else:
                queue.append(current_node.left)

            if current_node.right is None:
                current_node.right = new_node
                break
            else:
                queue.append(current_node.right)

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

    # Level order
    def __str__(self):
        res = []
        queue = deque([self.root])
        while queue:
            current = queue.popleft()
            res.append(str(current.value))
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return " ".join(res)

if __name__ == '__main__':
    binary_tree = BinaryTree(1)
    binary_tree.insert(2)
    binary_tree.insert(3)
    binary_tree.insert(4)
    binary_tree.insert(5)
    binary_tree.insert(6)
    print(binary_tree)
