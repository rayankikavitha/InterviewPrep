class Node:
    def __init__(self,val = None):
        self.val = val
        self.next = None


def find_lengths(l):
    count = 0
    if l is None:
        return 0
    while l is not None:
        l = l.next
        count += 1
    return count


def find_intersection(l1, l2):
    l1_len = find_lengths(l1)
    l2_len = find_lengths(l2)
    bigger = l1 if l1_len > l2_len else l2
    diff = abs(l1_len - l2_len)

    first = l1
    second = l2
    if bigger == first:
        while diff:
            first = first.next
            diff -= 1
    elif bigger == second:
        while diff:
            second = second.next
            diff -= 1

    while first.next != None and second.next != None:
        if first == second:
            return first.val
        else:
            first = first.next
            second = second.next
    return None # -1


def printlist(c):
    while c != None:
        print c.val,'->',
        c = c.next

a=Node(1)
b=Node(3)
c=Node(6)
d=Node(8)
e=Node(10)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = None

p=Node(2)
q=Node(5)




p.next = q
q.next = d


print find_intersection(a,p)