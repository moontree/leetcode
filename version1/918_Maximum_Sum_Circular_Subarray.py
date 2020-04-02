"""
Given a circular array C of integers represented by A,
find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.
(Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.
(Formally, for a subarray C[i], C[i+1], ..., C[j],
there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)



Example 1:

Input:
    [1,-2,3,-2]
Output:
    3
Explanation:
    Subarray [3] has maximum sum 3

Example 2:
Input:
    [5,-3,5]
Output:
    10
Explanation:
    Subarray [5,5] has maximum sum 5 + 5 = 10

Example 3:

Input:
    [3,-1,2,-1]
Output:
    4
Explanation:
    Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4

Example 4:

Input:
    [3,-2,2,-3]
Output:
    3
Explanation:
    Subarray [3] and [3,-2,2] both have maximum sum 3

Example 5:

Input:
    [-2,-3,-1]
Output:
    -1
Explanation:
    Subarray [-1] has maximum sum -1


Note:

    -30000 <= A[i] <= 30000
    1 <= A.length <= 30000
"""


class Solution(object):
    def maxSubarraySumCircular(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # single
        q = []
        res = -float('inf')
        for i, v in enumerate(A):
            if not q:
                q.append(v)
            else:
                q.append(max(q[-1], 0) + v)
            if res < q[-1]:
                res = q[-1]
        # [0, i) and [j, len(A)]
        right_sum, max_right = [0 for _ in range(len(A))], [0 for _ in range(len(A))]
        left_sum, right_sum[-1], max_right[-1] = 0, A[-1], A[-1]
        for i in range(len(A) - 2, -1, -1):
            right_sum[i] = right_sum[i + 1] + A[i]
            max_right[i] = max(max_right[i + 1], right_sum[i])
        for i in range(len(A) - 2):
            left_sum += A[i]
            v = left_sum + max_right[i + 2]
            if res < v:
                res = v
        return res


examples = [
    {
        "input": {
            "A": [1, -2, 3, -2],
        },
        "output": 3
    }, {
        "input": {
            "A": [5, -3, 5],
        },
        "output": 10
    }, {
        "input": {
            "A": [3, -1, 2, -1],
        },
        "output": 4
    }, {
        "input": {
            "A": [3, -2, 2, -3],
        },
        "output": 3
    }, {
        "input": {
            "A": [-2, -3, -1],
        },
        "output": -1
    }, {
        "input": {
            "A": [-5, -2, 5, 6, -2, -7, 0, 2, 8],
        },
        "output": 14
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
