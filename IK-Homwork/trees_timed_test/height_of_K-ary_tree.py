"""
Given an array of
Example k = 3 , means root as 3 childresn

for a tree with 1,2,3,4,5

there will be
     1
    / |  \
    2  3  4
   /
   5
height = 2

"""

class Node:
    def __init__(self, val, child = []):
        self.val = val
        self.child = child


def find_height_of_k_array_tree(root, k):
    maxh = 0
    if root is None:
        return -1
    for each in root.child:
        maxh = max(maxh+1, max([find_height_of_k_array_tree(each) for each in root.child]))
    return maxh+1

