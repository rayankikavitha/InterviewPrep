def isPalindrome( x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0 or (x != 0 and x % 10 == 0):
        return False
    # reverse
    r = 0
    nx = x
    print nx
    while x > 0:
        r = r * 10 + x % 10
        x = x / 10
        print r,x
    return nx == r or nx == r/10

def isPalindrome( x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0 or (x != 0 and x % 10 == 0):
        return False
    # reverse
    r = 0
    # do only half the time
    while x > r:
        r = r * 10 + x % 10
        x = x / 10
        print r,x
    return x == r or x == r/10

print isPalindrome(11)
