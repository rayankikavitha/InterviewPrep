"""
given = [[1],[[2,3]],[[[4,5]]],6]
output = [1,2,3,4,5,6]
"""

def flatten_list(nums):
	result=[]
	for num in nums:
		if type(num) != list:
			result.append(num)
		else:
			result += flatten_list(num)
			
	return result
	

nums = [[1],[[2,3]],[[[4,5]]],6]
print (flatten_list(nums))

"""
Reverse a string with spaces
"""
def reverse(strs):
	result =[]
	s = strs.split(' ')
	rs = [ word[::-1] for word in s]
	return ' '.join(rs)

print (reverse('Kavitha is smart'))