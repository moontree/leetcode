"""
=========================
Project -> File: leetcode -> 749_Contain_Virus.py
Author: zhangchao
=========================
A virus is spreading rapidly,
and your task is to quarantine the infected area by installing walls.

The world is modeled as a 2-D array of cells,
where 0 represents uninfected cells,
and 1 represents cells contaminated with the virus.
A wall (and only one wall) can be installed between any two 4-directionally adjacent cells, on the shared boundary.

Every night, the virus spreads to all neighboring cells in all four directions unless blocked by a wall.
Resources are limited.
Each day, you can install walls around only one region --
the affected area (continuous block of infected cells) that threatens the most uninfected cells the following night.
There will never be a tie.

Can you save the day?
If so, what is the number of walls required?
If not, and the world becomes fully infected, return the number of walls used.

Example 1:
Input:
grid =
    [[0,1,0,0,0,0,0,1],
     [0,1,0,0,0,0,0,1],
     [0,0,0,0,0,0,0,1],
     [0,0,0,0,0,0,0,0]]
Output:
    10
Explanation:
    There are 2 contaminated regions.
    On the first day, add 5 walls to quarantine the viral region on the left.
    The board after the virus spreads is:

    [[0,1,0,0,0,0,1,1],
     [0,1,0,0,0,0,1,1],
     [0,0,0,0,0,0,1,1],
     [0,0,0,0,0,0,0,1]]

    On the second day, add 5 walls to quarantine the viral region on the right. The virus is fully contained.

Example 2:
Input:
grid =
    [[1,1,1],
     [1,0,1],
     [1,1,1]]
Output:
    4
Explanation:
    Even though there is only one cell saved, there are 4 walls built.
    Notice that walls are only built on the shared boundary of two different cells.

Example 3:
Input:
grid =
    [[1,1,1,0,0,0,0,0,0],
     [1,0,1,0,1,1,1,1,1],
     [1,1,1,0,0,0,0,0,0]]
Output:
    13
Explanation:
    The region on the left only builds two new walls.

Note:
    The number of rows and columns of grid will each be in the range [1, 50].
    Each grid[i][j] will be either 0 or 1.
    Throughout the described process,
    there is always a contiguous viral region that will infect strictly more uncontaminated squares in the next round.
"""


class Solution(object):
    def containVirus(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r, c = len(grid), len(grid[0])

        # get blocks, set edges
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        res = 0

        used = {}
        edges = {}
        blocks = {}
        old = {}

        def dfs(i, j, k):
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < r and 0 <= nj < c and (ni, nj) not in used and (ni, nj) not in old:
                    if grid[ni][nj] == 1:
                        blocks[k].append([ni, nj])
                        used[(ni, nj)] = 1
                        dfs(ni, nj, k)
                    else:
                        if k in edges:
                            edges[k].append((ni, nj))
                        else:
                            edges[k] = [(ni, nj)]

        while True:
            k = 0
            used = {}
            edges = {}
            blocks = {}
            for i in range(r):
                for j in range(c):
                    if grid[i][j] and (i, j) not in used and (i, j) not in old:
                        k += 1
                        used[(i, j)] = 1
                        blocks[k] = [[i, j]]
                        dfs(i, j, k)

            kk, vv = -1, -1
            for k, v in edges.items():
                tmp_l = len(set(v))
                if tmp_l > vv:
                    kk, vv = k, tmp_l
            if kk == -1 or not edges:
                break
            res += len(edges[kk])

            for i, j in blocks[kk]:
                old[(i, j)] = 1
            for k in edges:
                if k != kk:
                    for ii, jj in edges[k]:
                        grid[ii][jj] = 1

        return res


examples = [
    {
        "input": {
            "grid": [
                [0, 1, 0, 0, 0, 0, 0, 1],
                [0, 1, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0]
            ],
        },
        "output": 10
    }, {
        "input": {
            "grid": [
                [1, 1, 1],
                [1, 0, 1],
                [1, 1, 1]
            ],
        },
        "output": 4
    }, {
        "input": {
            "grid": [
                [1, 1, 1, 0, 0, 0, 0, 0, 0],
                [1, 0, 1, 0, 1, 1, 1, 1, 1],
                [1, 1, 1, 0, 0, 0, 0, 0, 0]
            ],
        },
        "output": 13
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
