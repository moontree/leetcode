"""
You have a pointer at index 0 in an array of size arrLen.
At each step,
you can move 1 position to the left,
1 position to the right in the array
or stay in the same place
(The pointer should not be placed outside the array at any time).

Given two integers steps and arrLen,
return the number of ways such that your pointer still at index 0 after exactly steps steps.

Since the answer may be too large,
return it modulo 10^9 + 7.


Example 1:

Input:
    steps = 3, arrLen = 2
Output:
    4
Explanation:
    There are 4 differents ways to stay at index 0 after 3 steps.
    Right, Left, Stay
    Stay, Right, Left
    Right, Stay, Left
    Stay, Stay, Stay

Example 2:

Input:
    steps = 2, arrLen = 4
Output:
    2
Explanation:
    There are 2 differents ways to stay at index 0 after 2 steps
    Right, Left
    Stay, Stay

Example 3:

Input:
    steps = 4, arrLen = 2
Output:
    8


Constraints:

    1 <= steps <= 500
    1 <= arrLen <= 10^6
"""


class Solution(object):
    def numWays(self, steps, arrLen):
        """
        :type steps: int
        :type arrLen: int
        :rtype: int
        """
        mod = 10 ** 9 + 7
        jMax = min(steps, arrLen)
        dp = [[0] * jMax for i in range(steps + 1)]
        dp[0][0] = 1
        for i in range(1, steps + 1):
            dp[i][0] = (dp[i - 1][0] + dp[i - 1][1]) % mod
            for j in range(1, len(dp[i]) - 1):
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][j + 1]) % mod
            dp[i][-1] = (dp[i - 1][-2] + dp[i - 1][-1]) % mod
        return dp[steps][0]


examples = [
    {
        "input": {
            "steps": 3,
            "arrLen": 2
        },
        "output": 4
    }, {
        "input": {
            "steps": 2,
            "arrLen": 4
        },
        "output": 2
    }, {
        "input": {
            "steps": 4,
            "arrLen": 2
        },
        "output": 8
    }, {
        "input": {
            "steps": 430,
            "arrLen": 148488
        },
        "output": 525833932
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
