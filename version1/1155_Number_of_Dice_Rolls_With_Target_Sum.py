"""
You have d dice,
and each die has f faces numbered 1, 2, ..., f.

Return the number of possible ways (out of fd total ways)
modulo 10^9 + 7 to roll the dice so the sum of the face up numbers equals target.



Example 1:

Input:
    d = 1, f = 6, target = 3
Output:
    1
Explanation:
    You throw one die with 6 faces.  There is only one way to get a sum of 3.

Example 2:

Input:
    d = 2, f = 6, target = 7
Output:
    6
Explanation:
    You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
    1+6, 2+5, 3+4, 4+3, 5+2, 6+1.

Example 3:

Input:
    d = 2, f = 5, target = 10
Output:
    1
Explanation:
    You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.

Example 4:

Input:
    d = 1, f = 2, target = 3
Output:
    0
Explanation:
    You throw one die with 2 faces.  There is no way to get a sum of 3.

Example 5:

Input:
    d = 30, f = 30, target = 500
Output:
    222616187
Explanation:
    The answer must be returned modulo 10^9 + 7.

Constraints:

    1 <= d, f <= 30
    1 <= target <= 1000
"""


class Solution(object):
    def numRollsToTarget(self, d, f, target):
        """
        :type d: int
        :type f: int
        :type target: int
        :rtype: int
        """
        base = 10 ** 9 + 7
        if d * f < target:
            return 0
        if target == d:
            return 1
        if target < d:
            return 0

        dp = [[0 for _ in range(target + 1)] for _ in range(d + 1)]
        dp[0][0] = 1
        for dd in range(1, d + 1):
            for t in range(dd, min(target, d * f) + 1):
                dp[dd][t] = sum(dp[dd - 1][max(0, t - f): t]) % base
        return dp[-1][-1]


examples = [
    {
        "input": {
            "d": 1,
            "f": 6,
            "target": 3
        },
        "output": 1
    }, {
        "input": {
            "d": 2,
            "f": 6,
            "target": 7
        },
        "output": 6
    }, {
        "input": {
            "d": 2,
            "f": 5,
            "target": 10
        },
        "output": 1
    }, {
        "input": {
            "d": 1,
            "f": 2,
            "target": 3
        },
        "output": 0
    # }
    }, {
        "input": {
            "d": 30,
            "f": 30,
            "target": 500
        },
        "output": 222616187
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
