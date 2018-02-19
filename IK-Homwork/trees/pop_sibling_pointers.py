"""
Let us contruct the below tree
            5  -> None
          /   \
        4   ->   5  -> None
       /  \      \
      4 ->  4 ->  5  -> None

https://discuss.leetcode.com/topic/1106/o-1-space-o-n-complexity-iterative-solution/36
"""
class TreeLinkNode:
    # Constructor to create a new binary node
    def __init__(self, val):
        self.val = val
        self.next = None
        self.left = None
        self.right = None


def connect(root):
    while root:
        cur = tmp = TreeLinkNode(0)
        while root:
            if root.left:
                cur.next = root.left
                cur = root.left
            if root.right:
                cur.next = root.right
                cur = root.right
            root = root.next
        root = tmp.next