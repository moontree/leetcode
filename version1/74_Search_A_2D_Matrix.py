"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.

"""


def search_matrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    m = len(matrix)
    if m == 0:
        return False
    n = len(matrix[0])
    l = 0
    r = m * n - 1
    while l <= r:
        mi = (l + r) / 2
        mid_val = matrix[mi / n][mi % n]
        if target == mid_val:
            return True
        elif target > mid_val:
            l = mi + 1
        else:
            r = mi - 1
    return False


def search_matrix_2(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    m = len(matrix)
    if m == 0:
        return False
    n = len(matrix[0])
    i = m - 1
    j = 0
    while i > -1 and j < n:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] > target:
            i -= 1
        else:
            j += 1
    return False


examples = [
    {
        "matrix": [
            [1, 3, 5, 7],
            [10, 11, 16, 20],
            [23, 30, 34, 50]
        ],
        "target": 31,
        "res": True
    }, {
        "matrix": [
            [1], [3], [5]
        ],
        "target": 3,
        "res": True
    },
]


for example in examples:
    print search_matrix_2(example["matrix"], example["target"])
