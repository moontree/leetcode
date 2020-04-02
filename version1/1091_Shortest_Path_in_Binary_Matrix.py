"""
In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if
it is composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are different and share an edge or corner)
    C_1 is at location (0, 0) (ie. has value grid[0][0])
    C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
    If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.
If such a path does not exist, return -1.

Example 1:

Input:
    [[0,1],[1,0]]
Output:
    2

Example 2:

Input:
    [[0,0,0],[1,1,0],[1,1,0]]
Output:
    4

Note:

    1 <= grid.length == grid[0].length <= 100
    grid[r][c] is 0 or 1
"""


class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1:
            return -1
        r, c = len(grid), len(grid[0])
        q = [[0, 0]]
        grid[0][0] = 1
        res = 1
        directions = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
        while q:
            tmp = []
            for i, j in q:
                for d in directions:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < r and 0 <= nj < c and grid[ni][nj] == 0:
                        tmp.append([ni, nj])
                        grid[ni][nj] = 1
                        if ni == r - 1 and nj == c - 1:
                            return res + 1
            res += 1
            q = tmp
        return -1


examples = [
    {
        "input": {
            "grid": [
                [0, 1],
                [1, 0]
            ],
        },
        "output": 2
    }, {
        "input": {
            "grid": [
                [0, 0, 0],
                [1, 1, 0],
                [1, 1, 0]
            ],
        },
        "output": 4
    }, {
        "input": {
            "grid": [
                [0]
            ],
        },
        "output": 1
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
