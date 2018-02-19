class Node():
    def __init__(self,val):
        self.val = val
        self.next = None

def reverse(head):
    prev = None
    curr = head
    forward = None
    while curr != None:
        #switch pointers
        forward = curr.next
        curr.next = prev
        # move for next iteration
        prev = curr
        curr = forward
    return prev

a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
a.next = b
b.next = c
c.next = d
d.next = None



def printlist(head):
    c=head
    while c != None:
        print c.val, '->',
        c = c.next
    print "None"

printlist(a)
print"*******"
printlist(reverse(a))
