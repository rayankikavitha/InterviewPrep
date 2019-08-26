
# Find the number that is repeating the most. Example [0,0,3,4,5,4,4,4 ] , output :4

import heapq
def find_most_feq(input):
    result=[]
    h=[input[0]]
    for each in input[1:]:
        if each 




# binary search

def bin_search(nums,k):
    nums.sort()
    low, high = 0, len(nums)-1
    while low <= high:
        mid = (high+low)//2
        if nums[mid] < k :
            low = mid + 1
        elif nums[mid] > k:
            low = mid -1
        else:
            return mid
    return -1

#print (bin_search([7,2,3,10,8,0,5,-1,2],10))









# two sum

def two_sum(nums,k):
    d={}
    result=[]
    for i,v in enumerate(nums):
        if v not in d:
            d[k-v]=v
        else:
            result.append((v,d[v]))
    return result

def two_sum_v2(nums,k):
    nums.sort()
    result=[]
    i,j = 0, len(nums)-1
    while i < j:
        if nums[i]+ nums[j] < k:
            i +=1
        elif nums[i] +nums[j] > k:
            j -=1
        else:
            result.append((nums[i],nums[j]))
            i +=1
            j -=1
    return result




#print (two_sum_v2([7,2,3,10,8,0,5,5,-1,2],10))
















"""
2) How do you calculate L7 ( given a input like this ?

input = { "android":[1,1,0,0,0,1,0] ,
              "ios":[1,0,1,1,0,0,1],
           "laptop":[0,0,0,0,1,1,0]
       }

 category = {. "mobile": ["ios","android"]
               ,everything = ["ios","android","laptop"] }
 output = { "mobile ": [1,1,1,1,0,1,1,], everything :[1,1,1,1,1,1,1]
       }
 if any day is 1, then populate 1 in the output.
"""

input = { "android":[1,1,0,0,0,1,0] ,
              "ios":[1,0,1,1,0,0,1],
           "laptop":[0,0,0,0,1,1,0]
       }

category = {"mobile": ["ios","android"],"everything" :["ios","android","laptop"] }
               
import collections as collections
from functools import reduce

def call7(input,category):
    #result=collections.defaultdict(list)
    result={}
    newresult={}
    for category_key,category_val in category.items():
        if category_key not in result:
            result[category_key] =[0]*7
            for each_category_val in category_val:
                #result[category_key]= list(zip(result[category_key],input[each_category_val]))
                result[category_key]= list(map(max,result[category_key],input[each_category_val]))

    print (result)

#print(call7(input,category))




#merge intervals
given = [[20,30],[1,4],[3,6],[9,11],[11,12],[12,14]]
def merge_intervals(given):
    given.sort()
    result=[given[0]]
    for interval in given:
        if result[-1][1] >= interval[0]:
            result[-1][1] = interval[1]
        else:
            result.append(interval)
    return result

#print (merge_intervals(given))



input = ['opts','foo','bar','tops','pots','rab','ofo','hat']
output = [ ['opts','tops','pots'],['rab','bar'],['ofo','foo'],['hat']]
import collections as c
def anagram_sets(input):
    d=c.defaultdict(list)
    for each in input:
        curkey = ''.join(ch for ch in sorted(each))
        d[curkey].append(each)
    return d.values()

#print(anagram_sets(input))


#input =['i','love','i','loves','coffee','dog','coffee' ,'i']

#top k items
import heapq
def topk(input,k):
    result ={}
    nk=int(k)
    d={}
    for each in input:
        d[each] = d.get(each,0) + 1
    print (d)
    h=[] # heap
    for k,v in d.items():
        heapq.heappush(h,(v,(k,v)))
        if len(h) > nk:
            heapq.heappop(h)
        print (h)
        
    return h

print ('calling topk')

#print (topk(input,2))

"""
Popular Facebook problem
Input may or may not be sorted or have duplicates
Represent input stream as an array. Don't rely on size


"""
import heapq


def topK(iStream, iK):
    h = [iStream[0]]
    res = []
    for each in iStream[1:]:
        # heap root is at 0
        # insert only if the incoming value is greater or length of the heap is less than iK
        if each > h[0] or len(h) < iK:
            heapq.heappush(h, each)
        if len(h) > iK:
            heapq.heappop(h)
    while iK > 0:
        res.append(heapq.heappop(h))
        iK -= 1
    return res[::-1]

# print (topK([5,3,5,5,6,6,7,7,1,2,3,4,5],5))



