def addDigits(num):
    """
    :type num: int
    :rtype: int
    """
    sum_digits = 0
    while num > 9:
        while num > 0:
            r = num % 10
            sum_digits += r
            num = num / 10
        num = sum_digits
        sum_digits = 0

    return num


#print addDigits(38)
print (addDigits(198))
