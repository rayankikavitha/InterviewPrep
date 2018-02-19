"""
Popular interview Question
Given an array of numbers, nums, return an arry of numbers prodcuts
where products[i] is product of all nums[j], such that j!= i

Input = [1,2,3,4,5]
output = [120,60,40,30,24]

Do it in o(n) with out division
"""
def array_prodcut(nums):
    cp =[1]
    rcp =[1]
    result =[]
    # cumulative product from left to right
    for num in nums:
        newp = cp[len(cp)-1] * num
        cp.append(newp)
    # do the cumulative product for reverse, so get right to left
    for num in nums[::-1]:
        rnewp = rcp[len(rcp)-1] * num
        rcp.append(rnewp)
    print cp,rcp
    # cp, rcp will be like
    # [1,1,2,6,24,120]
    # [1,5,20,60,120,120]
    for i in xrange(1,len(cp)):

        p = cp[i-1] * rcp[len(cp)-i -1]
        result.append(p)
    return result

print array_prodcut([1,2,3,4,5])




