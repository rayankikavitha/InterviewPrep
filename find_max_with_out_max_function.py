s=[4,8,2,1,9,5,0,10,3]

def find_max(input):
    m = 0
    for each in s:
        if each > m :
            m = each
    return m

print find_max(s)

print max(s)