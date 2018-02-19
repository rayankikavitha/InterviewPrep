"""
Very well known interview problem

Given a binary tree, check if its a binary search tree
Duplicate elements are not allowed in a binary search tree
https://discuss.leetcode.com/topic/4659/c-in-order-traversal-and-please-do-not-rely-on-buggy-int_max-int_min-solutions-any-more/5

1) We can do inorder travel and it should give an sorted list

"""


import sys
import os

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def createTree(data):
    def deserialize():
        val = next(vals,None)
        if val == None:
            return None
        if val == '#':
            return None
        node = Node(int(val))
        node.left = deserialize()
        node.right = deserialize()
        return node
    vals = iter(data.split())
    return deserialize()

t= "10 # 5 20 # 3 8 # 30"

print createTree(t)


def  isBST(root):
    return isValidBST(root,floor=float('-inf'), ceiling=float('inf'))


def isValidBST(root, floor=float('-inf'), ceiling=float('inf')):
    if not root:
        return True
    if root.val <= floor or root.val >= ceiling:
        return False
    # in the left branch, root is the new ceiling; contrarily root is the new floor in right branch
    return isValidBST(root.left, floor, root.val) and isValidBST(root.right, root.val, ceiling)

def isValidBST2(self, root, left=float('-inf'), right=float('inf'), ):
    return not root or left < root.val <right and isValidBST(root.left,left, root.val and isValidBST(root.right, root.val, right))

print isBST(createTree(t))