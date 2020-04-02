"""
Write an efficient algorithm that searches for a value in an m x n matrix.
 This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
For example,

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""


def search_matrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    if not matrix:
        return False
    m, n = len(matrix), len(matrix[0])
    r, c = m - 1, 0
    while r > -1 and c < n:
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] < target:
            c += 1
        else:
            r -= 1
    return False
