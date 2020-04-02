"""
=========================
Project -> File: leetcode -> 778_Swim_in_Rising_Water.py
Author: zhangchao
=========================
On an N x N grid, each square grid[i][j] represents the elevation at that point (i,j).

Now rain starts to fall. At time t, the depth of the water everywhere is t.
You can swim from a square to another 4-directionally adjacent square
if and only if the elevation of both squares individually are at most t.
You can swim infinite distance in zero time.
Of course, you must stay within the boundaries of the grid during your swim.

You start at the top left square (0, 0).
What is the least time until you can reach the bottom right square (N-1, N-1)?

Example 1:

Input:
    [[0,2],[1,3]]
Output:
    3
Explanation:
    At time 0, you are in grid location (0, 0).
    You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
    You cannot reach point (1, 1) until time 3.
    When the depth of water is 3, we can swim anywhere inside the grid.

Example 2:

Input:
    [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
Output:
    16
Explanation:
     0  1  2  3  4
    24 23 22 21  5
    12 13 14 15 16
    11 17 18 19 20
    10  9  8  7  6

    The final route is marked in bold.
    We need to wait until time 16 so that (0, 0) and (4, 4) are connected.
Note:

    2 <= N <= 50.
    grid[i][j] is a permutation of [0, ..., N*N - 1].
"""
import heapq


class Solution(object):
    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        used = {}
        q = [[grid[0][0], 0, 0]]
        ans = 0
        while q:
            d, i, j = heapq.heappop(q)
            ans = max(ans, d)
            if i == j == n - 1:
                return ans
            for ni, nj in [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]:
                if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in used:
                    heapq.heappush(q, [grid[ni][nj], ni, nj])
                    used[(ni, nj)] = 1


examples = [
    {
        "input": {
            "grid": [
                [0, 2],
                [1, 3]
            ],
        },
        "output": 3
    }, {
        "input": {
            "grid": [
                [0, 1, 2, 3, 4],
                [24, 23, 22, 21, 5],
                [12, 13, 14, 15, 16],
                [11, 17, 18, 19, 20],
                [10, 9, 8, 7, 6]
            ],
        },
        "output": 16
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
