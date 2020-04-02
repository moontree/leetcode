"""
=========================
Project -> File: leetcode -> 1001_Grid_Illumination.py
Author: zhangchao
=========================
On a N x N grid of cells,
each cell (x, y) with 0 <= x < N and 0 <= y < N has a lamp.

Initially, some number of lamps are on.
lamps[i] tells us the location of the i-th lamp that is on.
Each lamp that is on illuminates every square on its x-axis, y-axis, and both diagonals (similar to a Queen in chess).

For the i-th query queries[i] = (x, y),
the answer to the query is 1 if the cell (x, y) is illuminated, else 0.

After each query (x, y) [in the order given by queries],
we turn off any lamps that are at cell (x, y) or are adjacent 8-directionally
(ie., share a corner or edge with cell (x, y).)

Return an array of answers.
Each value answer[i] should be equal to the answer of the i-th query queries[i].



Example 1:

Input:
    N = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
Output:
    [1,0]
Explanation:
    Before performing the first query we have both lamps [0,0] and [4,4] on.
    The grid representing which cells are lit looks like this,
    where [0,0] is the top left corner, and [4,4] is the bottom right corner:
    1 1 1 1 1
    1 1 0 0 1
    1 0 1 0 1
    1 0 0 1 1
    1 1 1 1 1
    Then the query at [1, 1] returns 1 because the cell is lit.
    After this query, the lamp at [0, 0] turns off, and the grid now looks like this:
    1 0 0 0 1
    0 1 0 0 1
    0 0 1 0 1
    0 0 0 1 1
    1 1 1 1 1
    Before performing the second query we have only the lamp [4,4] on.
    Now the query at [1,0] returns 0, because the cell is no longer lit.


Note:

    1 <= N <= 10^9
    0 <= lamps.length <= 20000
    0 <= queries.length <= 20000
    lamps[i].length == queries[i].length == 2
"""


class Solution(object):
    def gridIllumination(self, N, lamps, queries):
        """
        :type N: int
        :type lamps: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        cache = [{} for _ in range(4)]
        lights = {}
        for x, y in lamps:
            cache[0][x] = cache[0].get(x, 0) + 1
            cache[1][y] = cache[1].get(y, 0) + 1
            cache[2][x + y] = cache[2].get(x + y, 0) + 1
            cache[3][x - y] = cache[3].get(x - y, 0) + 1
            lights[(x, y)] = 1
        res = []
        for x, y in queries:
            if cache[0].get(x, 0) > 0 or cache[1].get(y, 0) > 0 or cache[2].get(x + y, 0) > 0 or cache[3].get(x - y, 0) > 0:
                res.append(1)
            else:
                res.append(0)
            for i in range(-1, 2):
                for j in range(-1, 2):
                    nx, ny = x + i, y + j
                    if (nx, ny) in lights:
                        if nx in cache[0]:
                            cache[0][nx] -= 1
                        if ny in cache[1]:
                            cache[1][ny] -= 1
                        if nx + ny in cache[2]:
                            cache[2][nx + ny] -= 1
                        if nx - ny in cache[3]:
                            cache[3][nx - ny] -= 1
                        del lights[(nx, ny)]
        return res



examples = [
    {
        "input": {
            "N": 5,
            "lamps": [[0, 0], [4, 4]],
            "queries": [[1, 1], [1, 0]]
        },
        "output": [1, 0]
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
