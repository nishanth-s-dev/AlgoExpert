# https://www.algoexpert.io/questions/bst-construction

class BST:
    def __init__(self, value):
        self.value, self.left, self.right = value, None, None

    def insert(self, value):
        new_node = BST(value)

        current = self
        while True:
            if value < self.value:
                if self.left is None:
                    self.left = new_node
                    break
                else:
                    current = self.left
            else:
                if self.right is None:
                    self.right = new_node
                    break
                else:
                    current = current.right

        return self

    def contains(self, value):
        current = self
        while True:
            if value == self.value:
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

    def delete(self, value):
        pass