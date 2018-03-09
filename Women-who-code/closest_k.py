"""
Given a sorted list, find kth nearest element given an element n
This is a binary search tree question, to get the order to log(n)
 Given a binary search tree and a value k. Find a node in the binary search tree whose value is closest to k.
Solution:  Since the tree is sorted, we search the appropriate side for an exact match, until we find one, or miss completely.
On the way back up, we look for a closer match.


"""
class bstnode():
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

#build BST
root = bstnode(20)
root.left = bstnode(15)
root.right = bstnode(30)
root.left.left = bstnode(12)
root.left.right = bstnode(17)
root.right.right = bstnode(40)
root.right.right.right = bstnode(50)

def find_nearest(root, k):
    """
    Given a binary search tree and a value k. Find a node in the binary search tree whose value is closest to k.
    for k = 42, output = 40
    :param root: root of a binary tree
    :param n: element
    :param k: kth value
    :return:
    """
    if root is None:
        return None

    if root.val == k:
        return root.val

    if root.val < k:
        temp = find_nearest(root.right, k)
    else:
        temp = find_nearest(root.left, k)
    # if the temp  is None, that means left and right subtrees are none, only root is nearest
    if temp is None:
        return root.val
    else:
        # find the closest between child value and the root
        if abs(root.val - k) < abs( temp - k):
            return root.val
        else:
            return temp


print find_nearest(root,19)



