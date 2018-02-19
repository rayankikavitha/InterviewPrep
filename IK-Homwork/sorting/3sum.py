"""
Some times this problem is disguised as traingle problem ( no.of traingles possible).i.e a+b > c or b+c > a or c+a > b
Sum exactly to a given k
Sum to the nearest number to given K ( sort and do a binary search to nearest)


"""

def printTriplets(intArr):
    intArr.sort() #sort the array
    result = set() #to eliminate duplicate results
    for i in xrange(len(intArr)):
        j = i+1
        k = len(intArr) - 1
        target = 0 - intArr[i]
        while j<k :
            if intArr[j] + intArr[k] < target:
                j +=1
            elif intArr[j] + intArr[k] > target:
                k -= 1
            else:
                result.add(tuple(sorted([intArr[i],intArr[j],intArr[k]])))
                j +=1
                k -=1
    return result