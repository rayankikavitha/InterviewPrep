"""
Given a number n, you have to find the next smallest palindromic number, larger than it
input = 5, output = 6
input = 10, output = 11
input = 101, output = 111
input = 55, output = 56
input = 99, output = 101

https://www.geeksforgeeks.org/given-a-number-find-next-smallest-palindrome-larger-than-this-number/
here can be three different types of inputs that need to be handled separately
1) The input number is Palindrome and has all 9s. input = , output = 1001
2) input number is not palindrome  input = 1234, output = 1331
3) input number is palindrome and doesn't have all 9s or same numerics input = 1221, output = 1331

input = 1234, output = 1331
"""
#for type 2,3
def next_palindrome_number_for_type23(input):
    nums=nums=list([int(i) for i in input])
    n = len(nums)
    mid = n/2
    #end of left side is always mid-1
    i = mid-1
    #beginning of right side depends if n is odd or even
    j = mid if n%2 == 0 else mid+1
    # a bool variable to check if copy of left side to right is sufficient or not
    leftsmaller = False
    # Initally, ignore the middle same digits
    while i>=0 and nums[i] == nums[j]:
        i -= 1
        j += 1
    # find if the middle digits need need to be incremented or not
    # or (copying left side is not sufficient)
    if i < 0 or nums[i] < nums[j]:
        leftsmaller = True
    #copy the mirror of left to right
    while i>=0:
        nums[j] = nums[i]
        j +=1
        i -=1
    # Handle the case where middle digits must be incremented.
    # case 1 and 2.2
    if leftsmaller:
        carry = 1
        #if there are odd digits, then increment the middle digit and store the carry
        if n%2==1:
            nums[mid] +=1
            carry = nums[mid]/10
            nums[mid] = nums[mid]%10
        i = mid -1
        j = mid if n%2==0 else mid+1
        # Add 1 to the rightmost digit of the left side, propagate the carry towards MSB digit
        # and simulataneously copying mirror of the left side to the right side.
        while i >=0:
            nums[i] = nums[i]+carry
            carry = nums[i]/10
            nums[i] = nums[i]%10
            nums[j] = nums[i] #copy mirror to the right
            i -=1
            j += 1
    return nums

def isall9(input):
    cnt = 0
    for each in input:
        if each == 9:
            cnt +=1
    if cnt == len(input):
        return True
    else:
        return False


def next_palindrome_number(input):
    #input type 1 : Al digits are 9
    # simply output 1 followed by n-1 0s followed by 1
    nums=list([int(i) for i in input])
    newnums=[]
    if isall9(nums):
        newnums.append(1)
        for i in range(len(nums)-1):
            newnums.append(0)
        newnums.append(1)
    #input type 2 and 3
    else:
        newnums = next_palindrome_number_for_type23(input)
    return newnums



print next_palindrome_number("99")
print next_palindrome_number("12921")
print next_palindrome_number("125322") # case 2.1
print next_palindrome_number("713322") # case 2.2












