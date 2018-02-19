"""
Write a function that reverses the given integers flip(arr)
Use that function to sort the list

"""
def flip(arr):
    i = 0
    j = len(arr)-1
    while i < j:
        arr[i],arr[j] = arr[j],arr[i]
        i += 1
        j -= 1

arr = [ 5,3,9,2,6,1,99]
#output = [1,2,3,5,6,9,99]
def pancake_sort(arr):



