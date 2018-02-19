def lcs(s):
    start = 0
    maxlen = 0
    visited ={}
    for i in range(len(s)):
        if s[i] in visited and start <= visited[s[i]]:
            start = visited[s[i]] + 1
        else:
            maxlen = max(maxlen, i - start +1 )
        visited[s[i]] = i
    return maxlen

input = "acdeghijdxyz"
input1 = "acdeghijkdxyzenoqrstx"
input2 ="abcdeafghi"

#print lcs(input)

#print lcs(input1)
#print lcs(input2)
print lcs("pwwkew")