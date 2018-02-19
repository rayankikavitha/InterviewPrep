"""
Given an array of numbers, positive integers only, group them in-place into evens and odds
Understand that grouping is just a special case of sorting.
Aim for o(n) , in-place

"""
def groupNumbers(intArr):
    """
    odd -odd j
    """
    i=0
    j = len(intArr)-1
    while i < j:
        eoi =intArr[i] % 2 # even-odd-for-i
        eoj = intArr[j] %2 # even-odd-for-j
        if eoi == eoj and eoi == 1: # both are odd
            j -= 1
        elif eoi == eoj and eoi ==0: # both are even
            i += 1
        elif eoi != eoj and eoi == 1 and eoj ==0 : # odd and even
            intArr[i],intArr[j] = intArr[j],intArr[i]
            i += 1
            j -= 1
        else: # even and odd
            i += 1
            j -=1
    return intArr