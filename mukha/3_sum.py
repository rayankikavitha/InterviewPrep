"""
For example, given array S = [-1, 0, 1, 2, -1, -4],
target = 0
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

sort and fix the each value and iterate the rest of the items like 2 sum
"""
def three_sum(input, target):
    input.sort()
    print input
    res = []
    for i in range(len(input) - 2):
        print "i = "+ str(i)
        if i > 0 and input[i] == input[i-1]:
            continue
        l = i + 1
        r = len(input) - 1
        while l < r:
            s = input[i] + input[l] + input[r]
            if s < target:
                l = l+1
            elif s > target:
                r = r - 1
            else:
                res.append( [input[i], input[l], input[r]])
                while l < r and input[l] == input[l+1]:
                    l = l+1
                while l < r and input[r] == input[r-1]:
                    r = r-1
                l = l + 1
                r = r - 1
    return res

S = [-1, 0, 1, 2, -1, -4]
print three_sum(S, 0)






