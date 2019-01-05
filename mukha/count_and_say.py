def getnextPattern(s):
    res = ''
    counter = 1
    i = 0
    s= s+'*'
    while i < len(s) - 1:
        if s[i] == s[i + 1]:
            counter += 1
        else:
            res += str(counter)+s[i]
            counter = 1
        i += 1

    return res


def countAndSay(n):
    """
    :type n: int
    :rtype: str
    """
    init = '1'
    if n == 1:
        return init
    i = 1
    while i < n:
        new_init = getnextPattern(init)
        #print new_init
        init = new_init
        i += 1
    return new_init

print countAndSay(4)
print getnextPattern("21")