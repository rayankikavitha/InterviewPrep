def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def detect_primes(a):
    s = ''
    for each in a:
        if is_prime(each):
            s += '1'
        else:
            s += '0'
    return s