"""
Implement pow(x,y) function
https://en.wikipedia.org/wiki/Exponentiation_by_squaring

https://stackoverflow.com/questions/101439/the-most-efficient-way-to-implement-an-integer-based-power-function-powint-int



"""
def kr_pow(base, exp):
    """
    Doesn't work for negative exp

    :param base:
    :param exp:
    :return:
    """
    # default power 0
    result = 1
    while exp:
        # power 1 and the last step
        if exp & 1 == 1:
            result *= base
        # divide the exponent
        exp >>=1
        base *= base
        print base, exp, result
    return result

def kr_pow2(base, exp):
    """
    works for negative integers, but not for decimals

    :param base:
    :param exp:
    :return:
    """
    if exp == 0:
        return 1
    if exp == 1:
        return base
    if exp < 0:
        return kr_pow2(1/base,-exp)
    if exp%2 == 0:
        half = kr_pow2(base,exp/2)
        return half * half
    else:
        half = kr_pow2(base, (exp - 1)/2)
        return base*half*half




print kr_pow(2,3)
#print kr_pow(4.5,-3)
#print kr_pow2(9,0.5)
#print kr_pow2(27, 1/3)