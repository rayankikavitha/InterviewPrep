"""
input = "abdbeafghfijki"
output = ["abdbea", "fghf","ijki"]
make partition, so that characters in that partition are unique to that partition.

input = cdcadfgf
ouput = ["cdcad","fgf"]
"""
def partition(s):
    d = {}
    seen = set()
    result =[]
    for i,v in enumerate(s):
        d[v] = i
    print d
    start,end,l = 0,0,0
    i = 0
    while i < len(s):
        if i == d[s[i]]:
            if s[i] in seen:
                seen.remove(s[i])
            if len(seen) == 0:
                end = d[s[i]]
                l = max(l, end - start + 1)
                print s[i], start, end, l
                if len(seen) == 0:
                    result.append(l)
                    #reset
                    start,end,l = i+1,i+1,0
        else:
            seen.add(s[i])
            print s[i], start, end, l
        i += 1
    return result





print partition("abacbdfgf")
print partition("cdcadfgf")
print partition("abdbeafghfijki")