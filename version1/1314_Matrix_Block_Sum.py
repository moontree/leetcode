"""
Given a m * n matrix mat and an integer K,
return a matrix answer where each answer[i][j]
is the sum of all elements mat[r][c] for i - K <= r <= i + K, j - K <= c <= j + K,
and (r, c) is a valid position in the matrix.


Example 1:

Input:
    mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
Output:
    [[12,21,16],[27,45,33],[24,39,28]]

Example 2:

Input:
    mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
Output:
    [[45,45,45],[45,45,45],[45,45,45]]

Constraints:

    m == mat.length
    n == mat[i].length
    1 <= m, n, K <= 100
    1 <= mat[i][j] <= 100
"""


class Solution(object):
    def matrixBlockSum(self, mat, K):
        """
        :type mat: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        r, c = len(mat), len(mat[0])
        row_sum = []
        for i in range(r):
            s, tmp = 0, []
            for j in range(c):
                s += mat[i][j]
                tmp.append(s)
            row_sum.append(tmp)

        mat_sum = [row_sum[0] + [0]]
        for i in range(1, r):
            mat_sum.append([mat_sum[-1][j] + row_sum[i][j] for j in range(c)])
            mat_sum[-1].append(0)
        mat_sum.append([0 for _ in range(c + 1)])
        res = []
        for i in range(r):
            res.append([])
            for j in range(c):
                x1, y1, x2, y2 = max(i - K, 0), max(j - K, 0), min(i + K, r - 1), min(j + K, c - 1)
                v = mat_sum[x2][y2] + mat_sum[x1 - 1][y1 - 1] - mat_sum[x1 - 1][y2] - mat_sum[x2][y1 - 1]
                res[-1].append(v)
        return res


examples = [
    {
        "input": {
            "mat": [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ],
            "K": 1
        },
        "output": [
            [12, 21, 16],
            [27, 45, 33],
            [24, 39, 28]
        ]
    }, {
        "input": {
            "mat": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            "K": 2
        },
        "output":[[45, 45, 45], [45, 45, 45], [45, 45, 45]]
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
