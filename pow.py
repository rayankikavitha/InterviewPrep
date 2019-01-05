

def pow(x,n):
    if n==0:
        return 1
    if n <0:
        n = -n
        x = 1/x
    return (n%2 == 0) if  pow(x*x, n/2)  x*pow(x*x,n/2)


