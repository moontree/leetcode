"""
Given a 2D array A, each cell is 0 (representing sea) or 1 (representing land)

A move consists of walking from one land square 4-directionally to another land square,
or off the boundary of the grid.

Return the number of land squares in the grid for which
we cannot walk off the boundary of the grid in any number of moves.



Example 1:

Input:
    [
        [0,0,0,0],
        [1,0,1,0],
        [0,1,1,0],
        [0,0,0,0]
    ]
Output:
    3
Explanation:
    There are three 1s that are enclosed by 0s, and one 1 that isn't enclosed because its on the boundary.

Example 2:

Input:
    [
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,0],
        [0,0,0,0]
    ]
Output:
    0
Explanation:
    All 1s are either on the boundary or can reach the boundary.

Note:

    1 <= A.length <= 500
    1 <= A[i].length <= 500
    0 <= A[i][j] <= 1
    All rows have the same size.
"""


class Solution(object):
    def numEnclaves(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        q = []
        r, c = len(A), len(A[0])
        for j in range(c):
            if A[0][j] == 1:
                q.append([0, j])
                A[0][j] = -1
        for j in range(c):
            if A[-1][j] == 1:
                q.append([r - 1, j])
                A[-1][j] = -1
        for i in range(1, r - 1):
            if A[i][0] == 1:
                q.append([i, 0])
                A[i][0] = -1
        for i in range(1, r - 1):
            if A[i][-1] == 1:
                q.append([i, c - 1])
                A[i][-1] = -1
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        while q:
            i, j = q.pop(0)
            for d in directions:
                ni, nj = i + d[0], j + d[1]
                if 0 <= ni < r and 0 <= nj < c and A[ni][nj] == 1:
                    q.append([ni, nj])
                    A[ni][nj] = -1
        res = 0
        for i in range(1, r - 1):
            for j in range(1, c - 1):
                if A[i][j] == 1:
                    res += 1
        return res


examples = [
    {
        "input": {
            "A": [
                [0, 0, 0, 0],
                [1, 0, 1, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 0]
            ],
        },
        "output": 3
    }, {
        "input": {
            "A": [
                [0, 1, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 0]
            ],
        },
        "output": 0
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
