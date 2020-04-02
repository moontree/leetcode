"""
=========================
Project -> File: leetcode -> 741_Cherry_Pickup.py
Author: zhangchao
=========================
In a N x N grid representing a field of cherries, each cell is one of three possible integers.

0 means the cell is empty, so you can pass through;
1 means the cell contains a cherry, that you can pick up and pass through;
-1 means the cell contains a thorn that blocks your way.

Your task is to collect maximum number of cherries possible by following the rules below:


Starting at the position (0, 0) and reaching (N-1, N-1)
by moving right or down through valid path cells (cells with value 0 or 1);
After reaching (N-1, N-1), returning to (0, 0) by moving left or up through valid path cells;
When passing through a path cell containing a cherry, you pick it up and the cell becomes an empty cell (0);
If there is no valid path between (0, 0) and (N-1, N-1), then no cherries can be collected.

Example 1:

Input:
    grid =
    [[0, 1, -1],
     [1, 0, -1],
     [1, 1,  1]]
Output:
    5
Explanation:
    The player started at (0, 0) and went down, down, right right to reach (2, 2).
    4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
    Then, the player went left, up, up, left to return home, picking up one more cherry.
    The total number of cherries picked up is 5, and this is the maximum possible.


Note:

    grid is an N by N 2D array, with 1 <= N <= 50.
    Each grid[i][j] is an integer in the set {-1, 0, 1}.
    It is guaranteed that grid[0][0] and grid[N-1][N-1] are not -1.
"""


class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        dp = [[[None for _ in range(n)] for _ in range(n)] for _ in range(n)]

        def helper(r1, c1, c2):
            r2 = r1 + c1 - c2
            if c1 == n or c2 == n or r1 == n or r2 == n or grid[r1][c1] == -1 or grid[r2][c2] == -1:
                return -10000
            if dp[r1][c1][c2] is not None:
                return dp[r1][c1][c2]
            elif r1 == c1 == n - 1:
                return grid[-1][-1]
            else:
                dp[r1][c1][c2] = max(
                    helper(r1 + 1, c1, c2),
                    helper(r1 + 1, c1, c2 + 1),
                    helper(r1, c1 + 1, c2),
                    helper(r1, c1 + 1, c2 + 1),
                ) + grid[r1][c1] + (grid[r2][c2] if r1 != r2 else 0)
            return dp[r1][c1][c2]
        v = helper(0, 0, 0)
        return max(0, v)


examples = [
    {
        "input": {
            "grid": [
                [0, 1, -1],
                [1, 0, -1],
                [1, 1, 1]
            ],
        },
        "output": 5
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
