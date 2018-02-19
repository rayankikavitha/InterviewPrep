"""
Compress the string

Twist1: the compressed string length cannot exceed original length. It can be same or less
Twist2: string can have any characters from

input : ABAB
output: no string reduction
"""
def length_encoding_string(s):
    res=[]
    d={}
    p = s[0]
    count = 1
    ns = s+str('0')
    for i in xrange(1,len(ns)):
        #print count
        if ns[i] == p:
            count += 1
        else:
            if count == 1:
                res.append(ns[i-1])
            else:
                res.append(str(count))
                res.append(ns[i-1])
            count = 1
            p = ns[i]

    redstr = ''.join(c for c in res)
    print redstr
    if len(redstr) <= len(s):
        return redstr
    else:
        return s

print length_encoding_string("aaabbccccaaabc")
print length_encoding_string("abab")
print length_encoding_string("a12bbbb")




