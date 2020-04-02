"""
Two images A and B are given,
represented as binary,
square matrices of the same size.
(A binary matrix has only 0s and 1s as values.)

We translate one image however we choose
(sliding it left, right, up, or down any number of units),
and place it on top of the other image.
After, the overlap of this translation is the number of positions that have a 1 in both images.

(Note also that a translation does not include any kind of rotation.)

What is the largest possible overlap?

Example 1:

Input:
    A = [
        [1,1,0],
        [0,1,0],
        [0,1,0]
    ]
   B = [
        [0,0,0],
        [0,1,1],
        [0,0,1]
    ]
Output:
    3
Explanation: We slide A to right by 1 unit and down by 1 unit.
Notes:

    1 <= A.length = A[0].length = B.length = B[0].length <= 30
    0 <= A[i][j], B[i][j] <= 1
"""
import numpy as np


class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        def bit_to_int(row):
            res = 0
            for v in row:
                res = (res << 1) + v
            return res

        def count(v):
            c = 0
            while v:
                if v % 2 == 1:
                    c += 1
                v = v >> 1
            return c

        ia, ib = [], []
        for row in A:
            ia.append(bit_to_int(row))
        for row in B:
            ib.append(bit_to_int(row))

        r, c = len(A), len(A[0])
        max_count = 0
        for i in range(r):
            for j in range(c):
                tmp1, tmp2 = 0, 0
                for k in range(r - i):
                    tmp1 += count((ia[i + k] << j) & ib[k])
                    tmp2 += count((ia[i + k] >> j) & ib[k])
                max_count = max(max_count, tmp2, tmp1)
            for j in range(c):
                tmp1, tmp2 = 0, 0
                for k in range(r - i):
                    tmp1 += count((ia[k] << j) & ib[i + k])
                    tmp2 += count((ia[k] >> j) & ib[i + k])
                max_count = max(max_count, tmp2, tmp1)

        return max_count


examples = [
    {
        "input": {
            "A": [
                [1, 1, 0],
                [0, 1, 0],
                [0, 1, 0]
            ],
            "B": [
                [0, 0, 0],
                [0, 1, 1],
                [0, 0, 1]
            ],
        },
        "output": 3
    }, {
        "input": {
            "A": [
                [0, 0],
                [0, 1],
            ],
            "B": [
                [1, 0],
                [0, 0],
            ],
        },
        "output": 1
    }
]


if __name__ == '__main__':
    solution = Solution()
    for n in dir(solution):
        if not n.startswith('__'):
            func = getattr(solution, n)
    print(func)
    for example in examples:
        print '----------'
        v = func(**example['input'])
        print v, v == example['output']



