"""
Given sequential numbers of n,of which of one is missing, find the missing number

ways :

We can use n(n+1)/2  - sum(input) to find the missing number
or
incase of integer overload, the next approach is
xor the value with index+1 if the numbers are from 1 ...n

"""

def find_missing(input):
    """


    :param input:
    :return:
    """
    input.sort()
    result = input[0]
    for i in xrange(len(input[1:])):
        t = (i+2) ^ input[i]
        result = result ^ t
    return result

def find_missing2(input):
    #actual length should be
    n = len(input)+1
    sum_actual = (n*(n+1))/2
    missing = sum_actual - sum(input)
    return missing

def find_missing3(input):
    """
    In case series doesn't start from 1
    :param input:
    :return:
    """
    #actual length should be
    input.sort()
    result = input[0]
    for i in xrange(len(input[1:])):
        t = (i + result) ^ input[i]
        result = result ^ t
    return result



given = [1,2,3,5,6,7,8]
given2 = [9,8,6,5,4,3]
print "Test case1"
print find_missing2(given)
print find_missing(given)
print "Test case2 if the series starts from some random number"
#print find_missing2(given2) Doesn't work
print find_missing3(given2)


