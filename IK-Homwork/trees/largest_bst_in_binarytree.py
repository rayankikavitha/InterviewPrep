"""

http://www.ideserve.co.in/learn/size-of-largest-bst-in-binary-tree
"""
class Node:
    # Constructor to create a new binary node
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def findsizeoflargestBST(root, min_ref, max_ref, isbst, max_size):
    # base case
    if root is None:
        isbst[0] = True
        return 0
    min_ref[0] = float('+inf')
    max_ref[0] = float('-inf')
    print min_ref, max_ref
    ls = findsizeoflargestBST(root.left, min_ref, max_ref, isbst, max_size)
    isleftvalid = isbst[0] and (max_ref[0] < root.val)

    tempMin = min(root.val, min_ref[0])
    tempMax = max(root.val, max_ref[0])

    rs = findsizeoflargestBST(root.right, min_ref, max_ref, isbst, max_size)
    isRightValid = isbst[0] and (root.val < min_ref[0])

    min_ref[0] = min(tempMin, min_ref[0])
    max_ref[0] = max(tempMax, max_ref[0])
    #print isleftvalid, isRightValid
    if isleftvalid and isRightValid:
        isbst[0] = True
        if (1+ ls + rs) > max_size[0]:
            max_size[0] = 1 + ls + rs
            #print max_size[0]
        return 1+ ls + rs

    isbst[0] = False
    return -1


def findlargestBST(root):
    min_ref =[1]
    max_ref = [1]
    isbst = [True]
    max_size = [1]
    findsizeoflargestBST(root, min_ref, max_ref, isbst, max_size)
    print max_size[0]

#https://discuss.leetcode.com/topic/36966/short-python-solution
"""
My dfs returns four values:

N is the size of the largest BST in the tree.
If the tree is a BST, then n is the number of nodes, otherwise it's -infinity.
If the tree is a BST, then min and max are the minimum/maximum value in the tree.
"""
def largestBSTSubtree(root):
    def dfs(root):
        if not root:
            return 0, 0, float('inf'), float('-inf')
        N1, n1, min1, max1 = dfs(root.left)
        N2, n2, min2, max2 = dfs(root.right)
        n = n1 + 1 + n2 if max1 < root.val < min2 else float('-inf')
        return max(N1, N2, n), n, min(min1, root.val), max(max2, root.val)
    return dfs(root)[0]

# Driver Program to test
root = Node(10)
root.left = Node(6)
root.right = Node(12)
root.left.left  = Node(7)
root.left.right = Node(4)
root.right.left = Node(9)
root.right.right = Node(14)
root.right.right.left = Node(13)
root.right.right.right = Node(16)

findlargestBST(root)
print largestBSTSubtree(root)