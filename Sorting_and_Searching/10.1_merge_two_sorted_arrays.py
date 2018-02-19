def merge_sort(nums):
    mid = len(nums)//2
    left = nums[:mid]
    right = nums[mid:]
    merge_sort(left)
    merge_sort(right)
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1
    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1
    while j < len(right):
        nums[k] = right(j)
        j += 1
        k += 1


"""
import heapq
h=[]

nums = [9,3,6,2,1,7,5,8,4]
for each in nums:
    heapq.heappush(h, each)
    heapq.h
print heapq.heappop(h)
#merge_sort(nums)
print nums
"""

def merger_first_into_second(arr1, arr2):
    arr3=[]*len(arr2)
    print arr3
    # i to iterate arr1, j to iterate arr2, k to iterate arr3
    i,j,k = 0,0,0
    while i < len(arr1) and j < len(arr1):
        print arr1[i],arr2[j]
        if arr1[i] < arr2[j]:
            arr3.append(arr1[i])
            i +=1
        else:
            arr3.append(arr2[j])
            j +=1
    arr2 = arr3
    return arr2

arr1 = [1,3,5]
arr2 =[2,4,6,0,0,0]
#print merger_first_into_second(arr1, arr2)


def merger_first_into_second_with_out_extra_memory(arr1, arr2):
    """
    Not using extra memory arr2 is 2*len(arr1)
    Start from the end

    :param arr1:
    :param arr2:
    :return:
    """
    # i to iterate arr1, j to iterate arr2, k to iterate arr3
    i, j, k = len(arr1)-1, len(arr1)-1, len(arr2)-1
    while i >= 0 and j >= 0:
        #print arr1[i], arr2[j]
        if arr1[i] < arr2[j]:
            arr2[k] = arr2[j]
            j -= 1
        else:
            arr2[k] = arr1[i]
            i -= 1
        k -=1
    # copy the rest of them
    while i >= 0:
        arr2[k] = arr1[i]
        i -=1
        k -=1
    while j >= 0:
        arr2[k] = arr2[j]
        j -=1
        k -=1
    return arr2

"""
while m > 0 and n > 0:
    if nums1[m - 1] >= nums2[n - 1]:
        nums1[m + n - 1] = nums1[m - 1]
        m = m - 1
    else:
        nums1[m + n - 1] = nums2[n - 1]
        n = n - 1

if n > 0:
    nums1[:n] = nums2[:n]
"""
print  merger_first_into_second_with_out_extra_memory(arr1, arr2)