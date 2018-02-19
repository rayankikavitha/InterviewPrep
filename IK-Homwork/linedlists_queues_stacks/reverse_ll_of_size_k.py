"""

https://www.geeksforgeeks.org/reverse-a-list-in-groups-of-given-size/
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def rev_ll_sizek(head, k):
    prev = None
    curr = head
    next = None
    count = 0
    # reverse first k nodes
    while curr and count < k:
        # reverse
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        count += 1

    # next is now at the (k+1)th node. recursivly call this function for the list starting from this node
    if next:
        head.next = rev_ll_sizek(next, k)

    return prev

def printll(head):
    while head:
        print head.val,
        head = head.next
    print

#driver program to test
n= Node(11)
n.next = Node(4)
n.next.next = Node(6)
n.next.next.next = Node(7)
n.next.next.next.next = Node(1)
n.next.next.next.next.next = Node(-99)
n.next.next.next.next.next.next = Node(0)
n.next.next.next.next.next.next.next = Node(2)

printll(n)
printll(rev_ll_sizek(n,3))