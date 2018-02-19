"""
Find LCA for Binary tree
1. Using O(N)
2. No parent pointers

Option 1 : How about generating all the paths from the root to leaf and
finding the intersecting node from the leaf node or the last intersecting node from the root.
  - step 1: find the path from the root to node1
  - step 2: find the path from the root to node2
  - step 3: traverse the path, until you find the mismatch and store the previous matching value.

https://www.geeksforgeeks.org/lowest-common-ancestor-binary-tree-set-1/

"""


def findLCA(root, n1, n2):
    if root is None:
        return None
    path1 = []
    path2 = []
    if not find_path(root, n1, path1) or not find_path(root, n2, path2):
        return None
    i = 0
    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:
            break
        i += 1
    return path1[i - 1][0]


def find_path(root, k, path=[]):
    """
    Returns True/False, if a path exists between root and node k.
    Also, populates the path if it exists
    :param root:
    :param k:
    :param path:
    :return:
    """
    if root is None:
        return None
    # path.append(root.val)  < if you just need to return the value
    path.append((root, root.val))
    if root.val == k:
        return True
    # find k in the left or right subtree
    if (root.left != None and find_path(root.left, k, path)) or (root.right != None and find_path(root.right, k, path)):
        return True

    # If not present in subtree rooted with root, remove
    # root from path and return False
    path.pop()
    return False


# Driver Program to test

# Driver program to test above function
# Let's create the Binary Tree shown in above diagram


# A binary tree node
class Node:
    # Constructor to create a new binary node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print "LCA(4, 5) = %d" % (findLCA(root, 4, 5, ))
print "LCA(4, 6) = %d" % (findLCA(root, 4, 6))
print "LCA(3, 4) = %d" % (findLCA(root, 3, 4))
print "LCA(2, 4) = %d" % (findLCA(root, 2, 4))
