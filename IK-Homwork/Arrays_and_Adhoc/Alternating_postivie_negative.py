"""
Given an array containing both +ve, -ve integers, return an array of alternating positive and negative integers
such that each of integers are in the same order as the input array
input = [2,3,-4,-9, -1, -7,1,-5,-6]
output =[2,-4, 3, -9,1,-1,-7,-5,-6]
implement this with out using additional space
"""
def alternate_pos_neg(arr):
    for i in range(len(arr)):
        j = 0
        while j+2 < len(arr):
            s=arr[j:j+3]  # basically s = [arr[j],arr[j+1],arr[j+2] 3 values
            #print s
            s = [ 1 if x > 0 else -1 for x in s]  # make it into -1 and +1 [1,1,-1]
            print s

            if s[0] == s[1] and s[1] != s[2]:
                arr[j+1],arr[j+2]= arr[j+2],arr[j+1]
                #print arr
            j += 1
    return arr

input = [2,3,-4,-9, -1, -7,1,-5,-6]
print alternate_pos_neg(input)
