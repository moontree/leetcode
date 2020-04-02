"""
A sequence of numbers is called arithmetic
if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequences:
    1, 3, 5, 7, 9
    7, 7, 7, 7
    3, -1, -5, -9

The following sequence is not arithmetic.
    1, 1, 2, 5, 7

A zero-indexed array A consisting of N numbers is given.
A subsequence slice of that array is any sequence of integers (P0, P1, ..., Pk) such that 0 <= P0 < P1 < ... < Pk < N.

A subsequence slice (P0, P1, ..., Pk) of array A is called arithmetic
if the sequence A[P0], A[P1], ..., A[Pk-1], A[Pk] is arithmetic.

In particular, this means that k >= 2.

The function should return the number of arithmetic subsequence slices in the array A.

The input contains N integers.
Every integer is in the range of -2^31 and 2^31-1 and 0 <= N <= 1000.
The output is guaranteed to be less than 2&31-1.


Example:

Input:
    [2, 4, 6, 8, 10]

Output:
    7

Explanation:
    All arithmetic subsequence slices are:
    [2,4,6]
    [4,6,8]
    [6,8,10]
    [2,4,6,8]
    [4,6,8,10]
    [2,4,6,8,10]
    [2,6,10]
"""
import json


class Solution(object):
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if len(A) < 3:
            return 0
        f = [{} for _ in range(len(A))]  # count of subarray ended by A[i]
        g = [{} for _ in range(len(A))]  # count of diff end by A[i]
        res = 0

        for i in range(len(A)):
            for j in range(i):
                diff = A[i] - A[j]
                g[i][diff] = g[i].get(diff, 0) + 1
                f[i][diff] = f[i].get(diff, 0) + f[j].get(diff, 0) + g[j].get(diff, 0)
            res += sum(f[i].values())
        return res


examples = [
    {
        "input": {
            "A": [2, 4, 6, 8, 10],
        },
        "output": 7
    }, {
        "input": {
            "A": [2, 2, 3, 4],
        },
        "output": 2
    }, {
        "input": {
            "A": [1, 1, 1, 1, 1],
        },
        "output": 16
    }, {
        "input": {
            "A": [79,20,64,28,67,81,60,58,97,85,92,96,82,89,46,50,15,2,36,44,54,2,90,37,7,79,26,40,34,67,64,28,60,89,46,31,9,95,43,19,47,64,48,95,80,31,47,19,72,99,28,46,13,9,64,4,68,74,50,28,69,94,93,3,80,78,23,80,43,49,77,18,68,28,13,61,34,44,80,70,55,85,0,37,93,40,47,47,45,23,26,74,45,67,34,20,33,71,48,96],
        },
        "output": 1030
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
