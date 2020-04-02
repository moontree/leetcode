"""
Given a non-empty 2D matrix matrix and an integer k,
find the max sum of a rectangle in the matrix such that its sum is no larger than k.

Example:
Given matrix = [
  [1,  0, 1],
  [0, -2, 3]
]
k = 2
The answer is 2. Because the sum of rectangle [[0, 1], [-2, 3]] is 2 and 2 is the max number no larger than k (k = 2).

Note:
The rectangle inside the matrix must have an area > 0.
What if the number of rows is much larger than the number of columns?
"""


class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        import bisect
        r, c = len(matrix), len(matrix[0])
        res = float("-inf")
        for ll in range(c):
            _s = [0] * r
            for rr in range(ll, c):
                for j in range(r):
                    _s[j] += matrix[j][rr]
                arr = [0]
                cur = 0
                for v in _s:
                    cur += v
                    loc = bisect.bisect_left(arr, cur - k)
                    if loc < len(arr):
                        res = max(res, cur - arr[loc])
                    bisect.insort(arr, cur)

        return res


examples = [
    {
        "input": {
            "matrix" : [
                [1,  0, 1],
                [0, -2, 3]
            ],
            "k": 2
        },
        "output": 2
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
