"""
Description:

Count the number of prime numbers less than a non-negative number, n.
"""


def count_primes(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 3:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
    return sum(primes)


print count_primes(2)
