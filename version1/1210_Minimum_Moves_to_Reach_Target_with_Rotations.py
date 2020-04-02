"""
In an n*n grid,
there is a snake that spans 2 cells and starts moving from the top left corner at (0, 0) and (0, 1).
The grid has empty cells represented by zeros and blocked cells represented by ones.
The snake wants to reach the lower right corner at (n-1, n-2) and (n-1, n-1).

In one move the snake can:

Move one cell to the right if there are no blocked cells there.
This move keeps the horizontal/vertical position of the snake as it is.
Move down one cell if there are no blocked cells there.
This move keeps the horizontal/vertical position of the snake as it is.

Rotate clockwise if it's in a horizontal position and the two cells under it are both empty.
In that case the snake moves from (r, c) and (r, c+1) to (r, c) and (r+1, c).

Rotate counterclockwise if it's in a vertical position and the two cells to its right are both empty.
In that case the snake moves from (r, c) and (r+1, c) to (r, c) and (r, c+1).

Return the minimum number of moves to reach the target.

If there is no way to reach the target, return -1.

Example 1:

Input:
grid = [
    [0,0,0,0,0,1],
    [1,1,0,0,1,0],
    [0,0,0,0,1,1],
    [0,0,1,0,1,0],
    [0,1,1,0,0,0],
    [0,1,1,0,0,0]
    ]
Output:
    11
Explanation:
    One possible solution is
    [right, right, rotate clockwise, right, down, down, down, down, rotate counterclockwise, right, down].

Example 2:

Input:
grid = [
    [0,0,1,1,1,1],
    [0,0,0,0,1,1],
    [1,1,0,0,0,1],
    [1,1,1,0,0,1],
    [1,1,1,0,0,1],
    [1,1,1,0,0,0]
    ]
Output:
    9

Constraints:

    2 <= n <= 100
    0 <= grid[i][j] <= 1
    It is guaranteed that the snake starts at empty cells.
"""


class Solution(object):
    def minimumMoves(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        r, c = len(grid), len(grid[0])
        if grid[-1][-2] or grid[-1][-1] == 1:
            return -1
        cache = {}

        start = (0, 1, 0, 0, 'h') # head, tail
        cache[start] = True
        q = [start]
        step = 0
        while q:
            near = []
            for hx, hy, tx, ty, flag in q:
                if hx == r - 1 and hy == c - 1 and tx == r - 1 and ty == r - 2:
                    return step
                if flag == 'h':
                    if hy + 1 < c and grid[hx][hy + 1] == 0:
                        new_position = (hx, hy + 1, tx, ty + 1, 'h')
                        if new_position not in cache:
                            cache[new_position] = True
                            near.append(new_position)
                    if hx + 1 < r and grid[hx + 1][ty] == 0 and grid[hx + 1][hy] == 0:
                        new_position = (hx + 1, ty, tx, ty, 'v')
                        if new_position not in cache:
                            cache[new_position] = True
                            near.append(new_position)
                        new_position = (hx + 1, hy, tx + 1, ty, 'h')
                        if new_position not in cache:
                            cache[new_position] = True
                            near.append(new_position)
                else:
                    if ty + 1 < c and grid[tx][ty + 1] == 0 and grid[hx][hy + 1] == 0:
                        new_position = (tx, ty + 1, tx, ty, 'h')
                        if new_position not in cache:
                            cache[new_position] = True
                            near.append(new_position)
                        new_position = (hx, hy + 1, tx, ty + 1, 'v')
                        if new_position not in cache:
                            cache[new_position] = True
                            near.append(new_position)
                    if hx + 1 < r and grid[hx + 1][hy] == 0:
                        new_position = (hx + 1, hy, tx + 1, ty, 'v')
                        if new_position not in cache:
                            cache[new_position] = True
                            near.append(new_position)

            q = near[:]
            step += 1
        return -1



examples = [
    {
        "input": {
            "grid": [
                [0, 0, 0, 0, 0, 1],
                [1, 1, 0, 0, 1, 0],
                [0, 0, 0, 0, 1, 1],
                [0, 0, 1, 0, 1, 0],
                [0, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 0, 0]
            ],
        },
        "output": 11
    }, {
        "input": {
            "grid":[
                [0, 0, 1, 1, 1, 1],
                [0, 0, 0, 0, 1, 1],
                [1, 1, 0, 0, 0, 1],
                [1, 1, 1, 0, 0, 1],
                [1, 1, 1, 0, 0, 1],
                [1, 1, 1, 0, 0, 0]
            ],
        },
        "output": 9
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
