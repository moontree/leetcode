"""
Given a 2D grid of 0s and 1s,
return the number of elements in the largest square subgrid that has all 1s on its border,
or 0 if such a subgrid doesn't exist in the grid.



Example 1:

Input:
    grid = [[1,1,1],[1,0,1],[1,1,1]]
Output:
    9

Example 2:

Input:
    grid = [[1,1,0,0]]
Output:
    1


Constraints:

    1 <= grid.length <= 100
    1 <= grid[0].length <= 100
    grid[i][j] is 0 or 1
"""


class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r, c = len(grid), len(grid[0])
        ones = [[[0, 0] for _ in range(c + 1)] for _ in range(r + 1)]  # continuious ones on [left, up]
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    ones[i][j][0] = ones[i][j - 1][0] + 1
                    ones[i][j][1] = ones[i - 1][j][1] + 1
                else:
                    ones[i][j][0] = 0
                    ones[i][j][1] = 0
        l = 0
        for i in range(r):
            for j in range(c):
                for ll in range(l, min(ones[i][j]) + 1)[::-1]:
                    if ones[i - ll + 1][j][0] >= ll and ones[i][j - ll + 1][1] >= ll > l:
                        l = ll

        return l * l


examples = [
    {
        "input": {
            "grid": [
                [1, 1, 1],
                [1, 0, 1],
                [1, 1, 1]
            ],
        },
        "output": 9
    }, {
        "input": {
            "grid": [
                [1, 1, 0, 0],
            ],
        },
        "output": 1
    }, {
        "input": {
            "grid":  [
                [0, 1, 1, 1, 1, 0],
                [1, 1, 0, 1, 1, 0],
                [1, 1, 0, 1, 0, 1],
                [1, 1, 0, 1, 1, 1],
                [1, 1, 0, 1, 1, 1],
                [1, 1, 1, 1, 1, 1],
                [1, 0, 1, 1, 1, 1],
                [0, 0, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1]
            ],
        },
        "output": 16
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
