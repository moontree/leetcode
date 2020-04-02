"""
=========================
Project -> File: leetcode -> 1329_Sort_the_Matrix_Diagonally.py
Author: zhangchao
=========================
Given a m * n matrix mat of integers,
sort it diagonally in ascending order from the top-left to the bottom-right then return the sorted array.

Example 1:

Input:
    mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output:
    [[1,1,1,1],[1,2,2,2],[1,2,3,3]]


Constraints:

    m == mat.length
    n == mat[i].length
    1 <= m, n <= 100
    1 <= mat[i][j] <= 100
"""


class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        r, c = len(mat), len(mat[0])
        for i in range(r)[::-1]:
            sr, sc, vals = i, 0, []
            k = 0
            while True:
                nr, nc = sr + k, sc + k
                if 0 <= nr < r and 0 <= nc < c:
                    vals.append(mat[nr][nc])
                    k += 1
                else:
                    break
            vals.sort()
            for jj in range(k):
                mat[sr + jj][sc + jj] = vals[jj]
        for j in range(1, c):
            sr, sc, vals = 0, j, []
            k = 0
            while True:
                nr, nc = sr + k, sc + k
                if 0 <= nr < r and 0 <= nc < c:
                    vals.append(mat[nr][nc])
                    k += 1
                else:
                    break
            vals.sort()
            for jj in range(k):
                mat[sr + jj][sc + jj] = vals[jj]
        return mat


examples = [
    {
        "input": {
            "mat": [
                [3, 3, 1, 1],
                [2, 2, 1, 2],
                [1, 1, 1, 2]
            ]
        },
        "output": [
            [1, 1, 1, 1],
            [1, 2, 2, 2],
            [1, 2, 3, 3]
        ]
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
