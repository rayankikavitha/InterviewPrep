def gcd(a, b):
    r = 1
    while r > 0:
        r = b % a
        b = a
        a = r

    return b

def gcd2( a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

print gcd(24,36)

print gcd(120,100)

print gcd(98,56)

print gcd2(4,6)

print gcd(4,6)

def gcd_of_list(nums):
    g = gcd(nums[0],nums[1])
    for num in nums[2:]:
        g = gcd(g, num)
    return g

glist = [12,36,72]
print "gcd list ="
print gcd_of_list(glist)