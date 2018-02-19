"""
https://articles.leetcode.com/construct-binary-tree-from-inorder-and-preorder-postorder-traversal/
http://edwardliwashu.blogspot.com/2013/01/construct-binary-tree-from-preorder-and.html
https://www.youtube.com/watch?v=PAYG5WEC1Gs
"""
class Node:
    # Constructor to create a new binary node
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def buildTree(inorder, preorder):
    il = len(inorder)
    pl = len(preorder)
    return buildTreehelper(inorder,0,il-1,preorder,0,pl-1)

def buildTreehelper(inorder,in_st,in_end, preorder, pre_st, pre_end):
    if in_st > in_end:
        return None

    rootindex = [ i for i in xrange(len(inorder)) if inorder[i] == preorder[pre_st]][0]
    root = Node(preorder[pre_st])
    newlen = rootindex - in_st
    #print rootindex, newlen
    root.left = buildTreehelper(inorder, in_st, rootindex-1, preorder, pre_st+1, pre_st + newlen )
    root.right = buildTreehelper(inorder, rootindex+1, in_end, preorder, pre_st+newlen+1, pre_end)
    return root

## modification, given inorder and postorder

def buildTreefromPostorder(inorder, instart, inend, postorder, postst, postend):
    if instart > inend:
        return None
    rootindex = [i for i in xrange(len(inorder)) if inorder[i] == postorder[postend]][0]



def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) +1

def print_nodes(q):
    for each in q:
        print each.val,

def bfs(root):
    if root is None:
        return None
    queue=[root]
    queue2=[]
    print queue[0].val
    while queue:

        c = queue.pop(0)

        if c.left:
            queue2.append(c.left)
        if c.right:
            queue2.append(c.right)

        if len(queue) == 0:

            for each in queue2:
                print each.val,
            print
            queue,queue2 = queue2, queue



inorder = [3,5,7,10,15,20,30]
preorder = [10,5,3,7,20,15,30]
newroot = buildTree(inorder, preorder)

bfs(newroot)