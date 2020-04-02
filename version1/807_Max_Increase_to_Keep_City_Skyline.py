"""
In a 2 dimensional array grid,
each value grid[i][j] represents the height of a building located there.
We are allowed to increase the height of any number of buildings,
by any amount (the amounts can be different for different buildings).
Height 0 is considered to be a building as well.

At the end, the "skyline" when viewed from all four directions of the grid,
i.e. top, bottom, left, and right,
must be the same as the skyline of the original grid.
A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance.
See the following example.

What is the maximum total sum that the height of the buildings can be increased?

Example:
Input:
    grid = [
    [3,0,8,4],
    [2,4,5,7],
    [9,2,6,3],
    [0,3,1,0]
    ]
Output:
    35
Explanation:
    The grid is:
    [ [3, 0, 8, 4],
      [2, 4, 5, 7],
      [9, 2, 6, 3],
      [0, 3, 1, 0] ]

    The skyline viewed from top or bottom is: [9, 4, 8, 7]
    The skyline viewed from left or right is: [8, 7, 9, 3]

The grid after increasing the height of buildings without affecting skylines is:

gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]

Notes:

    1 < grid.length = grid[0].length <= 50.
    All heights grid[i][j] are in the range [0, 100].
    All buildings in grid[i][j] occupy the entire grid cell:
    that is, they are a 1 x 1 x grid[i][j] rectangular prism.
"""


class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r, c = len(grid), len(grid[0])
        mr, mc = [0 for _ in range(r)], [0 for _ in range(c)]
        for i in range(r):
            for j in range(c):
                mr[i] = max(mr[i], grid[i][j])
                mc[j] = max(mc[j], grid[i][j])

        res = sum([min(mr[i], mc[j]) - grid[i][j] for j in range(c) for i in range(r)])
        return res


examples = [
    {
        "input": {
            "grid": [
                [3, 0, 8, 4],
                [2, 4, 5, 7],
                [9, 2, 6, 3],
                [0, 3, 1, 0]
            ],
        },
        "output": 35
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
        print func(**example['input']) == example['output']