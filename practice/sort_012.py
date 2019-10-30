
"""
print a tree level order


"""

def height(node):
	if 

def level_order(root):
	q=[root]
	result = []
	while q:
		curnode = root.children





"""
order numbers - [2,1,0,1,2,0,2,1,0]
"""



def sort_012(nums):
	left,mid,right = 0,0,len(nums)-1
	while mid < right:
		if nums[mid] == 0:
			nums[mid],nums[left] = nums[left],nums[mid]
			left += 1
		elif nums[mid] == 2:
			nums[mid],nums[right] = nums[right], nums[mid]
			right -=1
		else:
			mid +=1
		print (nums,left,right,mid)
	return nums

#print (sort_012([2,1,0,2,1,0,1,2,0,0,1,1,2,0,1]))



