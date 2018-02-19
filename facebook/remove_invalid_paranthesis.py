"""
Remove min number of paranthesis to make it balalnced

"""

def removeInvalidParentheses( s):
    def isvalid(s):
        ctr = 0
        for c in s:
            if c == '(':
                ctr += 1
            elif c == ')':
                ctr -= 1
                if ctr < 0:
                    return False
        return ctr == 0
    level = {s}
    print level
    while True:
        valid = filter(isvalid, level)
        print valid
        if valid:
            return valid
        level = {s[:i] + s[i+1:] for s in level for i in range(len(s))}

print removeInvalidParentheses("(()()")


def min_no_of_paranthesis(s):
    counter = 0
    mini = len(s)+1
    for ch in s:
        if ch == "(":
            counter  += 1
        else:
            counter -= 1
    mini = min(counter, mini)
    return abs(mini)

print min_no_of_paranthesis("())(())(()())))")