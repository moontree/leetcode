"""
Given an array A of non-negative integers,
return the maximum sum of elements in two non-overlapping (contiguous) subarrays,
hich have lengths L and M.
(For clarification, the L-length subarray could occur before or after the M-length subarray.)

Formally,
return the largest V for which V = (A[i] + A[i+1] + ... + A[i+L-1]) + (A[j] + A[j+1] + ... + A[j+M-1]) and either:

0 <= i < i + L - 1 < j < j + M - 1 < A.length, or
0 <= j < j + M - 1 < i < i + L - 1 < A.length.


Example 1:

Input:
    A = [0,6,5,2,2,5,1,9,4], L = 1, M = 2
Output:
    20
Explanation:
    One choice of subarrays is [9] with length 1, and [6,5] with length 2.

Example 2:
Input:
    A = [3,8,1,3,2,1,8,9,0], L = 3, M = 2
Output:
    29
Explanation:
    One choice of subarrays is [3,8,1] with length 3, and [8,9] with length 2.

Example 3:

Input:
    A = [2,1,5,6,0,9,5,0,3,8], L = 4, M = 3
Output:
    31
Explanation:
    One choice of subarrays is [5,6,0,9] with length 4, and [3,8] with length 3.

Note:
    L >= 1
    M >= 1
    L + M <= A.length <= 1000
    0 <= A[i] <= 1000
"""


class Solution(object):
    def maxSumTwoNoOverlap(self, A, L, M):
        """
        :type A: List[int]
        :type L: int
        :type M: int
        :rtype: int
        """
        n = len(A)
        right = [[0, 0] for _ in range(n)]
        rl, rm = n - 1, n - 1
        sl, sm = 0, 0
        for i in range(n)[::-1]:
            sl += A[i]
            sm += A[i]
            ll, lm = rl - i + 1, rm - i + 1
            if ll == L:
                right[i][0] = max(right[(i + 1) % n][0], sl)
                sl -= A[rl]
                rl -= 1
            if lm == M:
                right[i][1] = max(right[(i + 1) % n][1], sm)
                sm -= A[rm]
                rm -= 1
        ll, lm = 0, 0
        sl, sm = 0, 0
        res = 0
        max_l, max_m = 0, 0
        for i in range(n - 1):
            sl += A[i]
            sm += A[i]
            _ll, _lm = i - ll + 1, i - lm + 1
            if _ll == L:
                max_l = max(max_l, sl)
                sl -= A[ll]
                ll += 1
                res = max(res, max_l + right[i + 1][1])
            if _lm == M:
                max_m = max(max_m, sm)
                sm -= A[lm]
                lm += 1
                res = max(res, max_m + right[i + 1][0])
        return res


examples = [
    {
        "input": {
            "A": [0, 6, 5, 2, 2, 5, 1, 9, 4],
            "L": 1,
            "M": 2
        },
        "output": 20
    }, {
        "input": {
            "A": [3, 8, 1, 3, 2, 1, 8, 9, 0],
            "L": 3,
            "M": 2
        },
        "output": 29
    }, {
        "input": {
            "A": [2, 1, 5, 6, 0, 9, 5, 0, 3, 8],
            "L": 4,
            "M": 3
        },
        "output": 31
    }, {
        "input": {
            "A": [1, 0, 3],
            "L": 1,
            "M": 2
        },
        "output": 4
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
