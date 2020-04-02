"""
Given a m * n grid,
where each cell is either 0 (empty) or 1 (obstacle).
In one step, you can move up, down, left or right from and to an empty cell.

Return the minimum number of steps to walk from the upper left corner (0, 0)
to the lower right corner (m-1, n-1) given
that you can eliminate at most k obstacles.

If it is not possible to find such walk return -1.


Example 1:

Input:
    grid =
    [
        [0,0,0],
        [1,1,0],
        [0,0,0],
        [0,1,1],
        [0,0,0]
    ],
    k = 1
Output:
    6
Explanation:
    The shortest path without eliminating any obstacle is 10.
    The shortest path with one obstacle elimination at position (3,2) is 6.
    Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).


Example 2:

Input:
    grid =
    [
        [0,1,1],
        [1,1,1],
        [1,0,0]
    ],
    k = 1
Output:
    -1
Explanation:
    We need to eliminate at least two obstacles to find such a walk.


Constraints:

    grid.length == m
    grid[0].length == n
    1 <= m, n <= 40
    1 <= k <= m*n
    grid[i][j] == 0 or 1
    grid[0][0] == grid[m-1][n-1] == 0
"""


class Solution(object):
    def shortestPath(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        r, c = len(grid), len(grid[0])
        cache = {}
        tx, ty = r - 1, c - 1
        q = [[0, 0, k]]
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        step = 0
        while q:
            tmp = []
            for x, y, kk in q:
                if x == tx and y == ty:
                    return step
                for d in directions:
                    nx, ny = x + d[0], y + d[1]
                    if 0 <= nx < r and 0 <= ny < c:
                        if grid[nx][ny] == 0 and (nx, ny, kk) not in cache:
                            tmp.append([nx, ny, kk])
                            cache[(nx, ny, kk)] = 1
                        elif grid[nx][ny] == 1 and kk > 0 and (nx, ny, kk - 1) not in cache:
                            tmp.append([nx, ny, kk - 1])
                            cache[(nx, ny, kk - 1)] = 1
            q = tmp
            step += 1
        return -1


examples = [
    {
        "input": {
            "grid": [
                [0, 0, 0],
                [1, 1, 0],
                [0, 0, 0],
                [0, 1, 1],
                [0, 0, 0]
            ],
            "k": 1
        },
        "output": 6
    }, {
        "input": {
            "grid": [
                [0, 1, 1],
                [1, 1, 1],
                [1, 0, 0]
            ],
            "k": 1
        },
        "output": -1
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
