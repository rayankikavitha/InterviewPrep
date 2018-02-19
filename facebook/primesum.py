"""
Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.

NOTE A solution will always exist. read Goldbachs conjecture

Example:

Input : 4
Output: 2 + 2 = 4


"""

class Solution:
    def primesum(self, n):
        for i in xrange(2, n):
            if self.is_prime(i) and self.is_prime(n - i):
                return i, n - i

    def is_prime(self, n):
        if n < 2:
            return False

        for i in xrange(2, int(n**0.5) + 1):
            print i
            if n % i == 0:
                return False

        return True

s = Solution()
print s.is_prime( 23)
print s.primesum(13)