
def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1


def bfs(root):
	if root is None:
		return None
	q = [root]
	ph = height(root)+1
	while q:
		curr = q.pop(0)
		if height(q[0]) < ph:
			print (q)
            ph = height(q[0])
            print ('#######')

		print (curr.key)
		if curr.left:
			q.append(curr.left)
		if curr.right:
			q.append(curr.right)
		


print (bfs(root))



"""
Very well known interview problem

Given a binary tree, check if its a binary search tree
Duplicate elements are not allowed in a binary search tree
https://discuss.leetcode.com/topic/4659/c-in-order-traversal-and-please-do-not-rely-on-buggy-int_max-int_min-solutions-any-more/5

1) We can do inorder travel and it should give an sorted list

"""
def isBST(root):
	return isValidBST(root,floor=float('-inf'), ceiling=float('inf'))

def isValidBST(root, floor=float('-inf'), ceiling=float('inf')):
	if root is None:
		return True
	if root <= floor or root >= ceiling:
		return False
	return isBST(root.left, floor, root.key) and isBST(root.right, root.key,ceiling)





# find least common ancestor

def find_path(root, k,path=[]):
	if root is None:
		return None
	path.append(root.key)
	if root.key == k : 
		return True
	# find k in the left and right subtree
	if (root.left and find_path(root.left,k ,path)) or (root.right and find_path(root.right, k, path)):
		return True

	# At this point, remove the root note from the pop and return False
	path.pop()
	return False
	


def findLCA(root, val1, val2):
	lca = None
	if root is None:
		return None
	path1, path2 = [],[]

	if not find_path(root, val1, path1) or not find_path(root, val2, path2):
		return False
	l = min(len(path1),len(path2))
	i = 0
	while i < l:
		if path1[i] != path2[i]:
			break
		i += 1
	return path1[i-1]


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

print (findLCA(root, 4, 5, ))
print (findLCA(root, 4, 6))
print (findLCA(root, 3, 4))
print (findLCA(root, 2, 4))




