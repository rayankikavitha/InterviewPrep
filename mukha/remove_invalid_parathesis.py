"""
 We all know how to use stack to check for balancing of parathensis. or simple counter
 The counter will increase when it sees '(' and decreases when ')', when ever counter is negative, we have more ')'
 We all know how to check a string of parentheses is valid using a stack. Or even simpler use a counter. The counter will increase when it is ‘(‘ and decrease when it is ‘)’. Whenever the counter is negative, we have more ‘)’ than ‘(‘ in the prefix.
To make the prefix valid, we need to remove a ‘)’. The problem is: which one? The answer is any one in the prefix. However, if we remove any one, we will generate duplicate results, for example: s = ()), we can remove s[1] or s[2] but the result is the same (). Thus, we restrict ourself to remove the first ) in a series of concecutive )s.
After the removal, the prefix is then valid. We then call the function recursively to solve the rest of the string. However, we need to keep another information: the last removal position. If we do not have this position, we will generate duplicate by removing two ‘)’ in two steps only with a different order. For this, we keep tracking the last removal position and only remove ‘)’ after that.
Now one may ask. What about ‘(‘? What if s = ‘(()(()’ in which we need remove ‘(‘? The answer is: do the same from right to left. However a cleverer idea is: reverse the string and reuse the code! Here is the final implement in Java.


"""


def removeInvalidParentheses(self, s):
    """
    :type s: str
    :rtype: List[str]
    """
    result = []
    remove(s, result, 0, 0, ('(', ')'))
    return result

def remove(s, result, last_i, last_j, par):
    count = 0
    for i in xrange(last_i, len(s)):
        count += (s[i] == par[0]) - (s[i] == par[1])
        print count
        if count >= 0:
            continue
        for j in xrange(last_j, i + 1):
            if s[j] == par[1] and (j == last_j or s[j - 1] != par[1]):
                remove(s[:j] + s[j + 1:], result, i, j, par)
        return
    reversed_s = s[::-1]
    if par[0] == '(':
        remove(reversed_s, result, 0, 0, (')', '('))
    else:
        result.append(reversed_s)