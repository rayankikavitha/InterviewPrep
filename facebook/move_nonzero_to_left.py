"""
Given an int array [6,4,0,5,0,0,0,1,0]
move all non-zero numbers to left and zero numbers to right

"""
def movezeros(arr):
    """
    keep a counter, add into the array counter for every nonzero value.
    Do one more loop to add zeros, until counter is of n
    :param arr:
    :return:
    """
    counter = 0
    n = len(arr)
    for i in range(n):
        if arr[i] != 0:
            arr[counter] = arr[i]
            counter += 1
            print arr
    while counter < n:
        arr[counter] = 0
        counter += 1
    return arr



def sortnonzerozero(arr):
    """
    Remove is expensive
    :param arr:
    :return:
    """
    i = 0
    for i in range(len(arr)):
        v = arr[i]
        if v == 0:
            arr.remove(v)
            arr.append(v)
            print arr
    return arr

#print sortnonzerozero([6,4,0,5,0,0,1,0])
print movezeros([6,4,0,5,0,0,1,0])













def sort012( a, arr_size):
    lo = 0
    hi = arr_size - 1
    mid = 0
    while mid <= hi:
        print lo, hi, mid
        print a
        if a[mid] == 0:
            a[lo],a[mid] = a[mid],a[lo]
            lo = lo + 1
            mid = mid + 1
            print lo, hi, mid
        elif a[mid] == 1:
            mid = mid + 1
            print lo, hi, mid
        else:
            a[mid],a[hi] = a[hi],a[mid]
            hi = hi - 1
            print lo, hi, mid
    return a