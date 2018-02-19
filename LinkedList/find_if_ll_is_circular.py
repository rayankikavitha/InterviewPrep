class Node:
    def __init__(self,val = None):
        self.val = val
        self.next = None

class LinkedList(Node):
    def __init__(self, head=None):
        self.head = head

    # always add in the front
    def add(self, data):
        temp = Node(data)
        if self.head is None:
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp

    def printlist(self):
        c = self.head
        while c != None:
            print c.val,'->',
            c = c.next
a=Node(1)
b=Node(2)
c=Node(3)
d=Node(2)
e=Node(1)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = a

def find_circular(head):
    slow = head
    fast = head
    while slow and fast and fast.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

print find_circular(a)
