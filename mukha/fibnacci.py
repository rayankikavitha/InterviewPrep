# print nth fibonacci number
def fib(n):
    # iterative
    a = 0  #seeds
    b = 1  #seeds
    i = 2
    while  i < n:
        t = a+b
        a = b
        b = t

        i= i+1
    return t


def fib2(n):
    # recursive # n starts at 1
    if n<=0:
        print "error"
    elif n == 1:
        return 0
    elif n == 2 :
        return 1
    else:
        return fib2(n-1) + fib2(n-2)




print fib2(9)

print fib(9)
# 0,1,1,2,3,5,8,13,21,34
# 1,2,3,4,5,6,7,8,9,10

def fib3(n):
    res =[]