"""using stack to sort an array"""
input= [5,6,7,2,3,1,9,8]
oupput = [1,2,3,5,6,7,9,9]

def sort(input):
    s=input[0]
    for each in input[1:]:
        if each <= s[len(s)]:
            s.pop
        if s.insert(each,0)