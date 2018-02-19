"""
in = [2, 7, 11, 15, 5, 8, 4]
target = 9
output = [(2,7),(5,4)]
"""
def two_sum_with_out_memory(input, target):
    input.sort()
    res=[]
    # Initalize pointers for left and right
    l = 0
    r = len(input) - 1
    while l < r:
        s = input[l] + input[r]
        if s < target:
            l = l + 1
        elif s > target:
            r = r - 1
        else:
            res.append([input[l],input[r]])
            l += 1
            r -= 1
    return res

input = [2, 7, 11, 15, 5, 8, 4, 9, 0]
target = 9
print two_sum_with_out_memory(input, target)

def twosum_with_memory(input,target):
    """
    Note: if you parse input multiple times, it creates duplicates.
    try to create dictionary and dictionary look up in single pass to avoid duplicates
    """
    d ={}
    res=[]
    for each in input:
        if each in d:
            res.append([each,d[each]])
        else:
            d[target - each] =  each
    print d
    return res

print twosum_with_memory(input, target)




# two sum to return index
input = [2, 7, 11, 15, 5, 8, 4, 9, 0]
def twosum_to_return_index(input, target):
    d = {}
    res=[]
    for i, v in enumerate(input):
        if v in d:
            res.append([d[v], i])
        d[target - v] = i
    return res

print twosum_to_return_index(input,target)

def helper(input,target):
    d={}
    res=[]
    for each in input:
        if each in d:
            res.append([each,target-sum])
        else:
            d[target - each] = each
    return res

def helper2(input,target):
    input.sort()
    res=[]
    i,j = 0,len(input)-1
    while i < j:
        if input[i] + input[j] < target:
            i += 1
        elif input[i] +input[j] > target:
            j -= 1
        else:
            res.append((i,j))
            i += 1
            j -= 1
    return res


