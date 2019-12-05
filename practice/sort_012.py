
nums=[1,5,4,6,0,4,11,-1,9,2]
def threesum(nums,k):
	result=[]
	nums.sort()
	print (nums)
	i =0
	while i < len(nums)-2:
		if i > 0 and nums[i] == nums[i-1]:
			i +=1
		curnum = nums[i]
		start = i+1
		end = len(nums)-1
		print (i,start,end)
		while start < end:
			cursum = nums[i] + nums[start] + nums[end]
			if cursum < k:
				start +=1
			elif cursum > k:
				end -=1
			else:
				result.append((nums[i],nums[start],nums[end]))
				start +=1
				end -=1
		i += 1
	return result


print (threesum(nums,10))
			




"""
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1), ('yellow',1)]
from collections import defaultdict
def match_tuples(given):
	d=defaultdict(list)
	for each in given:
		d[each[0]].append(each[1])
	return d

print (match_tuples(s))



t = ( (1,3),(4,5),(3,1),(8,9),(5,4))
def match_tuples2(input):
    res=[]
    res.append( [(each[0],each[1]) for each in input if (each[1],each[0]) in input])

    return res

print (match_tuples2(t))


# top k frequency words
#https://gist.github.com/nwadams/f4bfe01699c3e87f629c416978c4dd48

# Recursive string permutations
def get_permutations(string):

    # Generate all permutations of the input string
    
    if len(string) <= 1:
        return set([string])
    all_chars_except_last = string[:-1]
    last_char = string[-1]
    perm_of_all_chars_except_last = get_permutations(all_chars_except_last)
    results =set()
    for one_perm_of_all_chars_except_last in perm_of_all_chars_except_last:
        for position in range(len(all_chars_except_last)+1):
            result = (one_perm_of_all_chars_except_last[:position]+last_char+\
            one_perm_of_all_chars_except_last[position:])
            results.add(result)
    return results




wishlists = [
  "U1,Amsterdam,Barcelona,London,Prague",
  "U2,Shanghai,Hong Kong,Moscow,Sydney,Melbourne",
  "U3,London,Boston,Amsterdam,Madrid",
  "U4,Barcelona,Prague,London,Sydney,Moscow",
  "U5,Amsterdam,Barcelona,London,Prague"
]


def prasetext(wishlists):
	buckets = {}
	for userrow in wishlists:
		each= userrow.split(',')
		buckets[each[0]] =[x for x in each[1:]]
	return buckets


#find a buddy for a guest if the wish list places match alteast 50%
def buddymap(wishlists, guest):
	buckets = prasetext(wishlists)
	buddy_result=[]
	if guest not in buckets.keys():
		return -1

	guestitems = set(buckets[guest])
	min_match_need = len(guestitems)//2

	for bucket in buckets.items():
		user_id,user_items = bucket
		if user_id != guest:
			match_count = len(guestitems.intersection(set(user_items)))
			if match_count >= min_match_need:
				buddy_result.append((user_id,match_count))
	# now we got buddy's matching greater than 50% wish list items
	# return them in the order of highest match to lowest
	buddy_result.sort(key =lambda x: -x[1])
	return [x[0] for x in buddy_result], buckets


#print(buddymap(wishlists,'U1'))
# recommend new places for the guest 
def find_recommendation(wishlists,guest):
	buddy_list,wishlist = buddymap(wishlists, guest)
	recommendations = set()
	guest_items=set(wishlist[guest])
	for buddy in buddy_list:
		current_bucket_items = wishlist[buddy]
		for each in current_bucket_items:
			recommendations.add(each)
	#print recommendations
	return recommendations - guest_items

print find_recommendation(wishlists, 'U1')


















given = ['i','love','coffee','dog','walk','i','coffee','coffee','my','day','my','day','day','day']
import heapq
def topk(given,x):
	d = {}
	h=[]
	result=[]
	for word in given:
		d[word] = d.get(word,0)+1

	for k,v in d.iteritems():
		heapq.heappush(h,(v,(k,v)))

		if len(h) > x:
			heapq.heappop(h)
			print (h)

	return [ x[1] for x in h]


#print (topk(given,2))















order numbers - [2,1,0,1,2,0,2,1,0]




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

"""

