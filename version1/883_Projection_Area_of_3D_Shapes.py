"""
On a N * N grid, we place some 1 * 1 * 1 cubes that are axis-aligned with the x, y, and z axes.

Each value v = grid[i][j] represents a tower of v cubes placed on top of grid cell (i, j).

Now we view the projection of these cubes onto the xy, yz, and zx planes.

A projection is like a shadow, that maps our 3 dimensional figure to a 2 dimensional plane.

Here, we are viewing the "shadow" when looking at the cubes from the top, the front, and the side.

Return the total area of all three projections.



Example 1:

Input:
    [[2]]
Output:
    5

Example 2:

Input:
    [[1,2],[3,4]]
Output:
    17
Explanation:
    Here are the three projections ("shadows") of the shape made with each axis-aligned plane.

Example 3:

Input:
    [[1,0],[0,2]]
Output:
    8

Example 4:

Input:
    [[1,1,1],[1,0,1],[1,1,1]]
Output:
    14

Example 5:

Input:
    [[2,2,2],[2,1,2],[2,2,2]]
Output:
    21


Note:
    1 <= grid.length = grid[0].length <= 50
    0 <= grid[i][j] <= 50
"""


class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0
        r, c = len(grid), len(grid[0])
        rv, cv = [0 for _ in range(r)], [0 for _ in range(c)]
        for i in range(r):
            for j in range(c):
                if grid[i][j]:
                    res += 1
                    rv[i] = max(rv[i], grid[i][j])
                    cv[j] = max(cv[j], grid[i][j])
        res += sum(rv) + sum(cv)
        return res


examples = [
    {
        "input": {
            "grid": [[2]],
        },
        "output": 5
    }, {
        "input": {
            "grid": [[1, 2], [3, 4]],
        },
        "output": 17
    }, {
        "input": {
            "grid": [[1, 0], [0, 2]],
        },
        "output": 8
    }, {
        "input": {
            "grid": [[1, 1, 1], [1, 0, 1], [1, 1, 1]],
        },
        "output": 14
    }, {
        "input": {
            "grid": [[2, 2, 2], [2, 1, 2], [2, 2, 2]],
        },
        "output": 21
    }
]


if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        v = func(**example['input'])
        print v, v == example['output']