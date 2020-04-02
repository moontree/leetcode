"""
Given the following details of a matrix with n columns and 2 rows :

The matrix is a binary matrix, which means each element in the matrix can be 0 or 1.
The sum of elements of the 0-th(upper) row is given as upper.
The sum of elements of the 1-st(lower) row is given as lower.
The sum of elements in the i-th column(0-indexed) is colsum[i],
where colsum is given as an integer array with length n.

Your task is to reconstruct the matrix with upper, lower and colsum.

Return it as a 2-D integer array.

If there are more than one valid solution, any of them will be accepted.

If no valid solution exists, return an empty 2-D array.



Example 1:

Input:
    upper = 2, lower = 1, colsum = [1,1,1]
Output:
    [[1,1,0],[0,0,1]]
Explanation:
    [[1,0,1],[0,1,0]], and [[0,1,1],[1,0,0]] are also correct answers.

Example 2:

Input:
    upper = 2, lower = 3, colsum = [2,2,1,1]
Output:
    []

Example 3:

Input:
    upper = 5, lower = 5, colsum = [2,1,2,0,1,0,1,2,0,1]
Output:
    [[1,1,1,0,1,0,0,1,0,0],[1,0,1,0,0,0,1,1,0,1]]


Constraints:

    1 <= colsum.length <= 10^5
    0 <= upper, lower <= colsum.length
    0 <= colsum[i] <= 2
"""


class Solution(object):
    def reconstructMatrix(self, upper, lower, colsum):
        """
        :type upper: int
        :type lower: int
        :type colsum: List[int]
        :rtype: List[List[int]]
        """
        if sum(colsum) != upper + lower:
            return []
        counts = [0, 0, 0]
        n = len(colsum)
        for c in colsum:
            counts[c] += 1
        a, b = max(upper, lower), min(upper, lower)
        if counts[2] > b:
            return []
        res = [[0 for _ in range(n)] for _ in range(2)]
        #
        ur, lr, ar = upper - counts[2], lower - counts[2], counts[2]
        for i, c in enumerate(colsum):
            if c == 1:
                if ur:
                    res[0][i] = 1
                    ur -= 1
                elif lr:
                    res[1][i] = 1
                    lr -= 1
            elif c == 2:
                res[0][i] = 1
                res[1][i] = 1
                ar -= 1
            if lr < 0 or ar < 0 or ur < 0:
                return []
        return res


examples = [
    {
        "input": {
            "upper": 2,
            "lower": 1,
            "colsum": [1, 1, 1]
        },
        "output": [[1, 1, 0], [0, 0, 1]]
    }, {
        "input": {
            "upper": 2,
            "lower": 3,
            "colsum": [2, 2, 1, 1]
        },
        "output": []
    }, {
        "input": {
            "upper": 5,
            "lower": 5,
            "colsum":  [2, 1, 2, 0, 1, 0, 1, 2, 0, 1]
        },
        "output": [
            [1, 1, 1, 0, 1, 0, 0, 1, 0, 0],
            [1, 0, 1, 0, 0, 0, 1, 1, 0, 1]
        ]
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
