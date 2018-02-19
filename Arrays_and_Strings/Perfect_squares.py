def numSquares( n):
    if n < 2:
        return n
    # create square numbers until n
    i=1
    squares =[]
    while i*i <= n:
        squares.append(i*i)
        i += 1
    print squares
    # create a set to check
    toCheck = {n}
    cnt = 0
    while toCheck:
        cnt += 1
        # keep the intermediate values
        temp = set()
        for x in toCheck:
            for y in squares:
                if x == y:
                    return cnt
                if x < y:
                    #print "before breaking(x,y)="+str(x)+" "+str(y)
                    break
                temp.add(x - y)
        toCheck = temp
    return cnt


def numSquares1(self, n):
    if n < 2:
        return n
    lst = []
    i = 1
    while i * i <= n:
        lst.append( i * i )
        i += 1
    cnt = 0
    toCheck = {n}
    while toCheck:
        cnt += 1
        temp = set()
        for x in toCheck:
            for y in lst:
                if x == y:
                    return cnt
                if x < y:
                    break
                temp.add(x-y)
        toCheck = temp

    return cnt

print numSquares(12)

print numSquares(13)