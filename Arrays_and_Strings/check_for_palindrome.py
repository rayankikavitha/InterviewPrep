s='madam'

def check_palindrome(s):
    return s == s[::-1]


def palindrome(s):
    i=0
    j = len(s) - 1
    while j>= i:
        if s[i] != s[j]:
            return False
        i = i+1
        j = j-1
    return True

print palindrome(s)
print palindrome('ismadamsi')