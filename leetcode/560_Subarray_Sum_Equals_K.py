
"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals
 to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2
https://leetcode.com/problems/subarray-sum-equals-k/solution/

The idea behind this approach is if you are caluclating the cumulative sum of an array
and at sum[i] and sum[j] , the cumulative sum is same, that means the values lying in between i and j add up to zero.
If we extend the same logic to K, if the cumulative sum difference of s[i] - s[j] = k,
then the values in between i, j add up to k.
"""


def subarraySum(nums, k):
    """
    using constant o(n)
    :type nums: List[int]
    :type k: int
    :rtype: int
    """

    d = {0:1}  # prefix sum array, so starting position also falls in the logic
    res = s = 0
    for n in nums:
        s = s + n  # increment current sum
        res = res+ d.get(s - k, 0)  # check if there is a prefix subarray we can take out to reach k
        d[s] = d.get(s, 0) + 1  # add current sum to sum count
        print d, res, s
    return res

def subarray2(nums,k):
    """
    o(n2)   brute force
    :param nums:
    :param k:
    :return:
    """
    count = 0
    for i in range(len(nums)):
        s = 0
        for j in range(i,len(nums)):
            s += nums[j]
            if s == k:
                count += 1
    return count

def subarraySum3(nums, k):
    """
    using constant o(n)
    :type nums: List[int]
    :type k: int
    :rtype: int
    """

    d = {nums[0]:1}  # prefix sum array, so starting position also falls in the logic
    res = s = 0
    for n in nums[1:]:
        s = s + n  # increment current sum
        res = res+ d.get(s - k, 0)  # check if there is a prefix subarray we can take out to reach k
        d[s] = d.get(s, 0) + 1  # add current sum to sum count
        print d, res, s
    return res

input = [3,4,7,2,-3,1,4,2]
print subarraySum(input,7)
print '*************'
print subarraySum3(input,7)
