input =['foo','bar','a','b','c','h','foo','bar','a','b','c','foo']

input1 ="big document so. So it is not a list. So keep track of the words. Words are awesome!"

"""
Make sure capital word and small word ar counted same.
that means word and Word are same
make sure they are no special characters so, awesome! and awesome is same.
output should be 
decreasing order of freq count
if there is duplicate freq count, then the order should be based on alphabetical order

foo, 3
a,2
b,2
bar,2
c,2
h,1

"""

def freq_count(input):
    """
    Returns non, if the input string is missing, else returns highly repeating character
    :param input: string
    :return: highly repeating character
    """
    d={}
    for each in input:
        if each in d:
            d[each] += 1
        else:
            d[each] = 1
    print d
    pairs = [(key,d[key]) for key in d]
    print pairs
    #nl = sorted(pairs, key=lambda x: (-x[1], x[0]))
    maxc = [ k for k,v in d.items() if v == max(d.values()) ]
    print maxc

document = "You'll need a pair. Pair of Jeans!.Cute and cute and cute!"
def freq_count_with_special_characters(input):
    tokens =input.split()
    d={}
    for each in input:
        if each in d:
            d[each] += 1
        else:
            d[each] = 1
    print d
    pairs = [(key,d[key]) for key in d]
    print pairs
    nl = sorted(pairs, key=lambda x: (-x[1], x[0]))
    print nl
print freq_count(input)

print freq_count('madam')
"""
https://www.interviewcake.com/
https://leetcode.com/problemset/all/
https://leetcode.com/problemset/all/
https://www.udemy.com/python-for-data-structures-algorithms-and-interviews/learn/v4/t/lecture/3179668?start=30

www.linkedin.com / in / abishr12

https: // www.interviewcake.com /
https: // leetcode.com / problemset / all /
https: // www.udemy.com / python -
for -data - structures - algorithms - and -interviews / learn / v4 / t / lecture / 3179668?start=30

"""
#from pramp

def word_count_engine(document):
    token_list = document.split()
    d = {}
    for token in token_list:
        ltoken = token.tolower()
        cleantoken = ''.join(ltoken.split('!'))
        if cleantoken in d:
            d[cleantoken.lower()] += 1
        else:
            d[cleantoken.lower()] = 1

    pairs = [[k, v] for k, v in d.iteritems()]
    result = sorted(pairs, lambda x: (-x[0], x[1]))

    return result