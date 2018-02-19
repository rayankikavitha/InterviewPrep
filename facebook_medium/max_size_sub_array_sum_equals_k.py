nums = [1, -1, 5, -2, 3]
k = 3
# output = 4 (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

nums1 = [-2, -1, 2, 1]
k1 = 1
#output = 2. (because the subarray [-1, 2] sums to 1 and is the longest)

def maxSubArrayLen(nums, k):
    ans, acc = 0, 0               # answer and the accumulative value of nums
    mp = {0:-1}                 #key is acc value, and value is the index
    for i in xrange(len(nums)):
        acc += nums[i]
        print i
        print acc
        if acc not in mp:
            mp[acc] = i
        if acc-k in mp:
            ans = max(ans, i-mp[acc-k])
            print ans
        print mp
        print '********'
    return ans

print maxSubArrayLen(nums, k)