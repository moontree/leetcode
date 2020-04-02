"""
On a 2-dimensional grid,
there are 4 types of squares:

    1 represents the starting square.  There is exactly one starting square.
    2 represents the ending square.  There is exactly one ending square.
    0 represents empty squares we can walk over.
    -1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square,
that walk over every non-obstacle square exactly once.



Example 1:

Input:
    [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output:
    2
Explanation: We have the following two paths:
    1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
    2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Example 2:

Input:
    [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation:
    We have the following four paths:
    1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
    2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
    3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
    4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

Example 3:

Input:
    [[0,1],[2,0]]
Output:
    0
Explanation:
    There is no path that walks over every empty square exactly once.
    Note that the starting and ending square can be anywhere in the grid.


Note:

    1 <= grid.length * grid[0].length <= 20
"""


class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r, c = len(grid), len(grid[0])
        target_steps = 1
        si, sj = None, None
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    target_steps += 1
                elif grid[i][j] == 1:
                    si, sj = i, j
        # print target_steps, si, sj

        self.res = 0

        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        def valid(i, j):
            return 0 <= i < r and 0 <=j < c

        def helper(i, j, cache, step):
            if cache[(i, j)] == 2:
                if step == target_steps:
                    self.res += 1
                else:
                    return
            elif cache[(i, j)] == 0 or cache[(i, j)] == 1:
                v = cache[(i, j)]
                cache[(i, j)] = -1
                for d in directions:
                    ni, nj = i + d[0], j + d[1]
                    if valid(ni, nj) and cache[(ni, nj)] >= 0:
                        helper(ni, nj, cache, step + 1)
                cache[(i, j)] = v

        cache = {
            (i, j): grid[i][j] for i in range(r) for j in range(c)
        }
        helper(si, sj, cache, 0)
        return self.res


examples = [
    {
        "input": {
            "grid": [
                [1, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 2, -1]
            ],
        },
        "output": 2
    }, {
        "input": {
            "grid": [
                [1, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 2]
            ]
        },
        "output": 4
    }, {
        "input": {
            "grid": [
                [0, 1],
                [2, 0]
            ],
        },
        "output": 0
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
