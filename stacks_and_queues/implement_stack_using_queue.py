from queue import Queue
class Stack(Queue):

    def __init__(self):
        self.eq = Queue()
        self.dq = Queue()

    def push(self,item):
        self.eq.enqueue(item)

    def pop(self):
        if self.dq.size() == 0:
            while self.eq.size() > 0:
                self.dq.enqueue(self.eq.dequeue())
        return self.dq.dequeue()

    def size(self):
        return self.dq.size() + self.eq.size()


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print "queue size="
print s.size()
print s.eq.items, s.dq.items
print s.pop()
print s.eq.items, s.dq.items


