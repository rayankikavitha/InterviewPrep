dS1  =[4,5,1,2,3]
S2 = [5,1,2,3,6]
#Output = [4,6]
# output2 =  [(4, 0), (6, 4)] <return indexes

# If numbers are repeating
L1 = [4, 4, 5, 1, 2, 3]
L2 = [5, 1, 2, 3, 6, 6]
#output = {4: 2, 6: 2}


def find_non_common(s1,s2):
    return list( set(s1).union(set(s2)) - set(s1).intersection(set(s2)))

def find_non_common2(s1,s2):
    """
     with out using set
    :param s1:
    :param s2:
    :return:
    """
    d={}
    for each in s1:
        d[each] = d.get(each,0) + 1
    print d
    for each in s2:
        d[each] = d.get(each, 0) - 1
    return [ (k, abs(v)) for k,v in d.iteritems() if v!= 0]

def find_non_common3(s1,s2):
    """
     with out using set
    :param s1:
    :param s2:
    :return:
    """
    d={}
    di ={}
    res=[]
    for i in range(len(s1)):
        d[s1[i]] = d.get(s1[i],0) + 1
        di[s1[i]] = i
    print d
    print di
    for i in range(len(s2)):
        d[s2[i]] = d.get(s2[i], 0) - 1
        if not di.has_key(s2[i]):
            di[s2[i]] = i
    print di

    return [ (k, di[k]) for k,v in d.iteritems() if v!= 0]



#print find_non_common(S1,S2)

#print find_non_common2(S1,S2)
print '**************************'

#print find_non_common2(L1, L2)

#print find_non_common3(S1, S2)

#####################################################################################
"""
Derive 312211 from 13112221
And from 13112221 to 312211 

1
11
21
1211
111221
312211
13112221
"""

def read_num(num):
    num = str(num)
    res =''
    i = 0
    d={[]}
    for i in range(len(num)):
        if num[i] in d:
            d[num[i]] = d[num[i]].append(num[i])

    return res

#print read_num(312211)

#Given an integer like 543, write a function to return String "500+40+3" and test your code

def read_a_num(nums):
    count = 0
    res =[]
    while nums>0:
        d = nums%10
        res.append( d * (10**count))
        nums =nums/10
        count = count+1
    return '+'.join(str(x) for x in res[::-1])

print read_a_num(543)

"""
target num = 13
 input = [7, 4, 10, -6, -2, 13, 2, 0, 17, 9, 6, 15, -4 ]
pairs to be returned would be (7, 6), (4, 9), (17, -4), (-2, 15), (13,0)
"""
def two_sum(nums, target):
    d={}
    res =[]
    for each in nums:
        if each not in d:
            d[target - each] = each
        else:
            res.append((each,d[each]))
    print d
    return res

print two_sum([7, 4, 10, -6, -2, 13, 2, 0, 17, 9, 6, 15, -4 ], 13)

