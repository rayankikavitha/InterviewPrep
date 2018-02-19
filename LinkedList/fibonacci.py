# print fibonacci series
#
def fib(n):
    a, b = 1,1
    print a
    print b
    for i in range(n-2):
        c  = a+b
        a = b
        b = c
        print c

# calculate nth fibonacci number
def fib2(n):
    if n in (0,1):
        return 1
    else:
        return fib2(n-1)+fib2(n-2)
def fib3(n):
    return 1 if n <= 1 else fib3(n-1) + fib3(n-2)


fib(5)
print fib2(4)
print fib3(4)