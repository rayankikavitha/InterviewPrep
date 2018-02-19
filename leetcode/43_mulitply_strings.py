"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.

"""
def multiply(num1,num2):
    product =[0]*(len(num1)+len(num2))
    pos = len(product) -1
    for n2 in reversed(num1):
        s = 0
        tpos = pos
        for n1 in reversed(num2):
            #print n1,n2
            product[tpos] += int(n1) * int(n2)
            product[tpos - 1] += product[tpos] / 10
            product[tpos] = product[tpos] %10
            #print product
            tpos -=1
        pos -= 1
    # remove leading zeros
    pt = 0
    while pt < len(product) - 1 and product[pt] == 0:
        pt += 1

    return ''.join(map(str, product[pt:]))


print multiply('12','99')
print multiply('8999','10000')