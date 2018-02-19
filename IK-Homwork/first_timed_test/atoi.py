"""
Gathering requirements is key to this problem

1) discards all leading whitespaces
2) sign of the number
3) overflow
4) invalid input

"""

import sys
def isNumericChar( x):
    if (x >= '0' and x <= '9'):
        return True
    return False


def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    # string has leading or ending spaces "   -123  "
    # string has negative or + sign +123, - 123
    # invalid numeric data like a999
    # overbound range
    res = 0
    sign = 1
    i = 0

    while i < len(str):

        if str[i] == '-':
            sign = -1 * sign

        if isNumericChar(str[i]) and res <= sys.maxint and res >= -sys.maxint:
            res = res * 10 + (ord(str[i]) - ord('0'))
            print res
        i += 1
    return res * sign

def myAtoi(self, s):
    """
    :type str: str
    :rtype: int
    """
    ###better to do strip before sanity check (although 8ms slower):
    # ls = list(s.strip())
    # if len(ls) == 0 : return 0
    if len(s) == 0: return 0
    ls = list(s.strip())

    sign = -1 if ls[0] == '-' else 1
    if ls[0] in ['-', '+']: del ls[0]
    ret, i = 0, 0
    while i < len(ls) and ls[i].isdigit():
        ret = ret * 10 + ord(ls[i]) - ord('0')
        i += 1
    return max(-2 ** 31, min(sign * ret, 2 ** 31 - 1))


print myAtoi('1')