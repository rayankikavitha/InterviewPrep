"""
shortest substring that contains a given set of characters

input = "helloworld"
control set = "[l,r,w]

output : "worl"

"""
def find_min_len_substring(s,p):
    length = 0
    result = []
    input = list(s)
    st = 0
    while st < len(s)-len(p):
        end = st+1
        cp = set(p) - set(s[st])  # copy the pattern set
        while end < len(s):
            #print s[st],s[end],cp
            if s[end] in cp:
                cp.remove(s[end])
            if len(cp) == 0: # we have seen all the elements
                result.append(s[st:end+1])
                break
            else:
                end +=1
        st +=1
    return result

given1 ="abcdba"
pattern1 = "bd"
print find_min_len_substring(given1, pattern1)


