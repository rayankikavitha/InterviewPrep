class Node:
    def __init__(self,val = None):
        self.val = val
        self.next = None

def merge_two_sorted_ll(head1, head2):
    first = head1
    second = head2
    p = Node() # dummy node to iterate
    fakehead = p  # store it as header
    while first and second:
        if first.val > second.val:
            p.next = second
            second = second.next
        else:
            p.next = first
            first = first.next
        p = p.next
    if first:
        p.next = first
    if second:
        p.next = second
    return fakehead.next

def printlist(head):
    while head:
        print head.val, '->',
        head = head.next

a=Node(1)
b=Node(3)
c=Node(6)
d=Node(2)
e=Node(5)
a.next = b
b.next = c
c.next = None
d.next = e
e.next = None

printlist(merge_two_sorted_ll(a,d))


