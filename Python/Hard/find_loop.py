# Problem : https://www.algoexpert.io/questions/find-loop

# Node
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) Time | O(n) Space
def findLoop(head):
    """
    * Initialize hashset
    * Loop through the linked list
    * If node not in hashset, add it. If node in hashset, we found the loop node. Simply return it.
    * If loop ended without returning, return head
    """
    visitedNodes = set()
    current = head
    while current:
        if current in visitedNodes:
            return current
        visitedNodes.add(current)
        current = current.next
    return head

# O(n) Time | O(1) Space
def findLoop(head):
    """
    * fast and slow pointer algorithm.
    * check whether loop available or not with fast and slow pointer algo.
    * If loop not exists, return head
    * if loop exists
        * set slow pointer to head
        * move each pointer one by one
        * when slow and fast pointer meets, that the loop node
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return head

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow