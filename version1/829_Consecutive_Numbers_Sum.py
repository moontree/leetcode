"""
Given a positive integer N,
how many ways can we write it as a sum of consecutive positive integers?

Example 1:

Input:
    5
Output:
    2
Explanation:
    5 = 5 = 2 + 3


Example 2:

Input:
    9
Output:
    3
Explanation:
    9 = 9 = 4 + 5 = 2 + 3 + 4


Example 3:

Input:
    15
Output:
    4
Explanation:
    15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5

Note:
    1 <= N <= 10 ^ 9.
"""
import math


class Solution(object):
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        max_nums = int(math.sqrt(2 * N + 0.25) - 0.5 + 1)
        print max_nums
        res = 0
        for i in range(1, max_nums, 2):
            if N % i == 0:
                res += 1
        for i in range(2, max_nums, 2):
            if N % i == i / 2:
                res += 1
        return res


examples = [
    {
        "input": {
            "N": 5
        },
        "output": 2
    }, {
        "input": {
            "N": 9
        },
        "output": 3
    }, {
        "input": {
            "N": 15
        },
        "output": 4
    }, {
        "input": {
            "N": 22
        },
        "output": 2
    }, {
        "input": {
            "N": 35
        },
        "output": 4
    },
]


if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        v = func(**example['input'])
        print v, v == example['output']