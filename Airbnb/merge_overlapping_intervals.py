import collections

# find minimum in a rotated sorted array
def find_min(arr):
	low,high=0,len(arr) -1
	return find_min_helper(arr,low,high)

def find_min_helper(arr,low,high):

	mid = (low+high)//2

	if mid < high and arr[mid] > arr[mid+1]:
		return arr[mid+1]
	if mid > low and arr[mid] < arr[mid-1]:
		return arr[mid]
	
	if arr[high] > arr[mid]:
		return find_min_helper(arr, low, mid -1)
	else:
		return find_min_helper(arr, mid+1, high)


print (find_min([6,7,8,1,2,3,4,5]))
print (find_min([6,7,8,9,10,1,2]))
print (find_min([9,10,1,2,3,4,5,6,7,8]))




interval = collections.namedtuple('interval',('left','right'))
# variation with named tuples

def add_intervals(intervals):
	result = [intervals[0]]
	for each in intervals[1:]:
		last_interval = result[-1]
		if last_interval.right >= each.left:
			new_interval = interval(min(last_interval.left,each.left), max(last_interval.right,each.right))
			result.append(new_interval)
		else:
			result.append(last_interval)
	return result



# if the intervals are array
def merge_intervals(intervals):
	intervals.sort()
	result =[intervals[0]]
	for interval in intervals[1:]:
		if result[-1][1] >= interval[0]:
			result[-1][1] = max(result[-1][1],interval[1])
		else:
			result.append(interval)
	return result


#print (add_intervals([ (1,3),(2,4),(5,7),(6,8)]))
#print (merge_intervals([ [1,5],[2,4],[6,9],[8,10]]))

