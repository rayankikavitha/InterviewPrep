def groupNumbers(intArr):
    """
    odd -odd j
    """
    i=0
    j = len(intArr)-1
    while i < j:
        eoi = intArr[i] % 2 # even-odd-for-i
        eoj = intArr[j] %2 # even-odd-for-j
        print i,j,intArr[i],intArr[j],eoi,eoj
        if eoi == eoj and eoi == 1: # both are odd
            j -= 1
        elif eoi == eoj and eoi == 0: # both are even
            i += 1
        elif eoi != eoj and eoi == 1 and eoj == 0 : # odd and even
            print "1,0"
            intArr[i],intArr[j] = intArr[j],intArr[i]
            i += 1
            j -= 1
        else: # even and odd
            i += 1
            j -=1
        print intArr
    return intArr

input = [5,2,4,3,7,3,2,8]
print groupNumbers(input)