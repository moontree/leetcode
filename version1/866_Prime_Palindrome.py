"""
Find the smallest prime palindrome greater than or equal to N.
Recall that a number is prime if it's only divisors are 1 and itself, and it is greater than 1.
For example, 2,3,5,7,11 and 13 are primes.
Recall that a number is a palindrome if it reads the same from left to right as it does from right to left.
For example, 12321 is a palindrome.

Example 1:
Input:
    6
Output:
    7

Example 2:

Input:
    8
Output:
    11

Example 3:

Input:
    13
Output:
    101


Note:

    1 <= N <= 10^8
    The answer is guaranteed to exist and be less than 2 * 10^8.
"""
import math

class Solution(object):
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        def is_prime(n):
            if n == 2:
                return True
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

        n = len(str(N))
        while True:
            if n == 1:
                for x in [2, 3, 5, 7]:
                    if x >= N:
                        return x
            else:
                p = n / 2
                if n % 2 == 1:
                    for l in range(10 ** (p - 1), 10 ** p):
                        for k in range(10):
                            x = int(str(l) + str(k) + str(l)[::-1])
                            if x >= N and is_prime(x):
                                return x
                else:
                    for l in range(10 ** (p - 1), 10 ** p):
                        x = int(str(l) + str(l)[::-1])
                        if x >= N and is_prime(x):
                            return x
            n += 1


examples = [
    {
        "input": {
            "N": 6
        },
        "output": 7
    }, {
        "input": {
            "N": 8
        },
        "output": 11
    }, {
        "input": {
            "N": 13
        },
        "output": 101
    },
]


import time
if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        start = time.time()
        v = func(**example['input'])
        end = time.time()
        print v, v == example['output'], end - start