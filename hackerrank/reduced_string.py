#input = '1222311'
#output = [(1,1),(3,2),(1,3),(2,1)]
# Its basically reading out like one 1, three 2, one 3, two 1
from itertools import groupby
from itertools import count


input = '1222311'
#print groupby(input)


#print(*[(len(list(c)), int(k)) for k, c in groupby(input)])
print [(k,len(list(c))) for k , c in groupby(input)]
newl = [str(len(list(c)))+k for k , c in groupby(input)]
print ''.join(x for x in newl)

input2 = '11321321'
def reverse_reduced_string(s):
    """
    It it a combination of numbers
    :param s:
    :return:
    """
    res=''
    for i in range(0,len(s),2):
        res = res+(s[i+1]*int(s[i]))
    return res

print reverse_reduced_string(input2)
