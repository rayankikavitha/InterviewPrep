def longestPalindrome( s):
    res = ""
    for i in xrange(len(s)):
        # odd case, like "aba"
        print i
        tmp = expandAroundCenter(s, i, i)
        print 'odd case :',tmp
        if len(tmp) > len(res):
            res = tmp
        # even case, like "abba"
        tmp = expandAroundCenter(s, i, i + 1)
        print 'even case :',tmp
        if len(tmp) > len(res):
            res = tmp
    return res

def longestPalindrome2(s):
    """
    Improving above function to use max
    :param s:
    :return:
    """
    res = ""
    for i in range(len(s)):
        res = max(expandAroundCenter(s, i, i), expandAroundCenter(s, i, i + 1), res, key=len)

    return res


# get the longest palindrome, l, r are the middle indexes
# from inner to outer
def expandAroundCenter(s, l, r):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        l -= 1
        r += 1
    return s[l + 1:r]

print longestPalindrome('babad')
print '*********'
print longestPalindrome('baabbaad')
