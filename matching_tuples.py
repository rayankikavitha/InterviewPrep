"""
Return tuples of a list, matching each item to another item.
"""
from collections import defaultdict
hand=[(2, "Club"), (4, "Heart"), (2, "Diamond"), (5, "Club"), (8, "Spades")]
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1), ('yellow',1)]
def match_tuples(input):
    # initalize it as a list
    d = defaultdict(list)
    for k,v in input:
        d[k].append(v)
    return d

print match_tuples(s)
print match_tuples(hand)

def match_regular(input):
    pair = []
    for each in input:
        if input.count(each) > 1:
            pair.append(each)
    return pair

print match_regular(s)

t = ( (1,3),(4,5),(3,1),(8,9),(5,4))
def match_tuples2(input):
    res=[]
    res.append( [(each[0],each[1]) for each in input if (each[1],each[0]) in input])

    return res

print match_tuples2(t)

