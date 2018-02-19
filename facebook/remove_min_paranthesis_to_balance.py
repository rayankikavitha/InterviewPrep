"""
Given an input string containing (()()( remove minimum number of paranthesis to make it balance and return
((a) -> (a)
)a( -> a

"""
def balanceparan(arr):
    s=[]
    invalid =[]
    for i in range(len(arr)):
        if arr[i] == '(':
            s.append(i)
        elif arr[i] ==')':
            if len(s) >0:
                s.pop()
            else:
                invalid.append(i)
    return s+invalid

print balanceparan("(()()(")
print balanceparan("((a)")
print balanceparan(")a(")

