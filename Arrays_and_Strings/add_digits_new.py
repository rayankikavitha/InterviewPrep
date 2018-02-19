n=1234
#output = 1
def find_digits_sum(num):
    sum_digits = 0
    while num >9:
        while num > 0:
            r = num%10
            sum_digits += r
            num = num/10
        num = sum_digits
        sum_digits = 0
    print "sum of the digits ="
    print num

m=8191979
s =791982
sar=5291982
find_digits_sum(1234)
find_digits_sum(m)
find_digits_sum(s)
find_digits_sum(sar)

