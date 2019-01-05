def numSetBits( A):
    ret = 0
    while A != 0:
        if A & 1:
            ret += 1
        A = A >> 1
    return ret

print numSetBits(78)
print bin(78)