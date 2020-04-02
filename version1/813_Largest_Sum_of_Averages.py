"""
We partition a row of numbers A into at most K adjacent (non-empty) groups,
then our score is the sum of the average of each group.
What is the largest score we can achieve?

Note that our partition must use every number in A, and that scores are not necessarily integers.

Example:
Input:
    A = [9,1,2,3,9]
    K = 3
Output:
    20
Explanation:
    The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
    We could have also partitioned A into [9, 1], [2], [3, 9], for example.
    That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.


Note:

    1 <= A.length <= 100.
    1 <= A[i] <= 10000.
    1 <= K <= A.length.
    Answers within 10^-6 of the correct answer will be accepted as correct.
"""


class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        n = len(A)
        dp = [[0 for _ in range(n)] for _ in range(K)]
        s = 0.
        for i in range(n):
            s += A[i]
            dp[0][i] = s / (i + 1)
        for i in range(K):
            dp[i][0] = A[0] + 0.
        for i in range(1, K):
            for j in range(1, n):
                s = 0.
                for k in range(j, 0, -1):
                    s += A[k]
                    diff = s / (j - k + 1) + dp[i - 1][k - 1]
                    if dp[i][j] < diff:
                        dp[i][j] = diff
        return dp[-1][-1]


examples = [
    {
        "input": {
            "A": [9, 1, 2, 3, 9],
            "K": 3,
        },
        "output": 20
    }, {
        "input": {
            "A": [9, 1, 2, 3, 9],
            "K": 4,
        },
        "output": 22.5
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
        print func(**example['input']) == example['output']