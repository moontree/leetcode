"""
Given a 2-dimensional grid of integers,
each value in the grid represents the color of the grid square at that location.

Two squares belong to the same connected component if and only if
they have the same color and are next to each other in any of the 4 directions.

The border of a connected component is all the squares in the connected component
that are either 4-directionally adjacent to a square not in the component,
or on the boundary of the grid (the first or last row or column).

Given a square at location (r0, c0) in the grid and a color,
color the border of the connected component of that square with the given color,
and return the final grid.



Example 1:

Input:
    grid = [[1,1],[1,2]],
    r0 = 0, c0 = 0, color = 3
Output:
    [[3, 3], [3, 2]]

Example 2:

Input:
    grid = [[1,2,2],[2,3,2]],
    r0 = 0, c0 = 1, color = 3
Output:
    [[1, 3, 3], [2, 3, 3]]

Example 3:

Input:
    grid = [[1,1,1],[1,1,1],[1,1,1]],
    r0 = 1, c0 = 1, color = 2
Output:
    [[2, 2, 2], [2, 1, 2], [2, 2, 2]]

Note:

    1 <= grid.length <= 50
    1 <= grid[0].length <= 50
    1 <= grid[i][j] <= 1000
    0 <= r0 < grid.length
    0 <= c0 < grid[0].length
    1 <= color <= 1000
"""


class Solution(object):
    def colorBorder(self, grid, r0, c0, color):
        """
        :type grid: List[List[int]]
        :type r0: int
        :type c0: int
        :type color: int
        :rtype: List[List[int]]
        """
        r, c = len(grid), len(grid[0])
        b = grid[r0][c0]
        grid[r0][c0] = -1
        q = [[r0, c0]]
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        edges = []
        while q:
            i, j = q.pop(0)
            nc = 0
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < r and 0 <= nj < c:
                    if grid[ni][nj] == b:
                        grid[ni][nj] = -1
                        nc += 1
                        q.append([ni, nj])
                    elif grid[ni][nj] == -1:
                        nc += 1
            if nc < 4:
                edges.append([i, j])
        for i in range(r):
            for j in range(c):
                if grid[i][j] == -1:
                    grid[i][j] = b
        for i, j in edges:
            grid[i][j] = color

        return grid


examples = [
    {
        "input": {
            "grid": [[1, 1], [1, 2]],
            "r0": 0,
            "c0": 0,
            "color": 3
        },
        "output": [[3, 3], [3, 2]]
    }, {
        "input": {
            "grid": [[1, 2, 2], [2, 3, 2]],
            "r0": 0,
            "c0": 1,
            "color": 3
        },
        "output": [[1, 3, 3], [2, 3, 3]]
    }, {
        "input": {
            "grid": [[1, 1, 1], [1, 1, 1], [1, 1, 1]],
            "r0": 1,
            "c0": 1,
            "color": 2
        },
        "output": [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
    }, {
        "input": {
            "grid": [
                [1, 2, 1, 2, 1, 2],
                [2, 2, 2, 2, 1, 2],
                [1, 2, 2, 2, 1, 2]
            ],
            "r0": 1,
            "c0": 3,
            "color": 1
        },
        "output": [
            [1, 1, 1, 1, 1, 2],
            [1, 2, 1, 1, 1, 2],
            [1, 1, 1, 1, 1, 2]
        ]
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
