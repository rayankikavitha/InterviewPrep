"""
    The general idea is to iterate over string s.
    Always put the character c and its location i in the dictionary d.
    1) If the sliding window contains less than or equal to k distinct characters, simply record the return value, and move on.
    2) Otherwise, we need to remove a character from the sliding window.
       Here's how to find the character to be removed:
       Because the values in d represents the rightmost location of each character in the sliding window, in order to find the longest substring T, we need to locate the smallest location, and remove it from the dictionary, and then record the return value.
"""

def lengthOfLongestSubstringKDistinct(s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # Use dictionary d to keep track of (character, location) pair,
        # where location is the rightmost location that the character appears at
        d = {}
        low, ret = 0, 0
        for i, c in enumerate(s):
            d[c] = i
            if len(d) > k: # if the count is greater than k, remove the one with the lowest index, so the window slides next 
            	print d, low
                low = min(d.values())
                del d[s[low]]
                low += 1
            	print d, low
            ret = max(i - low + 1, ret)
        return ret

print lengthOfLongestSubstringKDistinct('ecebd',2)