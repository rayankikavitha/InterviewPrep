""""
Merge first sorted array to second sorted array

"""

def merge_two_sorted_array(arr1,arr2):
    i,j,k = 0,0,0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[i]:
            arr1[i],arr2[i] = arr2[i],arr1[i]

        elif arr1[i] > arr2[i]:



