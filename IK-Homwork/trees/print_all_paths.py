"""
https://www.geeksforgeeks.org/given-a-binary-tree-print-out-all-of-its-root-to-leaf-paths-one-per-line/

https://leetcode.com/problems/binary-tree-paths/discuss/

"""


def printAllPaths(root):
    printpaths(root, path=[], count=0)


def printpaths(root, path, count):
    if not root:
        return path
    path[count] = root.val
    count += 1
    if root.left is None and root.right is None:
        printarray(path)
    else:
        printpaths(root.left, path, count)
        printpaths(root.right, path, count)


def printarray(path):
    for each in path:
        print each,
    print

print "********* This method is working fine *******************" \
      ""
# dfs recursively
# dfs recursively

def printAllPaths(root):
    if not root:
        return None
    res = []
    dfs(root, "", res)
    # print res
    for each in res:
        print each
    return res


def dfs(root, ls, res):
    if not root.left and not root.right:
        res.append(ls + str(root.val))
    if root.left:
        dfs(root.left, ls + str(root.val) + " ", res)
    if root.right:
        dfs(root.right, ls + str(root.val) + " ", res)

#output :