"""
Find the length of the longest substring that has matching opening and closing paranthesis
Input: "((((())((()"
output: 4 for "(())"
Output length, not the string.

https://docs.google.com/document/d/1UBFl633FsCZLq2Vejihj2g80Vdl9BNF6-N1D4J-clsI/edit



"""
import unittest


def findMaxLen(string):
    n = len(string)

    # Create a stack and push -1 as initial index to it.
    stk = []
    stk.append(-1)

    # Initialize result
    result = 0

    # Traverse all characters of given string
    for i in xrange(n):

        # If opening bracket, push index of it
        if string[i] == '(':
            stk.append(i)

        else:  # If closing bracket, i.e., str[i] = ')'

            # Pop the previous opening bracket's index
            stk.pop()

            # Check if this length formed with base of
            # current valid substring is more than max
            # so far
            if len(stk) != 0:
                result = max(result, i - stk[len(stk) - 1])
                print result,stk,i

            # If stack is empty. push current index as
            # base for next valid substring (if any)
            else:
                stk.append(i)

    return result


# Driver program
#string = "((()()"
#print findMaxLen(string)

#string = "()(()))))"
string = ")()())"
print findMaxLen(string)


def maxLenMatchingParen(input):
    s=[]
    count = 0
    maxlen = 0
    n = len(input)
    instate  = 0
    # we will store indexes of unmatched parantheses.
    for i in xrange(len(input)):
        if input[i] =='(':
            s.append(i)
        else:
            if len(s) != 0:
                #print s[len(s) - 1]
                print s,i
                if input[s[len(s)-1]] == '(':
                    s.pop()
                else:
                    s.append(i)
            else:
                s.append(i)
    print s
    # if the stack is empty then all pairs are matching
    if len(s) == 0:
        maxlen = n
    # else, adjacent indexes strings are matching
    else:
        curr = n
        top = 0
        while s:
            top = s.pop()
            #print curr,top
            maxlen = max( maxlen, curr - top - 1 )
            curr = top
        # catch when there is matching set at the beginning.
        maxlen = max(maxlen, curr)

    return maxlen

#assert(maxLenMatchingParen(")()())")==4)
#assert(maxLenMatchingParen("(((())))(((()")==8)

#assert(maxLenMatchingParen("()")==2)

#assert(maxLenMatchingParen("((())") == 4)
#assert(maxLenMatchingParen("()(())") == 6)
#assert(maxLenMatchingParen("(((((")==0)
#assert(maxLenMatchingParen(")))")==0)

#assert(maxLenMatchingParen("())")==2)
#assert(maxLenMatchingParen("(()")==2)
#assert(maxLenMatchingParen("((((())(((()")==4)







