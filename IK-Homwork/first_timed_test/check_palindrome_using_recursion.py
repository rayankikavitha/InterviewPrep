"""
Check if a string is palindrome using recursion

"""

def is_pal(input):
    """
    When you do string slicing, it creates internal variables. so iterate the string
    :param input:
    :return:
    """
    for i in xrange(len(input)):
       if input[i] != input[len(input)-1]:
           return False
       else:
           return is_pal( input[i+1: len(input)-1])
    return True

def is_pal2(input):
    """
    When you do string slicing, it creates internal variables. so iterate the string
    :param input:
    :return:
    """
    if input[0] != input[-1]:
        return False
    else:
        is_pal(input[1:-2])

print is_pal("madam")
print is_pal("maadam")