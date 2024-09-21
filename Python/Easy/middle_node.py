# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    if not linkedList:
        return linkedList

    slow, fast = linkedList, linkedList

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def middleNodeWithLength(linkedList):
    length = 0
    current = linkedList
    while current:
        length += 1
        current = current.next

    current = linkedList
    length = length // 2
    for _ in range(length):
        current = current.next

    return current
