"""
If all the nodes in a tree have same values, they are called uni-val trees
or single value trees

Method:
starts bottom up.

"""
class Node:
    # Constructor to create a new binary node
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# This function increments count by number of single
# valued subtrees under root. It returns true if subtree
# under root is Singly, else false.
def countSingleRec(root, count):
    # Return False to indicate None
    if root is None:
        return True

    # Recursively count in left and right subtrees also
    left = countSingleRec(root.left, count)
    right = countSingleRec(root.right, count)

    # If any of the subtress is not singly, then this
    # cannot be singly
    if left == False or right == False:
        return False

    # If left subtree is singly and non-empty , but data
    # doesn't match
    if root.left and root.val != root.left.val:
        return False

    # same for right subtree
    if root.right and root.val != root.right.val:
        return False

    # If none of the above conditions is True, then
    # tree rooted under root is single valued,increment
    # count and return true
    count[0] += 1
    return True


# This function mainly calss countSingleRec()
# after initializing count as 0
def countSingle(root):
    # initialize result
    count = [0]

    # Recursive function to count
    countSingleRec(root, count)

    return count[0]


# Driver program to test

"""Let us contruct the below tree 
            5
          /   \
        4       5
       /  \      \
      4    4      5
"""
root = Node(5)
root.left = Node(4)
root.right = Node(5)
root.left.left = Node(4)
root.left.right = Node(4)
root.right.right = Node(5)
countSingle(root)
print "Count of Single Valued Subtress is", countSingle(root)