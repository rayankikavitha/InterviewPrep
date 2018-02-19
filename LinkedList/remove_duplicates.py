"""
Remove duplicates form a listed list
1) using set - extra memory - O(n)
2) no extra memory - O(n*2)

"""
from  LinkedList import LinkedList

nums = [1,2,5,3,2,9,2,2,8]
l = LinkedList()
for i in range(len(nums)):
    l.add(nums[i])

l.printlist()

# Using extra memory
def delete_duplicates(ll):
    c = ll.head
    s = set()
    prev = None
    while c is not None:
        if c.val in s:
            prev.next = c.next
        else:
            s.add(c.val)
            prev = c
        c = c.next

#delete_duplicates(l)
print "after deleting duplicates"
l.printlist()

# with out using memory, maintaining runner
def delete_duplicates2(ll):
    curr = ll.head
    while curr is not None:
        # lets start runner as current position. If a duplication occurs next to each other we need this
        runner = curr
        #print "curr ="+str(curr.val)
        while runner.next  is not None:
            #print "runner = "+str(runner.next.val)
            if curr.val == runner.next.val:
                runner.next   = runner.next.next
            else:
                runner = runner.next
        curr = curr.next


delete_duplicates2(l)
print "after deleting duplicates"
l.printlist()




