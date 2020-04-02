"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.
If this is impossible, return -1 instead.


Example 1:


Input:
    [[2,1,1],[1,1,0],[0,1,1]]
Output:
    4

Example 2:

Input:
    [[2,1,1],[0,1,1],[1,0,1]]
Output:
    -1
Explanation:
    The orange in the bottom left corner (row 2, column 0) is never rotten,
    because rotting only happens 4-directionally.

Example 3:

Input:
    [[0,2]]
Output:
    0
Explanation:
    Since there are already no fresh oranges at minute 0, the answer is just 0.

Note:

    1 <= grid.length <= 10
    1 <= grid[0].length <= 10
    grid[i][j] is only 0, 1, or 2.
"""


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q = []
        r, c = len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 2:
                    q.append([i, j])

        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        step = -1
        while q:
            tmp = []
            for i, j in q:
                for d in directions:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < r and 0 <= nj < c and grid[ni][nj] == 1:
                        tmp.append([ni, nj])
                        grid[ni][nj] = 2
            # print q, '--', tmp
            q = tmp[:]
            step += 1
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    return -1
        return max(step, 0)


examples = [
    {
        "input": {
            "grid": [
                [2, 1, 1],
                [1, 1, 0],
                [0, 1, 1]
            ],
        },
        "output": 4
    }, {
        "input": {
            "grid": [
                [2, 1, 1],
                [0, 1, 1],
                [1, 0, 1]],
        },
        "output": -1
    }, {
        "input": {
            "grid": [
                [0, 2],
            ],
        },
        "output": 0
    }, {
        "input": {
            "grid": [
                [2, 2],
                [1, 1],
                [0, 0],
                [2, 0]
            ],
        },
        "output": 1
    }, {
        "input": {
            "grid": [
                [0]
            ],
        },
        "output": 0
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
