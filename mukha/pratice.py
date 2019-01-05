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
#print merge(input)


def find_most_ones(nums):
    curmax, fnlmax = 0,0
    for i in range(len(nums)):
        if nums[i] == 1:
            curmax += 1
        else:
            fnlmax = max(fnlmax, curmax)
            curmax = 0
    fnlmax = max(fnlmax, curmax)
    return fnlmax
print '********* find most ones **********'
print find_most_ones ([1,1,0,0,1,1,1,1,0,0,1,1,1])

#Given an unsorted integer array, find the first missing positive integer.
#For example,
#Given [1,2,0] return 3,
#and [3,4,-1,1] return 2.
#Your algorithm should run in O(n) time and uses constant space.
def first_missing_nonnegative_int(A):
    n = len(A)
    total = 0
    for i in range(len(A)):
        if A[i] > 0:
            total += A[i]
    sumtotal = n*(n+1) //2
    return sumtotal - total 

def firstMissingPositive(nums):
    """
    :type nums: List[int]
    :rtype: int
     Basic idea:
    1. for any array whose length is l, the first missing positive must be in range [1,...,l+1], 
        so we only have to care about those elements in this range and remove the rest.
    2. we can use the array index as the hash to restore the frequency of each number within 
         the range [1,...,l+1] 
    """
    nums.append(0)
    n = len(nums)
    for i in range(len(nums)): #delete those useless elements
        if nums[i]<0 or nums[i]>=n:
            nums[i]=0
    print nums
    for i in range(len(nums)): #use the index as the hash to record the frequency of each number
        print nums
        nums[nums[i]%n]+=n

    for i in range(1,len(nums)):
        print nums
        if nums[i]/n==0:
            return i
    return n
print '*******first Missing Positive********'
print firstMissingPositive([3,4,-1,1])
print firstMissingPositive([0, 10, 2, -10, -20])

def firstMissingPositive_v2(array):
    for cursor in range(N): 
        target = array[cursor]
        while target < N and target != array[target]:
            new_target = array[target]
            array[target] = target
            target = new_target

    #Pass 2, find first location where the index doesn't match the value
    for cursor in range(N):
        if array[cursor] != cursor:
            return cursor
    return N

# kth largest element in an array
def kth_largest(arr, k):
    pi = partition(arr,0,len(arr) -1)
    print pi
    while pi != k-1:
        if k < pi-1:
            return kth_largest(arr[:pi],k)
        else: 
            return kth_largest(arr[pi+1:],k)
    if pi == k-1:
        return arr[k]


def partition(arr,first, last):
    # choose a pivot and divide elements on the left side to be less than pivot and right side greater than pivot
    pivotvalue = arr[first]
    left = first+1
    right = last
    done = False
    while not done:
        while left <= right and arr[left] <= pivotvalue:
            left += 1
        while left <= right and arr[right] >= pivotvalue:
            right -= 1

        if right < left:
            done = True
        else:
            arr[left],arr[right] = arr[right],arr[left]
    arr[first],arr[right] = arr[right], arr[first]
    return right


nums1 = [9, 3, 6, 2, 1, 7, 5, 8, 4]
nums2 = [5, -2, -1, 4, 5, 1, 0]
print "********kth largest ********"
print kth_largest(nums1, 4)


# find first unique character in a string
# example leetcode  #output = l, loveleetcode  #output = v
def first_unique_char(s):
    # usually we can solve it using dictionary and set. 
    # In this version, we are solving using array
    freq = [0]*26
    for i in range(len(s)):
        freq[ord(s[i]) - ord('a')] += 1
    print freq
    for i in range(len(s)):
        if freq[ord(s[i]) - ord('a')]  == 1:
            return s[i]
    return -1

print '******** first unique character ********'
print first_unique_char('loveleetcode')


# add binary
def add_binary(a,b):
    # add two binary strings and return their result as binary string a = "11" b ="1". output = "100"
    c = '0'
    result =''
    mapping = {'110':'10','100':'01','010':'01','001':'01','000':'00','111':'11','101':'10','011':'10'}
    maxlen = max(len(a),len(b))
    if len(a) != maxlen:
        a = '0'*(maxlen - len(a)) + a
    if len(b) != maxlen:
        b = '0'*(maxlen - len(b)) + b

    for i in range(maxlen-1,-1,-1):
        #print a[i]+b[i]+c
        cs = mapping[a[i]+b[i]+c]

        result += cs[1]
        c = cs[0]
    result += c
    return result[::-1]

print "******* add binary strings********"
print add_binary('111','111')
print add_binary('11','1')

###################################
#--- search in a roated array----------
# input = [23, 48, 59, 60, 10 , 15, 19]
# find = 23
# output True/False
#########################################
def search_in_rotated_array(arr,k):
    return search_in_rotated_array_helper(arr,0,len(arr)-1,k)

def search_in_rotated_array_helper(arr,l,h,k):
    #takes care of duplicates too
    while l <= h:
        mid = (l+h)/2
        if k == arr[mid]:
            return mid
        if arr[l] < arr[mid] or arr[mid] > arr[h]: #rotation is on the right
            if arr[l] <= k <= arr[mid]:
                h = mid - 1
            else:
                l = mid + 1
        elif arr[mid] < arr[h] or arr[l]>arr[mid]:# rotation is on the left
            if arr[mid] <= k <= arr[h]:
                l = mid + 1
            else:
                h = mid - 1 
        else: # that means duplicate arr[mid] == arr[h] or arr[mid] = arr[l], move either one of the points to remove from consideration
            h -= 1  # even l += 1 also works
    return -1


print '***** search in rotated_array *******'
print search_in_rotated_array([19,23, 48, 59, 60, 10 , 15, 19],23)
    



###############################
# find min absolute difference
#############################
def min_absolute_diff(arr):
    arr.sort()
    curdiff = max(arr)
    for i in range(len(arr)-1):
        curdiff = min(curdiff, abs(arr[i] - arr[i+1]))
    return curdiff

print "**** min min_absolute_diff ********"
print min_absolute_diff([1,5,6,19,20,3,25])

#----------------------------------
#   longest non-repeating substring length - lcs ( longest common substring with non-repeating)
#   abcadefghabmn  
#    pwwkew
#----------------------------
def longest_non_repeating_substring(s):
    start = 0
    seen ={}
    maxlen = 0
    for i in range(len(s)):
        if s[i] in seen and start <= seen[s[i]]:
            start = seen[s[i]]+1
        else:
            maxlen = max(maxlen, i-start+1)
        print start, seen, maxlen
        seen[s[i]] = i
        
    return maxlen

print '**** longest non-repeating substring *****'
print longest_non_repeating_substring('abcadefghabmn')

#---------------------------
# implement strstr or return index of the first occurence of the substring, else return -1
#----------------------------
def strstr(haystack, needle):
    i,j = 0,0
    while i < len(haystack) and j < len(needle):
        
        if haystack[i] == needle[j]:
            i +=1
            j +=1
        else:
            i += 1

        if j == len(needle):
            return i - j 
    return -1
print '*** substring index *****'
print strstr('kavitham', 'ham')
print strstr('amruthapoojarayanki','pooja')
print strstr('kavitham','kavi')
print strstr('kavitham','amrutha')
#--------------------------------------------------------------------
# countandsay or reduced string example aaaaabbbbccccaaa -> a4b3c3a3 
#  21 ->  1211 -> 111221->312211 -> etc
#--------------------------------------------------------------------
def countandsay(s):
    res=''
    count = 1
    s = s+'*'
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            res += str(count)+s[i]
            count = 1

    return res

print '*** count and say *****'
print countandsay('121113')

#-------------------
# move zeros 
# given [2,3,0,6,0,0,8,0,9] output = [[2,3,6,8,9,0,0,0]]
#------------
def movezeros(nums):
    start = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[start] = nums[i]
            start += 1

    for i in range(start,len(nums)): # fill the rest of them with zeros.
        nums[i] = 0

    return nums

print '**** move zeros *****'
print movezeros([2,3,0,6,0,0,8,0,9])
#-----------------------------
#  Minimum Size Subarray Sum equals to 0 or K 
#. array can have negative and positive integers.
#  Example =  [2,3,5,-9,-1,5,-5,4,1,8,1]
#-----------------------------------
def min_size_subarray_sum(nums,k):
    result = None
    csum_map ={}
    csum = 0
    minlen,carray = len(nums),None
    for i in range(len(nums)):
        csum += nums[i]
        if (csum == k and csum not in csum_map) or k-csum in csum_map:
            carray = nums[csum_map.get(k-csum,0):i+1]
            print carray

            if minlen > len(carray):
               result = carray
               minlen = len(carray)
               print result, minlen
        csum_map[csum] = i
        #print csum_map
    return result

print '**** min size subarray sum ***'
print min_size_subarray_sum([2,3,5,-9,-1,5,-5,4,1,9,1],10)
#print min_size_subarray_sum([2,3,5,-9,-1,5,-5,4,1,8,1],0)
















#----------------------------
# kth largest element in an array 
# using quick select.
"""

  Move Zeroes
Editor's choice: Frequently asked in Facebook phone interview.
  Add Binary
Editor's choice: Frequently asked in Facebook phone interview.
  Intersection of Two Arrays II
Editor's choice: Frequently asked in Facebook phone interview.
  3Sum
Editor's choice: Frequently asked in Facebook phone interview.
  Valid Palindrome
  Valid Palindrome II
Editor's choice: Frequently asked in Facebook phone interview.
  Valid Number
  Minimum Size Subarray Sum
  Maximum Size Subarray Sum Equals k
  Valid Parentheses

  sorting and searching :

  First Bad Version
Editor's choice: Frequently asked in Facebook phone interview.
  Meeting Rooms II
Editor's choice: Frequently asked in Facebook onsite interview.
  Merge Sorted Array
Editor's choice: Frequently asked in Facebook phone interview.
  Merge Two Sorted Lists
  Merge k Sorted Lists
Editor's choice: Frequently asked in Facebook phone interview.
  Search in Rotated Sorted Array
Editor's choice: Frequently asked in Facebook onsite interview.
  Search in Rotated Sorted Array II
  Merge Intervals
  Smallest Range
Editor's choice: Frequently asked in Facebook onsite interview.

Others:

  Kth Largest Element in an Array
Editor's choice: Frequently asked in Facebook phone interview.
  Divide Two Integers
Editor's choice: Frequently asked in Facebook phone and onsite interview.
  Find the Celebrity
Editor's choice: Frequently asked in Facebook onsite interview.
  Task Scheduler
Editor's choice: Frequently asked in Facebook phone and onsite interview.
  Integer to English Words
Editor's choice: Frequently asked in Facebook on campus, phone and onsite interview.
  Minimum Window Substring
  Palindrome Pairs

  SQL :

  Second Highest Salary
  Nth Highest Salary
  Customers Who Never Order
  Friend Requests I: Overall Acceptance Rate
  Friend Requests II: Who Has the Most Friends
  Department Top Three Salaries
"""






