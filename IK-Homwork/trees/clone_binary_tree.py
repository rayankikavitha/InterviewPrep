"""
Given a binary tree, clone it and return the root of the cloned binary tree

Can be achieved best by recursion

"""

def clone_tree(root):
    if root is None:
        return None
    newroot = Node(root.val)
    newroot.left = clone_tree(root.left)
    newroot.right = clone_tree(root.right)
    return newroot

# Driver program to test binary tree node
class Node:
    # Constructor to create a new binary node
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inorder(root):
    if root is None:
        return None
    inorder(root.left)
    print root.val,
    inorder(root.right)



root1 = Node(9)
root1.left = Node(5)
root1.right = Node(13)
root1.left.left = Node(3)
root1.left.right = Node(7)
root1.right.left = Node(11)
root1.right.right = Node(15)

root2 =  clone_tree(root1)
print root2
inorder(root2)