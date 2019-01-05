"""
Given two strings as binary numbers 1s and 0s like 1101 and 0101 add it and return added binary value as string
concept
1      1
1      0
---   ---
10     01
so: sum is  a xor b xor c (carry)
carry is ( a and b) or ( b and c) or (a and c)

"""

def add_binary_practice(a,b):
    la = list(a)[::-1]
    lb = list(b)[::-1]
    n = max(len(a),len(b))
    result = [0] * (n+1)
    c = 0
    for i in range(n):
        num1 = ord(la[i]) - ord('0')
        num2 = ord(lb[i]) - ord('0')
        s = num1 ^ num2 ^ c
        c = (num1 & num2 ) or (num1 & c ) or (c & num2 )
        result[i] = s

    if c == 1:
        result.append(c)
    print result
    return ''.join(str(x) for x in result[::-1])

print '**** add binary practice ******'
print add_binary_practice('1101','0101')

# 1101
# 0101
# 10010

#  1011
#. 1010
#. 0101

























def add_binary(a,b):
    c=0
    la, lb = len(a),len(b)
    if la != lb:
        if la > lb:
            d = la - lb
            a = '0'*d + a
        else:
            d = lb - la
            b = '0'*d + b
    result =[]*(len(a)+1)
    print result
    for i in range(len(a)-1,-1,-1):
        print i
        s = int(a[i]) ^ int(b[i]) ^ c
        c = (int(a[i]) & int(b[i])) or (int(a[i]) & c) or (c & int(b[i]))
        result.append(str(s))
    if c > 0:
        result.append(str(c))
    return ''.join(result[::-1])



print add_binary('1101','0101')
