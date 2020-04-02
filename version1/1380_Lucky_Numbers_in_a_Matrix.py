"""
=========================
Project -> File: leetcode -> 1380_Lucky_Numbers_in_a_Matrix.py
Author: zhangchao
=========================
Given a m * n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.


Example 1:

Input:
    matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output:
    [15]
Explanation:
    15 is the only lucky number since it is the minimum in its row and the maximum in its column

Example 2:

Input:
    matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output:
    [12]
Explanation:
    12 is the only lucky number since it is the minimum in its row and the maximum in its column.

Example 3:

Input:
    matrix = [[7,8],[1,2]]
Output:
    [7]

Constraints:
    m == mat.length
    n == mat[i].length
    1 <= n, m <= 50
    1 <= matrix[i][j] <= 10^5.
    All elements in the matrix are distinct.
"""


class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        r, c = len(matrix), len(matrix[0])
        row, col = [100002 for _ in range(r)], [-1 for _ in range(c)]
        for i in range(r):
            for j in range(c):
                if matrix[i][j] < row[i]:
                    row[i] = matrix[i][j]
                if matrix[i][j] > col[j]:
                    col[j] = matrix[i][j]
        print row, col
        return [v1 for v1 in row for v2 in col if v1 == v2]


examples = [
    {
        "input": {
            "matrix": [
                [3, 7, 8],
                [9, 11, 13],
                [15, 16, 17]
            ],
        },
        "output": [15]
    }, {
        "input": {
            "matrix": [
                [1, 10, 4, 2],
                [9, 3, 8, 7],
                [15, 16, 17, 12]
            ],
        },
        "output": [12]
    }, {
        "input": {
            "matrix": [
                [7, 8],
                [1, 2]
            ],
        },
        "output": [7]
    }, {
        "input": {
            "matrix": [[56216], [63251], [75772], [1945], [27014]],
        },
        "output": [75772]
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
