"""
Reverse a binary tree i.e from left to right

input :
     6
    / \
    3  4
   /\  /\
  7  3 8 1

Output:
     6
    / \
   4   3
   /\  /\
  1 8  3 7


https://stackoverflow.com/questions/9460255/reverse-a-binary-tree-left-to-right
"""

def flipTree(root):
    if root is None:
        return None
    root.left,root.right = root.right,root.left
    flipTree(root.right)
    flipTree(root.left)
    return root

