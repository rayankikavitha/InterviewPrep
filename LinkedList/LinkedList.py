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