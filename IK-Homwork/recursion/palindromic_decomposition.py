"""
A palindromic decomposition of string S is a decomposition of the string into substrings,
such that all of those substrings are valid palindromes.

Input : abracadabra

output =

a|b|r|a|c|a|d|a|b|r|a
a|b|r|aca|d|a|b|r|a
a|b|r|a|c|ada|b|r|a

"""
def isPali(input):
    return input[::-1] == input

def partition(s):
    """
    Return a list by splitting input string at each index and applying recursion for the rest of the string.

    :param s:
    :return:
    """
    return [[s[:i]] + rest
            for i in xrange(1, len(s)+1)
            if s[:i] == s[i-1::-1]
            for rest in partition(s[i:])] or [[]]



def partition2(s):
    result =[]
    for i in xrange(1,len(s)+1):
        if isPali(s[:i]):
            for rest in partition2(s[i:]):
                result.append([[s[:i]] + rest])
    return result


print partition2("abracadabra")