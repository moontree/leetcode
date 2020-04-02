"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

For example,
Given the following matrix:

[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
You should return [1,2,3,6,9,8,7,4,5].


"""


examples = [
    {
        "matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        "output": [1, 2, 3, 6, 9, 8, 7, 4, 5]
    }, {
        "matrix": [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]],
        "output": [1, 2, 3, 6, 9, 12, 11, 10, 7, 4, 5, 8]
    }, {
        "matrix": [[]],
        "output": []
    }, {
        "matrix": [[6, 9, 7]],
        "output": []
    }, {
        "matrix": [[2,5,8],[4,0,-1]],
        "output": []
    }
]


def spiral_order(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return []
    start_row = 0
    end_row = len(matrix) - 1
    start_col = 0
    end_col = len(matrix[0]) - 1
    res = []
    while start_row < end_row and start_col < end_col:
        for j in range(start_col, end_col):
            res.append(matrix[start_row][j])
        for i in range(start_row, end_row):
            res.append(matrix[i][end_col])
        for j in range(end_col, start_col, -1):
            res.append(matrix[end_row][j])
        for i in range(end_row, start_row, -1):
            res.append(matrix[i][start_col])
        end_row -= 1
        end_col -= 1
        start_col += 1
        start_row += 1
    if start_row == end_row:
        res += matrix[start_row][start_col: end_col + 1]
    elif start_col == end_col:
        for i in range(start_row, end_row + 1):
            res.append(matrix[i][start_col])
    return res


for example in examples:
    print spiral_order(example["matrix"])