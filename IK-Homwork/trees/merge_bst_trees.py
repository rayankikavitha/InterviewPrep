"""
Merge BST trees


Option 1:
Traverse each tree, you get sorted array
Merge sorted arrays
Build new BST tree o(m+n)
Option 2:
inplace merging with doubly linked list O(m+n)

https://www.geeksforgeeks.org/merge-two-balanced-binary-search-trees/
"""
class Node:
    # Constructor to create a new binary node
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def Inorder(root):
    result =[]
    Inorder_helper(root, result)
    return result

def Inorder_helper(root,result=[]):
    if root == None:
        return None
    Inorder_helper(root.left, result)
    result.append(root.val)
    Inorder_helper(root.right, result)

def merge_sort(input1, input2):
    result =[]
    i,j = 0,0
    while i < len(input1) and j < len(input2):
        if input1[i] < input2[j]:
            result.append(input1[i])
            i +=1
        else:
            result.append(input2[j])
            j +=1
    if i < len(input1):
        result += input1[i:]
    if j < len(input2):
        result += input2[j:]
    return result

def create_bst(arr,st, end):
    if st > end:
        return None
    mid = (st + end)/2
    #print st,end,mid
    cnode = Node(arr[mid])
    cnode.left = create_bst(arr, st, mid-1)
    cnode.right = create_bst(arr, mid+1, end)
    return cnode


def merge_bst(root1, root2):
    tree1 = Inorder(root1)
    tree2 = Inorder(root2)
    print tree1, tree2
    sorted_result = merge_sort(tree1, tree2)
    print sorted_result

    newbst_root = create_bst(sorted_result, 0 , len(sorted_result) - 1)
    print newbst_root
    print bfs(newbst_root)





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

def print_nodes(q):
    for each in q:
        print each.val,

def height(root):
    if root is None:
        return 0
    return max(height(root.left), height(root.right)) + 1


# Driver program to test binary tree node

root1 = Node(9)
root1.left = Node(5)
root1.right = Node(13)
root1.left.left = Node(3)
root1.left.right = Node(7)
root1.right.left = Node(11)
root1.right.right = Node(15)

root2 = Node(10)
root2.left = Node(4)
root2.right = Node(14)
root2.left.left = Node(2)
root2.left.right = Node(6)
root2.right.left = Node(12)
root2.right.right = Node(16)

merge_bst(root1,root2)