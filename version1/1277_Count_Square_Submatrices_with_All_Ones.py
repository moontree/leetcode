"""
Given a m * n matrix of ones and zeros,
return how many square submatrices have all ones.

Example 1:

Input:
    matrix =
    [
      [0,1,1,1],
      [1,1,1,1],
      [0,1,1,1]
    ]
Output:
    15
Explanation:
    There are 10 squares of side 1.
    There are 4 squares of side 2.
    There is  1 square of side 3.
    Total number of squares = 10 + 4 + 1 = 15.

Example 2:

Input:
    matrix =
    [
      [1,0,1],
      [1,1,0],
      [1,1,0]
    ]
Output:
    7
Explanation:
    There are 6 squares of side 1.
    There is 1 square of side 2.
    Total number of squares = 6 + 1 = 7.

Constraints:
    1 <= arr.length <= 300
    1 <= arr[0].length <= 300
    0 <= arr[i][j] <= 1
"""


class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        r, c = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(c)] for _ in range(r)]
        res = 0
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
                    res += dp[i][j]
        return res

        #
        # for i in range(r):
        #     for j in range(c):
        #         print [l[i][j], u[i][j]],
        #     print

        # res = 0
        # for i in range(r):
        #     for j in range(c):
        #         if matrix[i][j]:
        #             n = min(u[i][j], l[i][j])
        #             for k in range(1, n + 1):
        #                 if l[i - k + 1][j] >= k and u[i][j - k + 1] >= k:
        #                     res += 1
        #                 else:
        #                     break
        # return res


examples = [
    {
        "input": {
            "matrix": [
                [0, 1, 1, 1],
                [1, 1, 1, 1],
                [0, 1, 1, 1]
            ],
        },
        "output": 15
    }, {
        "input": {
            "matrix": [
                [1, 0, 1],
                [1, 1, 0],
                [1, 1, 0]
            ],
        },
        "output": 7
    }, {
        "input": {
            "matrix": [
                [0, 1, 1, 1],
                [1, 1, 0, 1],
                [1, 1, 1, 1],
                [1, 0, 1, 0]
            ],
        },
        "output": 13
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
