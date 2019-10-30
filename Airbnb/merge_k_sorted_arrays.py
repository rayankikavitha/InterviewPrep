input = [ [5,10,15,20,25,30],[1,8,16,24,32,40],[10,20,30,40,50]]
import heapq

def merge_k_sorted_arrays(nums):
	h=[]
	result=[]
	for i,v in enumerate(nums):
		heapq.heappush(h, (v[0],i,0))

	while len(h) > 0:
		curr_min_tuple = heapq.heappop(h)
		item, array_index,item_index = curr_min_tuple
		result.append(item)
		if item_index < len(input[array_index])-1:
			heapq.heappush(h,(input[array_index][item_index+1],array_index,item_index+1))

	return result


print (merge_k_sorted_arrays(input))



