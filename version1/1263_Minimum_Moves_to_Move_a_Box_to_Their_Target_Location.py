"""
Storekeeper is a game in which the player pushes boxes around in a warehouse
trying to get them to target locations.

The game is represented by a grid of size m x n,
where each element is a wall, floor, or a box.

Your task is move the box 'B' to the target position 'T' under the following rules:

    Player is represented by character 'S' and can move up, down, left, right in the grid if it is a floor (empy cell).
    Floor is represented by character '.' that means free cell to walk.
    Wall is represented by character '#' that means obstacle  (impossible to walk there).
    There is only one box 'B' and one target cell 'T' in the grid.

The box can be moved to an adjacent free cell by standing next to the box and then moving in the direction of the box.
This is a push.
The player cannot walk through the box.
Return the minimum number of pushes to move the box to the target. If there is no way to reach the target, return -1.



Example 1:

Input:
    grid = [
        ["#","#","#","#","#","#"],
        ["#","T","#","#","#","#"],
        ["#",".",".","B",".","#"],
        ["#",".","#","#",".","#"],
        ["#",".",".",".","S","#"],
        ["#","#","#","#","#","#"]
    ]
Output:
    3
Explanation:
    We return only the number of times the box is pushed.

Example 2:

Input:
    grid = [
        ["#","#","#","#","#","#"],
        ["#","T","#","#","#","#"],
        ["#",".",".","B",".","#"],
        ["#","#","#","#",".","#"],
        ["#",".",".",".","S","#"],
        ["#","#","#","#","#","#"]
    ]
Output:
    -1

Example 3:

Input:
    grid = [
        ["#","#","#","#","#","#"],
        ["#","T",".",".","#","#"],
        ["#",".","#","B",".","#"],
        ["#",".",".",".",".","#"],
        ["#",".",".",".","S","#"],
        ["#","#","#","#","#","#"]
    ]
Output:
    5
Explanation:
    push the box down, left, left, up and up.

Example 4:

Input:
    grid = [
        ["#","#","#","#","#","#","#"],
        ["#","S","#",".","B","T","#"],
        ["#","#","#","#","#","#","#"]
    ]
Output:
    -1


Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m <= 20
    1 <= n <= 20
    grid contains only characters '.', '#',  'S' , 'T', or 'B'.
    There is only one character 'S', 'B' and 'T' in the grid.
"""


class Solution(object):
    def minPushBox(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        start, target, box = None, None, None
        r, c = len(grid), len(grid[0])
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 'T':
                    target = [i, j]
                if grid[i][j] == 'S':
                    start = [i, j]
                if grid[i][j] == 'B':
                    box = [i, j]

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def reachable(sx, sy, tx, ty, bx, by):
            cache = {(sx, sy): 1}
            qq = [[sx, sy]]
            while qq:
                tmp = []
                for x, y in qq:
                    if x == tx and y == ty:
                        return True
                    for d in directions:
                        nx, ny = x + d[0], y + d[1]
                        if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] != '#' \
                                and (nx != bx or ny != by) and (nx, ny) not in cache:
                            tmp.append([nx, ny])
                            cache[(nx, ny)] = 1
                qq = tmp
            return False
        reached = {}
        q, step = [[box, start]], 0
        while q:
            tmp = []
            for (cur_box, cur_people) in q:
                bx, by = cur_box
                sx, sy = cur_people
                if bx == target[0] and by == target[1]:
                    return step
                for d in directions:
                    nbx, nby = bx + d[0], by + d[1]
                    tx, ty = bx - d[0], by - d[1]
                    if 0 <= nbx < r and 0 <= nby < c and \
                        0 <= tx < r and 0 <= ty < c and \
                        (nbx, nby, d[0], d[1]) not in reached and grid[nbx][nby] != '#' and reachable(sx, sy, tx, ty, bx, by):
                        tmp.append([[nbx, nby], [tx, ty]])
                        reached[(nbx, nby, d[0], d[1])] = 1
            q = tmp
            step += 1
            # print step, q
        return -1


examples = [
    {
        "input": {
            "grid": [
                ["#", "#", "#", "#", "#", "#"],
                ["#", "T", "#", "#", "#", "#"],
                ["#", ".", ".", "B", ".", "#"],
                ["#", ".", "#", "#", ".", "#"],
                ["#", ".", ".", ".", "S", "#"],
                ["#", "#", "#", "#", "#", "#"]
            ],
        },
        "output": 3
    }, {
        "input": {
            "grid": [
                ["#", "#", "#", "#", "#", "#"],
                ["#", "T", "#", "#", "#", "#"],
                ["#", ".", ".", "B", ".", "#"],
                ["#", "#", "#", "#", ".", "#"],
                ["#", ".", ".", ".", "S", "#"],
                ["#", "#", "#", "#", "#", "#"]
            ],
        },
        "output": -1
    }, {
        "input": {
            "grid": [
                ["#", "#", "#", "#", "#", "#"],
                ["#", "T", ".", ".", "#", "#"],
                ["#", ".", "#", "B", ".", "#"],
                ["#", ".", ".", ".", ".", "#"],
                ["#", ".", ".", ".", "S", "#"],
                ["#", "#", "#", "#", "#", "#"]
            ],
        },
        "output": 5
    }, {
        "input": {
            "grid": [
                ["#", "#", "#", "#", "#", "#", "#"],
                ["#", "S", "#", ".", "B", "T", "#"],
                ["#", "#", "#", "#", "#", "#", "#"]
            ],
        },
        "output": -1
    }, {
        "input": {
            "grid": [
                ["#", ".", ".", "#", "#", "#", "#", "#"],
                ["#", ".", ".", "T", "#", ".", ".", "#"],
                ["#", ".", ".", ".", "#", "B", ".", "#"],
                ["#", ".", ".", ".", "#", ".", "S", "#"],
                ["#", ".", ".", "#", "#", "#", "#", "#"]
            ],
        },
        "output": 7
    }, {
        "input": {
            "grid": [
                ["#", ".", ".", "#", "T", "#", "#", "#", "#"],
                ["#", ".", ".", "#", ".", "#", ".", ".", "#"],
                ["#", ".", ".", "#", ".", "#", "B", ".", "#"],
                ["#", ".", ".", ".", ".", ".", ".", ".", "#"],
                ["#", ".", ".", ".", ".", "#", ".", "S", "#"],
                ["#", ".", ".", "#", ".", "#", "#", "#", "#"]
            ],
        },
        "output": 8
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
