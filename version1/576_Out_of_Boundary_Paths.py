"""
There is an m by n grid with a ball.
Given the start coordinate (i,j) of the ball,
you can move the ball to adjacent cell or cross the grid boundary in four directions (up, down, left, right).
However, you can at most move N times.
Find out the number of paths to move the ball out of grid boundary.
The answer may be very large, return it after mod 10**9 + 7.



Example 1:

Input:
    m = 2, n = 2, N = 2, i = 0, j = 0
Output:
    6

Example 2:

Input:
    m = 1, n = 3, N = 3, i = 0, j = 1
Output:
    12

Note:
    Once you move the ball out of boundary, you cannot move it back.
    The length and height of the grid is in range [1,50].
    N is in range [0,50].
"""


class Solution(object):
    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        base = 10 ** 9 + 7
        # dp[i][j][k]: get i, j by k steps
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[i][j] = 1
        res = 0
        if N == 0:
            return 0
        if i == 0:
            res += 1
        if i == m - 1:
            res += 1
        if j == 0:
            res += 1
        if j == n - 1:
            res += 1
        for _ in range(N - 1):
            tmp = [[0 for _ in range(n)] for _ in range(m)]
            for r in range(m):
                for c in range(n):
                    ll = dp[r][c - 1] if c > 0 else 0
                    rr = dp[r][c + 1] if c < n - 1 else 0
                    uu = dp[r - 1][c] if r > 0 else 0
                    dd = dp[r + 1][c] if r < m - 1 else 0
                    tmp[r][c] = ll + rr + uu + dd
                    if c == 0:
                        res += tmp[r][c]
                    if c == n - 1:
                        res += tmp[r][c]
            res += sum(tmp[0]) + sum(tmp[-1])
            dp = tmp
        return res % base


examples = [
    {
        "input": {
            "m": 2,
            "n": 2,
            "N": 2,
            "i": 0,
            "j": 0
        },
        "output": 6
    }, {
        "input": {
            "m": 1,
            "n": 3,
            "N": 3,
            "i": 0,
            "j": 1
        },
        "output": 12
    }, {
        "input": {
            "m": 1,
            "n": 1,
            "N": 0,
            "i": 0,
            "j": 0
        },
        "output": 0
    }, {
        "input": {
            "m": 2,
            "n": 1,
            "N": 2,
            "i": 0,
            "j": 0
        },
        "output": 6
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
