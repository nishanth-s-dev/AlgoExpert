# https://www.algoexpert.io/questions/min-height-bst

def minHeightBst(array):
    return constructMinHeightBst(array, None, 0, len(array) - 1)


def constructMinHeightBst(array, bst, startIdx, endIdx):
    if endIdx < startIdx:
        return

    midIdx = (startIdx + endIdx) // 2
    valueToInsert = array[midIdx]

    if bst is None:
        bst = BST(valueToInsert)
    else:
        bst.insert(valueToInsert)

    constructMinHeightBst(array, bst, startIdx, midIdx - 1)
    constructMinHeightBst(array, bst, midIdx + 1, endIdx)

    return bst


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)