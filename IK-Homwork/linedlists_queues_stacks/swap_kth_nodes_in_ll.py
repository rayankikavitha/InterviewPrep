"""
Swap kth node from the beginning, with kth node from the end.

https://docs.google.com/document/d/1UBFl633FsCZLq2Vejihj2g80Vdl9BNF6-N1D4J-clsI/edit

node1, prev1 = We need kth node, kth prev node
node2, prev2 = We need n-kth node, n-kth prev node
swap(node1, prev1, node2, prev2)

Tip : inorder to find n-kth node,( 1<k<n)
when we have kth node, start a new pointer from the header.
Move both pointers until kth pointer reaches end. By that time, header pointer will be at the n-kth node
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def swap2nodes(head,node1,prev1,node2,prev2):
    if not node1 or not node2:
        return
    # if swapping first node
    if not prev1:
        head = node2
    else:
        prev1.next = node2
    # symmertrical case k > n-k
    if not prev2:
        head = node1
    else:
        prev2.next = node1

    temp = node1.next
    node1.next = node2.next
    node2.next = temp
    return head


def swapkth(head, k):
    if not head or k < 1:
        return
    curr = head
    main = head
    prev = None
    while k > 1 and curr:
        prev = curr
        curr = curr.next
        k -= 1
    # at this point of time we got kth node details
    kth_prev = prev

    kth = curr
    kthnode = curr
    #print kth.val
    # by the time kth reaches end, main will be at n-kth
    while kth and kth.next:
        kth = kth.next
        mainprev = main
        main = main.next

    nkth_prev = mainprev
    nkth = main

    return swap2nodes(head,kthnode, kth_prev, nkth, nkth_prev)

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
printll(swapkth(n,1))
