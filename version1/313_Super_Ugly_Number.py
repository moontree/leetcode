"""
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given prime list primes of size k.
For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence of the first 12
super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k <= 100, 0 < n <= 106, 0 < primes[i] < 1000.
(4) The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
"""


def nth_super_ugly_number(n, primes):
    """
    :type n: int
    :type primes: List[int]
    :rtype: int
    """
    m = len(primes)
    vals = [1 for _ in xrange(m)]
    dp = [1 for _ in xrange(n)]
    idxs = [0 for _ in xrange(m)]
    for i in range(n):
        min_val = min(vals)
        dp[i] = min_val
        for k in xrange(m):
            if vals[k] == min_val:
                vals[k] = dp[idxs[k]] * primes[k]
                idxs[k] += 1
    return dp[-1]


examples = [
    {
        "primes": [2, 7, 13, 19],
        "res": [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32]
    }
]


for example in examples:
    print nth_super_ugly_number(13, example["primes"])
