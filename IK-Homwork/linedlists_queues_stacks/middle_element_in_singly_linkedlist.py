"""
https://docs.google.com/document/d/1UBFl633FsCZLq2Vejihj2g80Vdl9BNF6-N1D4J-clsI/edit

Option 1: Traversing the entire list and get the length, traverse again for half the length
Option 2: Slow (moves once) and Fast pointer ( Moves double). By the time fast pointer reaches the end, the slow will be half way

"""
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None


def findMiddleNode(head):
    if not head:
        return None
    slow = head
    fast = head
    while slow and fast:
        if not fast.next:
            break
        fast = fast.next.next
        slow = slow.next
    return slow.val