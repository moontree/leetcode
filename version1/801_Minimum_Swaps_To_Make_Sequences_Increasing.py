"""
We have two integer sequences A and B of the same non-zero length.

We are allowed to swap elements A[i] and B[i].
Note that both elements are in the same index position in their respective sequences.

At the end of some number of swaps, A and B are both strictly increasing.
(A sequence is strictly increasing if and only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)

Given A and B, return the minimum number of swaps to make both sequences strictly increasing.
It is guaranteed that the given input always makes it possible.

Example:
Input:
    A = [1,3,5,4], B = [1,2,3,7]
Output:
    1
Explanation:
    Swap A[3] and B[3].  Then the sequences are:
    A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
    which are both strictly increasing.
Note:
    A, B are arrays with the same length, and that length will be in the range [1, 1000].
    A[i], B[i] are integer values in the range [0, 2000].

"""


class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(A)
        dp = [[n, n] for _ in range(n)]
        dp[0] = [0, 1]
        # 0 : keep, 1: swap
        for i in range(1, n):
            if A[i] > A[i - 1] and B[i] > B[i - 1]: # no need to change
                if A[i] > B[i - 1] and B[i] > A[i - 1]: # can change
                    dp[i][0] = min(dp[i - 1])
                    dp[i][1] = min(dp[i - 1]) + 1
                else: # can not change
                    dp[i][0] = dp[i - 1][0]
                    dp[i][1] = dp[i - 1][1] + 1
            else: # have to change
                dp[i][1] = dp[i - 1][0] + 1
                dp[i][0] = dp[i - 1][1]


        print [v[0] for v in dp]
        print [v[1] for v in dp]
        # print dp
        return min(dp[-1])



examples = [
    {
        "input": {
            "A": [1, 3, 5, 4],
            "B": [1, 2, 3, 7],
        },
        "output": 1
    }, {
        "input": {
            "A": [0, 7, 8, 10, 10, 11, 12, 13, 19, 18],
            "B": [4, 4, 5, 7, 11, 14, 15, 16, 17, 20],
        },
        "output": 4
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
