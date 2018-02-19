"""
http://cslibrary.stanford.edu/110/BinaryTrees.html

http://techieme.in/count-binary-search-trees/

n=1, trees = 1
n=2, trees = 2
n=3, trees  = 5


The base case is t(0) = 1 and t(1) = 1, i.e. there is one empty BST and there is one BST with one node.

t(2) = t(1)(t0) * t(0)*t(1)
t(2) =

Strategy: consider that each value could be the root.
 Recursively find the size of the left and right subtrees.
"""

def find_how_many_trees(n):
    sum = 0
    if n <=1:
        return 1
    else:
        # there will be one value at the root, with whatever remains
        # on the left and right each forming their own subtrees.
        # Iterate through all the values that could be the root...
        for node in xrange(1,n+1):
            left = find_how_many_trees(node - 1)
            right = find_how_many_trees(n - node)
            #print n,left, right
            sum += left*right
    return sum



print find_how_many_trees(2) # 2
print find_how_many_trees(3) # 5
print find_how_many_trees(4) #14
print find_how_many_trees(5) #42
print find_how_many_trees(6) #132
