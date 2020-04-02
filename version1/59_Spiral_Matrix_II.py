"""
Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

For example,
Given n = 3,

You should return the following matrix:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""


def generate_matrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    num = 1
    start_row = 0
    end_row = n - 1
    start_col = 0
    end_col = n - 1
    matrix = [[0 for i in range(n)] for j in range(n)]
    while start_row <= end_row and start_col <= end_col:
        for j in range(start_col, end_col + 1):
            matrix[start_row][j] = num
            num += 1
        start_row += 1
        for i in range(start_row, end_row + 1):
            matrix[i][end_col] = num
            num += 1
        end_col -= 1
        for j in range(end_col, start_col - 1, -1):
            matrix[end_row][j] = num
            num += 1
        end_row -= 1
        for i in range(end_row, start_row - 1, -1):
            matrix[i][start_col] = num
            num += 1
        start_col += 1
    return matrix


print generate_matrix(0)
print generate_matrix(1)
print generate_matrix(2)
print generate_matrix(3)
print generate_matrix(4)
