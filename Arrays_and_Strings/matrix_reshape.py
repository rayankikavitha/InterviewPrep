


def matrixReshape( nums, r, c):
    """
    :type nums: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """
    # nums =[[2,3],[4,5]]

    #same as this
    # flat =[]
    # for each in nums:
    #    flat + = each
    flat = sum(nums, [])

    #  flatl = [ x[i][j] for i in range(len(x)) for j in range(len(x[i]))]
    if len(flat) != r * c:
        return nums
    tuples = zip(*([iter(flat)] * c))
    return map(list, tuples)

A1 =[[2,3],[4,5]]
A2 =[ [1,2,3],[4,5,6]]

print matrixReshape(A1,1,4)
print matrixReshape(A1,4,1)
print matrixReshape(A2, 3,2)

A=[1,4,7,8,9,       ]
B=[5,6,8,99,101,999]

