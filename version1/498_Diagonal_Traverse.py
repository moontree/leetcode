"""
Given a matrix of M x N elements (M rows, N columns),
return all elements of the matrix in diagonal order as shown in the below image.

Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output:  [1,2,4,7,5,3,6,8,9]
Explanation:

Note:
The total number of elements of the given matrix will not exceed 10,000.
"""


def find_diagonal_order(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    if not matrix:
        return []
    m, n = len(matrix), len(matrix[0])
    res = []
    flag = 1
    for s in xrange(m + n - 1):
        if flag == 0:
            for i in xrange(max(s - n + 1, 0), min(s + 1, m)):
                res.append(matrix[i][s - i])
            flag = 1
        else:
            for j in xrange(max(s - m + 1, 0), min(s + 1, n)):
                res.append(matrix[s - j][j])
            flag = 0
    return res


examples = [
    {
        "matrix": [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        "res": [1, 2, 4, 7, 5, 3, 6, 8, 9]
    }
]


for example in examples:
    print find_diagonal_order(example["matrix"])
