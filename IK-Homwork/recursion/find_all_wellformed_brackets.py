"""
Give a size = n, find all possible combinations of round brackets of size 2n
Input = 3
output = ()()(), ((())), (())(), ()(()),(()())
"""
def generateParenthesis( n):
    def generate(p, left, right, parens=[]):  # parent =[] is to catch all the outputs
        if left:         generate(p + '(', left-1, right)
        if right > left: generate(p + ')', left, right-1)
        if not right:    parens += p,  # comma is important to attach to the same string
        return parens
    return generate('', n, n)

print generateParenthesis(2)
print generateParenthesis(3)