"""
Main concept is building suffix trees

https://www.geeksforgeeks.org/suffix-tree-application-3-longest-repeated-substring/
Longest Repeated Substring in GEEKSFORGEEKS is: GEEKS
"""
# naive approach
# how about include exclude logic, take a substring and check its existance in the rest of the string

def longest_repeated_substring(s):
    maxlen = 0
    res=''
    start = 0
    for i in range(len(s)):
        ss = s[start:i]
        print ss
        if ss in s[start+1:]:
            curlen = len(ss)
            if curlen > maxlen:
                maxlen = curlen
                res = ss
        else:
            start +=1

    return maxlen,res

#print longest_repeated_substring("geeksforgeeks")
#print longest_repeated_substring("ABABABA")
print longest_repeated_substring("banana")