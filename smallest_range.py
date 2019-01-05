"""
Input:[[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].

"""
import heapq


def heappeek(h):
    c = heapq.heappop(h)
    heapq.heappush(h,c)
    return c[0]

def smallest_range(nums):
	k = len(nums)
	h=[]
	minrange = float("inf")
	currange = 0
	result =[]
	maxelement = 0
	for i,num in enumerate(nums):
		heapq.heappush(h, (nums[i][0],(i,0)))
		maxelement = max(maxelement, nums[i][0])
	print h

	while h and len(h)==k:
		#print h[0][0]
		currange = maxelement - heappeek(h)
		if currange < minrange:
			result = h
		val, pos = heapq.heappop(h)
		arrayindex,valueindex = pos
		if nums[pos[0]][pos[1]+1]:
			heapq.heappush(h, nums[arrayindex][valueindex+1])
			maxelement= max(maxelement,nums[arrayindex][arrayindex+1])

	return result

nums = [[4,10,15,24,26], [0,9,12,20], [5,18,22,30]]
print smallest_range(nums)