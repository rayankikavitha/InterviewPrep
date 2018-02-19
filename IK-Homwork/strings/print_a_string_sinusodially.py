"""
Google Worked should be printed as

  o   ~    k
 o g e w  r  e
g   l   o      d

"""
def sinusodial(s,n):
    """
    :param s: incoming string
    :param n: sinusodial length
    :return:
    """
    if n==1:
        return s
    sl=len(s)
    #https://snakify.org/lessons/two_dimensional_lists_arrays/
    # below method is wrong to create m*n list
    #a = [[0] * sl] * n
    # instead use this
    a = [[0] * sl for i in range(n)]
    # for counting zigzag rows -> n
    row,col = 0,0
    # create a 2d array of length sl, rows = n
    while col < sl:
        if s[col] ==' ':
            a[row][col] = '~'
        else:
            a[row][col] = s[col]
        if row == n-1:
            down = False
        if row == 0:
            down = True
        if down:
            row += 1
        else:
            row -= 1
        col += 1

    #print a
    # print the zig zag string
    for i in range(n):
        for j in range(sl):
            if a[i][j] != 0:
                print a[i][j],
            else:
                print ' ',
        print

def interleave(a, b):
    if len(a) == 0 and len(b) == 0:
        return []
    elif len(a) == 0:
        return [b]
    elif len(b) == 0:
        return [a]

    first = [a[0] + s for s in interleave(a[1:], b)]
    second = [b[0] + s for s in interleave(a, b[1:])]

    return first + second

sinusodial("google worked",2)
sinusodial("google worked", 3)
print '---------------------------'
sinusodial("google worked",4)

#print interleave("googleworked","1234567")

