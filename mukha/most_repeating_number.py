given=[0,0,3,4,5,4,4,4,4 ]
def find_the_most_repeating_num(nums):
    """
    Using extra memory
    :param nums:
    :return:
    """
    d={}
    for num in nums:
        d[num] = d.get(num,0) + 1
    print d
    return [k for k,v in d.iteritems() if v == max([ v for v in d.values()])]

print find_the_most_repeating_num(given)

def repeating_num_with_no_meme(nums):
    """
    condition : all the numbers in the list should be <= len(nums) K
    Given an array of size n, the array contains numbers in range from 0 to k-1 where k is a positive integer and k <= n.
    Find the maximum repeating number in this array. For example, let k be 10 the given array be
    arr[] = {1, 2, 2, 2, 0, 2, 0, 2, 3, 8, 0, 9, 2, 3}, the maximum repeating number would be 2.
     Expected time complexity is O(n) and extra space allowed is O(1). Modifications to array are allowed.
    :param nums:
    :return:
    """
    k = len(nums)
    print k
    for num in nums:
        nums[num % k] += k
        print nums
    # return index of the highest element
    return nums.index(max(nums))

#given2 = [1, 2, 2, 2, 0, 2, 0, 2, 3, 8, 0, 9, 2, 3]
#print "most repeating with out memory = "
#print repeating_num_with_no_meme(given)
#print repeating_num_with_no_meme(given2)
print repeating_num_with_no_meme([0,0,3,4,5,4,4,4])

def helper(nums):
    d={}
    for num in nums:
        d[num] = d.get(num,0)+1
    return [k for k,v in d.iteritems() if v == max(d.values())]
def helper2(nums):
    # [2,3,4,1,2]
    k=len(nums)
    for num in nums:
        nums[num%k] += k
        print nums
    return nums.index(max(nums))

print helper2([2,3,4,1,2])
