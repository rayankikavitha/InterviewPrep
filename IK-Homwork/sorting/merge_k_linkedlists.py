class Node(object):
    def __init__(self, x):
        self.val = x
        self.next = None

import heapq
def mergekLinkedLists(lst):
    """

    :param lst: list of nodes
    :return: list node
    """
    h=[]
    result_node = None
    result_value=[]
    # initalize the heap
    for node in lst:
        heapq.heappush(h,(node.val, node))
    while h:
        val, res  = heapq.heappop(h)
        if result_node is None:
            result_node = res
        result_value.append(val)
        next = res.next
        if next != None:
            heapq.heappush(h,(next.val,next))
    return result_node,result_value





#driver program to test
n= Node(1)
n.next = Node(3)
n.next.next = Node(5)
n.next.next.next = Node(7)
n.next.next.next.next = Node(9)
n.next.next.next.next.next = Node(11)
m= Node(2)
m.next = Node(4)
m.next.next = Node(6)
m.next.next.next = Node(8)
m.next.next.next.next = Node(10)
m.next.next.next.next.next = Node(12)
m.next.next.next.next.next.next = Node(14)
p= Node(5)
p.next = Node(10)
p.next.next = Node(15)

print mergekLinkedLists([m,n,p])