# linked list, delete middle node

class Node():
	def __init__(self,val):
		self.val = val
		self.next = None

class LL(Node):

	def __init__(self,head = None):
		self.head = None

	# add in the front 
	def add(self,data):
		tempnode = Node(data)
		if self.head is None:
			self.head = tempnode
		else:
			tempnode.next = self.head
			self.head = tempnode

	def printlist(self):
		t = self.head
		while t != None:
			print (str(t.val) + '->',end = ' ')
			t = t.next
		print ()



def delete_middle_node(ll,c):
	curr = ll.head
	while curr is not None:
		if curr.val == c:
			break
		curr = curr.next
    # just copy next doe values into 
	curr.val = curr.next.val
	curr.next = curr.next.next

def middle_element(ll):
	head = ll.head
	slow = head
	fast = head
	while slow and fast:
		if not fast.next:
			break
		fast = fast.next.next
		slow = slow.next
	return slow.val

		
		

l = LL()
#l.add(7)
l.add(6)
l.add(5)
l.add(4)
l.add(3)
l.add(2)
l.add(1)
l.printlist()
delete_middle_node(l,3)
l.printlist()
print (middle_element(l))













#build stacks out of 2 queues


"""
Implement additional method called getMin() for the stack.
At any point of time, it should return minimum
if the stack has[1,2,3,5] , output = 1
if the stack has [1,5,3,0], output = 0

Option1: maintaining a second stack with the mins seen so far
Option2 : not using additional stack, using the same stack for storing mins

"""


class Stack():
	def __init__(self):
		self.stack=[]
		self.minstack=[]

	def getMin(self):
		return self.minstack[len(self.minstack)-1]

	def add(self,val):
		self.stack.append(val)
		if len(self.minstack) > 0:
			currmin = self.minstack[len(self.minstack) - 1]
			if val < currmin:
				self.minstack.append(val)
		else:
			self.minstack.append(val)

	def pop(self):
		popped = self.stack.pop()
		print (popped)
		if popped == self.minstack[len(self.minstack) -1 ]:
			self.minstack.pop()

	def print(self):
		print (self.stack)
		print (self.minstack)

"""
s = Stack()
s.add(5)
s.add(9)
s.add(1)
s.add(12)
s.add(7)
s.add(0)
s.print()
print (s.getMin())

s.pop()
s.print()
print (s.getMin())
s.pop()
s.print()
print (s.getMin())
s.pop()
s.print()
print (s.getMin())
s.pop()
s.print()
print (s.getMin())
s.pop()
s.print()
"""

# build queue out of 2 stacks


class Queue():

	def __init__(self):
		self.pushstack = []
		self.popstack = []

	def enqueue(self,val):
		self.pushstack.append(val)

	def dequeue(self):
		if len(self.popstack) > 0:
			return self.popstack.pop()
		else:
			while self.pushstack:
				self.popstack.append(self.pushstack.pop())
			return self.popstack.pop()
	def print(self):
		print (self.pushstack)
		print (self.popstack)

"""
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print (q.dequeue())
q.enqueue(4)
q.enqueue(5)
print (q.dequeue())
q.print()
print (q.dequeue())
print (q.dequeue())
q.print()

"""








	








