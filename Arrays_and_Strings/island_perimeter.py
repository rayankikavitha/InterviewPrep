s=[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

islands*4 - neighbors * 2

def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    print nums
    if len(nums) == 1:
        return nums[0]
    for i in range(0,len(nums) - 1, 2):
        if nums[i] != nums[i + 1]:
            return nums[i]
    return nums[-1]


print singleNumber([1,2,3,1,3,2,4])
print singleNumber([1,2,3,1,3])