"""
in place in o(1) space

"""

def removedups(arr):
    if not arr:
        return 0
    tail = 0
    n = len(arr)
    for i in range(1,n):
        # compare 1st element with the prev element and if doesn't match increment
        # tail and copy the current to tail. This will leave all duplicates at the end
        if arr[i] != arr[tail]:
            tail += 1
            arr[tail] = arr[i]
            print arr, tail, i
    return arr[:tail+1]

print removedups([1,2,2,3])
print removedups([2,2,2])


