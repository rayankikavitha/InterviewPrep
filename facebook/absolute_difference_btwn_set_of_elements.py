input = [1, 5, 3, 19, 18, 25]
input2 =[1, 19, -4, 31, 38, 25, 100]
# output  = 1

def find_min_abs_diff(input):
    input.sort()
    diff = 10**20
    for i in xrange(len(input)  - 1):
        adiff = abs(input[i] - input[i+1])
        if adiff < diff:
            diff = adiff
    return diff

print find_min_abs_diff(input2)

