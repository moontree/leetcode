"""
Given a m x n matrix mat and an integer threshold.
Return the maximum side-length of a square with a sum less
than or equal to threshold or return 0 if there is no such square.



Example 1:


Input:
    mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
Output:
    2
Explanation:
    The maximum side length of square with sum less than 4 is 2 as shown.

Example 2:

Input:
    mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
Output:
    0

Example 3:

Input:
    mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6
Output:
    3

Example 4:

Input:
    mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], threshold = 40184
Output:
    2

Constraints:

    1 <= m, n <= 300
    m == mat.length
    n == mat[i].length
    0 <= mat[i][j] <= 10000
    0 <= threshold <= 10^5
"""


class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        r, c = len(mat), len(mat[0])
        row_sums = [[0 for _ in range(c)] for _ in range(r + 1)]
        for i in range(r):
            for j in range(c):
                row_sums[i][j] = row_sums[i - 1][j] + mat[i][j]
        sums = [[0 for _ in range(c + 1)] for _ in range(r + 1)]
        for i in range(r):
            for j in range(c):
                sums[i][j] = sums[i][j - 1] + row_sums[i][j]
        for row in sums:
            print row

        def helper(lt, rd):
            r1, c1 = lt
            r2, c2 = rd
            return sums[r2][c2] - sums[r1 - 1][c2] - sums[r2][c1 - 1] + sums[r1 - 1][c1 - 1]

        n = min(r, c)
        l = 1
        has_res = False
        for i in range(r):
            for j in range(c):
                lt = [i, j]
                while l <= n:
                    ni, nj = i + l - 1, j + l - 1
                    if 0 <= ni < r and 0 <= nj < c and helper(lt, [ni, nj]) <= threshold:
                        has_res = True
                        l += 1
                    else:
                        break
        return l - 1 if has_res else 0


examples = [
    {
        "input": {
            "mat": [
                [1, 1, 3, 2, 4, 3, 2],
                [1, 1, 3, 2, 4, 3, 2],
                [1, 1, 3, 2, 4, 3, 2]
            ],
            "threshold": 4
        },
        "output": 2
    }, {
        "input": {
            "mat": [
                [2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2],
                [2, 2, 2, 2, 2]
            ],
            "threshold": 1
        },
        "output": 0
    }, {
        "input": {
            "mat": [
                [1, 1, 1, 1],
                [1, 0, 0, 0],
                [1, 0, 0, 0],
                [1, 0, 0, 0]
            ],
            "threshold": 6
        },
        "output": 3
    }, {
        "input": {
            "mat": [
                [18, 70],
                [61, 1],
                [25, 85],
                [14, 40],
                [11, 96],
                [97, 96],
                [63, 45]
            ],
            "threshold": 40184
        },
        "output": 2
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
