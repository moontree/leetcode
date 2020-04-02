"""
Given an integer array A,
you partition the array into (contiguous) subarrays of length at most K.
After partitioning, each subarray has their values changed to become the maximum value of that subarray.

Return the largest sum of the given array after partitioning.



Example 1:

Input:
    A = [1,15,7,9,2,5,10], K = 3
Output:
    84
Explanation:
    A becomes [15,15,15,9,10,10,10]

Note:
    1 <= K <= A.length <= 500
    0 <= A[i] <= 10^6
"""


class Solution(object):
    def maxSumAfterPartitioning(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        dp = [0 for _ in range(len(A))]
        for r, v in enumerate(A):
            max_v = v
            for l in range(r, max(r - K, -1), -1):
                if max_v < A[l]:
                    max_v = A[l]
                if l == 0:
                    tmp = 0
                else:
                    tmp = dp[l - 1]
                # print r, l, tmp, tmp + max_v * (r - l + 1)
                dp[r] = max(dp[r], tmp + max_v * (r - l + 1))
        # print(dp)
        return dp[-1]


examples = [
    {
        "input": {
            "A": [1, 15, 7, 9, 2, 5, 10],
            "K": 3
        },
        "output": 84
    },  {
        "input": {
            "A": [3, 7],
            "K": 2
        },
        "output": 14
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
