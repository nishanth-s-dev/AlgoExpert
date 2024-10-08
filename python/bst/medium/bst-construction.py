# https://www.algoexpert.io/questions/bst-construction

class BST:
    def __init__(self, value):
        self.value, self.left, self.right = value, None, None

    def insert(self, value):
        new_node = BST(value)
        current = self
        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    break
                else:
                    current = current.right

        return self

    def contains(self, value):
        current = self
        while True:
            if value == current.value:
                return True
            elif value < current.value:
                if current.left is None:
                    return False
                else:
                    current = current.left
            else:
                if current.right is None:
                    return False
                else:
                    current = current.right

    # Need to revise this
    def remove(self, value, parent_node = None):
        current_node = self
        while current_node:
            if value < current_node.value:
                parent_node = current_node
                current_node = current_node.left
            elif value > current_node.value:
                parent_node = current_node
                current_node = current_node.right
            else:
                if current_node.left is not None and current_node.right is not None:
                    current_node.value = current_node.right.get_min_value()
                    current_node.right.remove(current_node.value, current_node)
                elif parent_node is None:
                    if current_node.left is not None:
                        current_node.value = current_node.left.value
                        current_node.right = current_node.left.right
                        current_node.left = current_node.left.left
                    elif current_node.right is not None:
                        current_node.value = current_node.right.value
                        current_node.left = current_node.right.left
                        current_node.right = current_node.right.right
                    else:
                        # This is a single-node tree; do nothing.
                        pass
                elif parent_node.left == current_node:
                    parent_node.left = current_node.left if current_node.left is not None else current_node.right
                elif parent_node.right == current_node:
                    parent_node.right = current_node.left if current_node.left is not None else current_node.right
                break
        return self

    def get_min_value(self):
        current_node = self
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value