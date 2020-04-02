"""
Given a 2D grid consists of 0s (land) and 1s (water).
An island is a maximal 4-directionally connected group of 0s and
a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.


Example 1:


Input:
    grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output:
    2
Explanation:
    Islands in gray are closed because they are completely surrounded by water (group of 1s).

Example 2:

Input:
    grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output:
    1

Example 3:

Input:
    grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output:
    2


Constraints:

    1 <= grid.length, grid[0].length <= 100
    0 <= grid[i][j] <=1
"""


class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r, c = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def helper(i, j, flag):
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < r and 0 <= nj < c and grid[ni][nj] == 0:
                    grid[ni][nj] = flag
                    helper(ni, nj, flag)

        color = 2
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    grid[i][j] = color
                    helper(i, j, color)
                    color += 1

        edge = {}
        for i in range(r):
            if grid[i][0] > 1:
                edge[grid[i][0]] = 1
            if grid[i][-1] > 1:
                edge[grid[i][-1]] = 1
        for j in range(c):
            if grid[0][j] > 1:
                edge[grid[0][j]] = 1
            if grid[-1][j] > 1:
                edge[grid[-1][j]] = 1
        return color - len(edge) - 2


examples = [
    {
        "input": {
            "grid": [
                [1, 1, 1, 1, 1, 1, 1, 0],
                [1, 0, 0, 0, 0, 1, 1, 0],
                [1, 0, 1, 0, 1, 1, 1, 0],
                [1, 0, 0, 0, 0, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 0]
            ],
        },
        "output": 2
    }, {
        "input": {
            "grid": [
                [0, 0, 1, 0, 0],
                [0, 1, 0, 1, 0],
                [0, 1, 1, 1, 0]
            ],
        },
        "output": 1
    }, {
        "input": {
            "grid": [
                [1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 0, 1, 1, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1]
            ],
        },
        "output": 2
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
