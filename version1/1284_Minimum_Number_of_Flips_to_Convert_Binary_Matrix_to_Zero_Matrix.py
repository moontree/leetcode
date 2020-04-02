"""
Given a m x n binary matrix mat.
In one step, you can choose one cell and flip it and all the four neighbours
of it if they exist (Flip is changing 1 to 0 and 0 to 1).
A pair of cells are called neighboors if they share one edge.

Return the minimum number of steps required to convert mat to a zero matrix or -1 if you cannot.

Binary matrix is a matrix with all cells equal to 0 or 1 only.

Zero matrix is a matrix with all cells equal to 0.



Example 1:


Input:
    mat = [[0,0],[0,1]]
Output:
    3
Explanation:
    One possible solution is to flip (1, 0) then (0, 1) and finally (1, 1) as shown.

Example 2:

Input:
    mat = [[0]]
Output:
    0
Explanation:
    Given matrix is a zero matrix. We don't need to change it.

Example 3:

Input:
    mat = [[1,1,1],[1,0,1],[0,0,0]]
Output:
    6

Example 4:

Input:
    mat = [[1,0,0],[1,0,0]]
Output:
    -1
Explanation:
    Given matrix can't be a zero matrix


Constraints:

    m == mat.length
    n == mat[0].length
    1 <= m <= 3
    1 <= n <= 3
    mat[i][j] is 0 or 1.
"""
import copy


class Solution(object):
    def minFlips(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        r, c = len(mat), len(mat[0])
        directions = [[-1, 0], [1, 0], [0, 0], [0, 1], [0, -1]]
        res = r * c + 1
        for i in range(2 ** (r * c)):
            s = bin(i)[2:][::-1]
            tmp = copy.deepcopy(mat)
            n = 0
            for j, v in enumerate(s):
                rr, cc = divmod(j, c)
                if v == '1':
                    n += 1
                    for d in directions:
                        nr, nc = d[0] + rr, d[1] + cc
                        if 0 <= nr < r and 0 <= nc < c:
                            tmp[nr][nc] = 1 - tmp[nr][nc]
            if sum([sum(row) for row in tmp]) == 0:
                res = min(res, n)
        if res == r * c + 1:
            return -1
        return res


examples = [
    {
        "input": {
            "mat": [[0, 0], [0, 1]],
        },
        "output": 3
    }, {
        "input": {
            "mat": [[0]],
        },
        "output": 0
    }, {
        "input": {
            "mat": [
                [1, 1, 1],
                [1, 0, 1],
                [0, 0, 0]
            ],
        },
        "output": 6
    }, {
        "input": {
            "mat": [
                [1, 0, 0],
                [1, 0, 0]
            ],
        },
        "output": -1
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
