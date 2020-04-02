"""
On a N * N grid, we place some 1 * 1 * 1 cubes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Return the total surface area of the resulting shapes.


Example 1:

Input:
    [[2]]
Output:
    10

Example 2:

Input:
    [[1,2],[3,4]]
Output:
    34

Example 3:

Input:
    [[1,0],[0,2]]
Output:
    16

Example 4:

Input:
    [[1,1,1],[1,0,1],[1,1,1]]
Output:
    32

Example 5:

Input:
    [[2,2,2],[2,1,2],[2,2,2]]
Output:
    46


Note:
    1 <= N <= 50
    0 <= grid[i][j] <= 50
"""


class Solution(object):
    def surfaceArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        r, c = len(grid), len(grid[0])
        tc = [0 for _ in range(c)]
        for i in range(r):
            ti = 0
            for j in range(c):

                if ti < grid[i][j]:
                    res += 2 * (grid[i][j] - ti)
                ti = grid[i][j]
                if tc[j] < grid[i][j]:
                    res += 2 * (grid[i][j] - tc[j])
                tc[j] = grid[i][j]
                if grid[i][j]:
                    res += 2
        return res


examples = [
    {
        "input": {
            "grid": [[2]],
        },
        "output": 10
    }, {
        "input": {
            "grid": [[1, 2], [3, 4]],
        },
        "output": 34
    }, {
        "input": {
            "grid": [[1, 0], [0, 2]],
        },
        "output": 16
    }, {
        "input": {
            "grid": [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
        },
        "output": 32
    }, {
        "input": {
            "grid": [[2, 2, 2], [2, 1, 2], [2, 2, 2]],
        },
        "output": 46
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
