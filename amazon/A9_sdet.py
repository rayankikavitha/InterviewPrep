"""
print fib series

"""
def fib(n):
    a = 0
    b = 1
    c =1
    result =[a,b]
    while c < n:
        t = a+b
        result.append(t)
        a = b
        b = t
        c +=1
    return result

#print fib(8)

"""
top k most search words

"""
import heapq
arr1 = [4,9,2,99,100,2,3,400,500]
arr2 = [ 889,99,9,1,2,3,4,5,5]
def topk(arr,k):
    h=[]
    #result=[]
    for each in arr:
        if len(h) < k or each > h[0]:
            heapq.heappush(h,each)
        if len(h)  > k:
            heapq.heappop(h)
    return h

def mink(arr,k):
    h=[]
    #result=[]
    for each in arr:
        if len(h) < k or each < -h[0]:
            heapq.heappush(h,-each)
            print h
        if len(h)  > k:
            heapq.heappop(h)
    return h

#print topk(arr1,3)
#print mink(arr2,3)
#print mink(arr1,3)

import sys
import os
import re
def count_no_words_lines(filein):
    fi = open(filein,'r')
    wordcounter = 0
    linecounter = 0
    for line in fi.readlines():
        wordcounter += len(line.split())
        linecounter += 1
    return linecounter, wordcounter

#print count_no_words_lines("find_merg_in_2_sorted_intervals.py")



def top_k_searchwords(arr, K):
    d={}
    result =[]
    for each in arr:
        d[each] = d.get(each, 0) + 1
    # d ={"I":1, "Coffee":3, "D": 4, "like":3}
    h=[]
    print d
    for k,v in d.iteritems():
        #print k,v
        if len(h) < K or v >= h[0][0]:
            heapq.heappush(h, (v,(k, v)))
        if len(h) > K:
            heapq.heappop(h)
        print h
    while h:
        result.append(heapq.heappop(h)[1][0])
    return result



search =["I", "like", "Coffee", "Dog", "Coffee", "phone", "like", "like", "Coffee", "Dresses", "Dresses", "Dresses", "Dresses","I","I","I"]
#print top_k_searchwords(search,2)


"""
a)Given a stock quotes over a month of time, return the buy day and sell day with the max profit
b)Find kth smallest
c) Write a function that takes 2 integers k and n  where 0<=k<=n and prints out all subsets of size k of integers 
one subset per line.

"""
quotes1 = [100, 180, 260, 310, 40, 535, 695]
quotes2 = [30, 29, 45, 49, 55, 40, 30, 31, 32]

"""
30 29 45 49 55 40 30 31 32
Output: 0 0 2 3 4 0 0 2 3
"""
def max_profit(arr):
    s=[]
    result=[]
    maxprofit = 0
    for i in xrange(len(arr)):
        if len(s)==0 or arr[i] >= arr[i-1]:
            s.append(i)

        else:
            s.append(0)
            counter = 0
    return s

#print max_profit(quotes1)

# balanced paranthesis
par = "(((()))(())()())"
def isbalanced(s):
    counter = 0
    for each in s :
        if each =="(":
            counter += 1
        else:
            counter -= 1
    if counter == 0:
        return True
    else:
        return False

#print isbalanced(par)

"""
Given an unsorted array, find kth smallest
"""
ua = [ 6,1,9,3,5,2,0]
def partition(arr,start,right):
    pivot = arr[start]
    left = start+1
    right = len(arr)-1
    done = False
    while not done:
        while left <=right and  arr[left] <= pivot:
            left = left + 1
        while left <=right and  arr[right] >= pivot:
            right -= 1
        if right < left:
            done = True
        else:
            arr[left], arr[right] = arr[right], arr[left]
        print arr
    arr[start], arr[right] = arr[right], arr[start]
    return right


def quick_select(arr,k):
    pi = partition(arr, 0, len(arr)-1)
    print pi
    while pi != k-1:
        if pi > k-1:
            return quick_select(arr[:pi],k)
        else:
            return quick_select(arr[pi+1:],k)

    if pi == k-1:
        return arr[0:pi]


# [0,1,2,3,5,6,9]
#print quick_select(ua,4)


def two_sum(arr,k):
    d={}
    res=[]
    for each in arr:
        if each in d:
            res.append((each,d[each]))
        else:
            d[k-each] = each
    return res

print two_sum(ua,5)

# find a subarry ( continous) which yields to sum = k in an given array
nums = [1, -1, 5, -2, 3]
#k = 3
nums1 = [-2, -1, 2, 1]
k1 = 1
# output = 4 ( from 0 to 3 )
def sum_k_subarry_length(arr, k):
    d={0:-1}   #answer the accumulative value of nums
    s = 0      #key is acc value and value is the index
    ans = 0
    for i in xrange(len(arr)):
        s += arr[i]
        if s not in d:
            d[s] = i
        if s-k in d:
            ans = max(ans, i -d[s-k])
        print d, ans
    return ans


input = ['opts','foo','bar','tops','pots','rab','ofo','hat']
output = [ ['opts','tops','pots'],['rab','bar'],['ofo','foo'],['hat']]
def anagramsets(arr):
    d={}
    for each in input:
        ss = ''.join(sorted(each))
        if ss in d:
            d[ss].append(each)
        else:
            d[ss] =[each]
    return d.values()

#print anagramsets(input)

def most_repeating_num(arr):
    d={}
    for num in arr:
        d[num] = d.get(num,0) +1
    print d
    return max(k for k,v in d.items() if v == max([v for v in d.values()]))

#print most_repeating_num([3,4,5,6,3,4,8,9,3,6,9,1,3,8,7,3])
ins = "acdeghijdxyz"
def longest_nonrepeating_substring(s):
    start = 0
    maxlen = 0
    visited ={}
    for i in xrange(len(ins)):
        if s[i] in visited and start <= visited[s[i]]:
            start =visited[s[i]]+1
        else:
            visited[s[i]] = i
            maxlen = max(maxlen, i- start +1)
    return maxlen

print longest_nonrepeating_substring(ins)


