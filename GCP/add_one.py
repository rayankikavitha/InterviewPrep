# add one 
# given [9]  output [1,0]
# given [7,8,9] output [7,9,0]
# given [9,9,9] output [1,0,0,0]

def addone(nums):
    n = len(nums)
    for i in range(len(nums)-1,-1,-1):
        if nums[i] < 9:
            nums[i] += 1
            return nums;
        nums[i] = 0
    nums.insert(0,1)
    return nums

print addone([7,8,9])
print addone([9,9,9])