"""
Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent,
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

"""


def sortColors( nums):
    i = j = 0
    for k in xrange(len(nums)):
        v = nums[k]
        print v
        nums[k] = 2
        if v < 2:
            nums[j] = 1
            j += 1
        if v == 0:
            nums[i] = 0
            i += 1
        print nums

print sortColors( [1,2,3,1,1,2,2,3,3,1,2])

t ='Name, age, sex'
v