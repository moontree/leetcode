"""
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place,
which means you have to modify the input 2D matrix directly.
 DO NOT allocate another 2D matrix and do the rotation.
"""
import numpy as np
examples = [
    {
        "input": [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        "output": [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
    }, {
        "input": [
            [5, 1, 9, 11],
            [2, 4, 8, 10],
            [13, 3, 6, 7],
            [15, 14, 12, 16]
        ],
        "output": [
            [15, 13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7, 10, 11]
        ]
    }
]


def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    loop = 0
    for i in range(n / 2):
        num = n - loop * 2 - 1
        if num < 1:
            break
        for j in range(i, i + num):
            new_coor = [[i, j]]
            while len(new_coor) < 4:
                new_coor.append([new_coor[-1][1], n - 1 - new_coor[-1][0]])
            tmp = matrix[new_coor[-1][0]][new_coor[-1][1]]
            for k in range(3, 0, -1):
                matrix[new_coor[k][0]][new_coor[k][1]] = matrix[new_coor[k - 1][0]][new_coor[k - 1][1]]
            matrix[i][j] = tmp
        loop += 1
    return matrix


"""
new_matrix[j][n - 1 - i] = matrix[i][j]

two steps:
m[i][j] -> m[j][i] -> m[j][n - 1 -i]
"""


def rotate2(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        matrix[i] = matrix[i][::-1]
    return matrix


for example in examples:
    print example
    output = rotate2(example["input"])
    equal = not np.sum(np.array(output) - np.array(example["input"]))
    print equal
