from stack import Stack
"""
Create two stacks, 1 for push and 1 for pop and use lazy copying from stack1 to stack2
"""

class Queue(Stack):
    def __init__(self):
        self.spush = Stack()
        self.spop = Stack()

    def push(self, item):
        self.spush.push(item)

    def pop(self):
        if self.spop.size() == 0 :
            while self.spush.size() > 0:
                self.spop.push(self.spush.pop())
        return self.spop.pop()

    def size(self):
        return self.spush.size() + self.spop.size()

    def print_queue(self):
        l1 = self.spop.size() - 1
        l2 = self.spush.size()
        if l1 > 0:
            while l1 >= 0:
                print self.spop.items[l1]
                l1 -= 1
        if l2 > 0:
            c = 0
            while  c < l2:
                print self.spush.items[c]
                c += 1




q = Queue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)
print "print queue"
q.print_queue()
print "popping events"
while q.size() > 0:
    print q.pop()
    print "----"
q.print_queue()
