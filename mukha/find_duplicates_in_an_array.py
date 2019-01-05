# with out using memory using the same list indexes as hash map items
def find_duplicates(nums):
    """
    o(n) - no extra memory or sorting. Use array indexes and make them negative as you keep visiting
        If you have seen negative value, that means that current element is duplicate
    :param nums:
    :return:
    """
    result = []
    for x in nums:
        if nums[abs(x) - 1] < 0:
            result.append(abs(x))
        else:
            nums[abs(x) - 1] = -1 * nums[abs(x) - 1]
            print nums
    return result


nums = [4,3,2,7,8,3,2,1]
print find_duplicates(nums)

def find_duplicates_using_extra_mem(nums):
    res =[]
    d={}
    for num in nums:
        if num in d:
            res.append(num)
        else:
            d[num] = 1
    return res

nums1 = [4,3,2,7,8,3,2,1]
print find_duplicates_using_extra_mem(nums1)


def find_first_duplicate(arr,n):
    """
    given an arry and n, if the array consits of values from 1 to n, find the first duplicate
    n = 4, arr = 1221 return 2
    n = 3, arr = 123 return None
    n = 3 , arr = 333 return 3
    n=4, arr = 1212 return 1
    constraints: no extra memory
    :param arr:
    :param n:
    :return:
    """
    res = None
    arr =[0]+arr
    print arr
    for i in range(0,n+1):
        if arr[i] != i: # i = 2, p = 3 v = 2
            print i,arr[i]
            if arr[arr[i]] == arr[i]:
                return arr[i]
    return res
print "**********************"
print find_first_duplicate([1,2,2,1],4)
print find_first_duplicate([1,2,1,2],4)
print find_first_duplicate([3,3,3],3)

print find_duplicates([1,2,2,1])





