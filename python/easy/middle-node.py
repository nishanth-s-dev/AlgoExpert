# Problem : https://www.algoexpert.io/questions/middle-node

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    """
    Finds the middle node of a linked list using the two-pointer technique.

    Thought Process:
    1. Initialize two pointers, slow and fast, both starting at the head of the linked list.
    2. Move the slow pointer one step and the fast pointer two steps in each iteration.
    3. When the fast pointer reaches the end, the slow pointer will be at the middle.
    4. Return the slow pointer.

    Time Complexity: O(n), where n is the number of nodes in the linked list.
    Space Complexity: O(1), as it uses only a constant amount of extra space.
    """
    if not linkedList:
        return linkedList

    slow, fast = linkedList, linkedList

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def middleNodeWithLength(linkedList):
    """
    Finds the middle node of a linked list by first calculating its length.

    Thought Process:
    1. Traverse the linked list to count the total number of nodes.
    2. Calculate the index of the middle node.
    3. Traverse the linked list again to reach the middle node.
    4. Return the middle node.

    Time Complexity: O(n), where n is the number of nodes in the linked list.
    Space Complexity: O(1), as it uses only a constant amount of extra space.
    """
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
