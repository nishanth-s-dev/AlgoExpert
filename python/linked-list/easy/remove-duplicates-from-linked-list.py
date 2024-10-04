# Problem : https://www.algoexpert.io/questions/remove-duplicates-from-linked-list

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    """
    Removes duplicates from a sorted linked list.

    Thought Process:
    1. Initialize a pointer to the current node starting at the head of the linked list.
    2. While the current node is not None, look for the next distinct node.
    3. If the next node has the same value as the current node, skip it.
    4. Set the next pointer of the current node to the next distinct node.
    5. Move to the next node and repeat until the end of the list is reached.
    6. Return the modified linked list.

    Time Complexity: O(n), where n is the number of nodes in the linked list, as each node is processed once.
    Space Complexity: O(1), as it modifies the list in place without using additional space.
    """
    currentNode = linkedList
    while currentNode:
        nextDistinctNode = currentNode.next
        while nextDistinctNode and nextDistinctNode.value == currentNode.value:
            nextDistinctNode = nextDistinctNode.next
        currentNode.next = nextDistinctNode
        currentNode = currentNode.next
    return linkedList