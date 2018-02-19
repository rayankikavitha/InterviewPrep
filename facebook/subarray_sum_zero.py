given = [-3, 1, 2, -3, 4]
output = [ [0, 2], [1, 3]]
"""
-3,1,2 adds up to zero  1,2,-3 adds up to zero
This is O(N**2) very inefficient.

We can do with dictionary in o(n)

"""
def substring_sum_zero(given):
    result =[]
    for i in range(len(given)):
        start = i
        tot = 0
        for j in range(len(given[i+1:])):
            tot = tot + given[j]
            print tot
            if tot == 0:
                end = j+i
                print (start,end)
                result.append([start,end])
    return result


print substring_sum_zero(given)



def subarray_sumzero(nums):
    """
    O(n)
    :param nums:
    :return:
    """
    d={}
    result =[]
    s=0
    for i in range(len(nums)):
        s += nums[i]
        if s == 0:
            d[s] = i
            result.append([0,i])
        elif s not in d:
            d[s] = [i]
        else:
            for each in d[s]:
                result.append([each+1, i])
            d[s].append(i)
        print d
    return result

print subarray_sumzero(given)
given2 =[-3, 1, 2, -3, 4, -1]
print subarray_sumzero(given2)