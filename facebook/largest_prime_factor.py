"""
The prime factors of 13195 are 5, 7, 13 and 29.
The largest is 29
"""

def primeFactors(n):
    # array to hold all prime numbers
    result =[]
    # Print the number of two's that divide n
    while n % 2 == 0:
        result.append(2),
        n = n / 2

    # n must be odd at this point
    # so a skip of 2 ( i = i + 2) can be used
    #for i in range(3, int(math.sqrt(n)) + 1, 2):
    for i in range(3, int(n**0.5) + 1, 2):
        # while i divides n , print i ad divide n
        while n % i == 0:
            result.append(i)
            n = n / i
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        result.append(n)
    return max(result)

print primeFactors(13195)
print primeFactors(100)

