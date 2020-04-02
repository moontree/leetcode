"""
Return the number of permutations of 1 to n so that prime numbers are at prime indices (1-indexed.)

(Recall that an integer is prime if and only if it is greater than 1,
and cannot be written as a product of two positive integers both smaller than it.)

Since the answer may be large, return the answer modulo 10^9 + 7.



Example 1:

Input:
    n = 5
Output:
    12
Explanation:
    For example [1,2,5,4,3] is a valid permutation,
    but [5,2,3,4,1] is not because the prime number 5 is at index 1.

Example 2:

Input:
    n = 100
Output:
    682289015


Constraints:

    1 <= n <= 100
"""


class Solution(object):
    def numPrimeArrangements(self, n):
        """
        :type n: int
        :rtype: int
        """
        base = 10 ** 9 + 7
        primes = {2: 1, 3: 1, 5: 1, 7: 1, 11: 1, 13: 1, 17: 1, 19: 1, 23: 1, 29: 1, 31: 1, 37: 1, 41: 1, 43: 1, 47: 1, 53: 1, 59: 1, 61: 1, 67: 1, 71: 1, 73: 1, 79: 1, 83: 1, 89: 1, 97: 1}
        pc, rc = 0, 0
        res = 1
        for i in range(n):
            if i + 1 in primes:
                pc += 1
                res = res * pc % base
            else:
                rc += 1
                res = res * rc % base
        return res


examples = [
    {
        "input": {
            "n": 5,
        },
        "output": 12
    }, {
        "input": {
            "n": 100,
        },
        "output": 682289015
    }
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
