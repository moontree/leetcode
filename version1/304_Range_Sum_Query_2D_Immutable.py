"""
Given a 2D matrix matrix,
 find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1)
  and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1)
 and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sum_region(2, 1, 4, 3) -> 8
sum_region(1, 1, 2, 2) -> 11
sum_region(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sum_region function.
You may assume that row1 <= row2 and col1 <= col2.
"""


class NumMatrix(object):
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        if matrix:
            m, n = len(matrix), len(matrix[0])
            self.sums = [[0 for _ in xrange(n + 1)] for _ in xrange(m + 1)]
            self.sums[1][1] = matrix[0][0]
            for i in xrange(1, m):
                self.sums[i + 1][1] = self.sums[i][1] + matrix[i][0]
            for j in xrange(1, n):
                self.sums[1][j + 1] = self.sums[1][j] + matrix[0][j]
            for i in xrange(1, m):
                for j in xrange(1, n):
                    self.sums[i + 1][j + 1] = self.sums[i + 1][j] + self.sums[i][j + 1] - self.sums[i][j] + matrix[i][j]

    def sum_region(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if not self.matrix:
            return 0
        row2 += 1
        col2 += 1
        return self.sums[row2][col2] - self.sums[row1][col2] - self.sums[row2][col1] + self.sums[row1][col1]


examples = [
    {
        "matrix": [
            [3, 0, 1, 4, 2],
            [5, 6, 3, 2, 1],
            [1, 2, 0, 1, 5],
            [4, 1, 0, 1, 7],
            [1, 0, 3, 0, 5]
        ],
        "region": [2, 1, 4, 3],
        "res": 8
    }
]


for example in examples:
    obj = NumMatrix(example["matrix"])
    a, b, c, d = (2, 1, 4, 3)
    print obj.sum_region(a, b, c, d)
    a, b, c, d = (1, 1, 2, 2)
    print obj.sum_region(a, b, c, d)
    a, b, c, d = (1, 2, 2, 4)
    print obj.sum_region(a, b, c, d)
