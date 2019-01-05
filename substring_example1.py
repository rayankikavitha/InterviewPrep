"""
Given a string s, break s such that every substring of the partition can be found in the dictionary.
Return the minimum break needed.
Example
Given a String CatMat
Given a dictionary ["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"]
return 1
we can break the sentences in three ways, as follows:
CatMat = Cat Mat break 1
CatMat = Ca tM at break 2
CatMat = C at Mat break 2
but the first way has the minimum break, thus return 1
public int wordBreak(String s, Set<String> dict) {
// Write your code here
}

"""
wordlist = ["Cat", "Mat", "Ca", "tM", "at", "C", "Dog", "og", "Do"]
s = "CatMat"
def wordBreak(s, wordlist):
    numbreak = 0
    wordlist.sort(key = len)
    print wordlist
    for word in wordlist:
        if word in s:
            numbreak +=1
    return numbreak



print wordBreak(s,wordlist)

"""
find a shortest string to cover all of a list of string, 
For example, [aab, aabb, bc], should return aabbc, 

"""
"""
given 2 list of interval representing users online offline timestamp e.g (already sorted), find all intervals that both of users are online. 
"""
A= [(3, 5), (7, 11)]
B=[(2, 4), (9, 10)]
# output --> [(3, 4), (9, 10)].


def online_time(a, b):
    result =[]
    for i in range(len(a)):
        s = a[i][0] if  a[i][0] > b[i][0] else b[i][0]
        e = a[i][1] if a[i][1] < b[i][1] else b[i][1]
        result.append((s,e))
    return result

print online_time(A, B)