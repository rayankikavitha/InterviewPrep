"""
https://discuss.leetcode.com/topic/71662/sliding-window-algorithm-template-to-solve-all-the-leetcode-substring-search-problem

Given the string, find the length of the longest substring T that contains at most k distinct characters

Example:

Input = S ="eceba", k = 2
output = "ece", only 2 distinct here, but the length is 3

"aabbcc", k = 3
There are substrings with exactly 3 unique characters
{"aabbcc" , "abbcc" , "aabbc" , "abbc" }
Max is "aabbcc" with length 6.


If there are no such substrings, all same characters, then print nothing
If there are multiple such strings, then print any one

http://www.geeksforgeeks.org/find-the-longest-substring-with-k-unique-characters-in-a-given-string/


def longest_substring_with_k_unique_characters2(s,k):

    Method 2 : o(n)
    Method 2 (Linear Time) Sliding window
    Idea is to maintain a window and add elements to the window till it contains less or equal k,
    update our result if required while doing so.
    If unique elements exceeds than required in window, start removing the elements from left side.
    :param s:
    :param k:
    :return:


"""

# Python program to find the longest substring with k unique
# characters in a given string
MAX_CHARS = 26

# This function calculates number of unique characters
# using a associative array count[]. Returns true if
# no. of characters are less than required else returns
# false.

def longest_substring_with_2_characters(s,k):
    d ={}
    start, end = 0,0
    counter = 0
    length = 0
    result =[]
    while end < len(s):
        print str(d)+" start = "+str(start)+" end = "+str(end)+" counter = "+str(counter)
        d[s[end]] = d.get(s[end],0) + 1  #add to the dict
        if d[s[end]] == 1:
            counter +=1   # new character
        # If there are more than k unique characters in
        # current window, remove from left side
        while counter > k:
            d[s[start]] = d[s[start]] - 1
            if d[s[start]] == 0:
                counter -=1
            start +=1
        if counter == k:
            length = max(length, end - start +1)
            result.append(s[start:end+1])

        end += 1

    # print any result with maximum length
    if len(result):
        fresult = [x for x in result if len(x) == max(map(len,result))][0]
        return fresult
    else:
        return None
    #return length,fresult


print longest_substring_with_2_characters("ecebg",2)
print longest_substring_with_2_characters("ttttttt",2)
print longest_substring_with_2_characters("aabbcc",2)

def longest_substring_with_k_unique_characters(s,k):
    """
    brute force O(n**2)
    keep iterating along with string, keeping track of seen characters in a set

    Returns substring with k unique characters and of max length
    :param S: Input string
    :param K: no.of unique characters
    :return:
    """
    # set length should be k

    result =[]
    for i in xrange(len(s) - k + 1):
        seen = set(s[i]) # start with first character
        j = i+1

        while j < len(s):
            #print j
            if s[j] not in seen:
                if len(seen) < k:
                    seen.add(s[j])
            else:
                j +=1
            if len(seen) == k:
                result.append(s[i:j+1])
        #print seen,i,j
    print result
    return max( map(len,result))

#print longest_substring_with_k_unique_characters("aabbcc", 3)