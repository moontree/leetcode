"""
=========================
Project -> File: leetcode -> 790_Domino_and_Tromino_Tiling.py
Author: zhangchao
=========================
We have two types of tiles: a 2x1 domino shape,
and an "L" tromino shape. These shapes may be rotated.

XX  <- domino

XX  <- "L" tromino
X
Given N, how many ways are there to tile a 2 x N board?
Return your answer modulo 10^9 + 7.

(In a tiling, every square must be covered by a tile.
Two tilings are different if and only if there are two 4-directionally adjacent cells on the board
such that exactly one of the tilings has both squares occupied by a tile.)

Example:
Input:
    3
Output:
    5
Explanation:
    The five different ways are listed below, different letters indicates different tiles:
    XYZ XXZ XYY XXY XYY
    XYZ YYZ XZZ XYY XXY
Note:

    N  will be in range [1, 1000].
"""


class Solution(object):
    def numTilings(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N <= 2:
            return N
        f2, f1 = 1, 2
        a1, b1 = 1, 1
        for i in range(N - 2):
            f2, f1, a1, b1 = f1, f2 + f1 + a1 + b1, f2 + b1, f2 + a1
        return f1 % (10 ** 9 + 7)


examples = [
    {
        "input": {
            "N": 3,
        },
        "output": 5
    },  {
        "input": {
            "N": 4,
        },
        "output": 11
    },  {
        "input": {
            "N": 5,
        },
        "output": 24
    }
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
