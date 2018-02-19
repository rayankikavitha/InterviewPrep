"""
starting second pointer when first pointer reaches n
By the time first pointer reaches end, second pointer reaches n
"""
class Node:
    def __init__(self,val = None):
        self.val = val
        self.next = None

a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
e=Node(5)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = None


def n_to_last_element(head):