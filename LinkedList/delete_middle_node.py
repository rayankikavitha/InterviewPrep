"""
Delete a node in the middle if head is not given and only the access to that element is given
Any node that is not the first and last node, not necessarily th exact middle
input:
 Delete c from the lined list : a -> b->c->d->e->f
ouput :
a->b->d->e->f
"""
from LinkedList import LinkedList
ll = LinkedList()
c=['f','e','d','c','b','a']
for each in c:
    ll.add(each)

ll.printlist()
print pointer
"""

just copy the next node over to the current node and then delete the next node.
"""
def delete_middle_node(ll):
    head = ll.head
    curr = head
    while curr is not None:
        print curr.val
        if curr.val == given:
            curr.next = curr.next.next
        else:
            curr = curr.next

delete_middle_node(ll, 'c')

ll.printlist()