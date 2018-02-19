
def removeDuplicates1(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    #return len(set(nums))
    count=0
    for i in range(1,len(nums)):
        if nums[i]!=nums[i-1]:
            count+=1
    return count+1

print removeDuplicates1([1,1,2,3,3,4,5,5,6])