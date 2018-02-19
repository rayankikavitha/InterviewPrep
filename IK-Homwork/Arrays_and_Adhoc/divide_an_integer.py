"""
35/3
Option 1:
other way doubling every time
35 - 3 q = +1
35 - 6 q = +2
35 - 9 q = +3
Option 2:
 left shift


discussion:
 35/3
 b_copy = 3
 q=1
 if 6 < = 35
    b_copy = 6
    q = 2
 12 <= 35
   b_copy = 12
   q = 4
 24 <= 35
   b_copy = 24
   q = 8
 48 <= 35 // while loop ends

 Answer = 8+ ( 35 - 24 / 3) # problem of recursion
"""

import sys


def divide_operation(a, b):
    q = 0
    while a >= b:
        a = a - b
        q += 1
    return q


def divide(a, b):
    if a == 0:
        return 0
    sign = 1
    if (a < 0 and b > 0) or (a > 0 and b < 0):
        sign = -1
    q = divide_operation(abs(a), abs(b))
    if q > sys.maxint:
        if sign == -1:
            return -sys.maxint - 1
        else:
            sys.maxint
    else:
        return sign * q