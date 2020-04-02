"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
"""


def set_zeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    m = len(matrix)
    n = len(matrix[0])
    first_row_has_zero = False
    for j in range(n):
        if matrix[0][j] == 0:
            first_row_has_zero = True
    for i in range(1, m):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][0] = matrix[0][j] = 0
    if first_row_has_zero:
        for j in range(n):
            matrix[0][j] = 0
