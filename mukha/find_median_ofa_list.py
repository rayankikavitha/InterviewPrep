l =[4,5,7,9,2,4,5,9]


def median(input):
    l =len(input)
    sl =sorted(input)
    print sl
    if l%2 == 0:
        m = (sl[l/2 - 1]+ sl[l/2]) /2.0
    else:
        m = sl[l/2]
    return m

print median(l[4:])