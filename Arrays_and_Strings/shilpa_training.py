import math as m
import random
print random.randrange(100)
import os
y=['a','b','c']
x=['1','2']

x =('x','y','z')
print x.count('x')
print x.index('z')

basket = set(['apple', 'orange', 'apple', 'pear', 'orange', 'banana'])
vegetables = set(['carrot','pear','tomato','spinach'])
print basket.pop()
basket.add('grape')
basket.clear()


def count_words(inputfile):
    filein = open(inputfile)
    tokens =[]
    d={}
    for line in filein:
        tokens = tokens+ line.split()
        print tokens

    print tokens

    for token in tokens:
        d[token] = d.get(token,0) +1
        print d
    print d

    s=sum(map(len,tokens))

    max_freq = max(d.values())
    for k,v in d.iteritems():
        if v == max_freq:
            return k

# 12/11/2017

input= ['cat','atc','tac','bat','tab','pure','rupe','taco','coat']
output =[ ['cat','atc','tac'],['bat','tab'], ['pure','rupe'],['taco','coat']]




def group_anagrams(input):
    d={}
    for each in input:
        token =''.join(sorted(each))
        if token in d:
            d[token].append(each)
        else:
            d[token] = [each]
        #print d, each
    return d.values()

print group_anagrams(input)



#check if its a palindrome


def isangram(s):
    i = 0
    j = len(s) - 1
    while i <= j:
        if s[i] != s[j]:
            return False
        i +=1
        j -=1
    return True


print isangram('madam')
print isangram('shilpa')
print isangram('madem')
print isangram('abccba')

print "#### 12/12/2017 ###########"


nums = [ 0,3,4,1]
n = 4
# sum = 4*5/2 = 10  (1,2,3,4)
# missing number = 2




t=[99,5,2,9,1,8,10,7,3]
#k = 3
output = [1,2,3]


import heapq
def mink(arr,k):
    h=[]
    result =[]
    for i in range(len(arr)):
        if len(h) < k or arr[i] < -h[0]:
            heapq.heappush(h,-arr[i])
        if len(h) > k:
            heapq.heappop(h)
    while h:
        result.append(-heapq.heappop(h))
    return result[::-1]
print "output from heapq"
#print mink(t,3)


h = []
heapq.heappush(h,4)
heapq.heappush(h,6)
heapq.heappush(h,100)
heapq.heappush(h,10)
print heapq.heappop(h)

heapq.heapify

arr =1+[ 1,2,3,4] + 1
left=  [1,1,2,6,24]  // accumulated multiplication from left
right= [24,24,12,4,1]  // accumated multiplication from right

product_arry_except itself:
 dont use divison

output :[72, 48,24, 36, 144 ]
