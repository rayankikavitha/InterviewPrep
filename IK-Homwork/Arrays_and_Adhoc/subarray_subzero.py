"""
Find a continous subset whos sum is zero.There can be duplicates

Input: [5,1,2,-3,6,-4,1]
output:[1,2,-3] or [-3,6,-4,1] any one subset

What is the complexity, if we need to print all subsets?

This is variation of maximum subarray problem.

Sounds like a dequeue problem with sliding window.

https://www.geeksforgeeks.org/find-if-there-is-a-subarray-with-0-sum/

Dict: We can also use hashing. The idea is to iterate through the array and for every element arr[i],
calculate sum of elements form 0 to i (this can simply be done as sum += arr[i]).
 If the current sum has been seen before, then there is a zero sum array.
 Hashing is used to store the sum values, so that we can quickly store sum and find out whether the current sum is
 seen before or not.

"""

def find_subarray_sumzero(nums):
    """
    Returns true/false
    :param nums:
    :return:
    """
    d={}
    s = 0
    for i in xrange(len(nums)):
        s += nums[i]
        if s not in d:
            d[s] = i
        else:def function():
            pass
            return True
    print d
    return False

def find_subarray_sumzero_indexes(nums):
    d={}
    result =[]
    s = 0
    for i in xrange(len(nums)):
        s += nums[i]
        #if sum is 0, we found a subarray starting from 0 and ending at index i
        if s == 0:
            d[s] = [i]
            result.append((0,i))
        elif s not in d:
            d[s]=[i]
        # if the sum is already in the dictionary we found zerosum
        # from previous indexes to current index
        else:
            for each in d[s]:
                result.append((each+1,i))
            d[s].append(i)

    print d
    return result

def find_subarray_sumzero_indexes2(nums):
    d={}
    result =[]
    s = 0
    for i in xrange(len(nums)):
        s += nums[i]
        #if sum is 0, we found a subarray starting from 0 and ending at index i
        if s == 0:
            d[s] = [i]
            result.append((0,i))
        elif s not in d:
            d[s]=[i]
        # if the sum is already in the dictionary we found zerosum
        # from previous indexes to current index
        else:
            for each in d[s]:
                result.append((each+1,i))
            d[s].append(i)

    #print d
    #return result   # it has indexes only
    # now translate it into subarrays
    for each in result:
        print nums[each[0]:each[1]+1]


#print find_subarray_sumzero([5,1,2,-3,6,-4,1])
#print find_subarray_sumzero([5,1,2,6,1])
print find_subarray_sumzero_indexes2([5,1,2,-3,6,-4,1])
#print find_subarray_sumzero_indexes([5,1,2,6,1])
#print find_subarray_sumzero_indexes([6, 3, -1, -3, 4, -2, 2,4, 6, -12, -7])
#print find_subarray_sumzero_indexes([0,1,2,3,4,-10])


