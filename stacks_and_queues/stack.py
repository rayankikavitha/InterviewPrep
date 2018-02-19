
class Stack:
    def __init__(self):
        self.items =[]

    def IsEmpty(self):
        return len(self.items) == 0

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            raise Exception("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.items.size == 0:
            raise Exception("Stack is empty")
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def print_stack(self):
        counter = len(self.items) - 1
        while  counter >= 0:
            print self.items[counter]
            counter -= 1


# test

s = Stack()
s.push(10)
s.push(9)
s.push(8)
s.push(7)
s.push(6)
print "size"
print s.size()
print "stack"
s.print_stack()
while s.size() > 0:
    print s.pop()
print"stack after pop"
s.print_stack()
print "*****************"




