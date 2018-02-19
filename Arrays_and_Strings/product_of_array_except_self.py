"""
Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Solve it without division and in O(n).

For example, given [1,2,3,4], return [24,12,8,6].
"""
import operator
def productExceptSelf(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    forward, backward = [],[]
    f = lambda x,y : x*y
    for i in xrange(1,len(nums)+1):
        forward.append(reduce(f,nums[0:i]))
    print forward
    for i in xrange(len(nums)-1,-1,-1):
        backward.append(reduce(f,nums[i:]))
    backward_rev = backward[::-1]
    print backward_rev
    # add 1 to forward array in the beginning
    # add 1 to backward array in the end
    forward.insert(0,1)
    backward_rev.append(1)
    print forward,backward_rev
    # make the final division array
    #final = [ x * y for x in forward[:len(forward)-1] for y in backward[1:]]
    final = []
    for i in xrange(len(forward)-1):
        final.append(forward[i] * backward_rev[i+1])
    print final

def productExceptSelf1(nums):
    p = 1
    n = len(nums)
    output = []
    for i in range(0, n):
        output.append(p)
        p = p * nums[i]
        print p,output
    p = 1
    for i in range(n - 1, -1, -1):
        output[i] = output[i] * p
        p = p * nums[i]
        print p,output
    return output



nums = [1,2,3,4]
productExceptSelf1(nums)
 1
 11
 121
 1331
14641

def helper(121)
    output 1331