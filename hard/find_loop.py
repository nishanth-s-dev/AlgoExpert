class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) | O(n)
def findLoopHashMethod(head):
    hset = set()
    current = head
    while current:
        if current in hset:
            return current
        hset.add(current)
        current = current.next

    return head

def findLoop(head):
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