def quick_sort(nums):
	quick_sort_helper(nums,0,len(nums)-1)
	return nums
	
def quick_sort_helper(nums,low,high):
	if low < high:
		p = partition(nums, low, high)
		print (p)
		quick_sort_helper(nums,0,p-1)
		quick_sort_helper(nums,p+1,high)



def partition(nums,low, high):
	partition_value = nums[low]

	leftmark = low +1
	rightmark = high

	done = False
	while not done:
		while leftmark < rightmark and nums[leftmark] < partition_value:
			leftmark += 1
		while leftmark < rightmark and nums[rightmark] > partition_value:
			rightmark -=1

		if rightmark < leftmark:
			done = True
		else:
			#swap
			nums[leftmark],nums[rightmark] = nums[rightmark], nums[leftmark]
	# final swap to put the partition in its position
	nums[low],nums[rightmark] = nums[rightmark], nums[low]
	return rightmark


def quicksort(a_list):
    """Hoare partition scheme, see https://en.wikipedia.org/wiki/Quicksort"""
    def _quicksort(a_list, low, high):
        # must run partition on sections with 2 elements or more
        if low < high: 
            p = partition(a_list, low, high)
            _quicksort(a_list, low, p)
            _quicksort(a_list, p+1, high)
    def partition(a_list, low, high):
        pivot = a_list[low]
        while True:
            while a_list[low] < pivot:
                low += 1
            while a_list[high] > pivot:
                high -= 1
            if low >= high:
                return high
            a_list[low], a_list[high] = a_list[high], a_list[low]
            low += 1
            high -= 1
    _quicksort(a_list, 0, len(a_list)-1)
    return a_list




print (quicksort([2,34,0,10,9,5,59,1]))
"""
Merge sort

nums = [2,34,0,10,9,5]

"""
def merge_sort(nums):
	if len(nums)< 2:
		return nums
	mid = len(nums)//2
	left = merge_sort(nums[:mid])
	right = merge_sort(nums[mid:])
	return merge(left,right)

def merge(left, right):
    """
    Traverse both sorted sub-arrays (left and right), and populate the result array
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]

    return result


#print (merge_sort( [2,34,0,10,9,5,59,1]))






"""
move zeros to left

[1,0,5,3,53,0,0,0,43]
"""
def move_zeros_left(nums):
	start = 0
	for i in range(len(nums)):
		if nums[i] != 0:
			nums[start] = nums[i] 
			start += 1
	# fill zeros at the end
	for i in range(start,len(nums)):
		nums[i]= 0
	return nums

print (move_zeros_left([1,0,5,3,53,0,0,0,43]))




"""
Merge 2 sorted arrays

[1,3,5,7]
[2,4,5, 6,8]

"""
def merge_two_sorted_arrays(arr1, arr2):
	i,j=0,0
	result =[]
	while i < len(arr1) and j < len(arr2):
		if arr1[i] < arr2[j]:
			result.append(arr1[i])
			i +=1
		elif arr1[i] > arr2[j]:
			result.append(arr2[j])
			j += 1
		else:
			result.append(arr1[i])
			result.append(arr2[j])
			i +=1
			j += 1
	while i < len(arr1):
		result.append(arr1[i])
		i +=1
	while j < len(arr2):
		result.append(arr2[j])
		j += 1
	return result

print (merge_two_sorted_arrays([1,3,5,7],[2,4,5,6,8,9,10,11,12]))




"""
Given an array of numbers, positive integers only, group them in-place into evens and odds
Understand that grouping is just a special case of sorting.
Aim for o(n) , in-place

1,2,3,4,5,6,7,8

1,2,4,6,3,5,8,9,1


"""

def group_even_odd(nums):
	# logic for odd numbers left and even on right
	i, j = 0,len(nums)-1
	while i < j:
		eoi = nums[i] % 2
		eoj = nums[j] % 2
		# both are odd
		if eoi == eoj  and eoi == 1: 
			j -=1
		elif eoi == eoj and eoi == 0:
			 i += 1
		elif eoi != eoj and eoi == 1 and eoi == 0:
			nums[i],nums[j] = nums[j],nums[i]
			i += 1
			j -= 1
		else:
			i +=1
			j -=1
	return nums

nums=[1,2,3,4,5,6,7,8,1]
print (group_even_odd(nums))
