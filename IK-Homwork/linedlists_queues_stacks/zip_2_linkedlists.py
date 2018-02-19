"""
Zip a linkedlist from its two ends
input : 1->2->3->4->5->6
output : 1->6->2->5->3->4

Extra credit implement unzip(zip(L1,L2))

http://programming-puzzle.blogspot.com/2014/02/zip-of-linked-list.html


"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def gethalfll(l):
    """
    :param l: Linkedlist
    :return: Returns pointer to half of the linkedlist
    """
    curr = l
    size = 0
    if l is None:
        return None
    while curr:
        size += 1
        curr = curr.next
    # get the head of the second half of linkedlist
    halfsize = size/2
    print size, halfsize
    curr = l
    while halfsize > 0:
        curr = curr.next
        halfsize -= 1
    return curr

def splitinhalf(head):
    """
    :param l: Linkedlist
    :return: Returns pointer to half of the linkedlist
    """
    first_head = head
    curr = head
    size = 0
    if head is None:
        return None
    while curr:
        size += 1
        curr = curr.next
    # get the head of the second half of linkedlist
    halfsize = size/2
    print size, halfsize
    curr = head
    while halfsize > 0:
        prev = curr
        curr = curr.next
        halfsize -= 1
    # make the first list break
    prev.next = None
    return first_head,curr

def revll(head):
    prev = None
    curr = head
    while curr:
        t = curr.next
        curr.next = prev
        prev = curr
        curr = t
        #print prev.val,curr.val,t.val
    return prev



def zipll(head1, head2):
    """
    zips l1 and l2 into l1
    :param l1:
    :param l2:
    :return: Head of the zipped linkedlist
    """
    head = head1
    while head1 and head2:
        #store the next pointers
        t1 = head1.next
        t2 = head2.next
        #swap the links
        head1.next = head2
        head2.next = t1
        # move the pointers
        head2 = t2
        head1 = t1
    # for left over from each list
    if head1:
        curr = head
        while curr.next:
            curr = curr.next
        curr.next = head1
    if head2:
        curr = head
        while curr.next:
            curr = curr.next
        curr.next = head2

    return head

def printll(head):
    while head:
        print head.val,
        head = head.next
    print


def ziplist(head):
    fl = head
    printll(head)
    fh, sh = splitinhalf(head)
    printll(fh)
    printll(sh)
    rl = revll(sh)
    printll(rl)
    printll(zipll(fh, rl))

#driver program to test
n= Node(1)
n.next = Node(2)
n.next.next = Node(3)
n.next.next.next = Node(4)
n.next.next.next.next = Node(5)
n.next.next.next.next.next = Node(6)
m= Node(1)
m.next = Node(2)
m.next.next = Node(3)
m.next.next.next = Node(4)
m.next.next.next.next = Node(5)
m.next.next.next.next.next = Node(6)
m.next.next.next.next.next.next = Node(7)

ziplist(m)
print '***********'
ziplist(n)





