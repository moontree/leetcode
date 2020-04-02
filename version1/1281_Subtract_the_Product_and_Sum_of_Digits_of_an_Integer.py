"""
Given an integer number n,
return the difference between the product of its digits and the sum of its digits.


Example 1:

Input:
    n = 234
Output:
    15
Explanation:
    Product of digits = 2 * 3 * 4 = 24
    Sum of digits = 2 + 3 + 4 = 9
    Result = 24 - 9 = 15


Example 2:

Input:
    n = 4421
Output:
    21
Explanation:
    Product of digits = 4 * 4 * 2 * 1 = 32
    Sum of digits = 4 + 4 + 2 + 1 = 11
    Result = 32 - 11 = 21

Constraints:

    1 <= n <= 10^5
"""


class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        a, b = 0, 1
        while n:
            a += n % 10
            b *= n % 10
            n /= 10

        return b - a


examples = [
    {
        "input": {
            "n": 234,
        },
        "output": 15
    }, {
        "input": {
            "n": 4421,
        },
        "output": 21
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
