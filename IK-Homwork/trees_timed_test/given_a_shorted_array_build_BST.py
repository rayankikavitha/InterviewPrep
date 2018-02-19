"""
Given a sorted array build BST, return its root.
"""
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_BST(arr):
    # pass indexes
    build_BST_helper(arr,0,len(arr)-1)


def build_BST_helper(arr,l,r):
    if l>r:
        return
    mid = (l+r)/2
    root = Node(arr[mid])
    root.left = build_BST_helper(arr[l:mid],l, mid-1)
    root.right = build_BST_helper(arr[mid+1:r],mid+1,r)
    return root

def inorder(root):
    if not root:
        return None
    inorder(root.left)
    print root.val
    inorder(root.right)

inorder(build_BST([1,2,3,4,5,6,7,8]))

