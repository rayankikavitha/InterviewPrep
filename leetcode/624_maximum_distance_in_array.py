"""
Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a-b|. Your task is to find the maximum distance.

Example 1:
Input:
[[1,2,3],
 [4,5],
 [1,2,3]]
Output: 4
Explanation:
One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Note:
Each given array will have at least 1 number. There will be at least two non-empty arrays.
The total number of the integers in all the m arrays will be in the range of [2, 10000].
The integers in the m arrays will be in the range of [-10000, 10000].


"""


def maxDistance(arrays):
    """
    :type arrays: List[List[int]]
    :rtype: int
    """
    mn = 10000
    mx = -10000
    res=0
    for a in arrays:
        res = max( res, max(mx - a[0], a[-1] - mn))
        mn = min(mn, a[0])
        mx = max(mx, a[-1])
        print res,mn,mx
    return res


input = [[1,2,3],[4,5],[1,2,3]]
input1=[[1,4],[0,5]]

print maxDistance(input1)