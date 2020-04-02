"""
On a 2 dimensional grid with R rows and C columns,
we start at (r0, c0) facing east.

Here, the north-west corner of the grid is at the first row and column,
and the south-east corner of the grid is at the last row and column.

Now, we walk in a clockwise spiral shape to visit every position in this grid.

Whenever we would move outside the boundary of the grid,
we continue our walk outside the grid (but may return to the grid boundary later.)

Eventually, we reach all R * C spaces of the grid.

Return a list of coordinates representing the positions of the grid in the order they were visited.



Example 1:

Input:
    R = 1, C = 4, r0 = 0, c0 = 0
Output:
    [[0,0],[0,1],[0,2],[0,3]]




Example 2:

Input: R = 5, C = 6, r0 = 1, c0 = 4
Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]

        col_0  col_1
row_0
row_1

Note:

1 <= R <= 100
1 <= C <= 100
0 <= r0 < R
0 <= c0 < C

"""


class Solution(object):
    def spiralMatrixIII(self, R, C, r0, c0):
        """
        :type R: int
        :type C: int
        :type r0: int
        :type c0: int
        :rtype: List[List[int]]
        """
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        count = R * C - 1
        d = 0
        step = 0
        x, y = r0, c0
        di = 0
        res = [[r0, c0]]
        while count:
            if step % 2 == 0:
                d += 1
            for k in range(d):
                x, y = x + directions[di][0], y + directions[di][1]
                if 0 <= x < R and 0 <= y < C:
                    count -= 1
                    res.append([x, y])
            step += 1
            di = (di + 1) % 4
        return res


examples = [
    {
        "input": {
            "R": 1,
            "C": 4,
            "r0": 0,
            "c0": 0
        },
        "output": [[0, 0], [0, 1], [0, 2], [0, 3]]
    }, {
        "input": {
            "R": 5,
            "C": 6,
            "r0": 1,
            "c0": 4
        },
        "output": [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
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