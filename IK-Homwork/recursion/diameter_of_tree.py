"""
The diameter of a tree (sometimes called the width) is the number of nodes on the longest path between two leaves in the tree.

http://www.geeksforgeeks.org/diameter-of-a-binary-tree/

http://techieme.in/tree-diameter/

The diameter of a tree T is the largest of the following quantities:
- The diameter of T's left subtree
- The diameter of the T's right subtree
- The longest path between leaves that goes through the root T ( This can be computed from the heights of the subtree)

"""
import math

class node:
    def __init__(self,val):
        self.left = None
        self.right = None
        self.val = val


def height(root):
    if root is None:
        return 0
    return max(height(root.left),height(root.left)) + 1


def diameter(root):
    if root is None:
        return 0

    # Get the height of left and right sub-trees
    lh = height(root.left)
    rh = height(root.right)

    # Get the diameter of the left and right sub-trees
    ld = diameter(root.left)
    rd = diameter(root.right)

    # Return max of the following tree:
    # 1) Diameter of left subtree
    # 2) Diameter of right subtree
    # 3) Height of left subtree + height of right subtree +1

    return max(lh+rh+1, max(ld, rd))



# define a tree

rt = node(10)
rt.left = node(5)
rt.right = node(20)
rt.left.left = node(1)
rt.left.right = node(7)
rt.right.right = node(25)
rt.right.right.right = node(30)


print diameter(rt)

print '********************'
#inoder

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print root.val
    inorder(root.right)

inorder(rt)

# breadt first search

def bfs(root):
    if root is None:
        return
    q=[root]
    print "printing bfs"
    while q:
        curnode = q.pop(0)
        print curnode.val
        if curnode.left:
            q.append(curnode.left)
        if curnode.right:
            q.append(curnode.right)

bfs(rt)

# depth first search
def dfs(root):
    if root is None:
        return
    s =[root]
    print "printing bfs"
    while s:
        curnode = s.pop()
        print curnode




