
class Queue:
    def __init__(self):
        self.items =[]

    def IsEmpty(self):
        return len(self.items) == 0

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        if len(self.items) == 0:
            raise Exception("Stack is empty")
        return self.items.pop()

    def size(self):
        return len(self.items)

    def print_queue(self):
        counter = len(self.items) - 1
        while  counter >= 0:
            print self.items[counter]
            counter -= 1


# test

s = Queue()
s.enqueue(10)
s.enqueue(9)
s.enqueue(8)
s.enqueue(7)
s.enqueue(6)
print "size"
print s.size()
print "Queue"
s.print_queue()
while s.size() > 0:
    print s.dequeue()
print"queue after dequeu"
s.print_queue()
print "*****************"




