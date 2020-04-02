"""
=========================
Project -> File: leetcode -> 1391_Check_if_There_is_a_Valid_Path_in_a_Grid.py
Author: zhangchao
=========================
Given a m x n grid. Each cell of the grid represents a street. The street of grid[i][j] can be:
1 which means a street connecting the left cell and the right cell.
2 which means a street connecting the upper cell and the lower cell.
3 which means a street connecting the left cell and the lower cell.
4 which means a street connecting the right cell and the lower cell.
5 which means a street connecting the left cell and the upper cell.
6 which means a street connecting the right cell and the upper cell.
You will initially start at the street of the upper-left cell (0,0).
A valid path in the grid is a path which starts from the upper left cell (0,0)
and ends at the bottom-right cell (m - 1, n - 1).
The path should only follow the streets.

Notice that you are not allowed to change any street.

Return true if there is a valid path in the grid or false otherwise.

Example 1:

Input:
    grid = [[2,4,3],[6,5,2]]
Output:
    true
Explanation:
    As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).

Example 2:

Input:
    grid = [[1,2,1],[1,2,1]]
Output:
    false
Explanation:
    As shown you the street at cell (0, 0) is not connected with any street
    of any other cell and you will get stuck at cell (0, 0)

Example 3:

Input:
    grid = [[1,1,2]]
Output:
    false
Explanation:
    You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).

Example 4:

Input:
    grid = [[1,1,1,1,1,1,3]]
Output:
    true

Example 5:

Input:
    grid = [[2],[2],[2],[2],[2],[2],[6]]
Output:
    true


Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 300
    1 <= grid[i][j] <= 6

"""


class Solution(object):
    def hasValidPath(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        r, c = len(grid), len(grid[0])
        directions = [
            [],
            [[0, 1, [1, 3, 5]], [0, -1, [1, 4, 6]]],
            [[1, 0, [2, 5, 6]], [-1, 0, [2, 3, 4]]],
            [[0, -1, [1, 4, 6]], [1, 0, [2, 5, 6]]],
            [[0, 1, [1, 3, 5]], [1, 0, [2, 5, 6]]],
            [[0, -1, [1, 4, 6]], [-1, 0, [2, 3, 4]]],
            [[0, 1, [1, 3, 5]], [-1, 0, [2, 4, 6]]],
        ]
        reached = {(0, 0): 1}
        q = [[0, 0, grid[0][0]]]
        while q:
            tmp = []
            for cx, cy, d in q:
                if cx == r - 1 and cy == c - 1:
                    return True
                for dx, dy, ds in directions[d]:
                    nx, ny = cx + dx, cy + dy
                    if 0 <= nx < r and 0 <= ny < c and (nx, ny) not in reached:
                        if grid[nx][ny] in ds:
                            reached[(nx, ny)] = 1
                            tmp.append([nx, ny, grid[nx][ny]])
            q = tmp
        return False


examples = [
    {
        "input": {
            "grid": [[2, 4, 3], [6, 5, 2]],
        },
        "output": True
    }, {
        "input": {
            "grid": [[1, 2, 1], [1, 2, 1]],
        },
        "output": False
    }, {
        "input": {
            "grid": [[1, 1, 2]],
        },
        "output": False
    }, {
        "input": {
            "grid": [[1, 1, 1, 1, 1, 1, 3]],
        },
        "output": True
    }, {
        "input": {
            "grid": [[2], [2], [2], [2], [2], [2], [6]],
        },
        "output": True
    }, {
        "input": {
            "grid": [[4, 1], [6, 1]],
        },
        "output": True
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
