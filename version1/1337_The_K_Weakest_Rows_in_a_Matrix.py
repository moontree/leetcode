"""
=========================
Project -> File: leetcode -> 1337_The_K_Weakest_Rows_in_a_Matrix.py
Author: zhangchao
=========================
Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians),
return the indexes of the k weakest rows in the matrix ordered from the weakest to the strongest.

A row i is weaker than row j,
if the number of soldiers in row i is less than the number of soldiers in row j,
or they have the same number of soldiers but i is less than j.
Soldiers are always stand in the frontier of a row,
that is, always ones may appear first and then zeros.

Example 1:

Input:
    mat =
    [[1,1,0,0,0],
    [1,1,1,1,0],
    [1,0,0,0,0],
    [1,1,0,0,0],
    [1,1,1,1,1]],
    k = 3
Output:
    [2,0,3]

Explanation:
    The number of soldiers for each row is:
    row 0 -> 2
    row 1 -> 4
    row 2 -> 1
    row 3 -> 2
    row 4 -> 5
    Rows ordered from the weakest to the strongest are [2,0,3,1,4]

Example 2:

Input:
    mat =
    [[1,0,0,0],
    [1,1,1,1],
    [1,0,0,0],
    [1,0,0,0]],
    k = 2
Output:
    [0,2]
Explanation:
    The number of soldiers for each row is:
    row 0 -> 1
    row 1 -> 4
    row 2 -> 1
    row 3 -> 1
    Rows ordered from the weakest to the strongest are [0,2,3,1]

Constraints:

    m == mat.length
    n == mat[i].length
    2 <= n, m <= 100
    1 <= k <= m
    matrix[i][j] is either 0 or 1.
"""


class Solution(object):
    def kWeakestRows(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        pairs = []
        for i, row in enumerate(mat):
            c = 0
            for v in row:
                if v == 1:
                    c += 1
                else:
                    break
            pairs.append([c, i])
        pairs.sort()
        return [v[1] for v in pairs[:k]]


examples = [
    {
        "input": {
            "mat": [
                [1, 1, 0, 0, 0],
                [1, 1, 1, 1, 0],
                [1, 0, 0, 0, 0],
                [1, 1, 0, 0, 0],
                [1, 1, 1, 1, 1]
            ],
            "k": 3
        },
        "output": [2, 0, 3]
    }, {
        "input": {
            "mat": [
                [1, 0, 0, 0],
                [1, 1, 1, 1],
                [1, 0, 0, 0],
                [1, 0, 0, 0]
            ],
            "k": 2
        },
        "output": [0, 2]
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
