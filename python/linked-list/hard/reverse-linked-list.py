# https://www.algoexpert.io/questions/reverse-linked-list

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head, prev = None):
    if head is None:
        return prev
    next = head.next
    head.next = prev
    return reverseLinkedList(next, head)
