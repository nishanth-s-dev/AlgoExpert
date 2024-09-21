# Problem : https://www.algoexpert.io/questions/find-loop

# Node
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# O(n) Time | O(n) Space
def findLoop(head):
    """
    This function detects a loop in a linked list.

    Thought Process:
    1. Initialize a set to keep track of visited nodes.
    2. Traverse the list starting from the head.
    3. For each node:
       - If it's already in the set, a loop is detected; return the node.
       - If not, add it to the set and move to the next node.
    4. If the end of the list is reached, return None.

    By using a hash set, we ensure that each node is processed once,
    allowing for efficient loop detection.
    """
    visitedNodes = set()
    current = head
    while current:
        if current in visitedNodes:
            return current
        visitedNodes.add(current)
        current = current.next
    return None

# O(n) Time | O(1) Space
def findLoop(head):
    """
    This function detects a loop in a linked list using Floyd's Tortoise and Hare algorithm.

    Thought Process:
    1. Initialize two pointers, slow and fast, both starting at the head.
    2. Move the slow pointer one step and the fast pointer two steps at a time.
    3. If there is a loop, the fast pointer will eventually meet the slow pointer.
       - If they meet, it indicates a loop exists.
    4. If the fast pointer reaches the end (null), there is no loop; return None.
    5. If a loop is detected, reset the slow pointer to the head.
    6. Move both pointers one step at a time until they meet again.
       - The meeting point will be the start of the loop.

    This approach is efficient as it uses constant space and has a linear time complexity.
    """
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow