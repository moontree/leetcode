"""
In a gold mine grid of size m * n,
each cell in this mine has an integer representing the amount of gold in that cell,
0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

    Every time you are located in a cell you will collect all the gold in that cell.
    From your position you can walk one step to the left, right, up or down.
    You can't visit the same cell more than once.
    Never visit a cell with 0 gold.
    You can start and stop collecting gold from any position in the grid that has some gold.


Example 1:

Input:
    grid = [[0,6,0],[5,8,7],[0,9,0]]
Output:
    24
Explanation:
    [[0,6,0],
     [5,8,7],
     [0,9,0]]
    Path to get the maximum gold, 9 -> 8 -> 7.

Example 2:

Input:
    grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output:
    28
Explanation:
    [[1,0,7],
     [2,0,6],
     [3,4,5],
     [0,3,0],
     [9,0,20]]
Path to get the maximum gold,
    1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.


Constraints:
    1 <= grid.length, grid[i].length <= 15
    0 <= grid[i][j] <= 100
    There are at most 25 cells containing gold.
"""


class Solution(object):
    def getMaximumGold(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r, c = len(grid), len(grid[0])

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def helper(si, sj):
            used = [[0 for _ in range(c)] for _ in range(r)]
            used[si][sj] = 1
            res = [0]

            def dfs(i, j, v, res):
                res[0] = max(res[0], v)
                for di, dj in directions:
                    ni, nj = di + i, dj + j
                    if 0 <= ni < r and 0 <= nj < c and grid[ni][nj] and not used[ni][nj]:
                        used[ni][nj] = 1
                        dfs(ni, nj, v + grid[ni][nj], res)
                        used[ni][nj] = 0
            dfs(si, sj, grid[si][sj], res)
            return res[0]

        res = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    v = helper(i, j)
                    if v > res:
                        res = v

        return res


examples = [
    {
        "input": {
            "grid":[
                [0, 6, 0],
                [5, 8, 7],
                [0, 9, 0]
            ],
        },
        "output": 24
    }, {
        "input": {
            "grid": [
                [1, 0, 7],
                [2, 0, 6],
                [3, 4, 5],
                [0, 3, 0],
                [9, 0, 20]
            ],
        },
        "output": 28
    }, {
        "input": {
            "grid": [
                [1, 0, 7, 0, 0, 0],
                [2, 0, 6, 0, 1, 0],
                [3, 5, 6, 7, 4, 2],
                [4, 3, 1, 0, 2, 0],
                [3, 0, 5, 0, 20, 0]
            ],
        },
        "output": 60
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
