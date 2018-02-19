import heapq
def freq_count(input, k):
    d={}
    result=[]
    for each in input:
        d[each] = d.get(each, 0) + 1
    h=[]
    for key, val in d.iteritems():
        heapq.heappush(h, (val,(key, val)))
        print h
        if len(h) > k :
            heapq.heappop(h)
            print h
    while k > 0:
        result.append(heapq.heappop(h)[1][0])
        k = k - 1
    return result[::-1]

input =['i','love','i','loves','coffee','dog','coffee' ,'i']

print freq_count(input, 2)

def last_k_freq_count(input,k):
    d = {}
    result = []
    for each in input:
        d[each] = d.get(each, 0) + 1
    h = []
    for key,val in d.iteritems():
        heapq.heappush(h, ( -val,(key,val)))
        print h
        if len(h) > k:
            heapq.heappop(h)

    while k > 0:
        result.append(heapq.heappop(h)[1][0])
        k = k -1

    return result[::-1]

input1 =[1,2,3,4,5,6]
input2 = [4,2,6,1,3,5]
input3 = [6,5,4,3,2,1]


def heappeek(h):
    c = heapq.heappop(h)
    heapq.heappush(h,c)
    return -c

def first_k(input, k):
    h =[input[0]]
    res =[]
    for each in input[1:]:
        c = heappeek(h)
        if c < each or len(h) < k:
            heapq.heappush(h,each)
        if len(h) > k:
            heapq.heappop(h)
        print h
    while k > 0:
        res.append(heapq.heappop(h))
        k = k -1
    return res



def last_k(input, k):
    h =[-input[0]]
    res =[]
    for each in input[1:]:
        # in case there the values are coming in sorted order.
        cur = heappeek(h)
        print cur
        if cur > each or len(h) < k:
            heapq.heappush(h,-each)
        print h
        if len(h) > k:
            heapq.heappop(h)
            print h
        print h
    print "nlargest"
    res.append(-heapq.nlargest(k))

    return res

import heapq
def topK(iStream, iK):
    h=[iStream[0]]
    res=[]
    for each in iStream[1:]:
        # heap root is at 0
        if each > h[0] or len(h) < iK:
            heapq.heappush(h,each)
        if len(h) > iK:
            heapq.heappop(h)
    while iK > 0:
        res.append(heapq.heappop(h))
        iK -= 1
    return res[::-1]

print "********** first k ***********"
print first_k(input1,2)
print last_k(input1,2)
print first_k(input3,2)






