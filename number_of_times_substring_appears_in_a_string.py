a = '000123000123'
b = '123'

c = "aaaaaa"
d = "aaa"

"""
count the number of times a substring appear in a string
"""

def count_substring_appearence(input, pattern):
    #return input.count(pattern)
    count = 0
    pn = len(pattern)
    for i in xrange(len(input) - pn + 1):
        if pattern == input[i:i+pn]:
            count += 1
    return count

print count_substring_appearence(c,d)

