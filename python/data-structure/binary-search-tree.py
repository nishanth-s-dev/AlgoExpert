class Node:
    def __init__(self, value):
        self.value, self.left, self.right = value, None, None

    def __str__(self):
        return str(self.value)

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def contains(self, value):
        if self.root is None:
            return False
        return self._contains_recursive(self.root, value)

    def _contains_recursive(self, node, value):
        # Base Conditions
        if node is None:
            return False
        if value == node.value:
            return True

        # Recursive calls
        if value < node.value:
            return self._contains_recursive(node.left, value)
        else:
            return self._contains_recursive(node.right, value)

    def remove(self, value):
        self.root = self._remove_recursive(self.root, value)

    def _remove_recursive(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._remove_recursive(node.left, value)
        elif value > node.value:
            node.right = self._remove_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_node = self._find_min(node.right)
                node.value = min_node.value
                node.right = self._remove_recursive(node.right, min_node.value)

        return node

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current


if __name__ == '__main__':
    tree = BinarySearchTree()
    array = [10, 5, 15, 3, 7, 12, 18]
    for item in array:
        tree.insert(item)

    tree.remove(10)