"""
=========================
Project -> File: leetcode -> 1362_Closest_Divisors.py
Author: zhangchao
=========================
Given an integer num,
find the closest two integers in absolute difference whose product equals num + 1 or num + 2.

Return the two integers in any order.


Example 1:

Input:
    num = 8
Output:
    [3,3]
Explanation:
    For num + 1 = 9, the closest divisors are 3 & 3,
    for num + 2 = 10, the closest divisors are 2 & 5, hence 3 & 3 is chosen.

Example 2:

Input:
    num = 123
Output:
    [5,25]

Example 3:

Input:
    num = 999
Output:
    [40,25]


Constraints:

    1 <= num <= 10^9
"""


class Solution(object):
    def closestDivisors(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        v = int((num + 2) ** 0.5)
        for l in range(v, 0, -1):
            if (num + 1) % l == 0:
                return [l, (num + 1) / l]
            if (num + 2) % l == 0:
                return [l, (num + 2) / l]


examples = [
    {
        "input": {
            "num": 8,
        },
        "output": [3, 3]
    }, {
        "input": {
            "num": 123,
        },
        "output": [5, 25]
    }, {
        "input": {
            "num": 999,
        },
        "output": [25, 40]
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
