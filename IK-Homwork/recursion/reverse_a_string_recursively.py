"""
Reverse a string recursively
"""
def revString(s):
    if len(s) == 0:
        return ""
    last = s[len(s)-1]
    revs = revString(s[:len(s)-1])
    return last+revs


print revString("kavitha")
