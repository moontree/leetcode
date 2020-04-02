"""
Given a matrix consisting of 0s and 1s,
we may choose any number of columns in the matrix and flip every cell in that column.
Flipping a cell changes the value of that cell from 0 to 1 or from 1 to 0.

Return the maximum number of rows that have all values equal after some number of flips.


Example 1:

Input:
    [[0,1],[1,1]]
Output:
    1
Explanation:
    After flipping no values, 1 row has all values equal.

Example 2:

Input:
    [[0,1],[1,0]]
Output:
    2
Explanation:
    After flipping values in the first column, both rows have equal values.

Example 3:
Input:
    [[0,0,0],[0,0,1],[1,1,0]]
Output:
    2
Explanation:
    After flipping values in the first two columns, the last two rows have equal values.

Note:
    1 <= matrix.length <= 300
    1 <= matrix[i].length <= 300
    All matrix[i].length's are equal
    matrix[i][j] is 0 or 1
"""


class Solution(object):
    def maxEqualRowsAfterFlips(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        cache = {}
        for row in matrix:
            if row[0] == 0:
                tmp = ''.join([str(v) for v in row])
            else:
                tmp = ''.join([str(1 - v) for v in row])
            cache[tmp] = cache.get(tmp, 0) + 1
        return max(cache.values())


examples = [
    {
        "input": {
            "matrix": [[0, 1], [1, 1]],
        },
        "output": 1
    }, {
        "input": {
            "matrix": [[0, 1], [1, 0]],
        },
        "output": 2
    }, {
        "input": {
            "matrix":  [
                [0, 0, 0],
                [0, 0, 1],
                [1, 1, 0]
            ],
        },
        "output": 2
    },
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
