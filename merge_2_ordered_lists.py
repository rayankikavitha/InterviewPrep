"""

"""
def merge_sort(arr1, arr2):
    i = 0
    j = 0
    final =[]
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            final.append(arr1[i])
            i += 1
        else:
            final.append(arr2[j])
            j += 1
    while i < len(arr1):
        final.append(arr1[i])
        i += 1
    while j < len(arr2):
        final.append(arr2[j])
        j += 1
    return final

print merge_sort([2,4,6,8,55,150],[1,3,7,9,10,99])


