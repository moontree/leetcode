"""
Given an N x N grid containing only values 0 and 1,
where 0 represents water and 1 represents land,
find a water cell such that its distance to the nearest land cell is maximized and return the distance.

The distance used in this problem is the Manhattan distance:
the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.

If no land or water exists in the grid, return -1.



Example 1:



Input:
    [[1,0,1],[0,0,0],[1,0,1]]
Output:
    2
Explanation:
    The cell (1, 1) is as far as possible from all the land with distance 2.

Example 2:

Input:
    [[1,0,0],[0,0,0],[0,0,0]]
Output:
    4
Explanation:
    The cell (2, 2) is as far as possible from all the land with distance 4.


Note:

    1 <= grid.length == grid[0].length <= 100
    grid[i][j] is 0 or 1
"""
import bisect


class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r, c = len(grid), len(grid[0])
        q = []
        res = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    q.append([i, j])

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while q:
            tmp = []
            for i, j in q:
                for d in directions:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < r and 0 <= nj < c and grid[ni][nj] == 0:
                        tmp.append([ni, nj])
                        grid[ni][nj] = 1
            q = tmp
            if q:
                res += 1

        return res if res else -1


examples = [
    {
        "input": {
            "grid": [
                [1, 0, 1],
                [0, 0, 0],
                [1, 0, 1]
            ],
        },
        "output": 2
    }, {
        "input": {
            "grid": [
                [1, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ],
        },
        "output": 4
    }, {
        "input": {
            "grid": [
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]
            ],
        },
        "output": -1
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
