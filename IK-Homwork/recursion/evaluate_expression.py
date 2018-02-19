"""
Given a string of integers as input, put between each pair of digits, of of {"","*","+"} such that the
expression you get will evaluate to k.
Putting an empty string ("") between two numbers mean, that the numbers are joined to form a new number
eg 1 "" 2 = 12

order of integers given as input neeeds to remain the same

input :
string of positve integers
Target K

Output:

All possible strings that evaluate to K

Example:
    If the input is "222" and K = 24
    possible answers are
    22 + 2  2 "" 2 "+" 2
    2+22

Remember the precendence matters
1. join ""
2. Multiplication (*)
3. Addition(+)

"""

"""
Top 3 points :
Lets use include exclude logic
# don't create intermediate variable in recursion. It is hard to keep track of them
# try to induce the rule for 1, 2, 3,...k ... n-1 and n

"""

def addOperators(num, target):
    """
    Uses include/exclude logic
     for i =1
     dfs(22,2,int(22),int(2),res,24)
     for i =2
     dfs(2,22,int(22),int(22),res,24)
    :param self:
    :param num:
    :param target:
    :return:
    """
    res = []
    for i in range(1,len(num)+1):
        if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
            print "from addOperators"
            print num[i:], num[:i], int(num[:i]), int(num[:i]), res,target
            dfs(num[i:], num[:i], int(num[:i]), int(num[:i]), res,target) # this step put first number in the string
    return res

def dfs( num, temp, cur, last, res,target):
    if not num:
        if cur == target:
            res.append(temp)
        return
    for i in range(1, len(num)+1):
        val = num[:i]
        if i == 1 or (i > 1 and num[0] != "0"): # prevent "00*" as a number
            print "from dfs"
            print num[i:], temp + "+" + val, cur + int(val), int(val), res, target
            dfs(num[i:], temp + "+" + val, cur+int(val), int(val), res, target)
            #dfs(num[i:], temp + "-" + val, cur-int(val), -int(val), res, target)
            dfs(num[i:], temp + "*" + val, cur-last+last*int(val), last*int(val), res, target)


print addOperators('222',24)

print addOperators('123',6)