import sys

s1 = 'oagciicgaoyjmahhamjymmwjnnjwmmvpxhpphxpvlikappakilyygvkkvgyymlpfddfplmhiodvvdoihfxpkggkpxfuevvuuvveu'
#output = 'Empty String'

def super_reduced_string(s):
    # Complete this function
    l = list(s)

    i = 0
    # replace the matching values with zeros
    while i < len(l) - 1:
        if l[i] == l[i + 1]:
            if i+1 != len(l)-1:
                newl = l[:i]+l[i+2:]
            else:
                newl = l[:i]
            i =0
            l = newl
        else:
            i = i + 1
    print l
    #count zeros and remove them.
    zero =l.count('0')
    while zero > 0:
        l.remove('0')
        zero -= 1

    # convert a list to string.
    if len(l):
        return ''.join(x for x in l)
    else:
        return 'Empty String'



s ='aaabccddd'
print super_reduced_string(s)
print super_reduced_string(s1)
