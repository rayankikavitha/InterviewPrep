"""
given = [ 'bat','tab','cat'], bat and tab can be comibed to form a palindrome
given = [ab,deedba] can be joined to form a palindrome
return the first one found

given = {"geekf", "geeks", "or","keeg", "abc", "bc"};

"""


def is_palindrome(given):
	return given == given[::-1]

def find_pairs(given):
	result =[]
	values = []
	d = {v[::-1]:i for i,v in enumerate(given)}
	for i,word in enumerate(given):
		for j in range(len(word)+1):
			prefix = word[:j]
			postfix = word[j:]

			#print (prefix)
			#print (postfix)
		    # if there is prefix and not the same word and the remaining characters are palidrome		
			if prefix in d and d[prefix] != i and is_palindrome(postfix):
				result.append((i,d[prefix]))
			if j > 0 and postfix in d and d[postfix] != i and is_palindrome(prefix):
				result.append((d[postfix],i))

			#print (result)
	return result
	

def palindromePairs(words) :
        if not words: return [[]]
        lookup = {w: i for i,w in enumerate(words)}   # swap key (index) and value (word)
        res = []
        for i, w in enumerate(words):
            for j in range(len(w)+1):
                pre, suf = w[:j], w[j:]   # pre(fix) and suf(fix)
                if pre==pre[::-1] and suf[::-1]!=w and suf[::-1] in lookup:
                    res.append([lookup[suf[::-1]], i])   # palindrome prefix e.g. 'lls' and 's', 'sssll' and 'lls' in Example 1
                if suf==suf[::-1] and pre[::-1]!=w and pre[::-1] in lookup and j!=len(w):   # j==len(w) case is already checked above
                    res.append([i, lookup[pre[::-1]]])   # palindrome suffix e.g. 'sll' and 's'
        return res

given1 = ["geekf", "geeks", "or","keeg", "abc", "bc"];
print (find_pairs(given1))
print (find_pairs(['bat','tab','cat']))
print (find_pairs(['ab','deedba']))

#print (palindromePairs(given1))



	
