"""
Given a set of time intervals in any order,
merge all overlapping intervals into one which should have only mutually exclusive intervals
Example: [ (1,3),(2,4),(5,7),(6,8)]
output : [ (1,4),(5,8)]

Niloy talked about binary search tree to reduce the sorting o(nlogn)


Version 2:

Instead of extra space, use the same array to update the boundaries.

"""

def merge_overlapping_intervals(nums):
    """
    sorting o(nlongn), then o(n)
    Sort the intervals by start
    Merge consecutive if overlap
    If no overlap, add the merged interval to the output
    :param nums:
    :return:
    """
    nums.sort()
    result =[[nums[0][0],nums[0][1]]]
    #print result
    for num in nums[1:]:
        if result[len(result)-1][1] >= num[0]:
            result[len(result)-1][1] = max(num[1], result[len(result)-1][1])
        else:
            result.append([num[0],num[1]])
    return result








print merge_overlapping_intervals([ (1,3),(2,4),(5,7),(6,8)])
print merge_overlapping_intervals([ [1,5],[2,4],[6,9],[8,10]])


