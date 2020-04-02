"""
Normally, the factorial of a positive integer n is the product of all positive integers less than or equal to n.
For example, factorial(10) = 10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1.

We instead make a clumsy factorial:
using the integers in decreasing order, we swap out the multiply operations for a fixed rotation of operations:
multiply (*), divide (/), add (+) and subtract (-) in this order.

For example, clumsy(10) = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1.
However, these operations are still applied using the usual order of operations of arithmetic:
we do all multiplication and division steps before any addition or subtraction steps,
and multiplication and division steps are processed left to right.

Additionally, the division that we use is floor division such that 10 * 9 / 8 equals 11.
This guarantees the result is an integer.

Implement the clumsy function as defined above: given an integer N, it returns the clumsy factorial of N.



Example 1:

Input:
    4
Output:
    7
Explanation:
    7 = 4 * 3 / 2 + 1

Example 2:

Input:
    10
Output:
    12
Explanation:
    12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1


Note:

    1 <= N <= 10000
    -2^31 <= answer <= 2^31 - 1  (The answer is guaranteed to fit within a 32-bit integer.)
"""


class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        temp = [0, 1, 2, 6, 7]
        if N <= 4:
            return temp[N]
        res = N + 1 + N - 3
        N -= 4
        while N > 0:
            if N > 4:
                res -= 4
                N -= 4
            elif N == 4:
                res -= 5
                break
            else:
                res -= temp[N]
                break
        return res


examples = [
    {
        "input": {
            "N": 4,
        },
        "output": 7
    }, {
        "input": {
            "N": 10,
        },
        "output": 12
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
