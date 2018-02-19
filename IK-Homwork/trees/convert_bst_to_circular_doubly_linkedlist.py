"""
http://cslibrary.stanford.edu/109/TreeListRecursion.html
"""

class Node:
    # Constructor to create a new binary node
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def join_nodes(node1, node2):
    node1.right = node2
    node2.left = node1

# given two circular doubly linked lists, append them and return the new list
def node_append(node1, node2):
    #if either is null, return the other
    if node1 is None:
        return node2
    if node2 is None:
        return node1

    # find the last node in each using the previous pointer node
    node1_last = node1.left
    node2_last = node2.left

    # join them to make it connected
    join_nodes(node1_last, node2)
    join_nodes(node2_last, node1)

    return node1


def treeToList(root):
    if root is None:
        return None

    # recursively do the substrees
    aList = treeToList(root.left)
    bList = treeToList(root.right)

    # make the single root node to a list length - 1 in preparation for appending
    root.left = root
    root.right = root

    # at this point, we have three lists and we append them together in the right order (alist, root, blist)
    aList = node_append(aList, root)
    aList = node_append(aList, bList)

    return aList

def final_treeToList(root):
    head = treeToList(root)
    printList(head)

def treeInsert(root,newval):
    if newval <= root.val:
        if root.left:
            treeInsert(root.left, newval)
        else:
            root.left = Node(newval)
    else:
        if root.right:
            treeInsert(root.right, newval)
        else:
            root.right = Node(newval)


# driver program to test

def printList(head):
    curr = head
    while curr:
        print curr.val,
        curr = curr.right
        if curr == head:
            break

root1 = Node(9)
root1.left = Node(5)
root1.right = Node(13)
root1.left.left = Node(3)
root1.left.right = Node(7)
root1.right.left = Node(11)
root1.right.right = Node(15)

print final_treeToList(root1)
