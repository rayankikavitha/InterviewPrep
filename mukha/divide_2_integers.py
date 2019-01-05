"""
No using mod, multiplication and division. use int max for overflows

"""
import sys
def divide(dividend, divisor):
    if divisor == 0:
        return sys.maxint
    if dividend == 0:
        return 0
    sign = 1
    if (dividend <0 and divisor > 0) or ( dividend > 0 and divisor < 0):
        sign = -1
    ans = divide_operation(abs(dividend), abs(divisor))
    print ans
    if ans > sys.maxint:
        if sign == -1:
            return -sys.maxsize-1
        else:
            return sys.maxint
    else:
        return sign*ans





def divide_operation(dividend,divisor):
    counter = 0
    while dividend >= divisor:
        dividend -= divisor
        counter += 1
    return counter

print divide(3,3)