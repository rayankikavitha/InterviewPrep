def bfs(root):
    queue =[root]
    ph = height(root) + 1
    while queue:

        # when the height changes, then we print the queue
        if height(queue[0]) < ph:
            print_nodes(queue)
            ph = height(queue[0])
            print '#'

        curr = queue.pop(0)

        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)

def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1


def print_nodes(q):
    for each in q:
        print each.val,

# Driver program to test binary tree node
class Node:
    # Constructor to create a new binary node
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print height(root)
print height(root.left)
print height(root.left.left)

print "****bfs****"
print bfs(root)