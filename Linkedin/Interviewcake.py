# Validate braces

"""
Write an efficient function that tells us whether or not an input string's openers and closers are properly nested.

Examples:

"{ [ ] ( ) }" should return True
"{ [ ( ] ) }" should return False
"{ [ }" should return False
"""
def match_braces(given):
	braces = {'}':'{',']':'[',')':'(',}
	openers = set(braces.values())
	closers = set(braces.keys())
	stack=[]
	for i,v in enumerate(given):
		if v in openers:
			stack.append(v)
		else:
			top = stack.pop()
			if top <> braces[v]:
				return False
	if len(stack) ==0:
		return True
	else:
		return False

print (match_braces('{[]()}'))
print (match_braces('{[(})}'))
print (match_braces("{[}"))
