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

def is_palindrome(head):
    """
    o(n) time complexity and o(n) space complexity using stack
    :param head:
    :return:
    """
    c = head
    s=[] #stack
    counter = 0
    while c != None:
        s.append(c.val)
        counter +=1
        c = c.next
    print s,counter
    c=head
    while c != None and counter/2 > 0:
        if c.val != s.pop():
            return False
        c = c.next
    return True

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
    return slow

def is_palindrome2(head):
    """
    o(n) time complexity and no extra space, but modifies the linkedlist
    traverse half and reverse the left side of the list list and compare left half and right half with 2 pointers
    :param head:
    :return:
    """
    c = head
    counter = 0
    while c != None:
        counter +=1
        c = c.next
    c=head
    while c != None and counter/2 > 0:
        if c.val != s.pop():
            return False
        c = c.next
    return True


a=Node(1)
b=Node(2)
c=Node(3)
d=Node(3)
e=Node(2)
f = Node(1)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = None

print is_palindrome(a)


