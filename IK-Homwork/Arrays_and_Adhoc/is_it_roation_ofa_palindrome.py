
"""
optimal solution, concate the is_rotate string and check the original string in it

"""
def is_it_rotation(str1, str2):
	newstr= str1+str2
	if newstr.find(str1) == -1 :
		return False
	else:
		return True


"""
aab
return = True
as aba is palindrome

option 1:
  use pointers to pass it to is_palindrome operation.
option2:
 check if its even or odd and start and start from the middle point

Possible slow downs


"""

def is_Pali(s):
    return s == s[::-1]

def check_if_rotated(s):
    for i in range(len(s)):
        news = s[i:]+ s[:i]
        if is_Pali(news):
            return 1
    return 0