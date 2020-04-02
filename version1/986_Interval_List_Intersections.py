"""
Given two lists of closed intervals,
each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

(Formally, a closed interval [a, b] (with a <= b)
denotes the set of real numbers x with a <= x <= b.
The intersection of two closed intervals is a set of real numbers that is either empty,
or can be represented as a closed interval.  For example, the intersection of [1, 3] and [2, 4] is [2, 3].)



Example 1:

Input:
    A = [[0,2],[5,10],[13,23],[24,25]],
    B = [[1,5],[8,12],[15,24],[25,26]]
Output:
    [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Reminder:
    The inputs and the desired output are lists of Interval objects, and not arrays or lists.


Note:

    0 <= A.length < 1000
    0 <= B.length < 1000
    0 <= A[i].start, A[i].end, B[i].start, B[i].end < 10^9
"""


class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """

        res = []
        ia, ib = 0, 0
        while ia < len(A) and ib < len(B):
            lo = max(A[ia][0], B[ib][0])
            hi = min(A[ia][1], B[ib][1])
            if lo <= hi:
                res.append([lo, hi])
            if A[ia][1] < B[ib][1]:
                ia += 1
            else:
                ib += 1
        return res


examples = [
    {
        "input": {
            "A": [[0, 2], [5, 10], [13, 23], [24, 25]],
            "B": [[1, 5], [8, 12], [15, 24], [25, 26]],
        },
        "output": [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
    }, {
        "input": {
            "A": [[0, 100]],
            "B": [[1, 5], [8, 12], [15, 24], [25, 26]],
        },
        "output": [[1, 5], [8, 12], [15, 24], [25, 26]]
    }, {
        "input": {
            "A": [[0, 100]],
            "B": [],
        },
        "output": []
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
