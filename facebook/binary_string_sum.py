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
