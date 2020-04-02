"""
In a row of dominoes,
A[i] and B[i] represent the top and bottom halves of the i-th domino.
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the i-th domino, so that A[i] and B[i] swap values.

Return the minimum number of rotations so that all the values in A are the same,
or all the values in B are the same.

If it cannot be done, return -1.

Example 1:

Input:
    A = [2,1,2,4,2,2], B = [5,2,6,2,3,2]
Output:
    2
Explanation:
    The first figure represents the dominoes as given by A and B: before we do any rotations.
    If we rotate the second and fourth dominoes,
    we can make every value in the top row equal to 2, as indicated by the second figure.

Example 2:

Input:
    A = [3,5,1,2,3], B = [3,6,3,3,4]
Output:
    -1
Explanation:
    In this case, it is not possible to rotate the dominoes to make one row of values equal.

Note:

    1 <= A[i], B[i] <= 6
    2 <= A.length == B.length <= 20000
"""


class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        cache = {
            i: 0 for i in range(1, 6)
        }
        n = len(A)
        for i in range(n):
            cache[A[i]] = cache.get(A[i], 0) + 1
            if A[i] != B[i]:
                cache[B[i]] = cache.get(B[i], 0) + 1
        target, count = -1, -1
        for k, v in cache.items():
            if v == n:
                target = k

        if target == -1:
            return -1
        ra, rb = 0, 0
        for i in range(n):
            if A[i] != target:
                ra += 1
            if B[i] != target:
                rb += 1
        return min(ra, rb)


examples = [
    {
        "input": {
            "A": [2, 1, 2, 4, 2, 2],
            "B": [5, 2, 6, 2, 3, 2]
        },
        "output": 2
    }, {
        "input": {
            "A": [3, 5, 1, 2, 3],
            "B": [3, 6, 3, 3, 4]
        },
        "output": -1
    }, {
        "input": {
            "A": [1, 1, 1, 1, 1],
            "B": [2, 2, 2, 2, 2]
        },
        "output": 0
    }, {
        "input": {
            "A": [1, 2],
            "B": [2, 1]
        },
        "output": 1
    }, {
        "input": {
            "A": [1, 2, 1, 1, 1, 2, 2, 2],
            "B": [2, 1, 2, 2, 2, 2, 2, 2]
        },
        "output": 1
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
