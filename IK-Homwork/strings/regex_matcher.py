"""
Implement a regular expression matcher that supports following characters
"." matches any single characters
"*" zero or more of the preceeding elements

example:
def matcher( "abcbc","ab.bc" ) -> True
def matcher("abcbbc", "abcb*c") ->True
def matcher("abcc", abccb*") -> True
def matcher("abc","a*bc") -> True
def matcher("bc","a*bc") -> True
def matcher("aaaaaaaaabc", "a*bc") -> True
def matcher("aaaaaaabc","aa*bc") -> True
def matcher("aaaabcc","a*bc.") ->True
"""


def matcher(s,r):
    if r is None or s is None:
        return False
    return stringMatching(r,0,s,0)

def stringMatching(r,i,s,j):
    """

    :param r:  reg expression string like a.c for abc or a*bc for abc
    :param i:   index of r
    :param s:  string
    :param j: index of s
    :return:  True /False
    """
    # if i reached the end, j has to reach end too.
    if i == len(r):
        return j == len(s)
    if i+1 < len(r) and r[i+1] =='*': # case when * is zero character  or atleast 1 character matching
        return stringMatching(r, i+2, s,j) or  ( j!= len(s) and (r[i] == s[j] or r[i] =='.')  and stringMatching(r,i,s,j+1))
    if j != len(s) and (r[i] == s[j] or r[i] =='.'):  # . any one character, then increment both indexes.
        return stringMatching(r,i+1,s,j+1)
    return False

# Unit Testing
print matcher("abcbc","ab.bc" )
print matcher("abcbbc", "abcb*c")
print matcher("abcc", "abccb*")
print matcher("abc","a*bc")
print matcher("bc","a*bc")
print matcher("aaaaaaaaabc", "a*bc")
print matcher("aaaaaaabc","aa*bc")
print matcher("aaaabcc","a*bc.")