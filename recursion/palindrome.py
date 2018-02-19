"""



"""

def atoi(input):
    """
    convert  a string into an integer
    :param input:
    :return:
    """
    res = 0
    i = 0
    sign = 1
    if input[0] == '-':
        sign = -1
        i = 1
    for j in range(i,len(input)):
        res = res*10 + (ord(input[j]) - ord('0'))
        #print res
    return sign*res

print atoi('123')
print atoi('-123')


def palindrome(input):
    """
    check if a string in palindrome recursively
    :param input:
    :return:
    """
    if len(input) in (1,2):
        return True
    elif input[0] == input[-1]:
        return palindrome(input[1:len(input)-1])
    else:
        return False

print palindrome('madam')
print palindrome('madama')

