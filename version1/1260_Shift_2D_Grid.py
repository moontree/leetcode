"""
Given a 2D grid of size m x n and an integer k.
You need to shift the grid k times.

In one shift operation:

    Element at grid[i][j] becomes at grid[i][j + 1].
    Element at grid[i][n - 1] becomes at grid[i + 1][0].
    Element at grid[n - 1][n - 1] becomes at grid[0][0].
    Return the 2D grid after applying shift operation k times.

Example 1:

Input:
    grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output:
    [[9,1,2],[3,4,5],[6,7,8]]

Example 2:

Input:
    grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
Output:
    [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

Example 3:

Input:
    grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output:
    [[1,2,3],[4,5,6],[7,8,9]]


Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m <= 50
    1 <= n <= 50
    -1000 <= grid[i][j] <= 1000
    0 <= k <= 100
"""


class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        r, c = len(grid), len(grid[0])
        grids = []
        for row in grid:
            grids += row
        k = k % (r * c)
        grids = grids[-k:] + grids[: -k]
        res = []
        for i in range(0, r * c, c):
            res.append(grids[i: i + c])
        return res


examples = [
    {
        "input": {
            "grid": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            "k": 1
        },
        "output": [[9, 1, 2], [3, 4, 5], [6, 7, 8]]
    }, {
        "input": {
            "grid": [
                [3, 8, 1, 9],
                [19, 7, 2, 5],
                [4, 6, 11, 10],
                [12, 0, 21, 13]
            ],
            "k": 4
        },
        "output": [
            [12, 0, 21, 13],
            [3, 8, 1, 9],
            [19, 7, 2, 5],
            [4, 6, 11, 10]
        ]
    }, {
        "input": {
            "grid": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            "k": 9
        },
        "output": [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
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
