"""
Find the sum of numbers that are divisible by 3 and 5 in 1000. So for sumup(10) = 23
sumup (10) = 3+5+6+9 = 23
"""
def sumup(num):
    tot = 0
    for i in range(num):
        if i%3 == 0 or i%5 == 0 :
            tot = tot + i

    return tot

def sumup_15(num):
    tot = 0
    for i in xrange(num):
        if i%15 == 0:
            tot = tot+i
    return tot

print sumup(10)
print sumup(1000)

def sumpup_actual_technique(num):
    """
    https://www.quora.com/What-is-the-sum-of-all-the-multiples-of-3-or-5-below-1000
    :param num:
    :return:
    """
    three = num
    while three%3 == 0:
        three -=1
    five = num
    while five%5 == 0:
        five -= 1
    if num >= 15:
        fifteen = num
        while fifteen%15 == 0:
            fifteen -= 1
        nfifteen = fifteen/15
        sumpup_15 = ((nfifteen * (nfifteen + 1)) / 2) * 15
    else:
        sumpup_15 = 0

    n_three = three/3
    n_five = five/5

    sumup_3 = ((n_three * (n_three +1))/2 ) * 3
    sumup_5 = ((n_five * (n_five + 1)) / 2) * 5

    sumup_3_5 = sumup_3 + sumup_5 - sumpup_15

    return sumup_3_5

print sumpup_actual_technique(10)
print sumpup_actual_technique(20)
print sumpup_actual_technique(1000)
print sumup_15(1000)






