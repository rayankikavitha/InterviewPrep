"""
With out using recursion print post-over traversal of a binary tree

LRV

"""
class Node:
    # Constructor to create a new binary node
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def postOrder(root):
    if root is None:
        return None
    stack = [root]
    revstack =[] # reverse stack to get right first node first
    while stack:
        # pop each element and copy to rev stack while adding children to stack
        c = stack.pop()
        revstack.append(c)
        #print stack,revstack
        if c.left:
            stack.append(c.left)
        if c.right:
            stack.append(c.right)
    # print revstack
    while revstack:
        print revstack.pop().val,






# Driver program to test binary tree node

root1 = Node(9)
root1.left = Node(5)
root1.right = Node(13)
root1.left.left = Node(3)
root1.left.right = Node(7)
root1.right.left = Node(11)
root1.right.right = Node(15)

root2 = Node(10)
root2.left = Node(4)
root2.right = Node(14)
root2.left.left = Node(2)
root2.left.right = Node(6)
root2.right.left = Node(12)
root2.right.right = Node(16)


postOrder(root1)