# Python program to find maximum contiguous subarray

def maxSubArraySum(a):
    size = len(a)
    max_so_far = a[0]
    curr_max = a[0]

    for i in range(1, size):
        curr_max = max(a[i], curr_max + a[i])
        #print curr_max
        max_so_far = max(max_so_far, curr_max)
        #print max_so_far
        #print '*********'
    return max_so_far



# Driver function to check the above function
a = [-2, -3, 4, -1, -2, 1, 5, -3]
print "Maximum contiguous sum is", maxSubArraySum(a)

# This code is contributed by _Devesh Agrawal_

s = "The    dog     walks"
#output ="ehT god sklaw'

def reverse_sentence(s):
    res =''
    for each in s.split():
        res = res+' '+ each[::-1]
    return res

print reverse_sentence(s)

def reversestr(s,start,end):
    while start < end:
        s[start],s[end] = s[end],s[start]
        start +=1
        end -=1



def reverse_sentence_preserve_spaces(s):
    i, j = 0, len(s)-1
    reversestr(s,i,j)
    for i in range(len(s)-1):
        if s[i+1]



