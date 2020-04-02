"""
=========================
Project -> File: leetcode -> 1368_Minimum_Cost_to_Make_at_Least_One_Valid_Path_in_a_Grid.py
Author: zhangchao
=========================
Given a m x n grid.
Each cell of the grid has a sign pointing to the next cell you should visit if you are currently in this cell.
The sign of grid[i][j] can be:
    1 which means go to the cell to the right. (i.e go from grid[i][j] to grid[i][j + 1])
    2 which means go to the cell to the left. (i.e go from grid[i][j] to grid[i][j - 1])
    3 which means go to the lower cell. (i.e go from grid[i][j] to grid[i + 1][j])
    4 which means go to the upper cell. (i.e go from grid[i][j] to grid[i - 1][j])
Notice that there could be some invalid signs on the cells of the grid which points outside the grid.

You will initially start at the upper left cell (0,0).
A valid path in the grid is a path which starts from the upper left cell (0,0) and
ends at the bottom-right cell (m - 1, n - 1) following the signs on the grid.
The valid path doesn't have to be the shortest.

You can modify the sign on a cell with cost = 1. You can modify the sign on a cell one time only.

Return the minimum cost to make the grid have at least one valid path.

Example 1:

Input:
    grid = [[1,1,1,1],[2,2,2,2],[1,1,1,1],[2,2,2,2]]
Output:
    3
Explanation:
    You will start at point (0, 0).
    The path to (3, 3) is as follows.
    (0, 0) --> (0, 1) --> (0, 2) --> (0, 3) change the arrow to down with
    cost = 1 --> (1, 3) --> (1, 2) --> (1, 1) --> (1, 0)
    change the arrow to down with cost = 1 --> (2, 0) --> (2, 1) --> (2, 2) --> (2, 3)
    change the arrow to down with cost = 1 --> (3, 3)
    The total cost = 3.

Example 2:
Input:
    grid = [[1,1,3],[3,2,2],[1,1,4]]
Output:
    0
Explanation:
    You can follow the path from (0, 0) to (2, 2).

Example 3:
Input:
    grid = [[1,2],[4,3]]
Output:
    1

Example 4:

Input:
    grid = [[2,2,2],[2,2,2]]
Output:
    3

Example 5:

Input:
    grid = [[4]]
Output:
    0


Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 100
"""


class Solution(object):
    def minCost(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        sign = [(), (0, 1), (0, -1), (1, 0), (-1, 0)]
        q, seen, s = [], set(), []
        i, j = 0, 0
        cost = 0
        while 0 <= i < m and 0 <= j < n and (i, j) not in seen:
            seen.add((i, j))
            q.append((i, j))
            di, dj = sign[grid[i][j]]
            i, j = i + di, j + dj
        while q:
            while q:
                i, j = q.pop(0)
                if (i, j) == (m - 1, n - 1):
                    return cost
                for (i, j) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    while 0 <= i < m and 0 <= j < n and (i, j) not in seen:
                        seen.add((i, j))
                        s.append((i, j))
                        di, dj = sign[grid[i][j]]
                        i, j = i + di, j + dj
            cost += 1
            q, s = s, q


examples = [
    {
        "input": {
            "grid": [
                [1, 1, 1, 1],
                [2, 2, 2, 2],
                [1, 1, 1, 1],
                [2, 2, 2, 2]
            ],
        },
        "output": 3
    }, {
        "input": {
            "grid": [
                [1, 1, 3],
                [3, 2, 2],
                [1, 1, 4]
            ],
        },
        "output": 0
    }, {
        "input": {
            "grid": [
                [1, 2],
                [4, 3]
            ],
        },
        "output": 1
    }, {
        "input": {
            "grid": [
                [2, 2, 2],
                [2, 2, 2]
            ],
        },
        "output": 3
    }, {
        "input": {
            "grid": [
                [4]
            ],
        },
        "output": 0
    }, {
        "input": {
            "grid": [
                [1, 1, 3],
                [4, 2, 2],
                [1, 1, 1]
            ],
        },
        "output": 1
    }, {
        "input": {
            "grid": [
                [2, 3, 1, 2, 2, 2],
                [1, 1, 4, 1, 4, 2],
                [2, 2, 4, 1, 4, 4],
                [1, 2, 2, 2, 3, 4],
                [3, 2, 4, 1, 4, 1],
                [3, 1, 4, 3, 2, 4],
                [4, 3, 1, 3, 1, 3],
                [3, 2, 3, 4, 3, 1],
                [1, 3, 4, 1, 4, 4]]
            ,
        },
        "output": 7
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
