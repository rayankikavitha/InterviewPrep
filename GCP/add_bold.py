
"""
Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.
Example 1:
Input: 
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"
Example 2:
Input: 
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"

 Solution : create a mapping of start letter to list of words in a given dictionary
 Iterate over sting, maintaining a list of words from dictionary that have partially matched up to the current index
 Matches list consists of previous matches that alsomatch the next c, plus new words with the start letter of c
 If all chars of a word are matched, mark all those chars in s as being in a tag
 finally, construct result by inserting opening and closing tags
 time = O(n*k + m ) n words in a dictionary of max length k,  m = length of the string
 space : O(nk + m)
"""
def addbold_interval(S,M):
	"""
	given string S and mapping M, return the string with bold tags
	We can use merge overlapping intervals method.
	So, we can transform ["aaa","aab","bc"] to [(0,2),(1,3),(4,5)] => [0,5]
	"""
	# create intervals
	intervals=[]
	merged_intervals = []
	for each in M:
		start = S.find(each)
		if start>=0:
			intervals.append((start,start+len(each)-1))
	print intervals
	merged_intervals = merge_intervals(intervals)

	boldstr =''
	btb, bte = '<b>','</b>'
	for interval in merged_intervals:
		boldstr += btb+S[interval[0]:interval[1]+1]+bte
	return boldstr


#import collections
#nums = collections.namedtuple('start','end')
def merge_intervals(nums):
	result = [nums[0]] # start with first value as result
	for num in nums[1:]:
		if result[-1][1] >= num[0]:           # keep merging if you see overlap
			result[-1][1] = max(num[1], result[-1][1])
		else:
			result.append([num[0],num[1]])
	return result
	

from collections import defaultdict
def addbold(dict, str):
	result =''
	in_tag = [ False for _ in range(len(s))] # bool indicates whether char should be inside a bold tag
	start_letters= defaultdict(list)  # mapping from start char to list of words with that  start char
	for word in dict:
		start_letters[word[0]].append(word) 
	print start_letters
	matches = []     # list of (word, word index) that matches up a word upto index

print '****** add bold tags ****'
print addbold_interval ("abcxyz123", ["abc","123"])

