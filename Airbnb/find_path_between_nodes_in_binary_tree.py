class node():
	def __init__(self,val = None):
		self.val = val
		self.left = None
		self.right = None

# create a binary tree
"""
17
 / \
 6 46
 / \ \
 3 12 56
 / / \ /
 1 9 15 48
"""

root = node(17)
root.left=node(6)
root.right=node(46)
root.left.left = node(3)
root.left.right = node(12)
root.left.right.left = node(9)
root.left.right.right = node(15)
root.left.left.left = node(1)
root.right.right = node(56)
root.right.right.left =node(48)

# find path is find common acestor
def find_path(root, val1, path=[]):
	if root is None:
		return False
	path.append(root.val)
	if root.val == val1:
		return True
	if find_path(root.left, val1, path) or find_path(root.right, val1, path):
		return True
	path.pop()
	return False

def path_between_nodes(root, val1, val2):
	path_between = []
	path1, path2 = [], []
	i,j = 0,0
	if find_path(root,val1,path1) and find_path(root,val2,path2):
		print ("path exists")
	
	
	
	while i < len(path1) and j < len(path2):
		if i == j and path1[i] == path2[j]:
			i +=1
			j +=1
		else:
			intersection = i -1
			break
	print (path1, path2)
	# now printing the path comes in the pictures
	for i in range(len(path1)-1, intersection-1, -1):
		path_between.append(path1[i])
	for i in range(intersection+1, len(path2)):
		path_between.append(path2[i])

	return path_between

#print (root.val)

#print (path_between_nodes(root ,3, 15))



def dfs_inorder(root):
	# inorder left,value,right
	if root:
		dfs_inorder(root.left)
		print (root.val)
		dfs_inorder(root.right)

def dfs_preorder(root):
	if root:
		print (root.val)
		dfs_preorder(root.left)
		dfs_preorder(root.right)

def dfs_postorder(root):
	# inorder left,value,right
	if root:
		dfs_postorder(root.left)
		dfs_postorder(root.right)
		print (root.val)


dfs_preorder(root)
dfs_inorder(root)
dfs_postorder(root)


def bfs(root):
	if root:
		q=[root]
	while q:
		cur_node = q.pop()
		print (cur_node.val, end = ' ')
		if cur_node.left:
			q.insert(0,cur_node.left)
		if cur_node.right:
			q.insert(0,cur_node.right)


print ("breadth first search")
bfs(root)






