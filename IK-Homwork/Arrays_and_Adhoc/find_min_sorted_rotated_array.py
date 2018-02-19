"""
Find min in a sorted roated array
Option 1: regular search o(n)
Option 2: o(log(n))

Binary search on looking for a element, whos prev element is greater than it.

https://www.geeksforgeeks.org/find-minimum-element-in-a-sorted-and-rotated-array/

"""
def find_min(arr):
    """
    The min element is the only element, whos prev is greater than curr element
    If there is no prev element, then there is no rotation.
    We check this condition for middle element by comparing it with mid-1 and mid+1

    Do this for left and right half side


    :param arr:
    :return:
    """
    low = 0
    high = len(arr)-1
    return find_min_helper(arr,low, high)


def find_min_helper(arr,low, high):
    # case when array is not rotated
    if high < low:
        return arr[0]
    # case when there is only 1 element
    if high == low:
        return arr[low]

    mid = (low+high)/2
    #print mid
    # Check if element (mid+1) is minimum element. Consider the cases like [3, 4, 5, 1, 2]
    if mid < high and arr[mid+1] < arr[mid]:
        return arr[mid+1]
    # Check if mid itself is minimum element
    if mid > low and arr[mid] < arr[mid-1]:
        return arr[mid]
    # decide to go to left or right
    if arr[high] > arr[mid]:
        return find_min_helper(arr, low, mid - 1)
    else:
        return find_min_helper(arr, mid+1, high)



print find_min([6,7,8,1,2,3,4,5])
print find_min([6,7,8,9,10,1,2])

print find_min([9,10,1,2,3,4,5,6,7,8])
