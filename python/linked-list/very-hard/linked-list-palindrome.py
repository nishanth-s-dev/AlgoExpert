# TODO : Need to learn optimized solution


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def linkedListPalindrome(head):
    values = get_list(head)
    return values == values[::-1]

def get_list(head):
    current = head
    res = []
    while current is not None:
        res.append(current.value)
        current = current.next
    return res