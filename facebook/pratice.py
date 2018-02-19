#no.of times substring appears in a string
print "no.of times substring appears ina  string"
s = "abcabcdefabcdefgh"
ss= "abcdef"

print s.count(ss)

def substring_occurences(s,ss):
    counter = 0
    for i in xrange(len(s) - len(ss)):
        if s[i:len(ss)+i] == ss:
            counter += 1
    return counter

print substring_occurences(s,ss)
s1 ='abc'
print substring_occurences(s,s1)
#**********************************************
print "give list of tuples, find how many unique minutes of the moview did the viewer watch"

input = [(0,15), (10,25),(20,30),(25,30), (40,50)]
t = [(0, 10), (15, 25), (12, 20), (30, 48)]

tol = t[0][1] - t[0][0]
for i in range(len(t) - 1):
    if t[i+1][0] >= t[i][1]:
        tol += t[i+1][1] - t[i+1][0]
    else:
        tol += t[i+1][1] - t[i][1]
print(tol)
#output =
def unique_minutes(input):
    input.sort()
    tot = 0
    ovr = 0
    for i in range(len(input)):
        tot = tot + input[i][1] - input[i][0]
        if i > 0 and input[i-1][1] > input[i][0]:
            ovr = ovr + input[i-1][1] - input[i][0]
    return tot - ovr

print unique_minutes(input)
print unique_minutes(t)
#************************************************
print "Delete duplicates in a list"
input =[5,2,7,1,3,2,1,6,9]
def del_duplicates(input):
    input.sort()
    i = 0
    while i < len(input) - 1:
        if input[i] == input[i+1]:
            del input[i]
        else:
            i = i+1
    return input

print del_duplicates(input)
#******************
print "count distinct words in a sentece"
s = "the message of the toastmaster club is the message"
def count_distinct_words(input):
    l = input.split()
    d={}
    for each in l:
        d[each] = d.get(each, 0) + 1
    print d
    return len(d)

print count_distinct_words(s)
#***************************************************
print "return tuples of a list matching each item to another item"
s = [ (1,2),(3,2),(2,1),(5,6),(3,4),(4,3),(2,3)]
def match_tuples(input):
    res =[]
    d =dict(input) # only works if tuples are unique
    print d
    for k,v in d.iteritems():
        if v in d.keys() and d[v] == k:
            res.append((k,v))
    print d
    return res

print match_tuples(s)
#***************************************
print "find the number that is repeating the most"
s = [0,0,3,4,5,4,4,4,4,5,5,5,5]
def most_repeated(input):
    d = {}
    for each in input:
        d[each] = d.get(each, 0) + 1
    print d

    return [k for k,v in d.iteritems() if v == max([v for v in d.values()])]

print most_repeated(s)

s1 = [0,0,3,4,5,4,4,4,4,5,4,9]
print "find the most repeating with collections"
import collections
def most_repeated_with_counter(input):
    return collections.Counter(input).most_common(1)[0][0]

print most_repeated_with_counter(s1)
###################################
print "find GCD"
sample  = [12,36,72]
sample2 = [24,36,45]
#OUTPUT = 6
def gcd(a,b):
    r=1
    while r > 0:
        r = a%b
        a = b
        b = r
    return a
def find_gcd(input):
    g = reduce(gcd,[x for x in input])
    return g

print find_gcd(sample2)
###########
print "find the first non-recurring element"
s1 = [5,0,0,9,4,5,4,4,4,4,4,3]
def first_non_recurring(input):
    d={}
    for i in xrange(len(input)):
        if input[i] in d:
            d[input[i]].append(i)
        else:
            d[input[i]] = [i]
    print d
    min_index = max(s1)+1
    for k, v in d.iteritems():
        if len(v) == 1:
            min_index = min(min_index,v[0])
            print min_index

    return input[min_index]

print first_non_recurring(s1)


def isPalindrome( s):
    """
    :type s: str
    :rtype: bool
    """
    if len(s) == 0:
        return True
    news = ''
    for ch in s:
        if ch.isdigit() or ch.isalpha():
            news = news+ch.lower()
            #news = ''.join(ch.lower())

    print news
    l = 0
    r = len(news) - 1
    while l < r:
        if news[l] == news[r]:
            l += 1
            r -= 1
        else:
            return False
    return True
print "*******isPalindrome*********"
print isPalindrome("A man, a plan, a canal: Panama")

def longest_common_prefix(str):
    if not str:
        return ''
    for i, l in enumerate(zip(*str)):
        if len(set(l)) > 1:
            return str[0][:i]
    else:
        return min(str)

print longest_common_prefix(['cat','cattle','cagter'])

print "Find repeating number with no mem"
index =  [0, 1, 2, 3, 4, 5, 6, 7]
given =  [2, 3, 4, 3, 2, 1, 5, 2]
#num%k = [2, 3, 4, 3, 2, 1, 5, 2]
after  = [ 2, 9, 28, 19,12 ,13 ,5 , 2 ]
def find_most_repeating_number(nums):
    k = len(nums)
    for num in nums:
        nums[num%k] += k
    return nums.index(max(nums))

print find_most_repeating_number(given)

print "*******Merge intervals*******"
input =[[1,3],[2,6],[5,8],[8,10],[15,18]]
def merge(intervals):
    result =[]
    intervals.sort()
    for each in intervals:
        if result and each[0] <= result[-1][1]:
            result[-1][1] = max(result[-1][1], each[1])
        else:
            result.append(each)
    return result
print merge(input)

print






