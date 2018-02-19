"""

"""
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder(root, result):
    if not root:
        return None
    inorder(root.left,result)
    result.append(root.val)
    inorder(root.right, result)


def kth_smallest(root, k):
    #inorder traversal and kth position
    res =[]
    inorder(root, res)
    print res
    return res[k]

# from leetcode
def kthsmallest(root, k):
    for val in inorder_with_yield(root):
        if k == 1:
            return val
        else:
            k -=1

def inorder_with_yield(root):
    if root is not None:
        for val in inorder_with_yield(root.left):
            yield val
        yield val
        for val in inorder_with_yield(root.right):
            yield val

# Driver program to test binary tree node

root1 = Node(9)
root1.left = Node(5)
root1.right = Node(13)
root1.left.left = Node(3)
root1.left.right = Node(7)
root1.right.left = Node(11)
root1.right.right = Node(15)

#print kth_smallest(root1,3)
print kthsmallest(root1,3)