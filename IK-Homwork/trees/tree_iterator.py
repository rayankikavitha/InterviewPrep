# Solution:
# with parent pointer : https://stackoverflow.com/questions/12850889/in-order-iterator-for-binary-tree
# with out parent pointer :
# https://discuss.leetcode.com/topic/6575/my-solutions-in-3-languages-with-stack
"""
 use Stack to store directed left children from root.
When next() be called, I just pop one element and process its right child as new root.
The code is pretty straightforward.

So this can satisfy O(h) memory, hasNext() in O(1) time,
But next() is O(h) time.



"""
class Node:
    # Constructor to create a new binary node
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Definition for a  binary tree node
class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = list()
        self.pushAll(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stack

    # @return an integer, the next smallest number
    def next(self):
        tmpNode = self.stack.pop()
        self.pushAll(tmpNode.right)
        return tmpNode.val

    def pushAll(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left



# Driver program to test binary tree node

root1 = Node(9)
root1.left = Node(5)
root1.right = Node(13)
root1.left.left = Node(3)
root1.left.right = Node(7)
root1.right.left = Node(11)
root1.right.right = Node(15)


b = BSTIterator(root1)
while b.hasNext():
    print b.next()