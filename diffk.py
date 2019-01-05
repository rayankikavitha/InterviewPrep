"""
Given an array A of integers and another non negative integer k,
find if there exists 2 indices i and j such that A[i] - A[j] = k, i != j.
A : [1 5 3]
k : 2
output = 1 yes as 5-3 is 2
Return 0 (False) / 1( False) for this problem.
"""
def diffk(nums, k):
    d={}
    for num in nums:
        if num in d:
            return True
        d[num - k ] = num

A = [1,5,3]
K = 2
print diffk(A, K)


def diffPossible(self, A, B):
    hashDict = dict()
    n = len(A)
    # print A, B
    for a in A:
        if a in hashDict:
            hashDict[a] += 1
        else:
            hashDict[a] = 1
    for i in range(n):
        x = A[i]
        if (x - B >= 0 and x - B in hashDict) or (x + B in hashDict):
            if B == 0:
                if hashDict[x] >= 2:
                    return 1
            else:
                return 1
        elif x + B in hashDict:
            return 1
        elif x in hashDict:
            del hashDict[x]
    # print hashDict
    return 0