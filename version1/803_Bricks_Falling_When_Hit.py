"""
We have a grid of 1s and 0s;
the 1s in a cell represent bricks.
A brick will not drop if and only if it is directly connected to the top of the grid,
or at least one of its (4-way) adjacent bricks will not drop.

We will do some erasures sequentially.
Each time we want to do the erasure at the location (i, j),
the brick (if it exists) on that location will disappear,
and then some other bricks may drop because of that erasure.

Return an array representing the number of bricks that will drop after each erasure in sequence.

Example 1:
Input:
    grid = [[1,0,0,0],[1,1,1,0]]
    hits = [[1,0]]
Output:
    [2]
Explanation:
    If we erase the brick at (1, 0), the brick at (1, 1) and (1, 2) will drop. So we should return 2.

Example 2:
Input:
    grid = [[1,0,0,0],[1,1,0,0]]
    hits = [[1,1],[1,0]]
Output:
    [0,0]
Explanation:
    When we erase the brick at (1, 0), the brick at (1, 1) has already disappeared due to the last move.
    So each erasure will cause no bricks dropping.
    Note that the erased brick (1, 0) will not be counted as a dropped brick.


Note:

    The number of rows and columns in the grid will be in the range [1, 200].
    The number of erasures will not exceed the area of the grid.
    It is guaranteed that each erasure will be different from any other erasure, and located inside the grid.
    An erasure may refer to a location with no brick - if it does, no bricks drop.
"""

class DSU:

    def __init__(self, n):
        self.cache = {i: i for i in xrange(n)}
        self.sz = {i: 1 for i in xrange(n)}
        self.n = n - 1

    def find(self, x):
        if self.cache[x] != x:
            self.cache[x] = self.find(self.cache[x])
        return self.cache[x]

    def union(self, x, y):
        a, b = self.find(x), self.find(y)
        if a == b:
            return
        if a < b:
            a, b = b, a

        self.cache[a] = b
        self.sz[b] += self.sz[a]

    def top(self):
        return self.sz[self.find(self.n)] - 1


class Solution(object):
    def hitBricks(self, grid, hits):
        """
        :type grid: List[List[int]]
        :type hits: List[List[int]]
        :rtype: List[int]
        """
        res = []
        r, c = len(grid), len(grid[0])
        memory = [v[:] for v in grid]
        n = r * c
        for i, j in hits:
            memory[i][j] = 0

        dsu = DSU(n + 1)
        for j in range(c):
            if memory[0][j]:
                dsu.union(j, n)

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for i in range(1, r):
            for j in range(c):
                if memory[i][j] == 1:
                    for d in directions:
                        ni, nj = i + d[0], j + d[1]
                        if 0 <= ni < r and 0 <= nj < c and memory[ni][nj]:
                            print i, j, ni, nj
                            dsu.union(i * c + j, ni * c + nj)

        for i, j in hits[::-1]:
            if grid[i][j] == 0:
                res.append(0)
            else:
                od = dsu.top()
                for d in directions:
                    ni, nj = i + d[0], j + d[1]
                    if 0 <= ni < r and 0 <= nj < c and memory[ni][nj]:
                        dsu.union(i * c + j, ni * c + nj)
                if i == 0:
                    dsu.union(j, n)
                res.append(max(dsu.top() - 1 - od, 0))
                memory[i][j] = 1
        return res[::-1]


examples = [
    {
        "input": {
            "grid": [[1, 0, 0, 0], [1, 1, 1, 0]],
            "hits": [[1, 0]]
        },
        "output": [2]
    },  {
        "input": {
            "grid": [[1, 0, 0, 0], [1, 1, 0, 0]],
            "hits": [[1, 1], [1, 0]]
        },
        "output": [0, 0]
    },  {
        "input": {
            "grid": [[1], [1], [1], [1], [1]],
            "hits": [[3, 0], [4, 0], [1, 0], [2, 0], [0, 0]]
        },
        "output": [1, 0, 1, 0, 0]
    },  {
        "input": {
            "grid": [[1, 0, 1], [1, 1, 1]],
            "hits": [[0, 0], [0, 2], [1, 1]]
        },
        "output": [0, 3, 0]
    },  {
        "input": {
            "grid":  [[1, 1, 1], [0, 1, 0], [0, 0, 0]],
            "hits": [[0, 2], [2, 0], [0, 1], [1, 2]],
        },
        "output": [0, 0, 1, 0]
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
