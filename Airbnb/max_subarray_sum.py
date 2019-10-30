"""
Given an array, describe an algorithm to identify the subarray with the maximum 
sum.  For example, if the input is [1, ‐3, 5, ‐2, 9, ‐8, ‐6, 4], the output would be [5, ‐2, 
9].

Keep track of 3 variables , max seens so far, min seen so far and sum at the end 

"""

def max_subarray_sum(nums):
	"""
	return sum
	"""
	max_so_far, min_so_far, sum_so_far = 0,0,0
	for num in nums:
		sum_so_far += num
		min_so_far = min(min_so_far, sum_so_far)
		max_so_far = max(max_so_far, sum_so_far - min_so_far)
		print (sum_so_far, min_so_far,max_so_far)
	return max_so_far


print (max_subarray_sum([1,-3,5,-2,9,-8,-6,4]))

print (max_subarray_sum([1,-3,5,-2,9,-8,-6,4, 10]))