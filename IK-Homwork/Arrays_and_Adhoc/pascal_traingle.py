"""
print pascal triangle for n lines

1
11
121
1331
14641
15101051

https://www.geeksforgeeks.org/pascal-triangle/

"""


def printnextseq(arr):
    p = 0
    r =[]
    for each in arr:
        r.append(each+p)
        p = each
    r.append(1)
    return r


def pascal(n):
    r=[1]
    s = 1
    print r
    while s <= n:
        nr = printnextseq(r)
        print nr
        r = nr
        s += 1


pascal(6)

#print printseq([1,3,3,1])
#print printnextseq([1,4,6,4,1])