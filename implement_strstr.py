"""
return index of the first occurence of the substring else return -1
"""
def strStr(haystack, needle):
    n=len(needle)
    for i in range(len(haystack) - len(needle)+1 ):
        if haystack[i:i+n] == needle:
            return i
    return -1


def strStr2( haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if len(haystack) < len(needle):  # early termination
        return -1
    if not needle:
        return 0

    i = j = 0
    while j < len(needle) and i < len(haystack):
        if haystack[i] != needle[j]:
            #print i,j
            i = i - j + 1
            j = 0
            continue
        i += 1
        j += 1
    return i - j if j == len(needle) else -1

def count_substring( haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    counter = 0
    if len(haystack) < len(needle):  # early termination
        return -1
    if not needle:
        return 0

    i = j = 0
    while j < len(needle) and i < len(haystack):
        if haystack[i] != needle[j]:
            #print i,j
            i = i - j + 1
            j = 0
            continue
        i += 1
        j += 1
        if j == len(needle):
            counter += 1
            j = 0
    return counter

#print strStr2("hello","ll")
print count_substring("hellowlllowlowl",'owl')
#print strStr2("abcdefghiabcdefgabcdefghijabcde","abcdefghij")
